Query
```sql
EXPLAIN ANALYZE
SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
FROM article a
JOIN publisher p ON p.id = a.publisher_id
WHERE a.region = 'US'
ORDER BY a.id DESC
LIMIT 20;
```


QUERY PLAN
----------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=0.59..4.69 rows=20 width=119) (actual time=0.264..0.440 rows=20 loops=1)
   ->  Nested Loop  (cost=0.59..513534.89 rows=2508658 width=119) (actual time=0.262..0.432 rows=20 loops=1)
         ->  Index Scan Backward using article_pkey on article a  (cost=0.43..450880.11 rows=2508658 width=91) (actual time=0.165..0.281 rows=20 loops=1)
               Filter: (region = 'US'::text)
               Rows Removed by Filter: 74
         ->  Memoize  (cost=0.16..0.18 rows=1 width=36) (actual time=0.006..0.006 rows=1 loops=20)
               Cache Key: a.publisher_id
               Cache Mode: logical
               Hits: 16  Misses: 4  Evictions: 0  Overflows: 0  Memory Usage: 1kB
               ->  Index Scan using publisher_pkey on publisher p  (cost=0.15..0.17 rows=1 width=36) (actual time=0.023..0.023 rows=1 loops=4)                          Index Cond: (id = a.publisher_id)
 Planning Time: 2.160 ms                                                                                                                            Execution Time: 0.855 ms
(13 rows




```sql
EXPLAIN ANALYZE
SELECT a.id, a.title, a.url, p.name AS "publisherName",
       a.category, a.region, a.published_at AS "publishedAt"
FROM article a
JOIN publisher p ON p.id = a.publisher_id
WHERE a.region = 'US' AND a.id < 500000
ORDER BY a.id DESC
LIMIT 20;

```

                                                                       QUERY PLAN
--------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=0.59..4.89 rows=20 width=119) (actual time=1.452..1.918 rows=20 loops=1)
   ->  Nested Loop  (cost=0.59..26572.84 rows=123758 width=119) (actual time=1.449..1.908 rows=20 loops=1)
         ->  Index Scan Backward using article_pkey on article a  (cost=0.43..23481.14 rows=123758 width=91) (actual time=1.400..1.802 rows=20 loops=1)
               Index Cond: (id < 500000)
               Filter: (region = 'US'::text)
               Rows Removed by Filter: 39
         ->  Memoize  (cost=0.16..0.18 rows=1 width=36) (actual time=0.003..0.004 rows=1 loops=20)
               Cache Key: a.publisher_id
               Cache Mode: logical
               Hits: 16  Misses: 4  Evictions: 0  Overflows: 0  Memory Usage: 1kB
               ->  Index Scan using publisher_pkey on publisher p  (cost=0.15..0.17 rows=1 width=36) (actual time=0.009..0.009 rows=1 loops=4)
                     Index Cond: (id = a.publisher_id)
 Planning Time: 0.668 ms
 Execution Time: 2.001 ms
(14 rows)