# Email Module — Engineering Problem Log
### emailControllerAuth2 · HCC-adam-backend · hcc-admin-v2

All findings below are backed by commits under `Syed_Sibteali_Baqar <sibteali786@gmail.com>`, verified per-repo via `git log --all --format='%an %ae'`. Two areas where underlying code was authored by someone else (Gmail OAuth refresh, SendGrid throttle constants) are explicitly separated — see Attribution Notes at the end.

---

## 1. Attachment Survival Through a Serialized Job Queue ✅
**Repo:** emailControllerAuth2 | **Commits:** `ee0172c`, `d4e0584`

### Problem
Bull jobs are serialized (stored in Redis as JSON) — they can't hold raw file buffers directly. Bulk emails needed to support attachments across a queued, asynchronous send.

### Root Cause / Design Constraint
A raw file buffer can't survive Redis serialization. The system needed a way to reference a file from a queued job without embedding its contents in the job payload.

### Solution
Multer configured with `diskStorage` (not `memoryStorage`) — uploaded files are written to `uploads/` on the initial request, and only the serializable file reference (`.path`, `.originalname`) goes into the Bull job payload. Both `gmailService.js` and `sendgridService.js` re-read the file from disk by path at actual send time — once **per recipient**, not once per job.

### Alternatives Considered
- **`memoryStorage` + base64-encoding into the job payload** — would avoid disk I/O but bloats Redis job size significantly for any real attachment, and still requires re-encoding per recipient anyway; disk-based reference is more scalable for a multi-recipient fan-out

### Tradeoffs & Real Open Gaps (unresolved — no fix commit exists)
- ⚠️ **Confirmed disk leak:** no `unlink`/cleanup call exists anywhere in the codebase — temp files in `uploads/` are never deleted after a job completes or fails. Disk usage grows unbounded over time.
- ⚠️ **Filename collision risk:** Multer's filename generator is `Date.now() + ext` with no UUID or per-request namespacing. With Bull running 5 concurrent workers, simultaneous multi-file uploads in the same millisecond could collide. This is inferred from the code (no incident commit found), not a confirmed production bug.

### Improvements
- Add a cleanup step (immediate post-send unlink, or a scheduled sweep of `uploads/` for files older than N hours) — straightforward fix for a real, currently-live gap
- Switch filename generation to include a UUID or request ID, removing the collision risk entirely regardless of concurrency

---

## 2. No Partial-State Job Tracking ⚠️ (open gap)
**Repo:** emailControllerAuth2

### Problem
Job status enum is exactly `['queued', 'processing', 'completed', 'failed']` — no `partial` state. A bulk job with 500 successful sends and 3 failures still reports as `completed`, with no visibility into the partial failure from the status field alone.

### Root Cause
Status tracking was designed around whole-job success/failure, not the more realistic scenario of a large recipient batch having some individual failures while the overall job still runs to completion.

### Tradeoffs
- ⚠️ Real UX/observability gap: an admin checking job status sees "completed" and might not know to check per-recipient results for actual delivery failures
- Per-recipient failures ARE caught and logged individually (see Item 3) — the data exists, it's just not reflected in the top-level status field

### Improvements
- Add a `partial` status computed from per-recipient results at job completion — straightforward given the underlying data already exists

---

## 3. Whole-Job Retry, No Per-Recipient Retry or Idempotency ⚠️ (open gap)
**Repo:** emailControllerAuth2 | **Uses Bull v4** (confirmed, not BullMQ)

### Problem
Bull's `attempts: 3` retries the **entire recipient batch** on failure, not individual failed recipients.

### Root Cause
Retry granularity is at the job level, not the recipient level — a design choice likely made for simplicity, but with a real consequence: a transient failure late in processing a 2000-recipient job risks re-sending to recipients who already succeeded, since there's no dedupe/idempotency check preventing duplicate sends on retry.

### Tradeoffs
- ⚠️ Real risk: duplicate emails to already-successful recipients on any job-level retry
- ✅ Individual per-recipient failures are still caught and logged (not silently dropped) — the gap is specifically retry granularity, not failure visibility

### Improvements
- Track already-sent recipients within a job and skip them on retry (idempotency key per recipient+job), or restructure to per-recipient sub-jobs with independent retry — the latter is the more standard Bull pattern for this exact scenario

---

## 4. Hardcoded Templates → Database-Driven Templates ✅
**Repo:** emailControllerAuth2 | **Commit:** `9a20fab` (Apr 20)

### Problem
Templates were originally 3 hardcoded IDs mapped to static `.html` files with a hardcoded metadata array in code — any new template required a code change and deploy.

### Solution
Introduced a `Template` Mongo model, controller, routes, and seeding — templates became data, not code. This is the direct architectural ancestor that made the later merge-tag whitelist validation (Item 5) possible, since whitelist validation needs templates to be queryable/mutable data.

### Tradeoffs
- ✅ Templates can now be added/edited without a deploy
- Sets up a clear "foundational refactor enabled a later feature" story — worth connecting explicitly to Item 5 in an interview if asked about how the merge-tag system evolved

---

## 5. Merge Tag Vocabulary Migration (frontend, same-day counterpart) ✅
**Repo:** hcc-admin-v2 | **Commit:** `9de73d3` (May 5 — same day as the backend whitelist fix `c4e8314`, already documented separately)

### Problem
Original placeholder vocabulary (`title`, `recipientName`, `additionalText`, `companyName`) needed to be replaced with a fixed, whitelist-compatible tag set to match the backend validation being introduced the same day.

### Solution
Migrated to a fixed 7-tag set: `firstName`, `lastName`, `company`, `email`, `senderName`, `senderTitle`, `bookingLink`. Added a client-side pre-save whitelist check mirroring the backend one, giving immediate feedback before a save attempt even reaches the server.

### Tradeoffs
- ✅ Coordinated same-day frontend/backend change — client and server enforce the same vocabulary, reducing round-trip failures
- Client-side check is a UX improvement, not a security boundary — the backend whitelist (already documented) remains the actual enforcement point

---

## 6. Unmitigated XSS in Template Rendering ⚠️ (real, open, unaddressed)
**Repos:** emailControllerAuth2, hcc-admin-v2

### Problem
`processTemplate()` has only ever been touched by 2 commits total (its original creation, plus the render-time fallback fix already documented) — it's a plain regex `.replace()` with no HTML-escaping of recipient-controlled values (name, company, email) and no double-substitution guard.

### Root Cause
Merge-tag substitution was built for correctness (does the tag resolve to the right value) but never hardened for safety (is the resolved value itself safe to inject into HTML). A contact whose name field contains `<script>` or literal `{{` characters flows directly into outbound email HTML.

### Confirmed Scope
Full-history grep for `xss`/`sanitiz`/`escape` returns **zero hits** in either repo. The frontend template builder also accepts pasted/uploaded raw HTML with no sanitization (no DOMPurify or equivalent).

### Tradeoffs
- ⚠️ Genuinely unmitigated — this is real, currently-exploitable (a malicious or malformed contact name/company field could inject content into emails sent to other recipients)

### Improvements
- HTML-escape all recipient-controlled values before substitution (straightforward, should be the first fix)
- Add DOMPurify (or equivalent) sanitization on the frontend template builder's raw HTML input
- This is a strong, honest "what I'd improve first" answer if asked about security gaps in this system — concrete, well-scoped, and not yet fixed

---

## 7. Gmail OAuth Failures — Built a Fallback, Not a Fix ✅
**Repos:** emailControllerAuth2, HCC-adam-backend | **Commits:** `ef11c68` (Apr 18), `56c6c2e`/`db4534b`/`695d724` (Apr 28 – May 6)

### Important Attribution Note
`createGmailClient()` and its token-refresh logic were **not authored by me** — written by a different contributor, never modified by me in either repo. Don't claim authorship of the OAuth refresh mechanism itself; the story here is architectural, not a fix to that code.

### Problem
`sendEmail()` was silently swallowing errors, including Gmail OAuth refresh failures — a failed send (for any reason, including an expired/revoked refresh token) would fail silently with no way for a caller to know or record it.

### Solution — real story: built around the fragile part rather than hardening it
1. `ef11c68`: changed `sendEmail()` to re-throw errors instead of swallowing them, so callers could catch and record per-recipient failures
2. `56c6c2e`/`db4534b`/`695d724`: added a service parameter letting callers route through **SendGrid instead of Gmail OAuth**, keeping the Gmail path untouched as a fallback option rather than the only path

### Alternatives Considered
- **Harden the Gmail OAuth refresh logic itself** (add try/catch around `getAccessToken()`, add locking around token updates) — not the path taken; instead, a second, more reliable provider (SendGrid) was made available as an alternative

### Tradeoffs
- ✅ Practical: rather than debugging someone else's fragile auth code, added a reliable alternate path — pragmatic engineering under the constraint of not owning that code
- ⚠️ The underlying Gmail OAuth fragility remains unaddressed for any caller still using it: no try/catch around `getAccessToken()` (unhandled throw on expired/revoked token), no locking around the read-then-`user.save()` token update (concurrent refresh races, last-write-wins, non-fatal but wasteful), no re-consent/scope-upgrade flow

### Improvements
- If continuing to support Gmail as a send path, the three gaps above are concrete, scoped fixes — but the more pragmatic answer (already taken) is steering usage toward the SendGrid path where reliability matters more

---

## 8. Job Status UI — Plain Polling, Not WebSocket/SSE ✅
**Repo:** hcc-admin-v2 | **Commit:** `ab4f99a` (Apr 27)

### Problem
Frontend needed to reflect bulk job status changes (queued → processing → completed) without a push mechanism.

### Solution
`setInterval` + `axios GET` every 60 seconds, plus a manual refresh button. A `pollingActive` ref stops the interval on fetch error rather than continuing to spam a broken endpoint.

### Alternatives Considered
- **WebSocket/SSE push** — rejected (implicitly, by not building it) in favor of simple polling, reasonable given this is an internal admin tool at modest scale, not a consumer real-time product

### Tradeoffs
- ✅ Simple, low-risk, written once and never needed fixing — no perf or stale-status bug history exists for this mechanism
- ⚠️ 60s polling means status can lag up to a minute behind actual state; also continues polling on inactive/backgrounded browser tabs, wasting requests

### Improvements
- Pause polling when the tab is inactive (`document.visibilityState`) — cheap win
- SSE would be a natural upgrade if real-time status becomes a real user need, following the same pattern already used elsewhere in this codebase for notifications

---

## 9. SendGrid Rate Limiting — Confirmed Gap, Correctly Attributed ⚠️
**Repo:** emailControllerAuth2

### Attribution Note
The batching/delay throttle itself (`batchSize=50`, 200ms/recipient, 1s/50-batch) was authored by a different contributor (base logic predates my commits). My commits (`ef11c68`, `7ca4a66`, `ebd7ea1`, `c08a425`) layered delivery logging and per-recipient personalization around the existing loop — not the throttling logic itself.

### Problem / Confirmed Gap
With Bull running multiple concurrent workers × 50-recipient batches across simultaneous jobs, large campaigns could burst past SendGrid's API rate limits with zero automated recovery (no 429-specific handling, no backoff-and-resume).

### Tradeoffs
- ⚠️ Real, unaddressed gap at the system level — worth being honest that the existing throttle constants weren't designed with multi-job concurrency in mind

### Improvements
- Add explicit 429 detection with exponential backoff and job-level pause/resume, rather than relying on fixed per-recipient delays alone — this is a clean, scoped "what I'd improve" answer, correctly framed as a system-level gap rather than personal authorship of a fix

---

## 10. Auth Downgrade — Session-Based Ownership Replaced with Client-Supplied Param (IDOR) ⚠️ (real, open security gap)
**Repo:** emailControllerAuth2 | **Commits:** `e37686e` (Apr 21), `42a3d98` (Apr 27)

### Problem
`requireAuth` middleware was deleted entirely. Contact-list and bulk-job endpoints switched their ownership check from `req.user.id` (session-derived, trustworthy) to `req.params.userId` (caller-supplied, untrustworthy) — meaning any caller who knows or guesses a valid Mongo `ObjectId` can read or delete another user's contact lists or bulk-job status.

### Root Cause / Context
Commit message and companion doc frame this explicitly as an **intentional stopgap** — unblocking frontend integration before Google OAuth session wiring was fully finished on the frontend side ("requires Google OAuth session cookie... will be validated end-to-end from frontend"). This was a deliberate, acknowledged tradeoff made under time pressure, not an accidental oversight.

### Status
**No later commit re-adds session-based checks** — this appears to still be open in the codebase today.

### Tradeoffs
- ⚠️ **Real IDOR (Insecure Direct Object Reference) vulnerability as currently committed.** Any authenticated-or-not caller with a guessable/enumerable ObjectId can access or delete another user's data.
- The tradeoff was explicit and documented at the time (unblock frontend work), which is a defensible engineering decision under deadline pressure — but it was never closed out once the blocking condition (frontend OAuth wiring) was presumably resolved.

### Improvements
- **This is the single highest-priority item across the entire email module documentation.** Re-introduce session-derived ownership checks (`req.user.id`) immediately; if `userId` is still needed as a param for any legitimate reason, validate it matches the authenticated session rather than trusting it directly.
- For interview use: frame honestly as "a deliberate stopgap that was never closed out — a real lesson in tracking follow-up work on intentional shortcuts," which is a mature, credible answer. For actual portfolio/security-conscious contexts, this should probably be fixed in the codebase before being discussed as a "resolved" story.

---

## Attribution Summary
**Confirmed authored by me** (commit hash cited above): Items 1, 4, 5, 7 (architectural response), 8, 10, and the logging/personalization layer in Item 10.

**Explicitly NOT authored by me** (context only, not claimed as my work):
- `createGmailClient()` / Gmail OAuth refresh logic — authored by a different contributor, never modified by me
- SendGrid batching/delay throttle constants — base logic predates my commits, also a different contributor
- Per-user OAuth token storage schema (`User.emailCredentials`) — predates my commits

**Open gaps with no fix commit by anyone** (absence-findings, not attributed to a specific author since no one has addressed them): attachment disk-leak/collision risk, no partial job state, no per-recipient retry/idempotency, unmitigated XSS, unaddressed 429/rate-limit handling.
