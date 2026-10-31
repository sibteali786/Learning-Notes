# Coastal Research Work

Backend engineer at Apex Research / Coastal Research (joined early Oct 2026). Stack: Node.js + Express + Prisma + PostgreSQL backend (`apex-v2`), four Next.js partner portals (Coastal Research, PolicyTrace AI, Policy Limit Research, Apex Research) that share one backend and one partner API (`/api/v1`).

**Rule for this file:** only work that was **merged** goes in. Proposals, research pages and open PRs stay out until they merge. Branch flow is QA → staging → testprod → production. "Reached" says how far each piece had got when it was written down.

Last synced: 2026-10-23 (all PRs by `baqarali110` in `coastal-research/*`)

## At a glance

| When | Initiative | Ticket | Merged PRs | One-line impact |
|---|---|---|---|---|
| Oct 6–9 | Partner API docs brought in line with the backend | — | 7 | Partner docs in 3 portals gained 20 missing, backend-verified items |
| Oct 7–9 | Consistent error shape across the backend | — | 11 | Every error now carries `message`, `code`, `requestId`, with no breaking change for partners |
| Oct 12–15 | Partner Webhook Subscriptions API | KAN-129 | 17 | Partners manage webhooks by API, rotate secrets, send tests, see every delivery attempt |
| Oct 15 | PR-H0 session hotfix + first backend test suite | KAN-156 | 1 | Closed an MFA bypass, session revival and open self-registration |
| Oct 16 | PII masking in logs | KAN-166 | 1 | Stopped writing SSN/licence/DOB in full to logs (9,749 prod audit rows held them) |
| Oct 16 | Deactivated firms actually lose access | KAN-158 | 5 | Turning off a firm now ends its logins, keys and webhooks |
| Oct 19–22 | PR-H1 identity: one staff rule, one integrations gate, brand from the firm | KAN-171 | 6 | Closed a cross-tenant webhook leak and avoided locking out 54 of 55 firm admins |
| Oct 20–23 | PR-H2 partner surface hardening | KAN-179, KAN-154 | 5 | Staff-only powers fenced off from firm keys; 500s → clear 4xx; retries no longer file a second billable case |

**Totals (as of 2026-10-23):** 50 merged PRs across 5 repos (apex-v2 18, CoastalResearch-v2 9, PolicyTraceAI 9, policylimitresearch-v2 9, apex-research 6). 4 of them promoted QA → staging by hand.

## Themes for case studies

- **Security hardening of a multi-tenant SaaS:** PR-H0, D6, D11, PR-H1, PR-H2 (OAuth Hardening Track, epic KAN-150).
- **Evolving a live partner API without breaking anyone:** error shape (additive only), webhook API, PR-H2 (log-only flags before enforcing).
- **Checking production data before changing anything:** D11 pre-check, PR-H1 role-template finding, PR-H2 nginx and audit-log analysis.
- **Keeping one backend and four portals in step:** every backend change shipped with matching docs PRs in all portals.
- **Bringing in automated testing:** first backend suite (node:test + supertest + Testcontainers), grew from 35 to 441 tests in about a week.

---

## Contributions

### 2026-10-23 · PR-H2: partner API surface hardening
**Ticket:** KAN-179 (also resolved KAN-154) · **Repos:** apex-v2 + 4 portals · **Reached:** QA (enforcement flags still log-only)

**Problem:** Any firm's API key could do staff-only work on its own firm (mark invoices paid, change prices, approve completion) and read every researcher's name and email. Bad input answered 500. A retried case create filed a second, billable case.

**What I did**
- Added a `STAFF` scope that only keys with no firm carry, and set a new key's scope from who holds it. It runs log-only behind `STAFF_SCOPE_ENFORCE` for a watch week before it enforces.
- Mapped body-parser, file-type and DB-down failures to 400/413/415/503 with clear codes (`FILE_TYPE_NOT_ALLOWED`, `DATABASE_UNAVAILABLE`).
- Built idempotent case creation (reserve, then complete) keyed on `Idempotency-Key` for firm keys, and updated the connector retry logic to match.
- Added `WWW-Authenticate` on 401s, accurate "expired" messages, "Case not found.", and page/limit validation (log-only first).
- Wrote partner docs for all four portals and a rollout runbook.

**Impact**
- Prod analysis first: 0 staff-route writes by firm keys in 90 days, so the fence breaks nobody. About 150 file-type 500s and about 550 DB-timeout 500s in 90 days now get correct 4xx/503 answers.
- Real duplicate cases found in prod (the same externalId filed 5 times) are now prevented for callers that send the header.
- Tests: 441 unit/API + 263 integration.

**Skills:** API design, authorization scopes, idempotency, safe rollout behind flags, nginx/audit log analysis
**PRs:** apex-v2 #894 · Coastal #452 · PolicyTrace #236 · PLR #216 · apex-research #28

### 2026-10-22 · PR-H1: identity rules (staff, integrations gate, case brand)
**Ticket:** KAN-171 (replaced KAN-160, KAN-168) · **Repos:** apex-v2 + 4 portals · **Reached:** QA

**Problem:** "Staff" was decided by a hard-coded company id that never matched production. Any staff role could edit any firm's webhooks, and flipping `isGlobal` on a firm's hook sent every firm's events to that firm's server (a cross-tenant leak). The case brand came from the request body instead of the firm.

**What I did**
- Made staff a single rule (role-based, with the staff company found by `siteType`), replacing 17 literal uses.
- Gated webhooks and API tokens on `integrations:manage` and refused `isGlobal` flips for every role. Added a staff-only `integrations:all_firms` permission with an admin UI toggle.
- Made the case brand come from the firm (`BRAND_MISMATCH` otherwise).
- Follow-up #888: firms no longer learn that the other brands exist (neutral 404s and error messages).
- Portals: gated the token and webhook pages on the permission and updated the docs.

**Impact**
- A pre-check on prod found that a code-only deploy would have locked out 54 of 55 company admins, because of a seeded role-template value. I shipped a data migration instead, so 0 users lost access.
- Closed the cross-tenant webhook leak.
- Tests: 150 → 169 unit/API, 151 integration. Before/after evidence screenshots in the PR.

**Skills:** RBAC, multi-tenant isolation, data migrations, production impact analysis
**PRs:** apex-v2 #825, #888 · Coastal #414 · PolicyTrace #231 · PLR #212 · apex-research #24

### 2026-10-16 · D11: deactivated firms lose access
**Ticket:** KAN-158 · **Repos:** apex-v2 + 4 portals · **Reached:** QA

**Problem:** Turning a firm off in the admin app changed nothing. Its users still logged in, its API keys worked and its webhooks fired. Prod had 12 inactive firms, and their owners were still logging in.

**What I did**
- Checked the firm's status at login (403 `FIRM_DEACTIVATED` after the password check), in session auth, on API keys and on the live event stream (with a 60 s recheck). Webhook firing now drops only firm-scoped hooks.
- Protected the staff company from deactivation, and stopped the login lookup and account-request matching from picking a dead firm.
- Documented the new error code in all four portals.

**Impact:** Deactivation now actually removes access. Production checks (9 queries) confirmed the only affected users were internal testers, who were told before the deploy. Tests: 61 unit/API, 40 integration.

**Skills:** authentication, production pre-checks, cross-app impact analysis
**PRs:** apex-v2 #801 · Coastal #400 · PolicyTrace #230 · PLR #211 · apex-research #23

### 2026-10-16 · D6: mask PII in logs
**Ticket:** KAN-166 · **Repos:** apex-v2 · **Reached:** QA

**Problem:** SSNs, driver's licence numbers and dates of birth were copied in full into CloudWatch, webhook delivery logs and the append-only audit log. In prod: 11 SSNs, 44 webhook log rows and 9,749 audit rows, because every case update copied the SSN whether or not it had changed.

**What I did:** Added a `maskPii` helper (last four digits only, DOB fully masked, in line with IRS TTIN practice) to the request audit, webhook logs, audit service and logger. The SSN is audited only when it changes (NIST AU-3(3)). Added the case id to the CloudWatch submission line so it stays observable.

**Impact:** New log entries no longer hold full PII. No API response or webhook payload changed. Tests: 45 unit/API, 26 integration.

**Skills:** data protection, compliance standards research, logging
**PRs:** apex-v2 #795

### 2026-10-15 · PR-H0: session hotfix + first backend test suite
**Ticket:** KAN-156 · **Repos:** apex-v2 · **Reached:** QA

**Problem:** Five session defects. The MFA challenge token worked as a full session (an MFA bypass). Logging in revived every revoked session before MFA. Self-registration was still open and could create firm owners on any brand. Changing your password, or being deactivated, left your other sessions alive.

**What I did:** One commit per defect. Added a purpose check in `authenticate`, a session watermark clamp, and watermark updates on password change and deactivation, and removed the registration routes. I also built the backend's **first automated test suite** (node:test + supertest + Testcontainers Postgres).

**Impact:** Closed an MFA bypass and four related session holes. Prod checks showed self-registration had been unused since July (0 register vs 1,329 login calls in 15 days), so removing it broke nobody. The test suite: 35 tests at launch, 19 of which fail on the old code.

**Skills:** auth/session security, JWT, test infrastructure
**PRs:** apex-v2 #786

### 2026-10-15 · Partner Webhook Subscriptions API
**Ticket:** KAN-129 (KAN-136 A, KAN-137 B, KAN-138 C, KAN-139 D) · **Repos:** apex-v2 + 4 portals · **Reached:** staging

**Problem:** Partners could manage webhooks only in the dashboard, with no API, no secret rotation, no test send and no record of delivery attempts.

**What I did**
- A: `/api/v1/webhooks` CRUD with a new `WEBHOOK` scope, where the firm comes only from the key. One shared service for the dashboard and the API, plus audit entries.
- B: secret rotation, a shared signer and a test route.
- C: a `webhook_delivery_attempts` table and a deliveries endpoint. Retries re-read the webhook, which fixed a silent bug where a deleted hook was still sent to.
- D: idempotency keys, dashboard rotate/attempts routes and docs.
- Portals: webhook token creation, an "API" badge, and Send test / Rotate secret / Attempts on the Webhooks page in every portal.
- Promoted to staging by hand (cherry-picking only my commits).

**Impact:** Partners can integrate webhooks fully by API and debug failed deliveries themselves.

**Skills:** API design, webhooks/HMAC signing, retry semantics, release management
**PRs:** apex-v2 #744, #747, #758, staging #772 · Coastal #374, #380, staging #395 · PolicyTrace #224, #226, staging #228 · PLR #206, #207, staging #209 · apex-research #19, staging #21

### 2026-10-09 · Consistent error shape across the backend
**Repos:** apex-v2 + 3 portals · **Reached:** staging

**Problem:** Errors came back in different shapes, many without a machine-readable code or a way to trace a request.

**What I did:** Six small PRs that route every error through one `send()` helper. They add `message`, an always-present `code`, an optional `field`, and a `requestId`, next to the existing `error` string. Additive only: I dropped two planned PRs because they would have changed status codes that partners see. I documented the shape in the portal docs.

**Impact:** Partners and support can match any failure to a request id and handle errors by code, with zero breaking changes.

**Skills:** backward-compatible API evolution, incremental delivery
**PRs:** apex-v2 #698, #700, #702, #705, #706, #710, staging #729 · Coastal #356 · PolicyTrace #218 · PLR #201

### 2026-10-07 · Partner API docs brought in line with the backend
**Repos:** CoastalResearch-v2, PolicyTraceAI, policylimitresearch-v2, apex-research · **Reached:** staging

**Problem:** The partner API docs pages were missing behaviour the backend really has.

**What I did:** Checked the docs against the backend code and added 20 of 26 missing items: scopes, token expiry, 400/409/413/429 cards, an error-code table, rate limits, statuses, upload rules and webhook fields. I adapted each portal's brand wording.

**Impact:** Partners integrate against docs that match production behaviour.

**Skills:** technical writing, code-to-docs verification
**PRs:** Coastal #341, staging #365 · PolicyTrace #214, staging #220 · PLR #196, staging #203 · apex-research #15
