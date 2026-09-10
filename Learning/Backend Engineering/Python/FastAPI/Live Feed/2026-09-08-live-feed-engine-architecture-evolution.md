# Live Feed Engine — Architecture Evolution

Companion description for `2026-09-08-live-feed-engine-architecture-evolution.html`, an
interactive click-through diagram of how the `GET /feed` request path evolved from Phase 0's
initial build through Phase 1's full bottleneck-diagnosis-and-fix cycle.

Open the HTML file in a browser. Click through stages 0 → 4 via the tab bar (or press `1`–`5`),
step through each stage's request path with the player controls or arrow keys, and read the
per-step detail (payload + numbers) in the side panel. The topology itself changes at Stage 4 —
the diagram switches from a "Single Process" to a "Multi-Worker" view automatically when you pick
that stage (or toggle it yourself with `O`).

## Components

| Node | Role | Present in | What it is |
|---|---|---|---|
| **k6 Load Client** | Load client | All stages | The load-testing tool driving 0→1000 ramping virtual users against `/feed`. |
| **Uvicorn (1 process)** | Web server process | Stages 0–3 | The original single-process ASGI server — one event loop, one CPU core. |
| **Gunicorn Master** | Web server process | Stage 4 | Replaces bare Uvicorn — binds the port and manages worker processes. |
| **4× UvicornWorker** | Worker processes | Stage 4 | Four independent OS processes, each its own event loop, spread across CPU cores. |
| **asyncpg Pool** | Connection pool | All stages | The application-level Postgres connection pool, created once per process in `lifespan`. |
| **PostgreSQL** | Datastore | All stages | `article` / `publisher` tables, `max_connections=100`. |
| **Diagnostics** | Diagnostic tools | Stage 3 only | Stand-in node for `EXPLAIN ANALYZE` and `docker stats`, the two tools used to locate the real bottleneck. |

## Stages, step by step

### Stage 0 — Initial Build (Phase 0)
The working end-to-end system, confirmed correct against real RSS-ingested data, but **never yet
tested under concurrent load**. Single Uvicorn process, `asyncpg` pool at `max_size=10`, cursor
pagination on `article.id` (not offset-based — chosen so pages never drift as rows insert
concurrently).

1. Client hits `GET /feed?region=&limit=&cursor=`.
2. Request borrows a connection from the pool (`max_size=10`).
3. Cursor-paginated query runs against Postgres.
4. Response returns — correctness confirmed, performance completely untested.

### Stage 1 — Baseline Load Test
Same topology as Stage 0, now hit with k6 ramping 0→1000 virtual users across five 30-second
stages, with a threshold of `p(99) < 200ms`.

1. 1,000 concurrent VUs arrive.
2. ~990 of them queue for the 10 available pool connections — the entire story of this stage.
3. The 10 requests that *do* get a connection run fine individually (query itself was never slow).
4. Every request eventually succeeds — **0% failed** — but p99 lands at **10.93s**, median 914ms,
   throughput ~205 req/s. This is queuing, not crashing: a critical distinction, since a system
   rejecting work looks very different from one just falling behind.

### Stage 2 — Pool Widened (10 → 50)
Same single Uvicorn worker; only `asyncpg`'s `max_size` changed, to test the simplest hypothesis
first.

1. Same k6 script re-run for a clean before/after.
2. 5x more requests can be in flight — median drops ~5x (914ms → ~180ms), throughput nearly
   doubles (~365-375 req/s).
3. But the tail barely moves: p99 only improves to **4.72–5.19s**, and a *new* symptom appears —
   ~965 iterations get cut off by k6's own graceful-stop timer, meaning they still hadn't finished.
4. Conclusion: real progress, but a different bottleneck is now the limiting factor underneath the
   one that was just fixed.

### Stage 3 — Diagnosis
No code changes in this stage — two diagnostic tools were used to find the actual cause before
touching anything else.

1. `docker stats feed_api` during a run showed CPU pinned at **~92–95%** — a percentage of a
   *single* core, meaning the one Uvicorn process was fully core-bound regardless of how many
   cores the host had free. Container logs also showed `OSError: [Errno 24] Too many open files`.
2. `EXPLAIN ANALYZE`, run directly against both query variants in `psql`, showed **Index Scan
   Backward on `article_pkey`, execution time <2ms** — ruling out query cost entirely, despite the
   project's own plan predicting expensive scans at this row count. Cursor pagination on an
   indexed PK is why: it jumps straight to the right row rather than scanning past discarded ones.
3. Conclusion: the bottleneck is CPU parallelism (one process, one core) plus a file-descriptor
   ceiling too low for the connection volume — not the database at all.

### Stage 4 — Fixed (4 Gunicorn Workers)
The topology itself changes here: Gunicorn now manages 4 independent `UvicornWorker` processes.
The diagram auto-switches to "Multi-Worker" mode when this stage is selected.

1. Same k6 script, third and final re-run, now against `gunicorn main:app -k
   uvicorn.workers.UvicornWorker --workers 4 --bind 0.0.0.0:8000`.
2. Requests spread across 4 real OS processes — `docker stats` now shows ~200% CPU (of a 400% max
   on 4 cores), confirming actual multi-core use.
3. Pool retuned from `max_size=50` down to `max_size=20` **per worker** — since each of the 4
   worker processes runs `lifespan` independently and gets its own pool, the real total is 4×20=80,
   deliberately kept under Postgres's `max_connections=100` with ~20 of headroom.
4. Container `ulimits.nofile` raised to 65536 in `docker-compose.yml`, fixing the Stage 3
   file-descriptor crash independently of the worker change.
5. Result: **p99 = 1.42s** (down from 10.93s → 4.72-5.19s → 1.42s), median 133ms, throughput
   **~1114 req/s** (up from ~205 → ~365-375), **0 interrupted iterations** (down from 965), 0%
   failed requests throughout every single stage. The `p(99)<200ms` threshold still technically
   fails — an honest result marking the real, measured ceiling of Postgres + this API alone,
   which is the documented trigger point for adding a cache (Redis) in the project's next phase.

## Numbers across all five stages

| Stage | Topology | p99 | Median | Throughput | Interrupted |
|---|---|---|---|---|---|
| 0 | 1 process, pool=10 | untested | untested | untested | — |
| 1 | 1 process, pool=10 | 10.93s | 914ms | ~205 req/s | 0 |
| 2 | 1 process, pool=50 | 4.72–5.19s | ~180ms | ~365–375 req/s | ~965 |
| 3 | (diagnosis only, no topology change) | — | — | — | — |
| 4 | 4 processes, pool=20 each | 1.42s | 133ms | ~1114 req/s | 0 |

## Notes for a workshop / self-study walkthrough

- The single most important idea to land is the **queuing vs. crashing distinction** in Stage 1 —
  0% failure with a 10.9s p99 is a different diagnosis entirely from a system throwing errors.
- Stage 2 is worth dwelling on for the *shape* of the improvement (big median win, small tail win,
  new symptom appears) — a common pattern when fixing one bottleneck exposes the next one.
- Stage 3 is the "measure, don't guess" moment: two tools, two negative-or-clarifying results
  (query is fine; CPU/FDs are not), used before writing a single line of fix code.
- Stage 4's pool-size math (4×20=80 vs. Postgres's `max_connections=100`) is the detail most likely
  to be missed by someone copying the fix without understanding it — worth pausing on explicitly.
