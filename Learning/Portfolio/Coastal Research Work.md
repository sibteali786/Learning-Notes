# Coastal Research Work

Backend engineer at Apex Research / Coastal Research (joined early Oct 2026). Stack: Node.js + Express + Prisma + PostgreSQL backend (`apex-v2`), four Next.js partner portals (Coastal Research, PolicyTrace AI, Policy Limit Research, Apex Research) that share one backend and one partner API (`/api/v1`).

**Rule for this file:** only work that was **merged** goes in. Proposals, research pages and open PRs stay out until they merge. Branch flow is QA → staging → testprod → production. "Reached" says how far each piece had got when it was written down.

Last synced: 2026-11-03 (all PRs by `baqarali110` in `coastal-research/*`)

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
| Oct 22–26 | Partner API docs from one source + brand leak fixes | KAN-155, KAN-193 | 12 | Four portals' docs built from one backend source; firms no longer see other brands or internal data |
| Oct 23–26 | PR-H3 data integrity, key hygiene, audit trail | KAN-197 | 1 | Firms can't overwrite researcher findings; 112k status-log rows now say who acted; wrong cancel wording fixed |
| Oct 26–29 | PR-H4 deploy safety: health check + automatic rollback | — | 37 | A deploy that doesn't come up is rolled back by itself and turns the job red, instead of a green job over a dead site; live on production since 29 Oct |
| Oct 27–30 | Faster deploys and a production disk that stops filling up | KAN-206 | 27 | PLR's QA deploy 9.6 → 5.5 min, PolicyTrace's image 1.4 GB → 284 MB, Coastal's build 395 → 104 s, QA reuses unchanged dependencies, production build cache capped at 10 GB (it had filled the disk to 94%) |
| Oct 29–30 | Possible duplicate cases flagged in the admin dashboard | KAN-231 | 6 | A new submission that matches an open case of the same firm on plaintiff, defendant, policy or claim number is flagged for staff, with an audited "Not a duplicate"; nothing is blocked and nothing reaches firms or partners |
| Oct 28 | Uptime alerts and a "service unavailable" screen | KAN-206 | 18 | Outages now page IT support, and users see a branded "We'll be right back" page or notice instead of raw errors; a slow connection no longer looks like an outage |
| Oct 30–Nov 2 | Zero-downtime deploys, phase 1: clean, fast container stops | — | 10 | Backend stop 10.3 s (killed, requests cut) → 0.2 s (clean exit); portal stop on production capped at 3 s, so the deploy gap drops from up to 13 s to about 3–6 s |
| Nov 2 | PR-H5 to H7 portal and staff-app hardening before the OAuth consent page | — | 5 | The backend's session-signing secret no longer ships in the Coastal, apex-research or staff-app images; refused sessions no longer leave users on an empty dashboard or a login loop; Clarity session replay no longer records staff screens; staff uploads over ~75 MB no longer fail at 30 s; a partner's consent link survives sign-in, MFA and a forced password change; outages and slow links get readable messages instead of crashes or endless spinners |
| Nov 2 | Admin Notes page no longer locks offices out of the dashboard | — | 1 | One page open sent ~2,700 API calls and used up the office's 1,000-per-15-min limit, so every admin screen failed for up to 15 min; now 2 calls, all firms' notes shown, notes no longer mixed up between firms with the same name |
| Nov 3 | OAuth branded providers: plan and Phase A prerequisites (CI on PRs, body-parser fix, env manifest + boot check, security-event channel) | KAN-240 (KAN-242 to KAN-245) | 4 | The backend's unit and API tests now run on every backend PR, integration tests on promotions and schema changes (report-only, tiered to fit the Actions budget); a crash-the-server advisory in request parsing fixed on QA after a merge had rolled it back; all 140 backend environment variables listed in one checked file, and a wrong OAuth setting now stops a box at start instead of running a weaker server; OAuth attacks (code or refresh-token reuse, cross-brand use) now have a channel that pages IT |
| Nov 3 | SF-1: approver decisions on a case limited to Admin and Research Manager | — | 1 | Any of the 13 researchers could approve a cancellation, re-open a case, settle a dispute with a refund, or move a case to another firm, on any case, by calling the API directly; now refused with 403 (the screens already hid these buttons) |

**Totals (as of 2026-11-03):** 174 merged PRs across 5 repos (apex-v2 57, CoastalResearch-v2 32, PolicyTraceAI 29, policylimitresearch-v2 31, apex-research 25). 27 of them promoted QA → staging, 9 staging → production (the portals on 26 Oct; all five repos on 29 Oct).

## Themes for case studies

- **Security hardening of a multi-tenant SaaS:** PR-H0, D6, D11, PR-H1, PR-H2, PR-H3 (OAuth Hardening Track, epic KAN-150); KAN-155 brand leak fixes.
- **Evolving a live partner API without breaking anyone:** error shape (additive only), webhook API, PR-H2 (log-only flags before enforcing).
- **Checking production data before changing anything:** D11 pre-check, PR-H1 role-template finding, PR-H2 nginx and audit-log analysis, PR-H3 status-log and cancel-request checks.
- **Docs as code:** KAN-155 moved four hand-kept docs pages into one source the backend builds per brand, also served to API keys for agents.
- **Keeping one backend and four portals in step:** every backend change shipped with matching docs PRs in all portals.
- **Reliability and incident readiness:** PR-H4 rollback, KAN-206 alerts, readiness check, maintenance page and in-app notice, each proven with a real outage on QA; zero-downtime deploys, starting with measuring the real gap per app.
- **Bringing in automated testing:** first backend suite (node:test + supertest + Testcontainers), grew from 35 to 441 tests in about a week.

---

## Contributions

### 2026-11-03 · SF-1: approver decisions on a case are Admin / Research Manager only
**Ticket:** — (security finding SF-1, hardening track) · **Repos:** apex-v2 · **Reached:** QA (3 Nov)

**Problem:** Five staff API routes (approve a cancellation, approve a re-open, re-open a case, resolve a dispute including the refund, and move a case to another firm) checked only the `cases:manage` permission. Every researcher holds it for their own cases, but the check accepted it for any case, so any researcher could make these decisions on any case by calling the API directly. The screens hid the buttons and a code comment said the backend enforced it, which was not true.

**What I did**
- Mapped every approver action in the staff API and found which were already limited to Admin / Research Manager and which were not (5 open; the case-type conversion I first counted was already guarded).
- Wrote read-only production checks and ran them before changing anything: only Admins and Research Managers had ever made these transitions, no role template or per-user override gave `cases:manage` to another role, and the move-to-another-firm route had never been used. So the fix blocks only the 13 researchers, who never used these routes.
- One role check at the top of each of the 5 handlers; researchers still file their cancel, re-open and dispute requests through their own routes.
- Tests run by both layers (fake and real Postgres): a researcher is refused on every route, Admin and RM pass, and the full approve flows work end to end. Chrome checks with screenshots for the lead page.

**Impact**
- Researcher accounts able to approve refunds, cancellations and re-opens or move cases between firms: 13 → 0.
- No change for the 9 Admin and Research Manager accounts or for any researcher workflow seen on production.

**Skills:** authorization review (role vs scope), Express middleware, Prisma, node:test (fake and real Postgres layers), production fact-finding with read-only SQL, Chrome end-to-end testing
**PRs:** apex-v2 #1086

### 2026-11-03 · OAuth branded providers: implementation plan and Phase A prerequisites
**Ticket:** KAN-240 (epic), KAN-242 (A1), KAN-243 (A2), KAN-244 (A3), KAN-245 (A4) · **Repos:** apex-v2 · **Reached:** QA (3 Nov)

**Problem:** With the hardening track mostly done, the OAuth provider had to be planned for real, with a new requirement: each of the four portals must look like its own OAuth provider (own issuer, login, consent, connected apps) on one shared backend. The earlier plan was single-brand. Before any OAuth code: no workflow ran the backend's tests on pull requests, and the token endpoint will parse form bodies through `body-parser`, which had a high advisory (one compressed request with trailing bytes can crash the process).

**What I did**
- Reviewed the earlier plan against Parecki's *OAuth 2.0 Simplified* (page by page) and the current RFCs, and checked it against the code on QA. Wrote plan v2.0: one authorization server, four issuers, one client per brand, RFC 9207 `iss` against mix-up attacks, a `PILOT` client status, per-brand switch-on. 20 corrections to the old plan, 17 prerequisites found already shipped, and one that had not (`CASE:READ`), all with evidence. The lead accepted every recommendation.
- Phase 0 facts with read-only production checks: canonical host per brand, enforcement flags (both log-only everywhere, which led to a new rule that staff routes refuse OAuth tokens whatever the flag says), active firms per brand.
- Set up the Jira epic (KAN-240) with one ticket per step.
- A1: first CI workflow on backend PRs. Report-only, and tiered after measuring Actions use (Team plan, 3,000 min/month; deploys already use most of it): unit, API, docs and lint on every non-draft PR; integration on promotions, schema changes or a label. Checked with actionlint and a 12-scenario logic table.
- A2: found that a merge earlier that day had rolled QA's lockfile back below production (18 packages behind, including this advisory); fixed `body-parser` (2.3.0 → 2.4.0, lockfile only) and reported the rest.
- A3: first committed list of the backend's environment variables (140 names, no values) with a test that fails when code reads an unlisted one; a new `APP_ENV` because `NODE_ENV` is `production` on every box; a startup check that refuses a wrong OAuth setting (localhost redirects outside QA, unknown brand, issuer not an https origin) and lists every problem. 42 tests, plus real starts of the backend with good and bad settings.
- A4: a security-event channel (`securityEvent()`): a fixed list of events with severities, only safe fields kept, no query strings logged, never throws; ships to CloudWatch only when configured, through the existing worker-thread transport. Set up the AWS side: per-environment log groups (production 365 days, QA 30), metric filters and alarms on the existing IT alert topics; found from CloudTrail that the backend's IAM user could already write there, so no IAM change was needed.

**Impact**
- Backend tests run on every backend PR: first run 1.9 min, 873 tests green.
- Estimated Actions use about 1,000 min/month instead of up to ~2,900 for running everything on every push.
- The `body-parser` crash advisory closed on QA, matching staging and production again.
- Environment variables documented: 0 → 140, kept complete by a test.

**Skills:** OAuth 2.0 / OIDC standards (RFC 6749, 7636, 8414, 9207, 9700), multi-tenant authorization server design, GitHub Actions, CI cost planning, dependency and supply-chain review, production fact-finding, Jira planning
**PRs:** apex-v2 #1101, #1105, #1106, #1108

### 2026-11-02 · Admin Notes page no longer locks offices out of the dashboard
**Ticket:** — (found in production logs) · **Repos:** apex-v2 · **Reached:** production (3 Nov, in the lead's staging → production PR #1084; QA and staging 2 Nov)

**Problem:** The Client Data → Notes page asked for notes and messages once per client firm, about 2,700 API calls at 1,347 firms. Production allows 1,000 per IP per 15 minutes, so one page open used up the office's allowance and every admin screen for everyone in that office failed with "Too many requests" for up to 15 minutes. Refused calls became empty lists, so the page also hid firms' notes without saying so.

**What I did**
- Found it from the production nginx logs (read only): every open of the page in 14 days hit the limit (22 Oct, 23 Oct, 2 Nov: 565, 487 and 848 refused calls), all from one office IP each time; and that the successful replies were almost all empty lists.
- Wrote a plan page with the evidence, the options (raising the limit, throttling, lazy loading per firm, bulk endpoints) and why bulk endpoints were the fix.
- Backend: two list endpoints for every firm's notes and messages, with the same permission and brand scope as the firm list, newest first, capped at 2,000 rows with a `truncated` flag.
- Frontend: the page makes 2 calls; notes are matched to firms by id instead of name; a failed load shows a message with Try again.
- Tests: 9 new API scenarios (ordering, staff company excluded, brand scope, cap, permissions); full backend suite 853/0.
- Built an isolated local copy (separate database, 1,347 firms) and compared QA's build with the fix in Chrome, plus a stress test on production's limiter settings.

**Impact**
- Requests per page open: 2,699 → 8 (2 for notes and messages).
- Firms with notes shown: 43 of 60 → 60 of 60; sent messages shown: 0 of 20 → 20 of 20.
- The next screen after Notes: "0 clients" (all refused) → loads normally.
- Page opens one office IP can make before reaching the limit: 0 → 199.

**Skills:** production log analysis, API rate limiting, React Query, REST API design, Prisma, node:test, Chrome-based end-to-end and stress testing
**PRs:** apex-v2 #1079, #1082 (staging)

### 2026-11-02 · PR-H5 to H7: portal and staff-app hardening before the OAuth consent page
**Ticket:** — (OAuth hardening track, H-27 to H-31) · **Repos:** CoastalResearch-v2, PolicyTraceAI, policylimitresearch-v2, apex-research, apex-v2 · **Reached:** production for the staff app (apex-v2, 3 Nov, lead's PR #1084); staging for the four portals (3 Nov; PolicyTrace and apex-research through the lead's QA → staging merges); QA 2 Nov

**Problem:** The OAuth consent page will live on the Coastal portal, and one "Approve" there gives a partner app access to every case of a firm. Checking the portal on QA showed: the page gate verified sessions with the backend's signing secret, baked into the Docker image (anyone holding the image could mint a session for any user), plus a `mock.` cookie bypass; after login only `/dashboard` was a valid target, so a consent link would be lost; nginx's HTML maintenance page crashed the API client; no request had a timeout; `/oauth` could be framed; Google Tag Manager ran on the login page; OAuth discovery (`/.well-known`) hit the site's own 404.

**What I did**
- Presence-only page gate, with the backend as the only verifier; removed the secret from the image and both compose files, and the `mock.` bypass.
- One `safeNext` return-URL rule (only `/dashboard…` and `/oauth/authorize…`; `//`, backslashes and other hosts refused) carried through tab switch, MFA, forced set-password and the 401 redirect.
- API client: readable errors for HTML and dropped replies, a 60 s limit on the wait for the server only (never on the download, after the review question about slow links), a "Still working…" notice after 10 s, `message`-first errors.
- `DENY` + `frame-ancestors 'none'` on `/oauth`; GTM moved off private pages (shared list with Clarity); `/.well-known` proxied to the backend.
- Evidence in Chrome: real sign-ins (owner, temporary password, MFA with a real authenticator app), a stand-in backend for outages and slow replies, a local nginx with production's config (found and fixed an edge case: the form showed only "Service unavailable"), and a production image built without the secret. The same checks against the other portals found that PolicyTrace and PLR left a refused session on an empty or blank dashboard.
- PR-H6 brought PolicyTrace and PLR to the same model and fixed that: the dashboard asks the backend once (`verifySession`), so a refused session is signed out to `/login?next=…` and an outage starts no loop. Chrome-tested on both portals, including a 60 s no-reply and a 75 s trickling reply ("Still working…" from 10 s, no cut-off).
- PR-H7 did the same for apex-research, which also had no security headers at all and verified sessions with the secret.
- The lead asked whether the staff app had the same problems; it did, plus two of its own. Fixed in apex-v2: role-only page gate (no secret in the image), a login loop when the profile cookie was missing (the shape of a September production lockout), deep links lost at login (now `?next=`, also after a session ends mid-case), uploads cut by axios's 30 s whole-request limit (proved with a slow-upload test: old code failed at 30.0 s, new finished at 35.1 s), "Login failed." during outages, GTM and Clarity session replay running on `/admin` (a known compliance gap), framing allowed, `/.well-known` hitting the app's 404. Twelve checks in Chrome and curl, including a forged SUPER_ADMIN cookie and a session ended server-side.

**Impact**
- The backend's session-signing secret no longer ships in the Coastal image (rotation to follow after release).
- A partner's consent link survives sign-in, MFA and a forced password change.
- Outages show "The service is temporarily unavailable…" instead of a parse crash; a silent server ends after 60 s instead of an endless spinner; slow downloads are never cut.
- PolicyTrace and PLR: a session the backend refuses ends on the login page with its cookie cleared, instead of an empty (PolicyTrace) or blank (PLR) dashboard.
- Staff app: no login loop; a staffer whose session ends lands back on the same case after signing in; uploads up to the 100 MB limit no longer fail at 30 s; Clarity no longer records staff screens with case data; OAuth discovery reaches the backend on the API host, which also completes the portals' path without an nginx change.

**Skills:** OAuth 2.0 security (RFC 6749 §10.13, RFC 8414, RFC 9700), Next.js middleware and headers, open-redirect defence, fetch timeouts and AbortSignal, nginx proxying, browser end-to-end testing, Docker image auditing
**PRs:** CoastalResearch-v2 #572, #584 (staging); PolicyTraceAI #274; policylimitresearch-v2 #257, #259 (staging); apex-research #61; apex-v2 #1075, #1082 (staging)

### 2026-10-30 · Zero-downtime deploys, phase 1: clean, fast container stops
**Ticket:** — (follow-up to KAN-206 and PR-H4) · **Repos:** apex-v2, CoastalResearch-v2, policylimitresearch-v2, PolicyTraceAI, apex-research · **Reached:** production for apex-v2 and Coastal (2 Nov, lead's staging → production PRs #1068 and #568); staging for PLR, PolicyTrace and apex-research (2 Nov); QA 30 Oct

**Problem:** Every deploy took the app it replaced offline, and since KAN-206 that showed as the branded maintenance page; the lead saw it on QA right after submitting a form. Each container has a fixed name and host port, so the new one can only start once the old one is gone.

**What I did**
- Measured the gap per app from QA docker events and nginx access logs, and found my own first estimate for the backend wrong. Node runs as PID 1 with no stop handler, so it ignored SIGTERM and kept serving through Docker's 10 s wait, then was killed. Its real gap is start-up only (≈ 6 s on production, where nginx sends `/api/` straight to the backend). The Next.js portals stop accepting at once and then wait on live-update streams until killed (up to 13 s).
- Wrote a proposal comparing seven approaches against each server's resources (blue/green with an nginx switch recommended). Scoped it to production only with the user and stated plainly what phase 1 can and cannot fix.
- Backend: a graceful SIGTERM handler that stops the cron jobs, stops accepting, ends SSE streams through the event bus, lets running requests finish, sweeps idle keep-alive sockets, closes the Prisma pool and exits, with a 5 s cap inside Docker's 10 s.
- Portals and the staff app: `stop_grace_period: 3s` in the production compose files only.
- Evidence: 7 unit tests on a real HTTP server (three fail without the idle-socket sweep), run on Node 20 and 26; full backend suite 844/0. A before/after of the real backend on node:20-alpine with a 100 ms probe.
- Verified the clean stop on QA (exit 0 in 2 s), then promoted to staging by hand together with KAN-206's slow-connection fix (one staging PR per repo).

**Impact**
- Backend `docker stop`: 10.3 s and exit 137 (requests in flight cut) → 0.2 s and exit 0.
- Expected on production: portal deploy gap from up to 13 s to about 3–6 s; the API's ≈ 6 s gap is unchanged, and phase 3 (blue/green) is what removes it.

**Skills:** Node.js process signals and HTTP server shutdown, Docker Compose, Next.js server internals, log-based measurement, node:test, honest scoping of a partial fix
**PRs:** apex-v2 #1048, #1063 (staging); CoastalResearch-v2 #553, #564 (staging); policylimitresearch-v2 #253, #255 (staging); PolicyTraceAI #270, #272 (staging); apex-research #57, #59 (staging)

### 2026-10-30 · KAN-231: possible duplicate cases flagged in the admin dashboard
**Ticket:** KAN-231 · **Repos:** apex-v2 · **Reached:** production branch (30 Oct, in the lead's staging → production PRs #1040 and #1050)

**Problem:** Clients submit the same matter again, sometimes weeks apart and through a different channel (portal, public form, partner API). Nothing linked the cases, so staff could not see that one already existed and could deliver mixed results. The existing Idempotency-Key only catches a retry of the same request within 24 hours.

**What I did**
- Weighed the lead's sketch (a match-keys table plus a persisted flags table) against a pure read-time query, and shipped a hybrid with the trade-off written up in the PR: one `case_match_keys` table holding the normalised plaintiff, defendant, policy and claim values, indexed per firm and maintained by one shared step at all 15 creation, edit and firm-link sites; flags derived at read time by one indexed self-join (1.4 ms for a 50-row page), so there is a single derived state and a dismissal can never be lost by a resync. Nothing on `cases`, so the spread-based client and tenant serializers cannot leak it; proven over HTTP.
- Tuned normalisation on a read-only prod preview of 35k live cases: "unknown defendant", "pending pending", "pre-lit", "case manager" and test numbers would have matched each other, so whole-word and repeated-character placeholder rules were added on top of the exact list.
- Applied the lead's scope rule: only cases created after the feature lands in that environment are checked (the instant comes from the migration's own timestamp, so no ops step per environment), and only open cases are offered as matches, never deleted, spam, cancelled or completed-and-delivered ones.
- UI: a `DUP?` chip on the board, a banner on the case page with each match as a link, its status and the reason ("same firm + claim number + policy number"), and a "Not a duplicate" per pair that is audited once per case. No backfill: the keys table fills at boot and rebuilds nightly.
- Evidence: 20 integration tests on a real Postgres, one per acceptance criterion, plus 14 unit tests; a recorded browser run on the local prod copy showing the UI, backend and database at each step, shared with the lead.
- Pre-production check against testprod found the key fill had silently failed there (7 of 1,112 cases keyed) because one 20,000-character pasted title exceeded Postgres's index-row limit; fixed by ignoring values over 200 characters (real values top out at 64). The same PR applied the lead's second ruling: a case created after the release stays a match after delivery or cancellation, pre-release cases count only while open. All 14 scope scenarios were then re-run in the browser (recorded) before the PR went in.
- Applied the lead's final rule the same day: a new case is checked against every case of its firm in every status (delivered, cancelled and spam included), only soft-deleted ones excluded. A read-time filter change, so no migration or backfill; proven with an integration test across eight statuses.

**Impact**
- Staff see a resubmission the moment it lands, with the open case it matches one click away. The recorded example was a real prod pair: two cases three days apart, different name spellings, identical policy and claim numbers.
- Before the scope rule 2,609 of 35,057 live prod cases would have carried a plaintiff flag; with it the day-one count is zero and only new submissions are checked.
- Dismissing a pair writes one dismissal row and one audit row per case, and never touches the case itself.

**Skills:** PostgreSQL (normalisation in SQL, indexed self-joins, EXPLAIN ANALYZE), Prisma migrations, Express, Next.js/React, design trade-off write-ups, browser e2e (Chrome), test design
**PRs:** apex-v2 #1031, #1034 (staging), #1041, #1042 (staging), #1046, #1047 (staging)

### 2026-10-28 · KAN-206: uptime alerts and a "service unavailable" screen
**Ticket:** KAN-206 (epic KAN-150; replaces PR-H4 Part B and SF-17) · **Repos:** apex-v2 + 4 portals, AWS, nginx on QA, testprod and production · **Reached:** production on 29 Oct for the notice and the readiness check (promotion PRs listed under PR-H4); the nginx maintenance page applied by hand on QA (28 Oct), testprod and production (30 Oct); the slow-connection fix on QA and staging (2 Nov; staging PRs listed under zero-downtime deploys)

**Problem:** When the site went down nobody was told: 9 CloudWatch alarms published to 3 SNS topics that had no subscribers. Users saw raw nginx 502 pages, JSON errors and broken widgets, and partners' API clients got HTML instead of a parseable error.

**What I did**
- Alerts (AWS, live): an IT topic for production and connectors and a separate QA topic, server status alarms on 4 servers, Route 53 checks with alarms on 6 public sites, the old database and analysis topics routed to their owners, and a Confluence runbook.
- `GET /api/health/ready`: a readiness check that pings the database (2 s timeout, 5 s cache, single-flight, own rate limit so polling can't eat the shared API budget); Route 53 check and alarm on QA.
- A "We'll be right back" notice in all five apps: polls readiness while the tab is visible, full screen on app pages and a banner on informational pages, keeps typed input and reconnects live updates on recovery.
- A branded maintenance page per brand plus a JSON 503 in the API's usual error shape, served by nginx when an app is down; applied to QA's nginx with backups, dry-run patches and file fingerprints to prove nothing else changed.
- Follow-up after the QA outage test showed a user with an open dashboard never saw the notice (each reload restarted the count): first check on page load, 5 s retries after a failure, failures remembered across reloads, and an immediate check when any request gets nginx's maintenance answer.
- Follow-up after the lead saw "We'll be right back" on all five portals from a slow rural connection while the server was up, with no way to close it: reproduced it locally with Chrome DevTools throttling, then made the notice tell "our server says it's down" (5xx) apart from "no answer" (slow or dropped connection). Only the first shows the full notice; the second shows a small closable "Your connection looks slow" strip that points to support after 2 minutes. Added "Continue anyway"/Escape, a 10 s limit and a first check after page load.

**Impact**
- QA outage tests (28 Oct): with a portal stopped its pages answered 503 with the branded page and the other sites stayed up; with the backend stopped for 4 min every `/api/cases` path and a partner `POST` got the JSON 503, and the alarm emailed IT 3.5 min in and again on recovery.
- The notice now appears about 10 to 25 s into an outage instead of about 65 s after each page load, and within about 1 s of a reload during one.
- Found along the way: on QA and testprod most `/api` calls go through Next.js and hang rather than fail fast when the backend is down.
- Production outage tests (2 Nov, quiet hour, with the lead's go-ahead): PolicyTrace stopped for about 30 s showed its branded page and reloaded itself; the backend stopped for about 70 s gave a JSON 503 on every brand's API in about 0.7 s and the in-app notice, which cleared on its own. Only the container under test was affected.
- Slow connection (6 s latency): the full-screen "our system is down" notice used to appear within about 40 s with the server up; now nothing appears. At 12 s latency only the closable connection strip shows. Real outages still show the full notice in about 25 s.

**Skills:** AWS (CloudWatch, SNS, Route 53), nginx, Next.js/React, Express, incident readiness, production operations, browser testing (Playwright)
**PRs:** apex-v2 #985, #988 (staging), #990, #991, #994, #1055 · Coastal #516, #517, #558 · PolicyTrace #259, #260, #271 · PLR #239, #240, #254 · apex-research #45, #47, #58

### 2026-10-27 · Faster deploys and a production disk that stops filling up
**Ticket:** KAN-206 (deploy-speed and disk items) · **Repos:** apex-v2 + 4 portals · **Reached:** production (29 Oct) for the production cache cap and `--no-audit`; the QA/testprod cache cap, prune retry, path filter, Prisma caching and build turns reached staging in all five repos on 30 Oct

**Problem:** QA deploys were slow (PLR's median 9.6 min on a shared 2-CPU box), and production's disk filled up every week: it was 94% full (3.9 GB free of 58 GB), 41 GB of it Docker build cache that the deploy's prune never actually cleared.

**What I did**
- Measured deploy times across 945 runs in the five repos to find where the time went, and tested each idea on its own before proposing it; dropped the ones that didn't help.
- PLR: `npm ci` and Next.js standalone output. PolicyTrace: standalone output.
- Production deploys now really clear the build cache and keep it capped at 10 GB (`-af --max-used-space 10GB --min-free-space 15GB`), with the flags configurable per server.
- Second round (29 Oct): found that Coastal's `npm ci` had gone from under a minute to 7 to 18 minutes because npm's built-in audit spent about 8 s on each CKEditor package after a new advisory; turned the audit off in the image build (`--no-audit`, as PLR already had).
- QA and testprod stopped wiping the build cache after every deploy (not one deploy since 15 Oct had reused its install layer, though only 11 of 347 QA merges changed a lockfile): QA keeps 12 GB (`--keep-storage`, the only flag its Docker 29.1.3 knows), testprod 12 GB plus an 8 GB free-space guard.
- apex-v2's QA deploy now skips pushes that change nothing in its images (connectors, docs, tests), with the list checked against the Dockerfiles and the files the API reads at runtime.
- `prisma generate` (Coastal, PLR, apex-v2 backend) moved into its own cached step, so it reruns only when the schema changes. Testing caught that the generator reads `tsconfig.json`; without it the client came out different, so I kept the output byte-identical and made sure PLR's committed client can never override the fresh one.
- QA builds now take turns, backend first: one box-wide `flock` around the build step only, plus a priority note so apex-v2 always builds before waiting portals (tested on the QA box with a fake docker, including stale notes and timeouts).

**Impact**
- PLR's QA deploy median 9.6 → 5.5 min; PolicyTrace's image 1.4 GB → 284 MB (QA deploy about 3.3 min).
- Production disk cleaned from 94% to 42% the same day; the cap keeps the cache from growing back.
- Coastal's image build 395 → 104 s in a like-for-like local test (`npm ci` 325 → 30.5 s, same 484 packages).
- First QA burst after the cache change (five merges, 29 Oct 14:47 UTC): PTA, PLR and apex-research reused their install layer, and an apex-v2 merge that changed no image input finished in 3 minutes, fully cached.
- Replayed over QA's history, the apex-v2 path filter would have skipped 77 of 196 deploys between 7 and 29 Oct.
- First real five-merge burst with builds taking turns (29 Oct 16:42 UTC): backend live in 3.7 min, portals at 7 to 16 min, QA swap peak 1.2 GB (2.8 GB with three parallel builds earlier that day).

**Skills:** Docker, Next.js builds, CI/CD performance, data analysis of CI runs, production operations
**PRs:** PLR #235, #237, #244, #249, #250, #251 (staging) · PolicyTrace #256, #257, #264, #267, #268 (staging) · apex-v2 #982, #1009, #1021, #1022, #1025, #1034 (staging) · Coastal #514, #525, #531, #540, #542, #546 (staging) · apex-research #43, #51, #54, #55 (staging)

### 2026-10-29 · PR-H4: deploy health check and automatic rollback
**Ticket:** — (OAuth Hardening Track H-26, epic KAN-150) · **Repos:** apex-v2 + 4 portals · **Reached:** production in all five repos (29 Oct)

**Problem:** Every deploy built the new image on the box, swapped containers and pruned the old image. Nothing checked that the new release answered, so a release that crashed at boot restarted in a loop behind a green job while every brand returned 502, and there was no image to go back to. Production deploys about once a day, and the OAuth token endpoint was about to ship.

**What I did**
- Wrote `deploy.sh`, `healthcheck.sh` and `rollback.sh`: keep the running images as `:<tag>-previous` (only if healthy, tagged by image id), build → migrate → swap, then require `/health` to answer and stay up with no restart; on failure put the previous images back and fail the job.
- Moved the QA, testprod and production workflows onto the script, and added a manual Rollback Production workflow (typed confirmation, production branch only).
- Gave the four portals (each brand will host its own OAuth consent page) the same safety net with one shared script that probes `/login`, so a backend outage never rolls a portal back.
- Tested with a local Docker harness first: it caught a bug where, after a failed migration, the never-run image would have become the rollback target.
- Wrote down why a rollback can't undo migrations, and which past migrations would have broken one (3 of 69).

**Impact**
- First real QA deploy (27 Oct): rollback image tagged, `/health` up in 6 s, healthy after the stability window, job green in about 6 minutes.
- Failure drill on QA: a release that crashed at boot was caught after 90 s and rolled back automatically; backend down about 2 minutes, frontend unaffected.
- All four portals deployed to QA with the new script (`/login` healthy in 3 s each).
- Found that a silent build longer than ~4 min made the runner's SSH drop (a false red while the deploy finished); added SSH keepalives. With five builds sharing the QA box, two builds were silent for 7m27s and 7m04s and all five deploys stayed green.
- Follow-ups (28–29 Oct): deploy workflows now refuse to run from any branch but their own (production could be deployed from a feature branch, and testprod from QA); after a staging incident where two deploys collided and left Coastal staging down for 10 minutes, deploys of the same app now wait for each other (`flock`) and a container that fails to start is rolled back. A timing analysis of 366 deploys showed the health check adds about 27 s; slow deploys came from builds sharing the 2-CPU QA box.
- Research for the same PR found that all 9 CloudWatch alarms notified nobody and that production's outbound TLS checks were off (tracked separately).
- Released to production on 29 Oct together with the KAN-206 notice and readiness check: QA → staging for all five repos (only my commits cherry-picked where others' QA work wasn't ready), then staging → production, apex-v2 first. Each production PR was checked beforehand: a clean `git merge-tree` that kept production's Dependabot bumps, testprod healthy on the same commit, the exact merge result built locally (786 backend tests passing), and the 7 migrations confirmed additive. All five production deploys went green with the new rollback and health-check steps.
- Follow-up the same day: a healthy apex-v2 QA release turned red because another app's deploy was pruning at that moment (Docker runs one prune at a time). The prune now retries only on that error and never fails a healthy deploy.

**Skills:** CI/CD, deployment safety, Docker, shell scripting, GitHub Actions, production operations
**PRs:** apex-v2 #957, #964, #984 (staging), #1001, #1004, #1007 (staging), #1013 (production), #1015 · Coastal #494, #499, #521 (staging), #523, #524, #528 (staging), #534 (production), #536 · PolicyTrace #250, #251, #261, #262, #263 (staging), #265 (production), #266 · PLR #230, #231, #241, #242, #243 (staging), #245 (production), #246 · apex-research #36, #39, #48, #49, #50 (staging), #52 (production), #53

### 2026-10-26 · PR-H3: data integrity, key hygiene, audit trail
**Ticket:** KAN-197 · **Repos:** apex-v2 (backend + connectors) · **Reached:** production (29 Oct, via staging #984 and production #1013)

**Problem:** Firms could blank or overwrite what researchers found (SSN, policy result) and delete case files. Key replies returned the key's hash. Deleting a provisional firm would have turned its keys into staff keys and its webhooks into feeds of every firm's events (D5, dormant). The status history couldn't tell a person from an API key, so every cancellation a firm asked for by API key was approved with the wrong wording, and audit rows written by keys had no IP or request id. The connector retried a rejected key forever.

**What I did**
- Made SSN, policy-result edits and file deletes staff-only, with an audit row for policy edits.
- Gave key replies an explicit shape (no hash), started new keys with `sk_` instead of a brand name, and widened log redaction.
- Kept firms that hold keys or webhooks (plus `ON DELETE RESTRICT` as a backstop). Revoking a key now reports the webhooks it created and can switch them off.
- Stamped every audit row with the request id and IP through an `AsyncLocalStorage` request context, added `changedByType` to status logs with a back-fill migration, and fixed the cancel-approval wording.
- Connector: a 401 from our API marks the connection "reconnect required" instead of retrying.

**Impact**
- Prod checks first: all "Rockpoint Prod Token" cancellations plus 14 by firm admins, attorneys and case managers had been approved with the wrong wording. No client had deleted a file in 90 days (staff 275), so the fence breaks nobody.
- Back-fill labels 112,463 status-log rows (80,034 key, 32,429 user), 0 unmatched.
- Tests: 700 unit/API, 312 integration, 1,192 connector. Each new test fails on the old code.

**Skills:** data integrity, audit logging, DB constraints and back-fill migrations, request context, production data analysis
**PRs:** apex-v2 #946

### 2026-10-23 · Partner API docs from one source + brand leak fixes
**Ticket:** KAN-155 (construction KAN-193) · **Repos:** apex-v2 + 4 portals · **Reached:** production (26 Oct)

**Problem:** Each portal kept its own hand-written API docs page (99.5% the same code, 11,389 lines across four), and they had drifted from the backend. A check of the docs against the backend also found answers and webhooks that named another brand or carried internal data.

**What I did**
- Checked the partner spec against the backend code: 274 findings.
- Moved the docs into one Markdown + OpenAPI source in the backend, built per brand at startup. The portal page reads it with a session; API keys get OpenAPI JSON, Markdown and `llms.txt` for agents.
- Moved them word for word first (0-word difference from the old pages), then a three-column layout, then 111 corrections that needed no product decision.
- Backend brand fixes (#922): the right "Asset Search" label for PolicyTrace, file links on the firm's own brand host, no internal data or staff emails in firm webhooks. Then per-environment hosts (#931) and a double-slash fix (#934).
- Portals: one shared renderer replaced each JSX page.

**Impact:** Docs for four brands are edited in one place and a firm only ever sees its own brand. Agents can read the docs with an API key.

**Skills:** docs as code, OpenAPI, multi-brand isolation, technical writing
**PRs:** apex-v2 #922, #923, #931, #934 · Coastal #470 · PolicyTrace #243 · PLR #223 · apex-research #33 · production (portals, also carried PR-H1/PR-H2): Coastal #485 · PolicyTrace #245 · PLR #225 · apex-research #35

### 2026-10-23 · PR-H2: partner API surface hardening
**Ticket:** KAN-179 (also resolved KAN-154) · **Repos:** apex-v2 + 4 portals · **Reached:** production, 26 Oct (enforcement flags still log-only)

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
**Ticket:** KAN-171 (replaced KAN-160, KAN-168) · **Repos:** apex-v2 + 4 portals · **Reached:** production, 26 Oct

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
