explain analyze select name from grades where id = 7;
                                                            QUERY PLAN
----------------------------------------------------------------------------------------------------------------------------------
 Gather  (cost=1000.00..114494.90 rows=40414 width=32) (actual time=4.127..3414.254 rows=1.00 loops=1)
   Workers Planned: 2
   Workers Launched: 2
   Buffers: shared read=67356 dirtied=67356 written=62865
   ->  Parallel Seq Scan on grades  (cost=0.00..109453.50 rows=16839 width=32) (actual time=2250.009..3384.044 rows=0.33 loops=3)
         Filter: (id = 7)
         Rows Removed by Filter: 3333333
         Buffers: shared read=67356 dirtied=67356 written=62865
 Planning:
   Buffers: shared hit=5 read=3
 Planning Time: 0.139 ms
 JIT:
   Functions: 12
   Options: Inlining false, Optimization false, Expressions true, Deforming true
   Timing: Generation 3.357 ms (Deform 2.168 ms), Inlining 0.000 ms, Optimization 0.729 ms, Emission 11.463 ms, Total 15.548 ms
 Execution Time: 3416.364 ms
(16 rows)


This one is without any index ( not even primary key)
After indexing 

explain analyze select name from grades where id = 7;
                                                    QUERY PLAN
-------------------------------------------------------------------------------------------------------------------
 Index Scan using id_idx on grades  (cost=0.43..8.45 rows=1 width=15) (actual time=0.052..0.053 rows=1.00 loops=1)
   Index Cond: (id = 7)
   Index Searches: 1
   Buffers: shared read=4
 Planning:
   Buffers: shared hit=23 read=1
 Planning Time: 0.492 ms
 Execution Time: 0.065 ms
(8 rows)

- Its still Index Scan ? it has to still visit disk to get Page where name is present ( id = 7 )

explain analyze select id from grades where id = 7;
```sql
                                                     QUERY PLAN
-----------------------------------------------------------------------------------------------------------------------
 Index Only Scan using id_idx on grades  (cost=0.43..4.45 rows=1 width=4) (actual time=0.029..0.029 rows=1.00 loops=1)
   Index Cond: (id = 7)
   Heap Fetches: 0
   Index Searches: 1
   Buffers: shared hit=4
 Planning Time: 0.053 ms
 Execution Time: 0.040 ms
(7 rows)
```

explain analyze select name from grades where id = 7;
                                                       QUERY PLAN
------------------------------------------------------------------------------------------------------------------------
 Index Only Scan using id_idx on grades  (cost=0.43..4.45 rows=1 width=15) (actual time=0.029..0.029 rows=1.00 loops=1)
   Index Cond: (id = 7)
   Heap Fetches: 0
   Index Searches: 1
   Buffers: shared hit=1 read=3
 Planning:
   Buffers: shared hit=19 read=1 dirtied=3
 Planning Time: 0.486 ms
 Execution Time: 0.039 ms
(9 rows)


- Since name is also included in the index itself thus we do not go to heap
explain analyze select g from grades where id = 7;
                                                    QUERY PLAN
------------------------------------------------------------------------------------------------------------------
 Index Scan using id_idx on grades  (cost=0.43..8.45 rows=1 width=4) (actual time=0.008..0.009 rows=1.00 loops=1)
   Index Cond: (id = 7)
   Index Searches: 1
   Buffers: shared hit=4
 Planning:
   Buffers: shared hit=3 dirtied=1
 Planning Time: 0.085 ms
 Execution Time: 0.018 ms
(8 rows)

see the diffrence for `g` its not in index ( Covering Index ) thus Index Scan and 