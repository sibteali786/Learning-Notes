# Drill Patterns

Scenario-style question PATTERNS, not fixed Q&A. Each maps to a numbers.md section. Tag legend: **[Recall]** = raw memorization of a number, **[Applied]** = dimensional-analysis / Fermi estimation using one or more numbers. When quizzing, instantiate a concrete question from a pattern (swap in real values), don't recite the pattern verbatim.

---

## Compute / Memory Hierarchy

- **[Recall]** Given a code snippet doing repeated random access into a large array that doesn't fit in L2 but does fit in RAM vs. one that thrashes to swap/SSD — ask which is faster and by roughly what factor.
- **[Recall]** Describe a profiler flame graph showing time spent in a mutex lock vs. a network call in the same function — ask which dominates and by how many orders of magnitude.
- **[Applied]** Given a batch job doing N sequential 1MB reads from SSD vs. the same N reads over network from a remote cache — ask for estimated total wall-clock time for each and which to pick under a latency budget.
- **[Applied]** Given a hot loop with an accidental cross-AZ call inside it (e.g. discovered in a code review), ask to estimate the added latency per iteration and total slowdown for a known iteration count.

## Storage — Item Sizes

- **[Recall]** Describe a data type (a struct/record with named fields: IDs, timestamps, short strings) — ask to eyeball its size in bytes and round to a clean number.
- **[Applied]** Given DAU and an action-per-user-per-day (e.g. photo uploads, chat messages, log lines) plus an item size, ask to derive bytes/day, and then GB or TB/year.
- **[Applied]** Given a comparison prompt ("a service ingests roughly one Wikipedia's worth of data every week") ask what that implies about GB/day and whether a single modern SSD instance keeps up.

## Caching

- **[Recall]** Describe a cache sizing scenario (dataset size, e.g. "400GB of session data") — ask whether it fits comfortably on a single modern cache instance or needs sharding.
- **[Applied]** Given QPS and cache node throughput ceiling, ask to estimate how many cache nodes are needed and whether that's a genuine architectural concern or premature.
- **[Applied]** Present a candidate's design that adds a cache in front of an indexed single-row DB lookup "to reduce latency" — ask whether that's justified given typical indexed-lookup latency, or over-engineering.

## Databases

- **[Recall]** Given a dataset size and write throughput (e.g. "8TB, 3k writes/sec"), ask whether sharding is warranted under 2026 single-instance limits.
- **[Applied]** Given entity count and average row size (e.g. "10M businesses, ~1KB/row, plus reviews at 5x volume"), ask to derive total storage and whether it changes the sharding decision.
- **[Applied]** Given a write-heavy scenario (e.g. "5k writes/sec of simple inserts"), ask whether a message queue is needed to buffer writes, or whether a single well-tuned instance already handles it.
- **[Recall]** Describe a backup/recovery scenario where nightly backups are starting to take hours — ask what threshold typically triggers sharding/partitioning consideration.

## Application Servers

- **[Recall]** Given a metric snapshot (CPU%, memory%, connection count) for an app server fleet, ask which metric is the actual bottleneck signal and whether scale-out is warranted.
- **[Applied]** Given expected concurrent connections for a service, ask to estimate how many app server instances are needed at 2026 per-instance connection ceilings.
- **[Applied]** Given an auto-scaling scenario with a traffic spike, ask whether container/instance startup time (30-60s) is fast enough to absorb it or whether pre-provisioning is needed.

## Message Queues

- **[Recall]** Present a design where a queue is inserted into a synchronous request path "for decoupling," ask whether added latency is acceptable given modern broker latency.
- **[Applied]** Given expected message volume/sec and broker throughput ceiling, ask to estimate broker count needed.
- **[Applied]** Given a retention requirement (e.g. "replay last 30 days of events") and per-message size, ask to estimate storage needed per broker and whether it's feasible.

## Network / Cross-Region

- **[Recall]** Describe a synchronous call chain that crosses regions (e.g. us-east → eu-west) on the hot path — ask to estimate the RTT tax and whether a sub-200ms p99 SLA survives it.
- **[Applied]** Given a multi-hop request (client → app server → DB, with one hop cross-AZ) ask to sum expected latency contributions and flag the dominant term.
- **[Recall]** Compare same-AZ vs cross-region latency order of magnitude given a real pair of regions — ask for the right ballpark (ms vs tens of ms vs hundreds of ms).

## Business / Scale (Fermi / Dimensional Analysis)

- **[Applied]** Classic Fermi chain: given DAU and an item-size assumption for a feed/timeline system, ask to derive daily storage growth from first principles (items/user/day × size/item × users).
- **[Applied]** Given a real-world comparison (e.g. "Netflix-scale video hours/day"), ask to reason from an order-of-magnitude anchor to a derived metric (e.g. estimate peak concurrent streams or bandwidth).
- **[Applied]** Given a partial breakdown missing one factor (e.g. storage/day known, storage/item known, users/day unknown), ask to back-solve the missing dimension.
- **[Recall]** Ask for the order of magnitude of a well-known metric (DAU of a major platform, searches/sec at a search engine) as a sanity-check anchor.
