# WhatsNextPlease + Chat App — Engineering Problem Log

Verified against actual git history. All items below are commit-checked and interview/portfolio ready.

---

## 1. Atomic IDP Migration with Rollback ✅
**Repo:** whatsnextplease-monolith (backend) | **Commit:** `764146b`

### Problem
Auto-migrating users from legacy JWT to Keycloak/Cognito on signin required two steps across two systems: create user in IDP, then link via `cognitoSub` in Postgres. A failure between those steps risks an orphaned IDP account with no working login path.

### Root Cause
No shared transaction is possible across Postgres and an external IDP (Keycloak/Cognito) — inherent limitation of migrating identity across systems live, not a coding mistake.

### Solution
Designed defensively from the very first commit (not a bug caught later):
1. Verify password before any IDP call (fail fast, no wasted IDP writes)
2. Create IDP user
3. Attempt DB transaction to link `cognitoSub`
4. On DB failure: explicitly delete the just-created IDP user (compensating action), fall back to legacy JWT for that login

```typescript
const createResult = await idpAdmin.createUser({...});
try {
  await prisma.$transaction(async tx => { /* link cognitoSub */ });
} catch (dbError) {
  logger.error('Database user creation failed, rolling back IDP user:', dbError);
  await idpAdmin.deleteUser(cognitoSub).catch(deleteError => { /* log */ });
}
```

### Alternatives Considered
- **Saga/outbox pattern with durable job queue** — correct even across process crashes mid-migration, rejected as over-engineered for signin-time migration on an internal tool

### Tradeoffs
- ✅ No orphaned accounts under normal failure modes
- ⚠️ Not truly atomic — a crash exactly between IDP creation and rollback attempt leaves an orphan (accepted, low-probability risk)
- ⚠️ **Known gap:** a separate admin-triggered bulk migration path (`migration.controller.ts`) has no rollback logic at all — same risk exists there, unaddressed

### Improvements / What I'd Do Differently
- Bring the bulk migration endpoint up to the same rollback standard as the signin path
- Add monitoring/alerting on orphaned-IDP-user rate to catch the non-atomic edge case in production

---

## 2. Private GitHub Package Auth Across 3 Build Environments ✅
**Repo:** whatsnextplease-monolith | **Commits:** `b0c4bfe` → `363cd69` → `85179d2` → `bac29d3` → `f35094d` → `51eba29`

### Problem
`@HillCountryCoder/auth-client` (private GitHub Package) failed to install with 401/403 across GitHub Actions, Vercel, and local Docker builds — three environments, three different auth mechanisms needed, in a monorepo where Vercel's default install pulls in backend workspace dependencies it doesn't need.

### Root Cause
- GitHub Actions' default `GITHUB_TOKEN` lacks cross-repo package read access
- Vercel has no native GitHub Packages authentication
- Monorepo `pnpm install` pulls all workspaces by default, including backend (which needs the package) even when only deploying frontend

### What Actually Happened (messier than initially framed)
Two separate credential-leak incidents preceded the final fix — a raw PAT was hardcoded in `.npmrc` (`b0c4bfe`), swapped to a placeholder same-day (`363cd69`), then a **second** raw PAT got hardcoded in a later commit (`85179d2`). The eventual fix deleted `.npmrc` from the repo entirely (`bac29d3`) rather than continuing to manage tokens in-file.

### Solution
Filtered install for Vercel — no secrets needed there at all:
```bash
pnpm install --filter=web --filter=@wnp/types --filter=@wnp/logger --filter=cdk
```
GitHub Actions uses a PAT with `read:packages` scope as a repo secret (not the default token).

### Alternatives Considered
- **`NPM_TOKEN` in Vercel env vars** — simpler setup, but means a GitHub PAT with package-read scope lives in a third-party platform
- **Separate `pnpm-workspace.vercel.yaml`** excluding backend — more explicit, adds a file-swap build step; rejected as unnecessary complexity

### Tradeoffs
- ✅ Zero secrets in Vercel; faster builds (skips unneeded backend deps)
- ⚠️ Filtered install is coupled to knowing exactly which workspaces frontend needs — silently breaks if a new shared package is added and not included in the filter list

### Improvements
- The real lesson here isn't the install strategy — it's that credentials ended up in a committed file twice before the team moved off file-based token storage. Worth naming explicitly in an interview: *"what changed my approach"* rather than presenting the final state as obviously correct from the start.

---

## 3. Env Var Typo Silently Breaking CORS in Production ✅
**Repo:** whatsnextplease-monolith (CDK stack) | **Commit:** `22027b5`

### Problem
CORS requests were being rejected in a way that didn't obviously point to its cause. The actual bug was several layers removed from the symptom.

### Root Cause
A one-character typo in a CDK Secrets Manager key name:
```diff
- ALLOWED_ORIGIS: ecs.Secret.fromSecretsManager(allowedOriginsChatSecret),
+ ALLOWED_ORIGINS: ecs.Secret.fromSecretsManager(allowedOriginsChatSecret),
```
The env var was correctly wired through Secrets Manager and CDK — just under the wrong name — so it deployed cleanly with no build or deploy error, and only surfaced as CORS rejections at runtime.

### Solution
Fixed the key name; deployed.

### Alternatives Considered
- **Runtime env var validation at boot** (e.g. zod schema check for required vars) — would have caught this at deploy time with a clear error instead of a confusing downstream symptom. Not implemented at the time; documented as a known gap.

### Tradeoffs
- ⚠️ No schema validation on required env vars at container startup — this bug class can recur
- This is a recurring theme in the codebase: `apps/docs/authentication/05-DEPLOYMENT.md` has a full troubleshooting runbook around ECS/env var issues, suggesting this wasn't a one-off

### Improvements
- Add zod (or similar) validation of all required env vars at application boot, failing fast with a clear error naming the missing/misnamed variable — instead of a downstream symptom several layers removed from the cause

---

## 4. Cross-Origin SSO Handoff for Embedded Chat App ✅
**Repo:** Chat-App-Frontend + chat-app-backend (separate repo from WNP) | **Commits:** `7d282a2` (original), `c9d2bbc` (symptom), `e11e0f2` (fix), `9af1333`/`3321aab` (refinement)

### Problem
Chat App is embedded via iframe into WNP, across different origins. Users would intermittently see "Authentication timeout" — auth handshake never completed.

### Root Cause
**Not CORS/cookies** (my initial assumption was wrong). The original design (`7d282a2`, Oct 17) had the parent (WNP) send an `INIT_CHAT` message via `postMessage`, with the iframe (Chat App) exchanging it via a REST call to its own backend. The actual bug was a **race condition**: the iframe's `postMessage` listener wasn't guaranteed to be mounted before the parent sent the init message — a classic cross-frame timing race, not a security/policy restriction.

### Solution
`e11e0f2` (Nov 10) replaced the postMessage handoff entirely: SSO token + signature passed as **URL query params**, authenticated via a **Socket.IO handshake** (`connectSocket({ ssoToken, ssoSignature })`) instead of a fire-and-forget message. Auth now rides on an already-established connection instead of assuming listener readiness.

`postMessage` remains in use today only for reauth pushes (`CHAT_REAUTH`) and presence/status events — not the initial handoff. The original REST+postMessage flow (`hooks/use-sso-auth.ts`) is now dead code.

### Alternatives Considered
- **Relaxing SameSite/CORS policy to allow direct cross-origin request** — not actually relevant since the real bug was timing, not policy; would not have fixed anything
- **Adding a "listener ready" handshake before sending `INIT_CHAT`** — plausible alternative fix that would have kept postMessage; team instead moved auth onto the WebSocket connection itself

### Tradeoffs
- ✅ Eliminates the mount-timing race entirely — no dependency on send/listen ordering across frames
- ⚠️ SSO token + signature in URL query params — same category of exposure risk (server logs, proxy logs) as query-param auth used elsewhere in these systems (see WNP SSE item below) — a consistent pattern worth being able to name as a recognized, accepted tradeoff
- The WebSocket-auth cutover needed two follow-up refinement commits within days of shipping — didn't work perfectly on the first pass

### Improvements
- Consider short-lived, single-use tokens specifically for the query-param handshake to limit exposure window
- Audit logging/proxy configs to ensure query strings carrying auth tokens aren't being logged in plaintext anywhere in the request path

---

## 5. SSE Reconnection & Multi-Tab Auth ✅
**Repo:** whatsnextplease-monolith | **Commits (real chronology):** `8eb09eb` (Jan 21) → `8592e6f`/`2c4e117` (Mar 1) → `19c0f87` (Jul 29) → `f0f23ab` (Sep 23)

### Problem
`EventSource` (SSE) can't send custom headers, so the app's standard bearer-token auth pattern didn't work for the notifications endpoint. Auth token had to be relayed via query string from the very first commit — that part never changed across the whole saga. The real bug that emerged later was a **multi-tab regression**.

### Root Cause
Browser API limitation (no header support in `EventSource`) required query-param auth from day one. Separately, a later hardening commit (`19c0f87`, adding CORS headers + server-side keepalive pings) changed `addClient` to kill any existing SSE connection for a given `userId` — meaning opening a second tab silently disconnected the first tab's notification stream. A "security/reliability improvement" commit was actually a regression.

### Solution
- Query-param token auth (`?token=${token}`, sourced from cookie client-side) — the only mechanism ever tried, present since `8eb09eb`
- Client-side reconnect with exponential backoff + jitter (`2c4e117`): `baseDelay * 1.5^retryCount`, capped at 30s
- `f0f23ab` fixed the multi-tab regression by restructuring the connection store from `Map<userId, ClientConnection>` to `Map<userId, Map<connectionId, ClientConnection>>`, tracking `tabId`, `userAgent`, `connectedAt`, with per-connection (not per-user) removal

### Alternatives Considered
- **WebSockets instead of SSE** — richer auth on handshake, rejected as unnecessary complexity for a one-directional server→client stream; SSE gives auto-reconnect for free at the browser API level

### Tradeoffs
- ⚠️ **Confirmed, real weakness:** the SSE query-param token is the same long-lived JWT used for `Authorization: Bearer` elsewhere — not a short-lived, scoped token. Exposed in server access logs and browser history for the full session lifetime, not a minimal window.
- ✅ Multi-tab now correctly isolates connections per tab/device after the fix

### Improvements
- Mint a short-lived, SSE-scoped token instead of reusing the general-purpose session JWT for the query param
- **Best interview angle:** own that a hardening commit silently broke multi-tab, and that it was caught and fixed with proper per-connection tracking — a regression-then-fix arc is more credible than a clean linear story

---

## 6. Dual Prisma Schema — Unresolved Service-Merge Debt ✅
**Repo:** whatsnextplease-monolith | **Common ancestor:** `f953344` ("feat: added web package")

### Problem
`apps/backend/prisma/schema.prisma` and `apps/web/prisma/schema.prisma` are two fully independent files — both 39 models, effectively identical content, each with its own complete `generator client` / `datasource db` block. Frontend has a genuine, independent Prisma Client with direct DB access, not a type-only stub.

### Root Cause
WNP originally started as **separate frontend and backend services**, each with their own schema. When the two were merged into a monorepo, **the Prisma schema consolidation was never actually completed** — it was logged as follow-up work and never finished, not a deliberate architecture choice. Confirmed in git history: 24 vs. 22 commits touching each schema file respectively, 7 divergent, kept in sync by hand with no automated tooling in `package.json`/`turbo.json`.

### Current State / Risk
- Any schema change must be manually applied twice, in two files, with no automated check enforcing parity
- Drift is only caught when it causes a runtime bug (type mismatch, missing field) — silent-failure risk consistent with a known pattern in this codebase (schema/data-shape mismatches failing silently rather than erroring)

### Alternatives Considered
- **Single shared schema package** (e.g. `packages/db` workspace both `apps/web` and `apps/backend` import from) — standard monorepo pattern, prevents drift by construction
- **Frontend goes through backend API only, no direct DB access** — removes the second Prisma Client entirely; larger change if frontend currently relies on direct queries for SSR performance

### Tradeoffs
- ⚠️ Live risk of drift causing silent bugs until actually resolved
- Strong, honest interview material precisely because it's unfinished: *"we merged two services and never finished consolidating the data layer — here's how I'd actually finish that migration and why."* Shows awareness of technical debt rather than only feature-shipping stories.

### Improvements
- Prioritize finishing the migration via shared-schema-package (fixes drift by construction, not discipline)
- In the interim, add a CI check diffing the two schema files and failing the build on divergence

---

## Dropped Items (confirmed not present in this repo)
- **Virus-scan timing / `NotFoundError` race** — no virus-scanning pipeline exists anywhere in this monorepo (no matching services, Lambda functions, or scan-related `NotFoundError` usages). Either lives in a separate, unsearched repo, or doesn't map to what was actually built here. Drop unless a specific service/repo can be named.
- **`ChatWindow.tsx` infinite re-render** — file doesn't exist in this repo's history under any name. Chat is implemented as an iframe embed of the separate chat-app repo (`3a4fcd0`), not an in-repo component managing message-list state via `useEffect` — the bug as originally described doesn't architecturally fit this codebase. Likely belongs to the chat-app repo, or check there next.

---

## Other Candidates (flagged, not yet full write-ups)

### A. Tenant-Scoped Unique Constraint Cleanup ✅
**Repo:** Chat App (Mongoose/MongoDB, not Prisma) | **Commit:** `1a065e1` (Nov 14, 2025)

#### Problem
Global unique indexes (`email`, `channel.name`, `attachment.metadata.s3.key`, `thread.parentMessageId`) were incompatible with multi-tenancy — they'd block legitimate duplicates across different tenants (e.g. the same email signing up under two different tenants).

#### Root Cause
Not a security regression, and not wholesale removal — it's cleanup that landed ~3.5 weeks *after* the original multi-tenant rollout (Item B). Tenant-scoped compound-unique indexes (`{tenantId, email}`, `{tenantId, username}`, `{tenantId, channelId, userId}`) had already been added during the original rollout (`f9bd51b`); this commit deleted the now-redundant global uniques left behind on those same models.

#### Solution
```js
// thread.model.ts — the one genuinely new piece of work here
-threadSchema.index({ parentMessageId: 1 }, { unique: true });
+threadSchema.index({ tenantId: 1, parentMessageId: 1 }, { unique: true, name: "tenant_parentMessage_unique_idx" });
```
`thread` had no tenant-scoped uniqueness before this commit — everything else was deleting dead global indexes already superseded by tenant-scoped ones.

#### Alternatives Considered
- Leaving global uniques in place alongside tenant-scoped ones — rejected as redundant and actively wrong (would still block cross-tenant duplicates the tenant-scoped index was designed to allow)

#### Tradeoffs
- ⚠️ `channel.name` and `attachment.metadata.s3.key` lost global uniqueness with no explicit tenant-scoped replacement in this specific commit (channel had a separate `tenant_name_idx` from the earlier rollout)
- ✅ Net effect is correct per-tenant data isolation — the "1.5 month gap between rollout and full cleanup" is the honest story: rescoping was staggered, not delivered atomically

#### Improvements
- This class of migration (adding tenant-scoped replacement indexes) is easy to leave inconsistent across models when done incrementally — a checklist or lint rule catching any `unique: true` index without a `tenantId` prefix would have caught the staggered rollout earlier

---

### B. Multi-Tenant Rollout → Regressions → Fixes ✅
**Repo:** Chat App | **Commits:** `182e3c6`, `f9bd51b`, `3f062a2`, `8d76ea1` (rollout, Oct 13–14) → `37d7930` (fix #1, Oct 17) → `9313e1c` (fix #2, Oct 20)

#### Problem
A 4-commit tenant-isolation rollout landed in ~25 hours (Oct 13–14). It took a full week and two follow-up fix commits before tenant isolation was actually correct — including a live cross-tenant data leak.

#### Root Cause (three distinct bugs found in the diffs, not the commit messages — no error strings anywhere in the log)
1. **AsyncLocalStorage misuse:** the original middleware called `next()` *after* `AsyncLocalStorage.run()`'s callback had already returned, so downstream handlers executed with no tenant context active at all.
2. **Missing hook method — real cross-tenant leak:** the Mongoose tenant-filter plugin auto-injected tenant scoping into most query methods, but `findById` was missing from the list. Any `Model.findById(...)` call anywhere in the codebase bypassed tenant isolation entirely until fixed.
3. **Chicken-and-egg auth gap:** original refresh tokens were opaque random strings looked up via `RefreshToken.findOne({token})` with no tenant context available before the query ran — needed `tenantId` to scope the query safely, didn't have it until after.

#### Solution
- Fixed the `next()` ordering so tenant context is actually live when downstream handlers run
- Added `findById` to the tenant-plugin's auto-scoped method list
- Rewrote refresh tokens as signed JWTs carrying `tenantId` in the payload, decoded *before* any DB access, with an explicit mismatch guard: `if (user.tenantId !== tenantId) throw new UnauthorizedError(...)`
- Also removed a duplicate `next()` call in socket auth middleware — left with the commit comment `// REMOVE the second next() call - it was here`, a direct admission of the original bug

#### Alternatives Considered
- Continuing with opaque refresh tokens + a separate tenant-lookup step before the token query — rejected in favor of JWT-embedded `tenantId`, which removes the ordering dependency entirely

#### Tradeoffs
- ⚠️ Real, live cross-tenant leak existed in production-reachable code for roughly a week (`findById` bypass) before caught
- No urgency language anywhere in commit messages (checked the full log: no "hotfix"/"urgent"/"critical" convention exists in this repo at all) — signal of the severity is only visible in the diffs themselves, not communicated at commit time

#### Improvements
- A test asserting **every** Mongoose model method is tenant-scoped (rather than an allowlist that can silently miss one) would have caught the `findById` gap before merge
- This is a strong "own the mistake" interview story: ship fast, catch a real data-isolation bug via testing/review (not an external report — no evidence of one), fix it within days

---

### C. Access Token Lifetime Extended (mislabeled as refresh token) ✅
**Repo:** Chat App | **Commit:** `d0db247` (May 25, 2026)

#### Problem
Commit message reads "Extend refresh token expiration to 7 days and add validation for SSO token format" — but the diff actually changes **access token** expiry, not refresh token:
```js
// auth.service.ts — generateAccessToken
-expiresIn: "15m",
+expiresIn: "7d",
```
Refresh-token logic (already JWT-based with 7d/30d expiry since the Item B fix) isn't touched at all — the commit message mislabels or conflates the two token types.

#### Root Cause
Unclear from the commit alone — no linked bug report, no revert nearby, isolated as the only commit in a 3-week window (May 8–25). The bundling of an auth-expiry change with SSO-token-format hardening in one commit, after a long gap, is circumstantially consistent with a reactive fix, but **not confirmed** by any direct evidence (no urgency language — this repo has no "hotfix:" convention at all).

#### Solution
- Access token lifetime: 15 minutes → 7 days
- SSO token parsing hardened with an explicit format check before JSON parsing:
```js
const decodedStr = Buffer.from(token, "base64").toString("utf-8");
+if (!decodedStr.startsWith("{")) {
+  throw new Error("Invalid token format: not a valid base64-encoded JSON payload");
+}
const payload: TenantTokenPayload = JSON.parse(decodedStr);
```

#### Tradeoffs
- ⚠️ **Security-relevant regression, likely understated by the commit message:** short-lived access tokens are a core theft/replay mitigation. Going from 15 minutes to 7 days significantly widens the exposure window if a token is ever leaked, and the commit message ("extend refresh token") doesn't accurately flag that this is what changed.
- ✅ SSO format validation is a straightforward, low-risk hardening — catches malformed tokens before a JSON parse error obscures the real problem

#### Improvements
- If session longevity was the actual goal, the correct lever is refresh token expiry (already 7d/30d) paired with short-lived access tokens and silent refresh — not extending the access token itself
- Frame honestly in interviews: *"the diff doesn't match its own commit message — worth flagging as a real risk I'd want to re-audit,"* not as a clean, intentional decision

---

### D. Presence Manager — Tenant Coupling Added, Then Reversed ✅
**Repo:** Chat App | **Commits:** `24d8971` (Oct 15, added) → `4be4784` (Oct 16, reversed — one day later)

#### Problem
`PresenceManager` initially took `tenantId` as a constructor parameter (`24d8971`). One day later, that was reversed — `tenantId` removed from the constructor entirely (`4be4784`).

#### Root Cause
`PresenceManager` is instantiated once as a **process-wide singleton** (`new PresenceManager(redisClient)` in `server.ts`, wired via a service locator) — not one instance per tenant. Binding `tenantId` at construction time was structurally incompatible with that singleton pattern from the moment it was added; the design inconsistency was baked in on day one and caught almost immediately.

#### Solution
Tenant is now passed as an explicit parameter on every method call instead of bound at construction:
```typescript
async processHeartbeat(userId: string, tenantId: string, status: PRESENCE_STATUS, ...) {...}
async setUserOffline(userId: string, tenantId: string) {...}
```
Redis keys built per-call: `presence:${tenantId}:${userId}`.

#### Alternatives Considered
- **Context-based resolution (AsyncLocalStorage)** — not used here; explicit per-method parameters were chosen instead, likely simpler to reason about for a small, well-defined method surface

#### Tradeoffs
- ⚠️ **The reversal left a real, still-live bug.** The class still declares `private tenantId: string`, but it's never assigned post-reversal — permanently `undefined`. Two call sites in `processHeartbeat` (the "status changed while already online" branch) still reference `this.tenantId` instead of the local parameter:
```typescript
await this.broadcastPresenceChange(userId, this.tenantId, "online", status); // undefined
this.resetOfflineTimer(userId, this.tenantId); // undefined
```
This narrowly breaks tenant-scoped Redis keys/broadcasts specifically for existing-online-user status changes (the "came online" branch correctly uses the local param and is unaffected).

#### Improvements
- Remove the now-dead `private tenantId` field entirely to eliminate the possibility of accidentally referencing it
- Fix the two orphaned `this.tenantId` references in `processHeartbeat` — this is a concrete, still-reproducible bug worth actually fixing, not just discussing
- Good interview material specifically for architecture/singleton-vs-per-instance-state judgment questions — a design mistake caught in one day, but the reversal itself was incomplete

### E. BuildKit Secrets for Docker Builds ✅
**Repo:** whatsnextplease-monolith | **Commit:** `f35094d`
Switched from `ARG`/`ENV`-passed secrets (which persist in image layers) to Docker BuildKit's `--secret` mount (available only during the specific `RUN` step, never persisted).
```bash
DOCKER_BUILDKIT=1 docker build --secret id=GITHUB_TOKEN,src=/path/to/token/file ...
```
**Tradeoff:** requires `DOCKER_BUILDKIT=1` explicitly set — silent "secret not found" failure if someone builds without it. Pairs naturally with Problem #2 as a follow-up: after the `.npmrc` credential leaks, this ensures the build process itself doesn't reintroduce the same class of exposure in a different form.


