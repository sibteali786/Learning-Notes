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
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=
```
%%