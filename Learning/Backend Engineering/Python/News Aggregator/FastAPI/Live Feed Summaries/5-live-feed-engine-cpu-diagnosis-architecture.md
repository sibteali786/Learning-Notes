# Live Feed Engine — CPU Diagnosis Architecture

Companion description for `5-live-feed-engine-cpu-diagnosis-architecture.html`. Open the HTML in a browser for the interactive click-through version; this file is the same content in reference form.

## System

FastAPI app (`main.py`) behind Gunicorn (managing 4 `UvicornWorker` processes), talking to Postgres via an `asyncpg` connection pool, on a host with **4 physical CPU cores**. Load tested with k6 (`ramping-vus`, 0→1000 VUs over 5 stages, threshold `p(99)<200ms`).

## Nodes

| Node | Role | What it is |
|---|---|---|
| k6 Load Test | Load Generator | Drives the load test, reports p99/throughput |
| FastAPI Worker | App Process | The Gunicorn `UvicornWorker` child that actually handles `GET /feed` |
| Gunicorn Master | Process Manager | The Arbiter — spawns/monitors workers, **handles zero HTTP requests itself** |
| System Monitors | Diagnostics | `docker stats`, `top` (inside container), `EXPLAIN ANALYZE` |
| py-spy | Profiler | Sampling profiler — `py-spy top` (live) and `py-spy record` (flamegraph) |
| Postgres | Datastore | `article` (1M rows) + `publisher`, indexed on `article.id` |

## Modes

- **Before Fix** — single Uvicorn worker, `asyncpg max_size=10`, no ulimit tuning. p99 = 10.93s.
- **After Fix** — 4 Gunicorn workers, ulimits raised, pool tuned progressively (20 → 22 per worker). p99 ≈ 1.35s.

## Flows

### 1 — Baseline Bottleneck (`before` mode)
1. k6 hits a single worker at 1000 VUs — p99 10.93s, throughput plateaus ~205 req/s.
2. `docker stats` shows one core pinned ~92-95% — confirms event-loop-bound, not query-bound.
3. Container logs reveal `OSError: [Errno 24] Too many open files` — ulimit too low.
4. `EXPLAIN ANALYZE` shows the query itself is ~2ms (Index Scan Backward on `article_pkey`) — rules out the query as the bottleneck from the very start.

### 2 — Worker + Pool Fix (`after` mode)
1. Gunicorn master spawns 4 `UvicornWorker` children — spreads work across all 4 cores.
2. `asyncpg` pool re-tuned: `min_size=5, max_size=20` per worker × 4 = 80 total connections, under Postgres's `max_connections=100`.
3. Same k6 script re-run against the fixed setup.
4. Result: p99 10.93s → 1.42s, throughput ~205 → ~1114 req/s, 0 interrupted iterations (down from 965) — a ~5-8x improvement from one root-cause fix (CPU parallelism) plus the pool bump.

### 3 — CPU Diagnosis (py-spy)
1. `top` inside the container: idle=0.0%, wait=0.0%, load average climbs 3.32→8.41 against `nproc`=4 — confirms genuinely CPU-bound.
2. `py-spy top --pid <master> --subprocesses` initially shows `_worker (concurrent.futures.thread)` dominating at ~1200% — but this appears even on the **master**, which handles zero requests. Diagnosed as a profiling artifact (the master's own bookkeeping thread, sibling of the arbiter loop), not real request cost.
3. Re-profiled with `py-spy record --pid <single-worker>` (no `--subprocesses`) for a clean flamegraph of just request handling.
4. Finding: `solve_dependencies` (FastAPI's per-request query-param resolution) is comparable in cost to the actual Postgres `fetch`/`execute`/`write` — despite the query being ~2ms.

### 4 — Experiments & Verdict
1. **Redis ruled out by reasoning**: Postgres's `shared_buffers`/OS cache already serves hot rows from memory at ~2ms — comparable to what Redis would offer. Not tested because the reasoning already ruled it out.
2. **response_model removed — falsified**: dropped Pydantic response validation, returned raw `JSONResponse`. p99 stayed ~1.53s — confirms the big cost was in dependency *resolution*, not response serialization.
3. **Raw `Request.query_params` — real, modest win**: bypassing FastAPI's `Query()` injection dropped p99 from ~1.4-1.6s to ~1.34-1.38s. Re-profiling confirmed `solve_dependencies` shrank.
4. **Access-log write discovered**: Gunicorn's `--access-logfile` writes a line per request through Python's `logging` module — a comparably-sized, previously-unnoticed cost.
5. **Pool tuned to 22×4**: 88 total connections, under Postgres's 97 non-superuser slots (100 − `superuser_reserved_connections=3`). Effect present but small/noisy — capped by CPU, not connection count.
6. **Verdict**: CPU stays saturated with no single dominant cost left — the remaining costs (dependency resolution, DB round-trip, response serialization, access logging) are now all comparably small. Since the host only has 4 physical cores, more replicas on the *same* machine would not add capacity — real horizontal scaling needs additional hardware.

## Key lesson: master vs. worker

The single most important distinction in this whole diagnosis: the Gunicorn **master/arbiter process spawns and monitors workers but never handles an HTTP request itself**. Profiling `--subprocesses` off the master mixes its own internal bookkeeping threads into the same view as real request-handling work — which is exactly what produced the misleading `_worker` finding in Flow 3. Always profile a **worker** PID directly for request-path questions; reach for `--subprocesses` only when deliberately wanting the aggregate picture.
