# Progress — SM-2 Spaced Repetition Tracking

One entry per topic (matches numbers.md/drills.md section headers). SM-2 algorithm, standard rules:

- After each answer, self-rate quality `q` 0-5 (0=blackout, 3=correct with difficulty, 5=perfect).
- If `q < 3`: `repetitions = 0`, `interval_days = 1` (reset — treat as new).
- If `q >= 3`:
  - `repetitions == 0` → `interval_days = 1`
  - `repetitions == 1` → `interval_days = 6`
  - `repetitions >= 2` → `interval_days = round(interval_days * ease_factor)`
  - `repetitions += 1`
- Ease factor update (always, any q): `ease_factor = max(1.3, ease_factor + (0.1 - (5-q)*(0.08 + (5-q)*0.02)))`
- `next_review_date = today + interval_days`
- `mastered = true` once `interval_days >= 21` (still occasionally resurfaced, deprioritized vs. due items).

All topics seeded fresh — repetitions=0, interval=0, due today (2026-07-23).

---

## Topics

### Compute / Memory Hierarchy
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: incorrect
- mastered: false

### Storage — Item Sizes
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: incorrect
- mastered: false

### Caching
- ease_factor: 2.18
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: correct (low confidence)
- mastered: false

### Databases
- ease_factor: 2.18
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: correct (low confidence)
- mastered: false

### Application Servers
- ease_factor: 2.18
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: correct (low confidence)
- mastered: false

### Message Queues
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: incorrect
- mastered: false

### Network / Cross-Region
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: incorrect
- mastered: false

### Business / Scale (Fermi)
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-24
- last_result: incorrect
- mastered: false

---

## History Log

(append-only, newest last)

| Date | Topic | Question (paraphrase) | My Answer | Correct? | Self-rating (0-5) | Notes |
|---|---|---|---|---|---|---|
| 2026-07-23 | Compute / Memory Hierarchy | 10k sequential 1MB reads: local SSD vs remote cache over network, estimate wall-clock each | SSD ~50s (5ms/read), network ~10-100s | No | 1 | Used 5ms/read for SSD (actual ~1ms → 10s). Also conflated cache-op latency (<1ms, small KV) with 1MB transfer time (bandwidth-bound, ~1-1.5ms/MB). Correct order: SSD ~10s, network ~13s — comparable, not 5x apart. |
| 2026-07-23 | Storage — Item Sizes | 20M DAU x 4 photos/day x 3MB, estimate daily ingest storage and single-SSD-instance fit at 30-day hot retention | 240PB/day, doesn't fit single instance | No | 1 | Off by 1000x: 240e6 MB = 240TB not 240PB (MB->TB is 10^6, not 10^9). Right conclusion (doesn't fit single ~60TB SSD instance) but for wrong magnitude — flag unit-conversion care, not a concept gap. |
| 2026-07-23 | Caching | 400GB session data, 50k ops/sec, single cache instance sub-ms reads — sharding needed? | No sharding needed, fits under 1TB/100-200k ops ceiling | Yes | 2 | Answer correct but low self-confidence — reinforce, don't treat as mastered yet. |
| 2026-07-23 | Databases | Postgres at 8TB, 3k WPS simple inserts — sharding justified? | Premature, under 64TB storage and 10-20k WPS ceilings | Yes | 2 | Correct but low confidence — same pattern as Caching Q, reinforce. |
| 2026-07-23 | Application Servers | 800k concurrent connections, 100k+/instance ceiling — how many instances, good/bad architecture? | 8 instances, unsure if good/bad architecture | Yes | 2 | Math right (add headroom, ~10-12 realistically). Conceptual gap: didn't recognize horizontal scaling here is expected/normal, not a red flag — contrast with premature-scaling pattern from DB/cache questions. |
| 2026-07-23 | Message Queues | Sync checkout API waits on queue write before responding — acceptable given modern broker latency? | Cited correct 1-5ms number but reasoned via "checkout is rare (Black Friday)" instead of latency-budget fit | No | 1 | Number recall was right; reasoning conflated throughput/scale concern (traffic spikes) with a latency-budget question. Re-drill: sync-flow latency questions are about ms-vs-SLA-budget, not request frequency. |
| 2026-07-23 | Network / Cross-Region | us-east to eu-west sync call on checkout hot path, 200ms p99 SLA — fits budget? | Used correct 150ms cross-region number but concluded "much lower than budget" | No | 1 | Number correct but interpretation wrong: 150/200 = 75% of budget consumed by one hop, not "much lower" — that's a red flag, not comfortable margin. Recurring pattern: needs to convert raw numbers into % of budget/threshold, not just compare magnitude loosely. |
| 2026-07-23 | Business / Scale (Fermi) | 30M DAU x 50 views/day x 200KB, daily egress — one server or many, and why? | Storage math correct (300TB/day) but didn't convert to bandwidth (bytes/sec, bits/sec) or compare vs instance network ceiling — concluded "cannot" without the calc | No | 1 | Same pattern as Network Q: raw total computed fine, but didn't push through to the actual threshold comparison (Gbps vs 25-100Gbps instance ceiling) needed to justify the verdict. Also didn't know egress terminology or bytes->bits (x8) conversion for bandwidth. |
