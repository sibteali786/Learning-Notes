---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Gather Merge  (cost=3918953.46..8933593.35 rows=43056508 width=8) (actual time=20160.191..30948.339 rows=43000301.00 loops=1)
   Workers Planned: 2                                                                                                                Workers Launched: 2
   Buffers: shared hit=789 read=952650, temp read=189384 written=189906
   ->  Sort  (cost=3917953.43..3962803.96 rows=17940212 width=8) (actual time=20011.438..22019.843 rows=14333433.67 loops=3)
         Sort Key: g DESC
         Sort Method: external merge  Disk: 253768kB
         Buffers: shared hit=789 read=952650, temp read=189384 written=189906
         Worker 0:  Sort Method: external merge  Disk: 251304kB
         Worker 1:  Sort Method: external merge  Disk: 252544kB
         ->  Parallel Seq Scan on students  (cost=0.00..1265901.48 rows=17940212 width=8) (actual time=128.033..13088.115 rows=14333433.67 loops=3)
               Filter: ((g > 8) AND (g < 95))
               Rows Removed by Filter: 2333233                                                                                                   Buffers: shared hit=715 read=952650
 Planning Time: 0.073 ms
 JIT:
   Functions: 12
   Options: Inlining true, Optimization true, Expressions true, Deforming true
   Timing: Generation 0.942 ms (Deform 0.309 ms), Inlining 259.131 ms, Optimization 67.196 ms, Emission 55.005 ms, Total 382.274 ms
 Execution Time: 33167.307 ms ^Y2G5MaKO

Its for non indexed, and 50M rows ^NyamK58z

explain analyze select id, g from students where g > 8 and g < 95 order by g desc; ^36vW7aO4

explain analyze select id, g from students where g > 8 and g < 95 order by g desc limit 1000; ^r9SzLNQS

Limit  (cost=2250543.97..2250660.44 rows=1000 width=8) (actual time=16603.312..16609.081 rows=1000.00 loops=1)
   Buffers: shared hit=1071 read=952368
   ->  Gather Merge  (cost=2250543.97..7265183.98 rows=43056509 width=8) (actual time=16574.034..16579.708 rows=1000.00 loops=1)
         Workers Planned: 2
         Workers Launched: 2
         Buffers: shared hit=1071 read=952368
         ->  Sort  (cost=2249543.95..2294394.48 rows=17940212 width=8) (actual time=16557.726..16557.813 rows=1000.00 loops=3)
               Sort Key: g DESC
               Sort Method: top-N heapsort  Memory: 115kB
               Buffers: shared hit=1071 read=952368
               Worker 0:  Sort Method: top-N heapsort  Memory: 115kB
               Worker 1:  Sort Method: top-N heapsort  Memory: 115kB
               ->  Parallel Seq Scan on students  (cost=0.00..1265901.48 rows=17940212 width=8) (actual time=81.805..13611.605 rows=14333433.67 loops=3)
                     Filter: ((g > 8) AND (g < 95))
                     Rows Removed by Filter: 2333233
                     Buffers: shared hit=997 read=952368
 Planning Time: 0.078 ms
 JIT:
   Functions: 13
   Options: Inlining true, Optimization true, Expressions true, Deforming true
   Timing: Generation 1.066 ms (Deform 0.353 ms), Inlining 181.089 ms, Optimization 52.462 ms, Emission 37.018 ms, Total 271.635 ms
 Execution Time: 16609.497 ms ^MYGjMpgV

Gather Merge  (cost=3918593.59..8932648.23 rows=43051483 width=8) (actual time=23407.568..34209.309 rows=43000301.00 loops=1)
   Workers Planned: 2
   Workers Launched: 2
   Buffers: shared hit=1542 read=951897, temp read=189383 written=189904
   ->  Sort  (cost=3917593.56..3962438.86 rows=17938118 width=8) (actual time=23298.711..25307.638 rows=14333433.67 loops=3)
         Sort Key: g DESC
         Sort Method: external merge  Disk: 252480kB
         Buffers: shared hit=1542 read=951897, temp read=189383 written=189904
         Worker 0:  Sort Method: external merge  Disk: 249384kB
         Worker 1:  Sort Method: external merge  Disk: 255744kB
         ->  Parallel Seq Scan on students  (cost=0.00..1265865.00 rows=17938118 width=8) (actual time=113.332..17011.944 rows=14333433.67 loops=3)
               Filter: ((g > 8) AND (g < 95))
               Rows Removed by Filter: 2333233
               Buffers: shared hit=1468 read=951897
 Planning:
   Buffers: shared hit=27 read=9 dirtied=2
 Planning Time: 12.182 ms
 JIT:
   Functions: 12
   Options: Inlining true, Optimization true, Expressions true, Deforming true
   Timing: Generation 0.960 ms (Deform 0.285 ms), Inlining 218.651 ms, Optimization 68.137 ms, Emission 52.198 ms, Total 339.946 ms
 Execution Time: 36379.358 ms ^306NN0D7

Afdter Indexing g  ^qpeYvfUN

Limit  (cost=0.56..1933.77 rows=1000 width=8) (actual time=2.282..3.871 rows=1000.00 loops=1)
   Buffers: shared hit=768 read=40
   ->  Index Scan Backward using g_index on students  (cost=0.56..83227396.87 rows=43051483 width=8) (actual time=2.281..3.683 rows=1000.00 loops=1)
         Index Cond: ((g > 8) AND (g < 95))
         Index Searches: 1
         Buffers: shared hit=768 read=40
 Planning:
   Buffers: shared hit=20
 Planning Time: 0.190 ms
 Execution Time: 4.001 ms
(10 rows) ^IKebkUqs

explain analyze select id, g from students where g > 8 and g < 95 order by g desc limit 1000; ^gEdGMsCf

Limit  (cost=0.56..2088.01 rows=1000 width=8) (actual time=2.221..3.943 rows=1000.00 loops=1)
   Buffers: shared hit=752 read=21
   ->  Index Scan Backward using g_index on students  (cost=0.56..8762738.72 rows=4197833 width=8) (actual time=2.219..3.800 rows=1000.00 loops=1)
         Index Cond: ((g > 10) AND (g < 20))
         Index Searches: 1
         Buffers: shared hit=752 read=21
 Planning:
   Buffers: shared hit=20
 Planning Time: 0.131 ms
 Execution Time: 4.074 ms
(10 rows) ^leCLVu3d

Gather Merge  (cost=1472145.96..1961052.79 rows=4197833 width=8) (actual time=16948.944..18078.841 rows=4498746.00 loops=1)
   Workers Planned: 2
   Workers Launched: 2
   Buffers: shared hit=2161 read=951278, temp read=19848 written=19901
   ->  Sort  (cost=1471145.93..1475518.67 rows=1749097 width=8) (actual time=16914.167..17107.819 rows=1499582.00 loops=3)
         Sort Key: g DESC
         Sort Method: external merge  Disk: 26872kB
         Buffers: shared hit=2161 read=951278, temp read=19848 written=19901
         Worker 0:  Sort Method: external merge  Disk: 26272kB
         Worker 1:  Sort Method: external merge  Disk: 26392kB
         ->  Parallel Seq Scan on students  (cost=0.00..1265865.00 rows=1749097 width=8) (actual time=89.072..16318.163 rows=1499582.00 loops=3)
               Filter: ((g > 10) AND (g < 20))
               Rows Removed by Filter: 15167085
               Buffers: shared hit=2087 read=951278
 Planning:
   Buffers: shared hit=20
 Planning Time: 0.126 ms
 JIT:
   Functions: 12
   Options: Inlining true, Optimization true, Expressions true, Deforming true
   Timing: Generation 0.937 ms (Deform 0.299 ms), Inlining 158.523 ms, Optimization 61.520 ms, Emission 44.615 ms, Total 265.595 ms
 Execution Time: 18310.276 ms
(22 rows) ^TQJBJRS2

explain analyze select id, g from students where g > 8 and g < 95 order by g desc; ^sN62G5Pc

explain analyze select id, g from students where g > 10 and g < 20 order by g desc limit 1000; ^Tk0repmF

Gather Merge  (cost=1472145.96..1961052.79 rows=4197833 width=8) (actual time=16135.685..17046.621 rows=4498746.00 loops=1)
   Workers Planned: 2
   Workers Launched: 2
   Buffers: shared hit=2913 read=950526, temp read=19848 written=19901
   ->  Sort  (cost=1471145.93..1475518.67 rows=1749097 width=8) (actual time=16103.397..16260.068 rows=1499582.00 loops=3)
         Sort Key: g DESC
         Sort Method: external merge  Disk: 26784kB
         Buffers: shared hit=2913 read=950526, temp read=19848 written=19901
         Worker 0:  Sort Method: external merge  Disk: 26144kB
         Worker 1:  Sort Method: external merge  Disk: 26608kB
         ->  Parallel Seq Scan on students  (cost=0.00..1265865.00 rows=1749097 width=8) (actual time=84.993..15531.587 rows=1499582.00 loops=3)
               Filter: ((g > 10) AND (g < 20))
               Rows Removed by Filter: 15167085
               Buffers: shared hit=2839 read=950526
 Planning:
   Buffers: shared hit=32 read=8 dirtied=3
 Planning Time: 12.894 ms
 JIT:
   Functions: 12
   Options: Inlining true, Optimization true, Expressions true, Deforming true
   Timing: Generation 0.864 ms (Deform 0.264 ms), Inlining 150.266 ms, Optimization 56.826 ms, Emission 46.839 ms, Total 254.794 ms
 Execution Time: 17243.445 ms ^mUtSX1ng

explain (analyze, buffers) select id, g from students where g > 10 and g < 20 order by g desc ^1CkIHpwe

Limit  (cost=0.56..2246.22 rows=1000 width=8) (actual time=2.121..3.203 rows=1000.00 loops=1)
   Buffers: shared hit=771 read=5
   ->  Index Only Scan Backward using g_index on students  (cost=0.56..9426883.05 rows=4197833 width=8) (actual time=2.120..3.139 rows=1000.00 loops=1)
         Index Cond: ((g > 10) AND (g < 20))
         Heap Fetches: 1000
         Index Searches: 1
         Buffers: shared hit=771 read=5
 Planning:
   Buffers: shared hit=20
 Planning Time: 0.162 ms
 Execution Time: 3.257 ms
(11 rows) ^BKFH4r2R

explain (analyze, buffers) select id, g from students where g > 10 and g < 20 order by g desc limit 1000; ^ZeY17obD

Limit  (cost=0.56..31.55 rows=1000 width=8) (actual time=0.023..0.378 rows=1000.00 loops=1)
   Buffers: shared hit=8
   ->  Index Only Scan Backward using g_index on students  (cost=0.56..130065.23 rows=4197833 width=8) (actual time=0.022..0.253 rows=1000.00 loops=1)
         Index Cond: ((g > 10) AND (g < 20))
         Heap Fetches: 0
         Index Searches: 1
         Buffers: shared hit=8
 Planning:
   Buffers: shared hit=24
 Planning Time: 0.231 ms
 Execution Time: 0.463 ms
(11 rows) ^fSGShhjI

explain (analyze, buffers) select id, g from students where g > 10 and g < 20 order by g desc limit 1000; ^hagGv5sv

After Vacuum ^DpRzd35r

Database ^kshQGdAT

App ^vqirKhSR

DISK ^qlewDIj6

RAM ^YuDVTzxm

- g has Index on it 
- id is Primary Key ^vBmLgGjQ

%%
## Drawing
```compressed-json
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
```
%%