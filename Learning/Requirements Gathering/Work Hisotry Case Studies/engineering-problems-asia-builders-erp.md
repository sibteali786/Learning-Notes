# Asia Builders ERP — Engineering Problem Log

Verified against actual git history. All items below are commit-checked and interview/portfolio ready.

---

## 1. Outstanding Balance Calculation — Partial Settlements Invisible to Aggregates ✅
**Commit:** `76ace4d` (May 10, 2026) — same commit that introduced the settlement feature itself

### Problem
Vendor outstanding-balance queries only summed transactions with `status = 'DUE'`, at full `t.amount`. Once partial settlements became possible, a `PARTIALLY_SETTLED` transaction was invisible to these queries entirely — a vendor could show **$0 owed while genuinely still owing money**.

### Root Cause
The aggregation logic was written before partial settlement existed as a concept, and wasn't updated in the same breath as the new `PARTIALLY_SETTLED` status was introduced — until this commit closed that gap.

### Solution
```sql
-- Before
COALESCE(SUM(t.amount), 0) ... WHERE status = 'DUE'

-- After
COALESCE(SUM(t.amount - t.settled_amount), 0) ... WHERE status IN ('DUE', 'PARTIALLY_SETTLED')
```
Landed alongside the migration introducing `transaction_settlements` and the `settled_amount` column — the fix was designed in *with* the feature that created the need for it, not shipped broken and patched later. `PARTIALLY_SETTLED` was never a reachable state before this commit, so no live data was ever miscalculated in production.

### Tradeoffs
- ✅ Outstanding balances now correctly reflect partial payments across both relevant statuses
- This is genuinely strong material for an ERP context: correctly identifying that a new feature (partial settlements) has ripple effects on *every* aggregate query touching that status, not just the write path

### Improvements
- A follow-up commit (`9bbbb0e`, "correct project ID comparison and improve outstanding amount calculation in transaction view") suggests at least one more refinement pass — worth a quick look before quoting exact figures in a portfolio writeup, but the core correctness fix here is solid as-is

---

## 2. Soft-Delete Cascade — Project/Vendor → Document ✅
**Commits (same day, Mar 10, 2026):** `2c63df0` (Documents module created) → `984d5f5` (~2h19m later, cascade added) → `74e0574` (migration)

### Problem
Soft-deleting a Project or Vendor needed to also soft-delete its attached Document rows — otherwise a "deleted" project's documents would remain live/visible despite the parent being gone.

### Root Cause
The Documents module was initially built with no cascade awareness; the gap was caught and closed within the same working session (~2 hours later), not after a production incident.

### Solution
```typescript
await this.softDeleteDocuments(DocumentEntityType.PROJECT, id);
await this.projectRepo.softDelete(id);

private async softDeleteDocuments(entityType, entityId) {
  await this.docRepo.createQueryBuilder().update(Document)
    .set({ deletedAt: new Date() })
    .where('entity_type = :type AND entity_id = :id AND deleted_at IS NULL', {...})
    .execute();
}
```
Mirrored in `vendors.service.ts`. Explicit, per-service call before each parent's `softDelete()` — not enforced by a global TypeORM subscriber.

### Tradeoffs
- ⚠️ **Real, honest open risk:** this is per-service, not centrally enforced. Any new entity type with attached documents must remember to replicate this call manually — nothing structurally prevents a future regression if a new module forgets it.
- ✅ Caught and fixed during the same build session, not after data was already inconsistent in production

### Improvements
- A TypeORM subscriber or lifecycle hook enforcing the cascade centrally (rather than per-service opt-in) would remove the "must remember to replicate" risk entirely — good "what I'd do differently" answer

---

## 3. R2 Storage — Saga/Compensating Delete Pattern ✅
**Commit:** `2c63df0` (Mar 10, 2026), Documents module

### Problem
File uploads involve two systems (R2 object storage + Postgres metadata row) with no shared transaction. A successful R2 upload followed by a failed DB write would leave an orphaned file in R2 with no corresponding record.

### Solution
Upload to R2 first, then wrap the DB `save()` in try/catch; on DB failure, call `storageService.delete()` as a compensating action and rethrow. Separately, `storage.service.ts`'s `delete()` deliberately swallows R2 errors: *"Log but don't throw — document soft-delete should still succeed even if R2 delete fails."*

### Scope
Lives in the generic, polymorphic Documents module (`entityType`/`entityId`) used by every file-upload path in the app — one implementation serving all upload flows, not duplicated per feature. A second, separate atomic pattern exists for avatar uploads in `AuthService` (`94aaa07`).

### Tradeoffs
- ✅ Prevents orphaned R2 files in the common failure case (DB write fails after upload succeeds)
- ⚠️ **Honest, undocumented gap:** no comment/TODO anywhere records the crash-between-upload-and-compensating-delete edge case (server dies mid-operation, after upload but before the compensating delete runs) — this is an accepted risk via a synchronous try/catch, not a durable outbox/queue pattern. It was never written down as a known tradeoff at the time; worth being upfront about that distinction if asked in an interview rather than presenting it as a fully-solved problem.

### Improvements
- A periodic orphan-cleanup job (scan R2 for files with no matching DB record) would close the crash-window gap without requiring a full durable-queue rebuild — pragmatic middle ground between "accept the small risk" and "build a saga/outbox system" for what's likely a very rare failure mode

---

## 4. Reports Module — pdfmake/ExcelJS over Puppeteer ✅
**Commits:** `36622ec` (plan doc), `22a200c` (implementation — ReportsModule registered, pdfmake/exceljs added)

### Problem
Needed to generate 6 report types (P&L, expense breakdown, vendor payments, project comparison, government audit, investment portfolio) as downloadable PDF/Excel, suitable for formal government audit submission, running on a resource-constrained VPS (Hostinger KVM2: 2 cores / 8GB RAM shared with the rest of the app).

### Root Cause / Design Constraint
Puppeteer (the common approach for HTML-to-PDF) ships a ~300MB Chromium binary and forks a full browser process per render — a serious resource concern on a small, shared VPS also running the API and Postgres.

### Solution
Chose **pdfmake** (pure JavaScript, ~2MB, no browser process, generates PDF documents from a JSON definition object directly in TypeScript) and **ExcelJS** (styled multi-sheet workbooks) instead. No Puppeteer dependency exists anywhere in the codebase — confirmed the decision was actually followed through, not just planned.

### Alternatives Considered
- **Puppeteer/HTML-to-PDF** — rejected specifically for the VPS resource profile, not for capability reasons; the reports themselves are tabular financials with no charts or complex visual layout, well within pdfmake's capabilities

### Tradeoffs
- ✅ Zero extra OS dependencies, no browser cold-start, negligible memory per report, runs inline in the NestJS event loop
- Reasoning is explicit and well-documented in the planning doc itself — a clean, complete "infrastructure-constrained technology choice" story with the actual tradeoff table already written out

### Improvements
- No post-deploy performance issues found in commit history on the real VPS — worth confirming this holds under real report volume (large date ranges, big transaction counts) before citing "zero issues" as a confirmed fact rather than "no issues surfaced yet"

---

## 5. Role-Based Access Control — REVIEWER Read-Only Enforcement ✅
**Commit:** `9612f65` (May 13, 2026), 35 files touched

### Problem
Needed a read-only reviewer role (e.g. for CA consultant or audit reviewers) that could view all ERP data without being able to mutate anything — enforced consistently across every module, not just a UI-level toggle.

### Solution
New `RolesGuard` + `@Roles()` decorator applied across projects, vendors, transactions, investments, documents, users, reports, and dashboard controllers — a genuinely cross-cutting change spanning the whole API surface in one commit. Paired with a frontend `useIsReadOnly()` hook disabling mutating UI actions for reviewers.

### Tradeoffs
- ✅ Consistent enforcement across every module in a single coordinated change, rather than a piecemeal per-route retrofit
- This is strong architecture material: a real cross-cutting concern (authorization) implemented as a reusable guard + decorator pattern rather than duplicated checks in every controller method

### Correction — verify before citing in an interview
A commonly-repeated detail ("25 passing API tests" for this feature) doesn't check out against the actual test suite — no `.spec.ts` file references `RolesGuard`/`@Roles`/`UserRole`, and there are only 13 test files total in the whole API. **Don't repeat the 25-tests figure without independently verifying it** — it may have existed and been later removed, or run uncommitted at the time. Frame the feature itself (real, substantial, well-scoped) separately from that specific test-count claim.

---

## 6. Vendor Type Soft-Delete Reactivation Bug ✅
**Commits:** `0aa827f` (May 4, 2026, initial) → `1762300` (Jun 4, 2026, fix — one month later)

### Problem
Deleting a vendor type (e.g. "Contractor") and then trying to recreate one with the same name threw a false **"already exists"** error — even though the type was already soft-deleted and shouldn't have blocked recreation.

### Root Cause
The original `create()` method only checked for a slug collision and threw unconditionally on any match — it never checked whether the colliding row was actually active or soft-deleted. A soft-deleted row still existed in the table, so the uniqueness check treated it the same as a live one.

### Solution
```typescript
if (existing) {
  if (existing.isActive) throw new BadRequestException(`A vendor type named "${dto.label.trim()}" already exists`);
  existing.isActive = true;   // reactivate soft-deleted type, preserve isContractor/isSystemDefined
  return this.repo.save(existing);
}
```
Also updated `prune.ts` to use `INSERT ... ON CONFLICT (slug) DO UPDATE SET is_active = true`, making system-type restoration idempotent regardless of how many times seeding runs.

### Tradeoffs
- ✅ Correctly distinguishes "name taken by an active record" from "name previously used by a now-deleted record" — the actual bug class, fixed at its root rather than worked around
- One-month gap between the original bug and the fix is honest material — this wasn't caught immediately, it took real usage to surface

### Improvements
- This exact bug class (soft-delete + uniqueness constraint interaction) is worth checking for in any other entity using both `SoftDeleteBaseEntity` and a unique slug/name field — a good instinct to mention if asked "how would you prevent this elsewhere"
