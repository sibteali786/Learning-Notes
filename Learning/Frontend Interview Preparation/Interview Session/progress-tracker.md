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
| 2026-07-20 | useEffect vs useLayoutEffect + bug case | React hooks | pass | no | Strong — correct timing/sync distinction + canonical tooltip flicker example |
| 2026-07-20 | useLayoutEffect prod pitfall (blocking) | React hooks | wrong | yes | Said fetch would block paint (fetch is async, doesn't block); missed real answer: sync work in body blocks paint (DOM measurement/layout thrashing) |
| 2026-07-20 | Intersection Observer: what/why/use case | Browser internals | fail | yes | No knowledge at all — confirmed flagged weak spot |
| 2026-07-20 | GraphQL vs REST (HxLabs) — benefit + downside | GraphQL | partial | yes (downside half) | Benefit example weak (just a query param case, not real over/under-fetch story); downside skipped entirely — missing N+1/caching/query-depth answers |
| 2026-07-20 | Mentoring story (WhatsNextPlease) | Leadership | pass (polish) | no | Concrete gap/action/outcome but no metric, no follow-up on whether it stuck — tighten before Tuesday, not a requeue topic |
| 2026-07-20 | Event bubbling vs capturing + delegation use case | JS fundamentals | partial | yes | Delegation use case right; phase mechanics wrong (said bubbling "skips" capturing — both phases always run); code bug: `handler()` called immediately instead of passed as ref |

## Requeue Queue

(empty — populated during sessions)

## Session History

### 2026-07-19
- Session started. Tracker created. Resume content captured inline (Hill Country Coders, Ensemble UI, HxLabs, Gul-e-Shaor).
- In progress.
