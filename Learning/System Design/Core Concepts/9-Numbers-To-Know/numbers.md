# Numbers to Know — Canonical Reference

Sources: [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832) (classic, ~2012-era hardware), [computers-are-fast.github.io](https://computers-are-fast.github.io/) (intuition drills), "Numbers to Know" 2026 hardware article, "Estimation" article (Fermi technique).

Two eras of numbers are kept side by side on purpose: the **gist** numbers are still what interviewers often expect verbatim (they're the "textbook" reference), but modern hardware (2026) is meaningfully faster/bigger in several places. Where they diverge, both are shown — gist labeled *(classic)*, current labeled *(2026)*. Don't silently trust old orders-of-magnitude for storage/DB sizing decisions.

---

## Metric Prefixes

**Last verified: 2026-07-23** — source: Estimation article

Stick to powers of 1000, not 1024, for interview mental math.

| Power (1000^x) | Number | Prefix |
|---|---|---|
| 0 | Unit | — |
| 1 | Thousand | Kilo (K) |
| 2 | Million | Mega (M) |
| 3 | Billion | Giga (G) |
| 4 | Trillion | Tera (T) |
| 5 | Quadrillion | Peta (P) |

---

## Compute / Memory Hierarchy (raw latency)

**Last verified: 2026-07-23** — source: gist (classic) + computers-are-fast.github.io

| Operation | Time (classic) | Comparison |
|---|---|---|
| L1 cache reference | 0.5 ns | — |
| Branch mispredict | 5 ns | 10x L1 |
| L2 cache reference | 7 ns | 14x L1 |
| Mutex lock/unlock | 25 ns | — |
| Main memory reference (RAM) | 100 ns | 20x L2, 200x L1 |
| Compress 1KB with Zippy | 3,000 ns (3 µs) | — |
| Send 1KB over 1 Gbps network | 10,000 ns (10 µs) | — |
| Read 1MB sequentially from memory | 250,000 ns (250 µs / 0.25 ms) | — |
| Round trip within same datacenter | 500,000 ns (0.5 ms) | — |
| Read 1MB sequentially from SSD | 1,000,000 ns (1 ms) | 4x memory |
| Disk seek | 10,000,000 ns (10 ms) | — |
| Read 1MB sequentially from spinning disk | 20,000,000 ns (20 ms) | 20x SSD |
| Send packet CA → Netherlands → CA | 150,000,000 ns (150 ms) | — |

**2026 reality check** (source: 2026 hardware article) — the relative ordering above still holds (RAM > SSD > disk > network), but absolute SSD numbers have improved and the *economics* have shifted: gigantic NVMe SSDs are now cheap enough that many "needs a cluster" problems from the classic era fit on one machine with local SSD. Don't reflexively add caching layers to avoid indexed SSD lookups — a simple indexed row read is sub-millisecond to a few ms, already fast enough.

---

## Storage — Item Sizes

**Last verified: 2026-07-23** — source: Estimation article

| Item | Size |
|---|---|
| A two-hour movie | 1 GB |
| A small book of plain text | 1 MB |
| A high-resolution photo | 1 MB |
| A medium-resolution image / site graphic | 100 KB |
| A tweet-length text record | ~140 B–1 KB (round up) |

Rule of thumb for sizing a record/struct: sum the fields, then round generously (323 bytes → call it 500 B or 1 KB). Precision isn't the goal.

---

## Caching

**Last verified: 2026-07-23** — source: 2026 hardware article

| Metric | 2026 value |
|---|---|
| Memory capacity | Up to ~1 TB on memory-optimized instances |
| Read latency | < 1 ms within region |
| Write latency | < 1 ms same-AZ, 1–2 ms cross-AZ |
| Throughput | 100k–200k+ ops/sec per instance (e.g. Graviton-based Redis) |

**Scale triggers:** dataset approaching 1TB, sustained throughput > 100k ops/sec, read latency requirement < 0.5ms consistently.

**Classic contrast:** older guidance assumed 32–64GB Redis instances requiring careful partial-dataset caching. That constraint is largely gone — "cache everything" is now often cheaper than engineering selective caching logic.

---

## Databases

**Last verified: 2026-07-23** — source: 2026 hardware article

| Metric | 2026 value |
|---|---|
| Storage (single instance) | Up to 64 TiB most engines, up to 256 TiB on Aurora |
| Read latency | 1–5 ms cached, 5–30 ms disk |
| Write (commit) latency | 5–15 ms |
| Read throughput | Up to 50k TPS single-node (Aurora/RDS) |
| Write throughput | 10k–20k TPS single-node |
| Concurrent connections | 5k–20k |

**Scale/sharding triggers:** dataset approaching/exceeding 50 TiB, write throughput consistently > 10k TPS, read latency needs < 5ms uncached, cross-region distribution requirement, backup/recovery windows stretching to hours.

**Common interview mistake:** premature sharding. E.g. 10M businesses × 1KB = 10GB; even 10x'd for reviews, 100GB — no sharding case. A single well-tuned Postgres does 20k+ simple writes/sec; 5k WPS does not justify a message queue.

---

## Application Servers

**Last verified: 2026-07-23** — source: 2026 hardware article

| Metric | 2026 value |
|---|---|
| Concurrent connections | 100k+ per instance |
| CPU | 8–64 cores |
| Memory | 64–512 GB standard, up to 2 TB high-memory |
| Network | 25 Gbps standard, 50–100 Gbps high-performance |
| Startup time (containerized) | 30–60 sec |

**Scale triggers:** CPU > 70–80% sustained, response latency exceeding SLA, memory > 70–80%, network bandwidth approaching instance limits.

CPU, not memory, is almost always the first bottleneck — don't shy away from memory-heavy local caching/session state on app servers.

---

## Message Queues

**Last verified: 2026-07-23** — source: 2026 hardware article

| Metric | 2026 value |
|---|---|
| Throughput | Up to 1M msgs/sec per broker |
| End-to-end latency | 1–5 ms within region |
| Message size (efficient range) | 1 KB – 10 MB |
| Storage per broker | Up to 50 TB |
| Retention | Weeks to months |

**Scale triggers:** nearing 800k msgs/sec per broker, partition count approaching 200k per cluster, growing consumer lag, cross-region replication need.

Modern queues are fast enough (sub-5ms) to sit inside synchronous request flows — reliable delivery + decoupling without forcing an async API.

---

## Network / Cross-Region

**Last verified: 2026-07-23** — source: 2026 hardware article + gist (classic)

| Path | Latency (2026) |
|---|---|
| Within a single AZ | < 1 ms |
| Across AZs, same region | 1–2 ms |
| Cross-region | 50–150 ms |

**Classic reference point (gist):** CA ↔ Netherlands round trip ≈ 150 ms — still a reasonable upper-bound anchor for cross-region/cross-ocean synchronous calls.

Bandwidth within a datacenter: 25 Gbps common, 50–100 Gbps+ on high-performance instances.

---

## Business / Scale Orders of Magnitude

**Last verified: 2026-07-23** — source: Estimation article

| Metric | Order of magnitude |
|---|---|
| DAU of major social networks | O(1B) |
| Hours of video streamed on Netflix/day | O(100M) |
| Google searches/sec | O(100k) |
| Size of Wikipedia | O(100GB) |

Treat these as ballpark anchors, not precise facts — the interview goal is directionally correct estimation, not memorized precision.
