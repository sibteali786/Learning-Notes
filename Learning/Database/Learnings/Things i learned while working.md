```table-of-contents
```

# COALESCE
- **Providing Default Values:** Replacing `NULL` results with a placeholder like 'N/A' or 0 for display or calculations.
- **Contact Hierarchy:** Selecting the best available contact method (e.g., check `Mobile`, if `NULL` check `Work Phone`, if `NULL` use 'No Contact').
- **Math Operations:** Preventing entire calculations from becoming `NULL` (e.g., `Price * COALESCE(Discount, 0)`).
- **Data Consolidation:** Merging data from multiple columns after a `JOIN` where values might exist in one source but not another.
Example

Suppose you have a table where some users have a `Nickname` and others only have a `FirstName`:
```sql
SELECT COALESCE(Nickname, FirstName, 'User') AS DisplayName 
FROM Users;
```

1. If `Nickname` exists, it returns it.
2. If `Nickname` is `NULL` but `FirstName` exists, it returns `FirstName`.
3. If both are `NULL`, it defaults to 'User'.


# Fetching list of vendors with each project and aggregated amount
### Option A — N+1 (current implicit risk)

```
1 query → get all vendors
For each vendor:
  1 query → sum transactions
  1 query → get projects with paid each
= 1 + (N × 2) queries
```

With 50 vendors = **101 queries**. Slow.

### Option B — Correlated subquery in SELECT (recommended)

sql

```sql
SELECT
  v.id,
  v.name,
  -- subquery runs once per vendor row, inline
  (SELECT COALESCE(SUM(t.amount), 0)
   FROM transactions t
   WHERE t.vendor_id = v.id 
     AND t.transaction_type = 'EXPENSE'
     AND t.deleted_at IS NULL) AS "amountPaid",

  JSON_AGG(DISTINCT JSONB_BUILD_OBJECT(
    'projectId', p.id,
    'projectName', p.name,
    -- nested correlated subquery: paid for THIS vendor on THIS project
    'paid', (SELECT COALESCE(SUM(t2.amount), 0)
             FROM transactions t2
             WHERE t2.vendor_id = v.id
               AND t2.project_id = p.id
               AND t2.transaction_type = 'EXPENSE'
               AND t2.deleted_at IS NULL)
  )) FILTER (WHERE p.id IS NOT NULL) AS "activeProjects"
FROM vendors v
LEFT JOIN project_vendors pv ON pv.vendor_id = v.id AND pv.is_active = true
LEFT JOIN projects p ON p.id = pv.project_id AND p.deleted_at IS NULL
WHERE v.deleted_at IS NULL
GROUP BY v.id
```

**Always 1 query total.** PostgreSQL optimizes the correlated subqueries into efficient hash joins internally. The tradeoff is the SQL is more complex to read but performance is much better.

### Option C — Window functions

Would need `PARTITION BY v.id, p.id` inside aggregates — gets messy when you need both vendor-level and project-level sums in the same row. Not worth it here.


## `findAll()` Query Breakdown

Here's the full query with each part explained:

```ts
const qb = this.vendorRepo
  .createQueryBuilder('v')
```

`createQueryBuilder('v')` starts a query on the `vendors` table and gives it the alias `v`. Think of `v` as a shorthand — anywhere you write `v.name` in the query, it means `vendors.name`.

---

```ts
.leftJoin('v.projectVendors', 'pv', 'pv.is_active = true')
.leftJoin('pv.project', 'p', 'p.deleted_at IS NULL')
```

**`leftJoin`** means: include the vendor row even if no matching rows exist in the joined table (as opposed to `innerJoin` which would drop vendors with no project links).

- First join: follows the `projectVendors` relation on the `Vendor` entity (defined via `@OneToMany`) to reach the `project_vendors` table, aliased as `pv`. The third argument `'pv.is_active = true'` is an **inline condition** — only join rows where the link is active.
- Second join: from `pv`, follows the `project` relation to reach the `projects` table, aliased as `p`. Only joins non-deleted projects.

Result so far: one row per vendor-project combination. A vendor on 3 projects = 3 rows. That's why we need `GROUP BY v.id` later to collapse them back.

---

```ts
'v.id    AS id',
'v.name  AS name',
'v.vendor_type AS "vendorType"',
'v.phone AS phone',
```

Simple column selects. `AS "vendorType"` uses double quotes because PostgreSQL would lowercase `vendorType` to `vendortype` without them — the quotes preserve the camelCase so TypeScript gets the right key name.

---

```ts
`COALESCE(SUM(DISTINCT pv.contract_amount), 0) AS "contractAmount"`,
```

- `SUM(pv.contract_amount)` — adds up `contract_amount` across all `project_vendors` rows for this vendor (remember, one row per project after the join).
- `DISTINCT` — prevents double-counting if the join produces duplicates.
- `COALESCE(..., 0)` — if the sum is `NULL` (vendor has no project links), return `0` instead.

Example: vendor linked to Plot 930 (1,400,000) and Green Valley (850,000) → `contractAmount = 2,250,000`.

---

```ts
`(SELECT COALESCE(SUM(t2.amount), 0)
  FROM transactions t2
  WHERE t2.vendor_id = v.id
    AND t2.transaction_type = 'EXPENSE'
    AND t2.deleted_at IS NULL
 ) AS "amountPaid"`,
```

This is a **correlated subquery** — it's a complete `SELECT` nested inside the outer query's column list. The word "correlated" means it references `v.id` from the outer query, so it re-runs for each vendor row.

Why not just `SUM(t.amount)` with another join? Because we already have a join on `pv` and `p` that's creating multiple rows per vendor. Adding a third join on transactions would multiply rows further, making `SUM` count the same transaction multiple times (a classic fan-out bug). The subquery avoids this entirely — it runs independently per vendor.

---

```ts
`GREATEST(
  COALESCE(SUM(DISTINCT pv.contract_amount), 0) -
  (SELECT COALESCE(SUM(t2.amount), 0) FROM transactions t2
   WHERE t2.vendor_id = v.id AND ...),
  0
) AS outstanding`,
```

- Reuses the same `SUM(pv.contract_amount)` and the same subquery to compute `contractAmount - amountPaid`.
- `GREATEST(..., 0)` clamps the result to never go below zero — so if paid > contract (overpaid), outstanding shows `0` not a negative number.

---

```ts
`JSON_AGG(
  DISTINCT JSONB_BUILD_OBJECT(
    'projectId',   p.id,
    'projectName', p.name,
    'paid', (SELECT COALESCE(SUM(t3.amount), 0)
             FROM transactions t3
             WHERE t3.vendor_id = v.id
               AND t3.project_id = p.id
               AND t3.transaction_type = 'EXPENSE'
               AND t3.deleted_at IS NULL)
  )
) FILTER (WHERE p.id IS NOT NULL) AS "activeProjects"`,
```

- `JSONB_BUILD_OBJECT(...)` — constructs a JSON object `{ projectId: 5, projectName: "Plot 930", paid: 780000 }` for each vendor-project row.
- The nested subquery inside is another correlated subquery, this time scoped to **both** `v.id` AND `p.id` — so it gives paid amount for this vendor on this specific project.
- `JSON_AGG(DISTINCT ...)` — aggregates all those JSON objects into an array `[{...}, {...}]`, one entry per project. `DISTINCT` deduplicates in case the join produced duplicate project rows.
- `FILTER (WHERE p.id IS NOT NULL)` — if the vendor has no active projects, `p.id` is `NULL` (from the LEFT JOIN), and this filter prevents a `[null]` array — instead you get `null` which we can handle on the frontend as an empty list.

---

```ts
.where('v.deleted_at IS NULL')
.groupBy('v.id')
```

- `.where` filters out soft-deleted vendors.
- `.groupBy('v.id')` — this is **required** because we used aggregate functions (`SUM`, `JSON_AGG`). PostgreSQL needs to know: "collapse all rows with the same `v.id` into one". Without it, you'd get a SQL error.

---

```ts
qb.orderBy('v.name', 'ASC').offset(skip).limit(limit);
```

Standard pagination. `offset(skip)` skips the first N rows (e.g. page 2 with limit 15 → skip 15). `limit` caps how many rows come back.

---

```ts
const [rows, total] = await Promise.all([
  qb.getRawMany(),
  this.vendorRepo.count({ where: { deletedAt: IsNull() } }),
]);
```

- `getRawMany()` — executes the query and returns plain objects (not TypeORM entity instances). Used here because we have custom `SELECT` aliases and aggregates that don't map to entity properties.
- `Promise.all([...])` — runs both queries **in parallel** instead of sequentially, saving one round-trip to the DB.
- The count query is separate and simple — TypeORM's `.count()` is fine here since we just need the total number of non-deleted vendors for pagination metadata.