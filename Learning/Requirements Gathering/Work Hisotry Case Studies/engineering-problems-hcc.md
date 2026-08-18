# HCC CRM Platform — Engineering Problem Log

Verified against git history via Claude Code, author-filtered to your commits.

---

## 1. Keycloak Audience-Validation Bug ✅
**Repo:** identity-provider-shared-infra | **Commits:** `713614e` → `f343037` → `813cb49` → `cfbb372`

### Problem
Token verification (`jwt.verify({ audience: clientId })`) was failing in a way that wasn't immediately obvious why.

### Root Cause
Keycloak's default `aud` (audience) claim is `account`, not the client ID — a Keycloak-specific behavior that doesn't match the "audience = client ID" assumption baked into most generic JWT verification setups.

### Solution
Disabled strict audience validation on that claim; instead validate the `azp` (authorized party) claim against the expected client ID — which is Keycloak's actual mechanism for identifying the requesting client.

### Investigation Arc (the real interview story)
`713614e` (debug logging added) → `f343037` (comprehensive step-by-step logging) → `813cb49` (standalone JWT-verify CLI diagnostic script written next day) → `cfbb372` (actual fix + cleanup of debug logging). A classic bug → over-logging → build a tool → find it → clean up arc.

### Alternatives Considered
- Continuing to fight the `aud` claim (e.g. reconfiguring Keycloak to emit a different audience) — rejected in favor of validating the claim Keycloak actually uses for this purpose (`azp`)

### Tradeoffs
- ✅ Correctly aligned with Keycloak's actual token semantics instead of fighting them
- Building a standalone CLI diagnostic script mid-investigation is worth mentioning — shows escalation from "add more logs" to "build a repeatable tool" when logging alone wasn't converging

### Improvements
- The diagnostic CLI script could be kept as a permanent debugging tool for future token issues rather than a one-off

---

## 2. Dual-IdP Custom Attribute (`wnp_role`) ✅
**Repo:** identity-provider-shared-infra | **Commits:** `8961cb8`, `a3258e7`, `813cb49`

### Problem
Needed a custom `wnp_role` attribute usable by both Keycloak (local) and AWS Cognito (staging/prod), consistently available in issued tokens.

### Root Cause
Custom attributes aren't available by default in either IdP — Keycloak requires declaring them in the user profile schema before they can be set, and Cognito requires an explicit custom attribute definition.

### Solution
- **Keycloak** (`8961cb8`): declared via the `components` key in `realm-export.json` using the declarative user profile provider, admin-only editable
- **Cognito** (`a3258e7`): matching `StringAttribute` definition for `wnp_role`
- **Both** (`813cb49`): protocol mapper wiring `wnp_role` into ID and access tokens for both clients, so downstream services see the same attribute regardless of which IdP authenticated the user

### Alternatives Considered
- Top-level `userProfileConfig` in Keycloak — not supported; the `components` key is the correct encoding (this was a real gotcha, not a stylistic choice)

### Tradeoffs
- ✅ Consistent attribute available across both IdPs, abstracting the dual-provider complexity from downstream consumers
- ⚠️ Two independent schema definitions to keep in sync (Keycloak realm config + Cognito attribute schema) — no shared source of truth between them

### Improvements
- A shared config/schema definition generating both the Keycloak `components` block and the Cognito attribute definition would remove the manual-sync risk

---

## 3. Role/Group Sync — Token Claims to App Enum ✅
**Repo:** identity-provider-shared-infra | **Commit:** `b1e2df1`

### Problem
Keycloak issues roles across two different claim shapes (`realm_access.roles` and `resource_access[clientId].roles`) — needed to map these into the app's own `UserGroup` enum reliably.

### Solution
Merges both role sources, filters to only recognized `UserGroup` values, silently drops unrecognized roles.

### Tradeoffs
- ⚠️ Silent drop of unrecognized roles is a deliberate but risky choice — a role added in Keycloak that isn't yet mapped in the app enum disappears without any error or log, which could mask a real config gap
- ✅ Prevents unknown/malformed roles from ever reaching app logic in an unexpected shape

### Improvements
- Log (not just drop) unrecognized roles at sync time, so a Keycloak/app enum mismatch is visible rather than silent

---

> Note: the shared-webhook delivery-tracking system and the merge-tag validation work are documented in full in `engineering-problems-email-module.md` (richer version, superseding earlier drafts here).

## 4. Frontend Selection Performance — useState → useRef + Virtualization ✅
**Repo:** hcc-admin-v2 | **Commit:** `4bf4f73` (May 14)

### Problem
A bulk-selection UI (contact list drawer) became sluggish as selection size grew — every checkbox toggle felt laggy.

### Root Cause
`useState({})` for the selection map meant every single toggle triggered a full object-spread copy of the entire map (O(n) per toggle) plus a full re-render of the component tree — the real cost was React re-render overhead, not the underlying computation.

### Solution
- Replaced `useState` with a mutable `useRef` for the selection map (no copy, no re-render on mutation)
- Added a cheap version counter, incremented explicitly to trigger a re-render only when actually needed
- Added `react-window`'s `FixedSizeList` for the selected-members panel, with `ResizeObserver`-driven sizing, to virtualize rendering of large selected-item lists

### Alternatives Considered
- Web workers to offload the computation — rejected because the bottleneck was DOM/re-render cost, not CPU-bound computation; a web worker wouldn't have addressed the actual cost

### Tradeoffs
- ✅ Eliminates O(n) copy-per-toggle and unnecessary re-renders; virtualization keeps DOM node count bounded regardless of list size
- ⚠️ `useRef`-based state requires manual re-render triggering — more error-prone than `useState` if a future contributor mutates the ref without bumping the version counter

### Improvements
- Already a clean, complete fix; the "identified the real bottleneck (render cost, not compute cost) before reaching for the wrong tool (web workers)" framing is the strongest part of this story

---

## 5. `assignedTo` Filter Bug (ReferenceError, likely still unfixed) ⚠️
**Repo:** HCC-adam-backend | **Commit:** `5561...df` "Refactor client model and controller to use ObjectId for assigned fields" (Apr 28)

### Problem — corrected from original recollection
Originally recalled as a name-format string mismatch (`"Adam Khan"` sent by frontend, DB returning empty). **Actual bug is different and more serious:** during a migration from flat string fields to `{ id: ObjectId, name: String }` sub-objects, the controller destructures `assignedToId` from `req.query` but then references an **undeclared `assignedTo` variable** in the filter condition — a `ReferenceError` at runtime, caught by try/catch and surfacing as a generic 500 error, not a silent empty result.

### Status
**Appears unfixed at HEAD** — no later commit from you addresses it.

### Why this is still good interview material
- Shows you can accurately diagnose a bug from symptoms even when your own memory of the mechanism was wrong — "I recalled this as a data-format issue; on re-investigation, it's actually a leftover variable reference from an incomplete schema migration"
- Real, concrete, fixable — could point to the actual fix as a "here's what I'd do" answer

### Recommended Fix
Reference `assignedToId` consistently in the filter condition instead of the undeclared `assignedTo`, and verify the query still matches on the correct `ObjectId` sub-field path post-migration.

---

## 6. Local/Prod Redis Separation ⚠️ (inferred, not fully confirmed)
**Repo:** emailControllerAuth2 | **Commits:** `9389ebd` (Dec 30) → `93b6b62` (Apr 21, ~4 months later)

### Problem
Original `docker-compose` was wired only to a single cloud Redis (Redis Labs) endpoint with hardcoded credentials — no isolated local Redis service existed for development.

### Solution
`93b6b62` added `docker-compose.redis-local.yml`, an isolated local Redis on a distinct port.

### Evidence Caveat — be honest about this if asked
No commit message explicitly narrates "local dev workers consumed production queue jobs." The mechanics support that story (unnamespaced `send-bulk-email` queue name, single shared credential-bearing compose file before the fix) — but this is **inferred from the setup, not proven by a commit**. If you recall this incident clearly from memory/Slack, that's your source of truth for the narrative; don't present the git evidence alone as proof of the incident in an interview.

### Tradeoffs
- ✅ Isolated local Redis removes the *possibility* of local/prod queue collision going forward
- ⚠️ ~4 month gap between initial setup and the fix — worth having an honest answer for why, if you remember (e.g. didn't surface as a problem until team grew, or discovered incidentally)

---

## Corrections to Prior Recollection (don't repeat these in an interview)
1. **No GraphQL exists in HCC-adam-backend.** It's plain REST/Express + Mongoose.
2. **No RBAC/role-routing commits found in HCC-adam-backend under this authorship** — the BGC/Sales Rep/Admin/TaskTeam endpoint-routing work isn't in this repo's history; don't cite it as located here without re-verification.
3. **`contactListController.js` / `normalizeMembers` doesn't exist in HCC-adam-backend.**
4. **Queue technology is Bull (v4), not BullMQ** — correct this in resume/portfolio language.
