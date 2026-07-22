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

All topics seeded fresh — repetitions=0, interval=0, due today (2026-07-21).

---

## Topics

### Compute / Memory Hierarchy
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-22
- last_result: incorrect
- mastered: false

### Storage — Item Sizes
- ease_factor: 1.96
- interval_days: 1
- repetitions: 0
- next_review_date: 2026-07-22
- last_result: incorrect
- mastered: false

### Caching
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

### Databases
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

### Application Servers
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

### Message Queues
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

### Network / Cross-Region
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

### Business / Scale (Fermi)
- ease_factor: 2.5
- interval_days: 0
- repetitions: 0
- next_review_date: 2026-07-21
- last_result: —
- mastered: false

---

## History Log

(append-only, newest last)

| Date | Topic | Question (paraphrase) | My Answer | Correct? | Self-rating (0-5) | Notes |
|---|---|---|---|---|---|---|
| 2026-07-21 | Compute / Memory Hierarchy | 10k sequential 1MB reads: local SSD vs remote cache over network, estimate wall-clock each | SSD ~50s (5ms/read), network ~10-100s | No | 1 | Used 5ms/read for SSD (actual ~1ms → 10s). Also conflated cache-op latency (<1ms, small KV) with 1MB transfer time (bandwidth-bound, ~1-1.5ms/MB). Correct order: SSD ~10s, network ~13s — comparable, not 5x apart. |
| 2026-07-21 | Storage — Item Sizes | 20M DAU x 4 photos/day x 3MB, estimate daily ingest storage and single-SSD-instance fit at 30-day hot retention | 240PB/day, doesn't fit single instance | No | 1 | Off by 1000x: 240e6 MB = 240TB not 240PB (MB->TB is 10^6, not 10^9). Right conclusion (doesn't fit single ~60TB SSD instance) but for wrong magnitude — flag unit-conversion care, not a concept gap. |
