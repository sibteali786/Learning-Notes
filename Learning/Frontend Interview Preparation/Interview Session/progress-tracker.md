# Interview Prep Progress Tracker — LAAM Senior Frontend Engineer

Interview date: Tuesday (next occurring after 2026-07-19)

## JD Requirement Checklist

| Requirement | Status | Notes |
|---|---|---|
| React.js + TypeScript | untested | |
| Vue.js | untested | Resume is React-heavy; may need to address gap/transfer story |
| State mgmt (Redux/Context) | weak (self-reported) | Daily driver is Zustand — needs Redux/Context drilling |
| REST/GraphQL integration | untested | HxLabs project used GraphQL |
| Testing (Jest/RTL/Cypress) | untested | JD: dev-owned testing, no separate QA |
| Accessibility | untested | |
| Performance / responsive | untested | |
| Build tools (Webpack/Vite) | untested | |
| Mentoring | untested | Lead Engineer title at Hill Country Coders — has story material |
| Browser internals (CRP, Core Web Vitals, Intersection Observer) | weak (self-reported) | Failed Intersection Observer before — hit hard |
| **Scope note** | | 2026-07-20: user flagged interview may be Full Stack, not pure frontend. Adding below rows. Frontend rows above still in scope. |
| NestJS (architecture, DI, modules) | untested | |
| Node.js internals (event loop, streams, cluster) | untested | |
| PostgreSQL (design, indexing, query optimization) | untested | |
| Prisma ORM (query methods, relations, migrations) | untested | |
| API design best practices (REST/GraphQL API design, not just consumption) | untested | |
| React lifecycle/hooks/state mgmt/memoization/props drilling (full-stack-lens re-ask) | partially covered | Already drilled hooks/context/memoization above from frontend angle |

## Question Log

| Date | Question | Tier/Topic | Verdict | Requeued? | Notes |
|---|---|---|---|---|---|
| 2026-07-20 | Closure def + real example | JS fundamentals | weak | yes | Def ok, example weak (setState in useEffect not a real closure demo) |
| 2026-07-20 | Implement debounce | JS coding | pass | no | Minor typo (timeoutID/timeoutId case mismatch), logic correct |
| 2026-07-20 | Context API vs Zustand + pitfall | React state mgmt | weak→resolved | partial | First pass incomplete (only pitfall, no "why Context" answer); resolved on follow-up code task (useMemo + split contexts) |
| 2026-07-20 | Fix Context re-render via code | React perf | pass | no | Correct approaches (useMemo, split contexts), minor JSX/var-name typos |
| 2026-07-20 | Promise states + immutability | JS fundamentals | partial | yes | States correct, never stated immutability rule explicitly, 2 code bugs (swallowed rejection via catch, unconditional finally) |
| 2026-07-20 | Promise immutability requeue | JS fundamentals | resolved (mostly) | no | Correctly stated settled promise never changes state; admitted not knowing "why" — spec guarantee for safety/no race conditions. Low-risk gap, have 1-liner ready |
| 2026-07-20 | useEffect vs useLayoutEffect + bug case | React hooks | pass | no | Strong — correct timing/sync distinction + canonical tooltip flicker example |
| 2026-07-20 | useLayoutEffect prod pitfall (blocking) | React hooks | wrong | yes | Said fetch would block paint (fetch is async, doesn't block); missed real answer: sync work in body blocks paint (DOM measurement/layout thrashing) |
| 2026-07-20 | useLayoutEffect prod pitfall (requeue #2) | React hooks | still weak | yes (3rd pass needed) | Heavy sync computation correct now; REPEATED async/await-blocks-paint misconception. Needs one more pass — this is a recurring gap, flag as priority before Tuesday |
| 2026-07-20 | useLayoutEffect requeue #3 (await/paint T-F check) | React hooks | pass | resolved | Correctly said await does NOT block paint, correctly justified via event loop control handoff. Misconception fixed |
| 2026-07-20 | Intersection Observer: what/why/use case | Browser internals | fail | yes | No knowledge at all — confirmed flagged weak spot |
| 2026-07-20 | IO requeue: implement useLazyImage hook | Browser internals | weak-recovering | watch, not hard requeue | Concept internalized after explanation (unobserve after load, rootMargin/threshold, cleanup); code has structural bug (braces misplaced — observe/cleanup fell outside useEffect), typo isInteresting/isIntersecting, isLoaded never wired |
| 2026-07-20 | GraphQL vs REST (HxLabs) — benefit + downside | GraphQL | partial | yes (downside half) | Benefit example weak (just a query param case, not real over/under-fetch story); downside skipped entirely — missing N+1/caching/query-depth answers |
| 2026-07-20 | GraphQL downsides requeue (caching + query cost) | GraphQL | still partial | yes (2nd requeue) | Named N+1 (valid but off-target — asked specifically for caching/query-depth), missed both requested topics. Priority gap before Tuesday |
| 2026-07-20 | Mentoring story (WhatsNextPlease) | Leadership | pass (polish) | no | Concrete gap/action/outcome but no metric, no follow-up on whether it stuck — tighten before Tuesday, not a requeue topic |
| 2026-07-20 | Event bubbling vs capturing + delegation use case | JS fundamentals | partial | yes | Delegation use case right; phase mechanics wrong (said bubbling "skips" capturing — both phases always run); code bug: `handler()` called immediately instead of passed as ref |
| 2026-07-20 | Bubbling/capturing requeue (addEventListener 3rd arg) | JS fundamentals | pass | resolved | Correct: true=capture, false=bubble (default), parent capture fires before child capture (root→target order) |
| 2026-07-20 | Closures: private var + var-in-loop pitfall (requeue) | JS fundamentals | pass | resolved | Correct private counter pattern (minor typo), correct var-in-loop fix; asked clarifying Q on function-scope which was answered well |
| 2026-07-20 | useMemo vs useCallback — when memoizing doesn't help | React perf | pass | no | Strong — correct pairing w/ React.memo, React 19 compiler awareness, correct "no consumer = wasted" case |
| 2026-07-20 | RTL testing: mock/assert/behavior-vs-implementation | Testing | pass | resolved | Correct core point (spy≠behavior proof), correct sync/async query usage (getByRole vs findByRole), correct error-path mocking |
| 2026-07-20 | Node event loop phases + setTimeout vs setImmediate | Node internals (full-stack) | partial | yes | setImmediate/setTimeout distinction correct; phase order garbled (said poll before timers — actual order: timers→pending callbacks→idle/prepare→poll→check→close) |
| 2026-07-20 | Event loop phase order requeue | Node internals (full-stack) | pass | resolved | Correct order stated: nextTick/microtask → timers → idle/prepare → poll → check → close callbacks, draining nextTick/microtask between every phase |
| 2026-07-20 | B-tree index + when NOT to index | PostgreSQL (full-stack) | partial | yes | Write-cost tradeoff solid; never explained B-tree structure/mechanics (balanced tree, O(log n), sorted, range-query support) |
| 2026-07-20 | B-tree structure requeue | PostgreSQL (full-stack) | still partial | flag as known gap | Structural facts right (sorted keys, balanced, order=branching factor); missed WHY good for ranges (linked sorted leaf nodes → sequential scan; hash index can't do this). Known gap going into Tuesday |
| 2026-07-20 | Prisma N+1 problem + fix | Prisma/ORM (full-stack) | pass | no | Concept + fix (include/select) correct; code bugs: await inside forEach (no-op), findUnique wrong signature, typo |
| 2026-07-20 | REST pagination design: offset vs cursor | API design (full-stack) | partial | yes | Tradeoffs correct (drift, no page-jump) but never committed to a recommendation; missed OFFSET perf degradation (scan-and-discard cost) as key reason cursor wins at scale |
| 2026-07-20 | Pagination requeue — commit + perf reason | API design (full-stack) | pass | resolved | Committed to cursor-based for high-write infinite-scroll feed, correctly cited offset scan-and-discard cost as the perf reason |

## Requeue Queue

(empty — populated during sessions)

| 2026-07-20 | NestJS: Guard vs Interceptor vs Middleware | NestJS (full-stack) | pass | no | Correct order/context for all three; undersold interceptor's before+after wrapping (RxJS pipe), only described after-side use cases |
| 2026-07-20 | Component body console.log timing + why it matters | React lifecycle | partial | no (noted) | Timing correct (render phase, before commit); missed "why it matters" — impure render risk, StrictMode double-invoke, discarded renders never commit |
| 2026-07-20 | useEffect search bug (race condition) | useEffect pitfalls | partial | yes | Good instinct (debounce) but missed actual bug: no cleanup/AbortController → stale out-of-order response can overwrite newer results |
| 2026-07-20 | useContext with no Provider above — what happens | useContext | fail | yes | No idea. Correct answer: falls back to createContext default value; if no default given, destructuring undefined throws TypeError. Wrapper hook pattern (throw if !context) is the senior-level fix |

## Session History

### 2026-07-19
- Session started. Tracker created. Resume content captured inline (Hill Country Coders, Ensemble UI, HxLabs, Gul-e-Shaor).
- In progress.
