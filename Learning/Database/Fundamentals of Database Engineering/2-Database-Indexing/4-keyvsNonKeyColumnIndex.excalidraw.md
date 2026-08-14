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

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCABNHgBxAFYAWVwAaQB5NNLIWERKqCwoTrLMbmcAFgBmZPj6gDYeev4ymFGe

eIB2bTGABgnZjfWxsYAOeNnE46XIChJ1bjPjzcWiyEkEQmVpbgmx+u16xKAoHAwHrK4QazKYLcbbg5hQUhsADWCAAwmx8GxSJUAMTxBD4/FDSCaXDYJHKRFCDjEdGY7ESBHWZhwXCBHLEiAAM0I+HwAGVYNCJIIPJz4YiUQB1W6Sbh8F4QCXIhCCmDC9CiirgqmfDjhPJoeLgtis7BqFZG7awxWU4RwACSxENqHyAF1wVzyFkndwOEI+eDCDSsJV

cNtOVSafrmC7/YHFWEEMR7hd1vV1vFfmNwYwWOwuGgeJdFXnWJwAHKcMT3LPzCY8CY2rrlZgAEQy/RTaC5BDC4M0whpAFFglkci73eChHBiLgu/d1sdZud6jw1suFS3MeTk9xe/h+4r+phBhJavO3qRUI0mMoEKhUAAKPTwgC8U3ix0S9QmW1m2jaN+EwTACf6gagiIUMwb6TNscz1NsxyoDcxDqG+xwAJTPmSUBCAQqBQIQWRvjw2xnNsCSJPEg

FNokJzaCBiSQWw0GwU21pNjR1qoJipowfEmEADocI+qBSliKIsKgAAK+DWPqxBFmJKmqWp6kaZpWnaTpul6VpEmkFJzCoAAMrg1LYG8Sm8CJYkAEJCFyXJMPIqDMJIbLJqgkhqG+S7MYEuDEG+P48LMiHUIRmRwJBIQhV+iQTMcYwoaQaj9Bwb6JYk2yzHZj7OAAfI+/JYlAj4vmw76fusP5/pMtGJPMxy7NozUsWxGz0dsaw8ChsoYdhT64fh+C

EcRCCkda8Q0ZMxyAeu5HJClEydQJkwgZt2izOsvFsPxH7CaJGllaQFUtAgMBoMoqBtsO/KogV6lnRVt7qGwNkDEwHAEVkpD3o+baEMwSJFr+6yzMcSL2c9amOc5rloB5XnED5fkBXFwWhWuEWwtF+ixUFCXASlaUZdk2Xfrl+UnephlSag2xoKgr03ggH1faeP1/XeD53SDYO8PU8RNmMMNw6pDNMKg8Qs2z72SJ9aDfaQv3jf9gMC6D4MLEcEt0

2pxWPjJbIEME438ggACOrN4KJnDuXhxDZLklWvlAb6UdagHxOFALkVsyFQQJdU7H1A1oZIQ04dgeEEURJF+wtux/gkTbHAts31Ot2WbT8IE7XtfFyEdktaQAYry/SkGgT5PrdJVYagACCFZts+t0ADyoD+mHHfpABKrEmYPmRsIwaOaDAqBV/gNdFiBDYgfpq9r+vG96QjLksMjnmBGjvme5mOfEzj/vbHZckKcGt0ACqTWg3vrGt+jMHZABSDp3

8gz0V5ZRFOBuT9s9NocBAEcDcg6DgRAOC30IqQIQCAopgMToQIw84CwIKQVFYcmA4CBFjAWEyCIcF3QQFyLE+h4GkIQM9B+1CODKDQLUbITBMGO0ovRfqb9nwdkoaQfQTNGLbGYm/TCUVoGwPgQsaYEx4ioDfig8BxF0EcNErtKisxFHMFwdQohjt6h/GtDnJRqA75sCiONZKcQeCHB0XZPBCBsBCAgeYx+qAQJnE2E2Pab9IyUDvgMSoF51Ay1v

ADfmVUarUW/L+f8gFgKgSSoxU+I92LwTxshVC6Fm4jTjmNCaJEyIUSojRER9EFpMVznBTigceIlwEgPR80tpLXw4IpZSm9uk9N6X08SklXJmQshwKyyYizPW3kjdy+9vJH38t+LGIUwp4yiv0QmSyqZJTJhQdKMhKY5Tys9Y2rNyru2qp7Wq9UthpymC1NqHUQ7ZTDr1P2kdcnDVGgnSa01yJzWSotEpK1Ji5yzEvbau19qHQmM0l6ZzLrXVQLde

6j1y5iQVhzJWXMa7q0UXzIGgtwYTEhtDWGhtVJTN3jM1G6Nj6LLPisyKBMibxS2clVKuyKZZUObTTSrSmbyzOYrZWqBVa4s1vzYGOthai22OLMlfLBnXjlqVIVmKRVit5pEgl0qFh63lWiwqJVZJmz5EEVmNs7bWFQI7eEQgXYTnOe+b2lEEj+1ynNYO6TurhzeTk6OeSvnjUTlNZO2hU6+wzlnGYoL84QuLgdUuMLDXqTngvZ8DdUBN2wm3Duma

e591hTpYe0FUBj30BPby09Z7VyYIvECjY1r9ObS2zelK3IowPrS/yMaGW40QlfeSHT4EMIQE/cNL8HGiS/j/P+ADiFGh4KAlRQC0BSODDQxByDUCoNURgtxtDcH4MIeWSB2Dt38KoZupB9DVFMJYWw8gbiuFjB4SZJ8l7BHCLojoiRqB11wKYcLORCizG7uofurBmikjaLMcOfRp7UBGPDfBHRUULFWM8ccWx9i36OMwM41xWDR1oC8Zo3xOjOSU

JyPydB4hZazE9JwKAFdcDUPwJaTx4ITxQBbkQZQhZ0DBC5IMXMTAiLuD4x8QT0BTScj0DkXAwYmC+jQPGfAJp0r+AIEE08ITLzhPxc+D2H5YnXLGABICSVkngTSWxOCCEkLvIDZ8gp3zinkVmJRJI5S6IMWqU82pux6nbChaXQSz1WkmXaZ03grb4sJf6VF4ZllrITLpu2veNL5mYz7RfNZMVNmJXZeTfZ3LqZHLpictmxmLmme6vExqjFmrFged

op5PrXn9X9THfJ8dg0/LIn8m5C0UhAqAiCjrcbC6QsaWXclKk2YIpundB6T0FvorVZzFW3M1Zaq1lKoWCxiVQwNppTL1Ku05fpayxl+N1ksuxsVnZezMpbJpim/lzNVXnXZtt0Vu3xVGcO+DWVBqNstKVbLQVv3hXYp5hrYHhLhb6rOxpE5ptyBmstpa/k9sbWiTtQ6t2tXnUod9u6wOJxQUvIjj1wNbmBtJ2LOGwu6ckLRrsxtcFM2E3QqLdpNN

daM2N1QM3XNndUAFvqP3FNakS2j3HpPVA1ahe114EvRtiXtc64ck5HeHbZmHwxr227/bL6iRiyOjxz9X7v2nd/X+dN/6jIgcApddNd2rv/TAjdQHD07pURB9R56j0EINMQ0P5CBGMNurQ29seH36ifVgl9b6+EUKod+0Rv7JG+8A7dWR6dQO6MD2gyDjtoMdTgwhrByGTFofMZYgiNiUi4ft6gJxLi3Ekc8fI8j2w/F5HBBZKAbAx6sCMPRw9ipY

EIAABLvE+GeWWKRwSeWYLpqAplgxIn3H2ZBs/d9+gDPgIoABfJYJQygVAkHsegUp1i4DaGMTkPR6PQGCeCEYaBxhjGSGMLNHsMlFMHlL+OCJxs4P3oxEuHrL+GsL+CBOCP6twIcAtECOFOmEuH7M8C2G8B8F8GgCcCPkwhqM2GUMqCiHSFiLiISASEgAOGSBSFGLSBiDQYyOQJAqyOyKJoqDyHyGqBqEqBiNqImAiCqDKFHPKHCOISiIIR/lqCmD

qMIHqAaPcCaGaBaPcNaOCHaDOE6JOB6Hwd6AgKpqgOpkGCGD/ugLgPEJGEOMQDGHGKfnCAgHuGgNRHVPIo2DmKWK5AWKgb4S2GWAWFWKMvRgFBcICOuEGO2J2O4agAeEeC2IONSMQKOJkK7IYdOLOPOAkRsMuKuGRKBHlOCLAnvmpi4bPmwLuN2IkQftxsEhIFgD4EpqJNYAQDAFPu5BkHHKgCQFFLdF6AYE7PalkShFeA+KLshNYGjN3CJD+Daq

QC7NeNWrdC7MwNgAANwBIUBb6VAtHyTBioAdEcbdFhDBB9EDFIqJGIhCJE7jEUCTE3FNwnE0g3HS5LErEq4zzrHhDbFUbMa0ZT7yjkGQDUYsZsa8icYTCNGnhSYCaVDCa8HBHibmAEAIkyZj5wDybMZtEqZ1EWGKhYgfDBg6ZNHoCHFtFvGdHnG9EVTXFDF3GjHE4mRPFMBTFZpi5vFzFS69w5xYjfFrGoAbEAkj6uLj7hB0b76HiH7bjKaL4EEr

40RbhlAb5b474cAVH1GykX5X6Ki37oAVgwBsYtD1DHBGBv7wAf48acjWHjBrgJD/6/iZy7TwG7QQH3BeYpC7TyK4yJCwFLjIGyjfCiIwG4FqlL6EGyzJCqmQCQhkEyGShohsEMjoB4j0FEiMHkh6E0jUFpnQCcEsheQciei8gChCgKEiFKFiHJmSF3BFhJkqjyGVCKH2F+CSBOHqHEmaGwDaFgkQB6GOjOgFBGEthehsamGElVEtjBguzWEQipDK

FpFdmVEJgthJh1EzAvzkSbhxkMD+GcDcDEF+H5iVjVgRGJCNjHA/AxEGlxHBALg9gNGKipEjhjhZGjk5FzhPmyxLgrjWbmmTD7k7goh1FJFyllC2kSAOhuwCLmGOxzlYDJhRSzFIbbCNDrS7H7EwVwVYgIWiRIUEbECoXvGISYUhyAk0bSlGiMZ8HMasbsYwlwm8b8YybImch5gSYYlsV9BybggKZRDKakBmFEktgknab4A4XoCwUmTwUcCIVWEo

U8noUUUjycij6SmT7T5bplEKlRnKlr6KjqkDCanakQV6Vakn58h6lFDX6QCGkQCkCJD8hGCmQVgACK/IVpvQjIX+io9pvwcQUwr6AZ3iPAAZEZkAnGCwTw/+fUMwOwuwZwwZUhVo34E2xKUVUgBl8oQRZQCZ9GA5lBKZ9ItBmZDBr5TBuZrBZVHBzI3BrsVG5ZLZIo1Z4oshCA9ZcojZtZzZlZrZ7Vy5qhsY3Z4lvZnG8QOhtoVIw52Rxhk5olM5

N+VhYYEw7Z0Yaha5GmiYbhdRq0AZdiFwYmZ5gmZEJ1p6YRNY9aOwu0A5IMHYj5CRFlr5DhGR44uQX5ioM4P5+R/55wIEKUiEA5oFz1L5LY0FlJ+CRx7R6sXRD4FxziDJJFNxwx9xzsjxzx0xKl3c/JXxMswpopvEqiFUU11oOxOogSFJGA0N1Jpx8NPRlxyNgxtxIxDxjq7JgQLx3JaFuNixgpBNvxIp/xxN1CpN1o2wFN9F1FIJRYA5EJjF0J3w

LFmJSJFCKJZQXF6J+AqtjI/Fiogl+JIl0565ZQElZJUl1NVJxx9NdJTN/RKNTJbNGNHNWNXJMx7xfNApyxgtNxRNRAYtssEtUtLYmlE+NFoeR++oipy+9wRleBoQGpx+z5spll2p6mtlpQ9l5QdREAjQVQtQAAVo0HAMoAAGo+U2n+UtiBWNTURjDYEpSPBLj5XRWhkNShUZhQzNSzSTCpUNmyyvrZX4Gx1EHrhbAkFQhFVNlUGpnlV0Gcikg5ks

H5l9BFmNWll8EtUDVtVigz1dUhm9UbmdWtWahDWKi6idlbWywaFkhaFWgDlDkGFfXjkmFLWm0OWrUSC4Cv7LmbWjXbWuEJFrgbDmmZz7khFHlEHGinmXUXnfA8D/6HD0R0WzkPkcxg2p2vVpHvWfloBTjfW5G/kFEAU/DwSnAljbg1FgUynJFQXU076B2k6ezriIT1B12bBjaIQriURHCgoS3Oa9ZBpFKho8PgR+y+w8PJBIQKIdYS0oZhZNKTL6

7TKdpzJ+RTWZibJhR7DHDHLGqhJXjszarMOkQLDwQcOATrD+xfh/gXA1JNiObMT06ub9YiPZQRSHCs5jCSMZjJDrBOZyM+wNKJpKMQ4DJGRDIxbjK2ThPJbmSpYxMe7nYqNUpqPG6eyaOyNm6NhQwprVZnKmPrjOl11/Bjb0QhVBw049R06DQM5uMhoeNGKbDWOWZnDNNASiz8PBOhZzbJrhNqRLZXQrYorrb6QYr/bYnOAVg+QhByCFO3gVqkCI

rZxo66QXbpPdpZPaNri6Ny5SxQ7fanKw7qo2RTMzNvC4DzO/bsxLMrMzBrM6T8oqrHNvSnNoDnOzNXOCA3OLNYj3P1CPPaQY6moWwWq2x47Wq2ou0k7RKewuoU4RQepVMda05+p1OuOFKNOnBATwSRr7A0ReZc55w85/izahPzbdJq51yZrZqtztyS7S6y4DPaQK5lpK5VozzUsa4NogT7NaQbNG7dqgg7O5N6OW5DoF7uJZDjqD7IR4YO6zrO7z

re6izLpu5rr57XrbrgZqIHq6Wd7HoR5AJR6fqx7noJ63xJ7sJuLcQrg6IZ4x7fq/i54+7SJAZfjcSLJgZB56t15xAWZvp6IgyIbErhpfiN4YYER2KEsQQKuGuEY94eJnBeYAEBmUaU17EMMk1OosPmPsN2OcOsN5Tel8NBOhYuOxwNM/IpttTeGSOpvhqnDdMuqKPZSwqCvZYaOD7ZPYw6N5NVYGMGbXgRJaxwtmNsOWPaCtMiw3ntRer2aON4zO

MYtVtYs1ueM+O7A+MJCeP+OBPeryMhOHQRZxNKrRaStJOfbnspajJpaxMpOIxpNCvzLbN5Z7PhMFM3PjvFM/ilOAoVP0Qovepovdart9brtJwRQZjTvhS+MwenBrTlsKN9MC5aRDOIrIprb8ubYnOTOmjTNfPXMVS3P/NGgPMKpbypOG5duZM9uisfv6RfYw5vP4dwCEeXPEePh/PLPkeAuUe6TPMsd/ZYofMEcXNzM/Mkc8cAtAtaQgtY5gtWwQ

v47QtjGOqmMItupItU4Luhw1PotRxCOM7uM4utRlOiwEs7SoZTaktFxtv9NUu1rq71zTE5oMv5r8nMvdJsvlqVpTxcvOf1rLwTA4caSdtXZ+QivvsDuySSvW4yvCJytTqoAzpO5iQu5xwLqyyhee4rqQKavutx4Gu6sV6iQB54Lh4GJnoB5mvauWv3qoCsLJ4h52uwbvpmvOt25/oAbwKetNtiKl6lch6OmBuN7wYhtYJhu7mRvN7jQxs7Rxsd5d

5EaOy961tptD5UVQDAn0YpXS2QlMXK3HgDC61Cbq2cVomSa8V604kCV4nCXv07XiVaYW3SUQCMNqC5sTsWOFuArcOlupTluCP1OQeiNebiNxC7uNsyMtsocUunt65Ps0eRd0daMxfitiQnKGOGYmM/v5tTszu2PzsOOZKIQrtGeg/uaiMZhbs/C+N1TTsHtdRHu9MI9odiTJbRM2TJMaTxMjJjI88poRfqNo+9vLK7Oxfo7Go1b48lN2NlPriAc+

PU6osGdgeU+YvU9NMwetPwebCIdw/HtJoc+nTwrDM3GjNhevMiciqfOcdSfcfjy8eywUfW8i8ZPZT0cY/W/Mc/aseieETidEeO+kcu+rMCdPNQ4vMTOB/2+ScLPO+yeR/AvGqY7mzmrKdWoOyE4wsmSafk7acByerVO+oa8fJrva9md4vpxWdEuxp2fkv87W9qTcuufu3ud5pe3eeby+ccsBc1rzzC6Nohct8UrUdZao+hTps+8Ss3xAa97Pzysd

5pdzqu7Zdqt5catut+7FdkLDf6tkKVcnqR61eZ6CL1d0wMJWtNePqtfhr2u8Ifrn9CKUSgTdd55Feyw4tISDfKLl4jcA28wcbrXkdjTcI2ZiKNvN0zCLdTEy3AjN3mIzJspGWwdNv4nFJj5w6stSOvKWjq5UjQ8dNUonVMrJ0dSdDSAOUWspn5Sgl+OygaVzpNhZgFYCsNsDbDrBK6fQausMFGCTAAIN5eREhCyrmliwnpNANhkojhR5gEVJIHMD

IioMygKBI0MSizgLB18+A1AK+gDaT1EyfVWenVXTJ0EsyVVZeg4VXr1UuCJZDWuCW3rqgqye9XQQfTSq8B96p9YQvYJbCX1VyN9HsnfT7IP1dCs1Z+vgzHJlAJyPoE2s9xWrzkww9QDao4WvpiUKCe1RcL8FODsM7yqJU6twHkGQBIGHAK6ntwigRUIoU1WIo9QwbgVwaZQN8ukQ/ITgX6ZQH6nkS3L/UkodUa0JmDKLUNMG5Az/HpnPDDtjGY7E

zJ+GOBgR/gyQKzA2FmAMRGwpPEWCcDWiVsIO2vHwoPn+BQxaIr6MMj+kCwcRgs3ENnie1hRc9L2QvOmPz0SbnCkeBuSfqL2yjpCdmiUMEMyiKykwlhr2A5BVjGD6N/e33WqOMLmBNR5g80ICO1hA7bJZo2ScDsI0aaNgIqC0TMOUmOzrDZgyUBvltF5wOdTeNvZbJb2w7hNY+GqQHPtklTI49UJwbYHJxuGqMX2GjR4X2meEFYNkZ8Z7B8K5TvY5

U17SJteCOZEj4ce2RHCYxBy8B/87KakZDh5HQ4/hcOHbDilJE6ojszTfWCnxUgKcM+OOFTlC1z7qdYWJmLTn7AijLhjEoWNXslChEg8teTOUNKLEYgNhfYATWaO1DLbeppsZLPnCb2t5t9aWYuTvoyy844j5cI8dlhWmVyq4guPLUfiyxUge8tmFmYOGbmeGDp5+zCZRsjzuGe87E2jEUoQHOiEBkwpEZMcOgX7Js4gX4N9J/Edxr8suqrXnmXmy

69d/cJXX1mVyjzH9jWNXA1nVybE3or+d6ZhLfxa7Pp2oXmB1s/ydYSCxhrrRsYXi/A7QRYjeA/lBizjEoQBk3QxGWPsaQC5ufeZICgxS4rck2iXYAoz1AjL9sK1NHHiOyMzjtRhgIyYcBHCizCkO6SBzFmBvKWjK+1o0iGQyeCbDGI2w5ILsNfH7CuI8PY4ZFhvbc90snPG9gkzvZXsMsE/S7PcMSr9RGR34F4Q9jeHbJ2RZWTkT8MHZ/DTGAIlJ

ECOawgiAUy4apuaIjbLDYRg2BsBcGnZOiUgv4VEeiNs6Yj3R2IlNBhxGYEjNI/IuUQjjxTCjyRa4SkRKNQCxjX2DIxMZhOZGPYSYuE0rG9kOSETFUUovkVtkD6aohRB2ckWKJSjSShOMo95gDnlEGSyRuqZUeDk0jqjsc4LbPgThZLjEC+PsIvsaIUZmjTgdEmESZ0aZAE7RUPDYMNnohA9XRjfD0TBEc56RvRbnell3z5KFpreffUMZy0H7poR+

jad3shM2avt4xTwzCUWILzpdHwskvyFmIZQ5i8xBY5JlbhLGJcJG5YlLqv2Vbr9ax6rBsVqx7E6sWxIeCrka2q4kIuxL/S/mJGv6NdmuNrVPCONCxP9Ouk4uAT116mziFoJQxcQNLcSbDRYQ+YNtVyQybjl+6GHcUxGdHtd8MibJAceLRGnjzSGbA7rty9JMYcgitDjMdwhqncbu53ETJdzzHXdpMfFO7gbQe7J4nummUkurHe5XihhUSEYbEnvG

JIkoT4haHML2HwR3xSwgKdW2KS/iNho2W8jsJzwYy6khwttoj0lHGQ4uCkRCbBJ5EmR4JgvGCRVPyl0jMm8kvtrOwDJKScJIBNSV8MBBciiJNvEiZ4UBGWY7kiDKieCK6heE/J0IzXl+PcbwjmJSIxaOxM2Boi9OJLbifZ1Q58TzemHVbKikJG6TiRVksSYZNsmINWo0kyqRzNfTFSeZrw1ke8IFnlYhZmkvnoc2E6yjLJokiVIqKLDGT7JPsqUT

H3NkCigc4k2ybTzDnqRHJSnXHKpx1GslvuBo/2N5J4i+SLR9EwKTW1tENoHR4Ul0V1DdH6yKWcU3SAlI75JT/RqU6MWJHSn+cfiWU4fprj5ZNzWZ6YlCZ7zrAJiuZSYufsWNTFITe5BUqqXtBqmOA6pIUBqfFyaljpZYZY7DG1KrEdSaxBXFed1O9wzio8S4x2ENKq6npRpZCbsXvzoR9jE8g42aZwnmljilpKQKceIk/679eAc4zaT6wAE7SVx+

0zvKANEiOkkgJ0pvJhnOn7j42h4m6cvJPFASHp6AxUGHSlLYCZ8uAhfOoJVLr5iBp4MyrQ0goUDSBGdGgfqVnK51rYiAKoPQC5AABVCsBwL8p6Zv8PA19FsF6iZgUGoEGYTkIgCcZIYPjP9leWSgAgvCiQfuj1Q/lcIsqagpUnlW0HT0HBZggwRVUXrVUV6c9cwcWR4LNUBCO9M+u4IoKdVuq0hBwa4LbLDUr6ADbweNV8GTVpqLYJ+iOWCGeg36

EQywtEO/qzA4hXgxIQIGSG0UFgpwQ4KUVgYBEiwPCvIQUO0KAgVwa4IMveXKG/kXqKRN6nUM+rOLCGv1FoYUSSgBxM4MDKhrUXwUsVKgLcLkGhBljQJ5y8CW6BeP6HoAylFS68FUqwA1L0Ar0nbhHXOoHd3pzFE7vCR+kQAOKJ1bijrUGXYlcSimR7m4uJKvdoZ1NRpTXB9zVKgMtSjAVpQjpoKygc+GOtGSwXGUcF2+Ugcku2VELT8mdYoPQMqA

OhLomgJEDQutjD5jw1pTgUwoCo8DEGjEP2HsG3KvpWo+5SamePaiIQAou0XaLk3EX3BQCKQURM1FETSLjK6gtYDRCXCHAkg1ECpukPkUwh96SiiABmQXrZlmCpgjRegCZAWDtFZZXRbYMGoGKBARiw+s4NMV6K3BohDwSoUsUugClZtCav2QCH2gghroEIeCVcVUD3FoYb+uwL/rxCrFvipUP4sHr0QwUmgi6mEpjKqrzy4ReUHtKhhnAfgZQ+Ip

UKwYpKcGaS+ai2CaHENWhOwV0ucC6FFKU6vQyGh9xzYF9yJSQQuOsGnmHseI+c3GVNFsTYZaIQEdHj6tbZzZKZMktmbR38hQxNkOwX4csqwAuT7ITBCgGyDRhCBWAqygAPpEVXJ7NPUXVkojkSby64F+M1BDXzCsZn4lYd+MDW+YdoH45DsbzCaaQWlmAVAOiBpA0tEpEuTzo3PbVWELUbIMZMAmF7Rqp+JKeNRbhpmjzypUaieezOmilSEuy87z

LlAPEIDVuokXvFu3IhTonwU1daJhDqUr4XVTDcdiWrabWZp23qlnr6pxlg9SIz8qHn+EeCyMw14E8LB20nX3Dp1Z8BNSLI7Upq01Ga1AFmpqV5rh1andOW6ssxlq7EdyKtRjIWEfi/Vz6htcGqhgviH14a9nimhA3dqbI7fOlv2u744iQNVsUdW8HHXhMHZsaweSFCA1zqypaY24X3O7RkRV1S88dEkAWnwDrpa3DxPupLwiQj1pokeKeo6XPTaK

4aI4IhBmCiI5UpwVutyAYpQkPppGFWoMuGWnlRlZ3WTCDJbCG1plYq2ZVDPJL1KL1X3eDb7FvVeqW2tahicUlfXBqP1RvI4T+vY20iY1AG1lCxqNSPgqN+OVNeSHTXLEIN2a26MoGg3zkC1efDORsMSQNgkNlax4NWsWHOaC5rm4sI2pw2eaKZlG4dcRt7V1zyNKUmXMVvi3UbRAtGo0BOqXV+a41gG2dY1LHk0jn2Ma7jSPKlaL8qIAmq6YgOE2

JdRNh649SHGk1IKJSWAnSjgijoYLZFBA/ciZVwXHKqhhCqyttQuXZ1HKygYcMQFqCNBmAqILkAwrJVcDIAgVNYCGrGHeEX47DJIGCEVCAqnRAZfJX8jOCYFIV6VYFAirwJIq1NhVHFYotJX4rDBlVFImopJX6DCyDVSwToorI0rd6bKwxXWUZX7kSqZi8+uyo7JeDuVkAU0LYr5UzUBVTioVS4sWozLZyX9GwokG8UJDlqfihIv/i8yzRmoESw8o

Jihgar8h8DcjptH2B2JKGN+dBkko20QAahuDeoRkotVEM/qOS4lD+HojZVQaRqp1VbVpo204adtJGg7RZpo03JrtDktzQ9q8lPiAtVYkLX9o5syaktM9QcS12w1aSCNekvrtRrMlC1bJN2q8V5qVb8aVuv2iLQDpfc7dIdUIUCS6Xy0NNR3bTf0tYpAyJAemzIQZvGX60TNYMgkuZpe6WbLa1m62s7rOKu77ajJVmujV1He6Td2NP3Rbp9qB6/im

xUWqHuDoaUZtKCubQQqGX6Ultq+FbYcrwWOrO9lA7bSQroFkK1aqIUyGXSEATAayENF5YwqsEQBrt3mRBnYhFizQ7p4BF7V6RFis4MwxYHYDsBCo/acumw9MDItHofz9lodUggouPrJk8VBK+gqopMFpE8V5KrRU1SpVI6hC5ihwcYqPpo7+qyO/RajsgCeDr6BOiAETvNB+Cg6j9QIeToIav0qd2eqIRKpsItwGdsqpnfKoSLph1w2cdhrzvuAQ

MudUStACuEmCQwvtBqp6urs71S6zVDQyAJaoV2kNHgcqaxvapoaD6SlEgT7iRyvXJaYVmccNk5ow2rCxsjaipoVojW/qmtU6tcJsjWCJqQt1qMLUiAi2ZrotSKOLcmtg3uSRDpayGEhsRHoTXxT2/gdlv9Uvq1gkw99TnK/Wtr22hGkrZwBI0+ipqfozzmRB77qQqNIQOreEAa30a/1nvQg6ofiA8aOtPcjjZPJYZtbF598G3MXi3VCbd1ImidKl

AVYSaT1DuwQ66pMOWYyI4hg9cDykP1qZDwauQy2q81tr4jvm5Q+hNZRqHgNw6yFqJC0M6GotUG/NUYY04lHEkZhl+BYZqTWGV4VRlWSkCSDubnDeG79Y0cCMeGe1IuLkj4frl+HtgARtSEEZo2hHZYjWhI8uqiNnx2jrGq1j5q61T8etlx3jcIlFhibRI0CkbcvK3bt5xNE2qTdt1k0MYOlvSz6fQwGWJ7fpS+rWoDMRK3dJlQlcGdTrNpzKrN56

oQ0lvIllGU4n6vDbYcw01HGIzo3DQJFZ5FbrjKPf9SofOMxGOjNW0LWBsi2Qbc1AxtOcYf1GiHHg8wMY7BwmPvapjT66Qw4fmOSbFjrhyNXsdWNeHRcmxirT3H8PVbk1tWsdWEcfYnG/N5Jto5SfuNxHF1yp248kZTHSt116RqBduqPHvGcj42wU8wCm2h0292lbgFss22Lar9N+ogZvhIFbayBQ+s5TZVH1Z0rlEgO+B5Q/j2QP4g8fkEuWeW+U

Ltbymuh8riD5LM4a4TOBcBF1t0jQ1yTMA3SGxTBHg5pU/aLEiiIqe9RwGiACBBBlnntt+qeiDof0qgn9EO1/cSvf1g7P9G9JffwV/12DwDSoBlU4Mx0n0WV/+3HSNS5W304DdixA2TvNWhDRVgDA0rTohD2QcDzhD+vgbqLmkoYgBYXaQaNDZVIl/O13oAW4MqqElhq4pdg3fKZEZdFOzJc0MXCK7qIK4WaLwZ6Gd7nVsM0dvDLqxZhrGWYP4JWq

0RTVHSdULk0uB5NKy617jM4JUmdE7svwcrCbJiZghHA0wFmJY24YuFQSzhLMiJtTKZn3s6xDGtYPsCeFbnXZrKEBdTk5T4T0V5ERNbLxMzfne6f5tON+aMSfz71ocf/KIj2jTGgp5wLMLu04YbBNGnTQKK6MBDCC0L1cwZkbIEmmyhJUckSYKKtk2SjsUMaxvbIiNcazg4vHGH7CDJkWnsFwSi58O5RCz1T4cxmDpLw56SSR1k4ObwHZM8BTJ0fP

2RZP0kqWHL4UKYM5dVFY80+oLTPinO1FG6i1ZOTyYaPXMmiacXF9NrxZ+QZVB8oUtEXOL1WxoJLQa1w9JcFwRjSNQdXw7jRlNpTgxfnMMYFyH7q4Zg3iJCPUDylKH7hZR6eYmOF2xGF1hF3U6PP1N8bwo68pVhlxVbbyQEW/HqV/wDyHzyuBrdsSNNNbjS+pDXAcTNJTz3y2hj8l/sIgiqDdVpX/GYAtF2ZbSf5UGEs2RDXGHSjgO0GNNuMwz+wJ

hcAobTuq6vf8BBbeS6RwCfDrgCjmbGGYMI/PfdvzawX4COPs37B4IcQYC4FkmPYzwLLm0RtBYim+xWoS4BCzUn/yPBULwpk4ZhdpnXCqZQyPC3TKaM3GGrOlkiwZewmsjjL2SUy9lHMt0XCm47Ri7+fagsWG6bFjaRxeeSxWeLvJ78VBYEveIHRIl04GJfLkZW4gWVnEfxPxHyWzeNli2YHKRy6p1Lvl4480aJvEXGRpFsm+RYpsezqbHqbkVZbc

v/YPLQc7WGpbsTK2z2Eco27Zctmm2RR3lq8tJKTlBWtROfUK/nxEMRWs5EUHySB05vYmq+0jaxpI3kRZw0R6Vn8JlYaOUt4puV7wzsa2OFWdjgY1SC3LKvtzKrIsO6mMLqvamGrSEJq0PJau9arj48/O5mI6t9a0jho3qwusy7b8hrYkL3NvP3ljXtpWCY+SfxNZn8Y8E0x8FNIWt39hxK1xaWtYkGAhpxa02WOaX+BzDv5e6EPPsDnsCaDpiGM6

/sDgGnSrrvtgELdZePGmYFRoG8lNWeuHr3rk234xHX27jkY9StOPV9JBNQmwT/01PaCaM0wmjaEMizZJS+thJrxePBi5mcZv/mYMgF0G8LaQsQ3A7PN84AxDhsJAEbC0FKIhdggo3DgAEdG5BIZmsb8bOF3GwL3wskmMx2l9W81dJuFZybTdXWzRYsuoAv2whoB0iIBspInS6YWdvZ1RYB34rUHeuoJYFvrChbkdyS+LcNm/Y8RWHaW3CllvRyFR

Zt8JY8EttKnVbmY4mxrYocsjtb1Dqi+pJptW3Db5k423Zc8vyPHLFtly9bcMe235bsctSz5edsBXFOrtlyYMbCvwtC+kV7ORaY5u5Q4r3N0zsHeSth3d2BJvOKLakup2VItckqJKY87J3djrLEq/3zbncsqrOd2q93K1MqOuNhdkm5j3a1tWtL8yO4+1oeur6XrqXDef1c6mDW6xLdqBNPfbsHWj5k14aafJmt925r18m/otZDxSKh8jrLPBPc2t

vypWO1ue3bn/6L2dpR11ewAvXGiQN7F10vFAMct/A97GR4bVkeakn2JBkMc+5YeghWmCqNpzZbpQW27LDKfe102tvdMnLNt6dc5T6cuXj6RQFYeYA0BkjYBztfQpfYFVPtfbIYL8RBnVCEWiCYydbVqE8fXAgRIYp+uFUzYv2Fmr9iDbFU/FxVg7n9RgqHW/rzLNn16COn/djrpXdn0dvZlwQOZx1lBIDVi6A7AfvoIH+V+hZA8Ku5AznzCeBoim

GDbBLn0DzOuomirIbBZtzOXMRaEs1XXU+82GIW1+HoMVCzzJqi8x9SnNsH5d2S0hleUqQpmhl3QxgwIahqtFtdLuxmnrtL2G6vdExKve7Rxr+7LdbchvWKQvpU189TumkkXpNdXFHaZej25a65rV7Patruvfa+FqbFw94JSPdgO6W323pmmvpY/YT3P2hlF3EZdrUM0TL7uUyuE3y5gOIm8956gvW64ZqI1PXBuz3Yls5qclfdAb2vUKWt3/Ew3E

IU56gvOfoLLncda50nTucS7h9HL702AFoG+nXn6AO+EiG2CBA4A+gCuD89tLMLf8gBfxntNagc4fwiBcFzMEBD/A0JFEEpCIMVCKDXegcWQcPUB1oumYGL2HVi8h3VDodTZ2HS2cJdb1qVf+ql/SrJcD0+zyZYl12ZpcjmfBY5knQ4qQMqu2XaB2czTo8U2FhwvLsD0kISL5KbVSUAcnkPuAAhedlBmMptGNHauHqp5/g+edqGXn0l15uXVkrvMA

UbVKUXqM+b1fx7HdhrwvUW7d1muy3Fe315W6Do2vpToWO14TWD226W9n1zXfR8Le66S3Hu52qx4rfc1j1Ne3gNx6De8fG9Ie8WuTSvuRvo9Mb2PVxnj2Gbk9mtK7jxXfvpvQZmbrPTB8J25v3uBb22sXtNdevzX5bn3Rx9k/HWePdbpT/x9U/rLZtdplt6crwE97nTrwfvetuNX+fHnfbgdy85vy519ANCnbgAA14gTCad5duX2xn2oym1qNBxaj

ZUYqzpRiJgTRE0xRYsJPd4yvzMDkR60ZTQRPSQV37qzwBvQewWUWErjBjZvF3e4JeUrH3HZ2lV2ZKqAGmVNZuQpS5Jc/uxqPK4nf4NJ3MvgPYQqctm65ff0p30qnxXgc3KoFZoeqYsJzqyFEE0P+5u3UYgiq5mTzDBhV9UNSWEfgP7B9V3A+EvLg1Nauy790EvHfWbxTD/63+ZvXA2gLkD2CNA54eiN8zTaizgE1QvzBUHyF1G5g5juRrThWN7C5

cIQnY2snhNzMdRCQ5m4QbjGQywlB1s6ODkej/y8RPpsN0mLTN32CzY4eQouHvjrm1DZy0g+62AZSRuFG9gtbxLUdsWzHeyuLZZLUtsZjLYD5y3lL9t8kbtBMl+WCbpJzH10z7S4/eZVDkyxyNocG2ZY1l0X7I/sumPwoWYBOWpDMk29/ZJthW2pa8ykp8mjjjUc5K6MJbWPHk11J499sLHOLDPmB6ZwEWsOZgv4EsxlqmzhPRHmT6J/laTt8kirm

T9O5lNSfZ2AmudzJ4RZvKBQcfuMVq8Q843zIGwmyZCLPKIgFjcuGph6xI2/C5GV+VTx8A3Y351P8uDT0a82OacTWj+bT0/mNM6eXz5r1rJa6JEohPfVrE4n0mX62vvylNPpdrlM+DxuIgR2Gcf/M9Ot8Cpgs3K6+w2nb0RNn919btY0agKbHpHg51+evfOfevzwDlh79/Aer+QLNh4Hx41B9QxwfcqACFD+RsoW4fxJjCzg+gkPscb0kPG2j8ItY

+dmJX3x9qbbRypt1fEWXotj/Zh2Ytqfdh3YsYrD32v8dLVnyEt5gb0jygdZLMCD8+fCW0F9JHYX2kdtfJSxjlrZNSxbpNLeq3l9sfLmSACtbIy1AC1fEn0stNfG2zF8SA1S3CUDfCx0ZhI5GR2IC5HB2x4YrfT9ht8nJLPnt9XHT2xZNvbI0Vd9vHDYG4d/HbFm98WLIxHkR/gAP258RHHAK9F47CU0TspTOTwSctIaPwH5Y/aqwT99IJP0X9FfN

P1Lt70DP0SMPwVo2xhc/XMXz8QoQv1Kd1uOMzX942dqWqct5d3F3lW7Rpwb9pnTu1acT5Vv3PlZrDv26dppYezmk+/MewH8nxKe22tEIMf32sIgwxD4EerGvAWcNBBfz/4wFaNhX8w4dfxNMjQLfw7o4BNT0KEATWNyBM3vJ+3Ypk3fTVTc09YzTKBTNLN3M8c3XPT/sjGH61MY/rEBzP8QbC/3BtuTSGwr4ILPi1v8xhEuUh81gZ/1h80LBH0xs

OkPBxR9mZL/3R85fLjQADbA8KGV8tHVX2osmA+hxl46bJh0p8ffGn3gD6fbi099FglAPZ90ArnxFsefCJzEcLoC3nwD/g23h18THQQPICZfQ4JIdinE4NT8zg4AIotKbRgP1t9HFgKsc2AgQMl8uAyEON9hJAOXF9zfcJUt8HHE2ECtNRFxyZMhjaQOd8fbaKxeC/HJnzsMUodqB981A/33ZssA34OD99IUP1idkpLj2MDNIUwJScIxNJ3j8MnKw

KKcqpZP0AC7AjU0KdKA7tGz8z4NwLnkPwWI2L9fAsv0rE+rSvwGtgg4az3kwg/fg7sWnZv2iCe7NvyvQunSaX7Eu/PpzBEy/QZy/QJBGYQyCR/LIMkEcgyfzrx8g2fwm55/ICEX9LrcoJ8ZKgo00yNi/WoK2BfgXfxOdMBdvV895tVt0wVCBYLxucjlLtzC8HnKgR20/TdAHiBUQJEAdB58OAAoAr3boAX0ozP5w+VERCSwDI8oGJRShwXRBkAI2

Ff8lFhX0LiDzNf+TKiRcAdHvVRd6vKs3RdQdC93rMiVGqg/1uvb/V68v3OfSa9HBd9wpdQDVlQXCIDDlXx1RzBlzJomXOalYMQPcISW95zXAFqBoPXt0iF+XFD0qRiUdMG1dkPK0EO8tVRdAcMNgOBzldxdbMMl1rvZVwPC7vMj1XBeoURCjdtlXV1e9fnOjxhocIHXW3RNAajmwhi3ZmnE9y9dOSk99Azjzk8A9YN1FJCjA1ygiRoGCKig4I5Hg

QimPezxY9UIpzxk9q3TCLc8g9TYgaDQSJoK08yveN108OglPS6CjPdPV6DM9Y2mzdzaeZRddhPAiJd0iI+CI9ckIp2hQjMaK1xidQsFz3k9a3eiO+dvPRMI+Y/PB0zbdltbBQzCB9D0zTpcw55121c6eyBaAK4efDGBSAHgEHhUvaM24E53T5S4hFhV9DMMpgFsKBAYCCKF9INzU4B4V93LMBmAdoVQWRdoyRsDf4yzMs21dgdUcJG9SqFr3B0VF

ScPUUuveHR69xyGwWfcSXQbwx0VwrKO/dNwqA23D4DXcNm99w2XWnNQPC8PFUFyXAHnxzwuVU28jQbMFAJGBEVzU09zZ8JXkZhFGQCYeFHDwu88PRVwI9fwiqNVdSPGoJyVJgMKRXBqPcCOdUUTOzTGxULC+zDU3gwbDdRG1YonkMCNcu2yccsdHlZQJQoLSTVO1NoBgQZ4e3x6NwNekxi0DDTtUkDUTSzG4QoYOdhs4rDWYPWjXNP2FdQ/wUWAB

87dTYNlNO1UrXWN5Igqwj8U7FNEXwrmWeA5gFTBA1nUNIfYxCM6NZRwx9u0L1V0sJQgp0cDl1EpxSMynXdgrED7SMN7w/wWKnG1ELY5wgN9/SoEWjhjZaIAhVorE2v8yxG7TxNto+ozf9OtI4IOjsY9Q2HVzojjFA1wtG6L0NYtRkx9clol6Mzg/wd6PswgfJQI2ifo4NX+idoiCXCYiNTwzK1wY8PwFCcRGGNigK4eGPq1EY9wxq1gjBGLod4YK

UOPhDo7GBxiUjBUIrscnDUP60vtKoKPtPENiSHwvjamMYjaKZiPvttPNiN00OI/TwBlDPRN2M8M9Uz34iBgwSKRN6Y4oxZM0TRBmZjDnQk0fVGQnEz9gto3YA1jvNPaIxj+YzZGOibg4LSFiLo0WO0NxY/oxg1KQtxy9hRDWWLejiWed1As5glzGVk4RN1F+j04AGKJMFDC2OTVQYvKz5D/RSP00gjYuGKgBrYiWlHjO1eUzNibY8fkVCy4s+Cdi

UxF2P2iqpKuzXU+NYAQjCtnB6wpiMwKmI+tptBMNtMNI5MP89HTPZTTCpAELyzDehHt2IV+3UhRi9KgAAC0EAKoA2A7AHl24wqwiCNnd6HaaJ9IfgQ6jZM/kDyKBEAQV6POBsvTsLzNwo/8BzNL9MKKB0GvWKMXC6zJKPa8pw/FzSjZwjKKfdOzdcNJcJCXKOZVVwwc2pdCo2l2KjxzPcMFUUDSqKPCBg5bxsIHQBqI28FVG8iCVKPcg329UACs0

ji4GLqJmAjRMUXuoxdF8wHAfwvBmI9GhNVwAifwZaCOAQaMCKGjgTfN1ddRIovXEiSIySPd1pIn1zQiNjBSJojXPBT3c9sAJvRU97dQT2Ej8Imz1MSDcUiJL1yIiT0oi5I5zzsSlI32gddnExGIbcISP4xAjw3TTxDjWIgxPYi/pFN0hMsSHiMgA+gsz2qif7N7iE8PEwiJVwJIxCIsTvXC12sT5IjCPsTlIsJOU8Ik1vRvizne+K0jUwjtzdNzK

bty9NqBL+LH0f4iQC5B+QWoH5BJASQELp+E0BMjNwE95Tncgo+iD6jdoH8BKE7EcFy8Q0ZXRleQjEXgX8iKvW6jYlsElfAwSpgSKOBBoovBLPcxwhKMvcGzEhNSiKVchNCFMoqhI6o33CRQ/cQDfKOoSJvI0FYSAPMoEcV5vdlzlVeEiEA/gBElcyajB6diTX0zg8V0EwOoigyO9moSkTqgAmD8KUT8PaXSI9OE8aNvNJogCmBofgM70KU+DAyNo

8ijS9TTjJZEs2JY7dL6KmhvYRsEAg3+JcCLjljBjUx4TokDWFjLomkzFi6TCWPuiHfODUZjZUMAhSBQnTuKv9lYkiHpSoeCQRdZuYkeK1ixTXWLD9DA6eI0hZ4k2PnizYpGJWNLYg4zRjwuO2Iwh0/EuL5iqpTSW8C0jRsGeME2U+P60LMO3H9ir4vfyzZrNBmIpTaIKlMkMpUulPDQGU8NBgJMA4eN2jeY6EL8h2UyuNOid0GuKujaTXQwbj4tR

6KWiRU323RkPoruNpSW43qFlS2JUJ0BisHJVPi1x4hOwhiDY6GLmY54hGN1TRTfVNRjFTI1I3iI001LDTM/C1PdjrU+RC9i3jcdEdTL4y+xk1r7HhQVpmgh+0STw45JM6DUk4GU/szNROMs9s2clOLVRDdQKMQfU3OO156UtOCZTg0nph5jZfcNM9hI0k5E5TY0nlLri+UxNMMMm4qQOXT3VDiDTTxUpWI3TvxGVMZS80llPQsh1YtJ1iwY1VLid

IYwUMfBNU02MOMa01SBRjrYlW1Ljm0+wM1NCLS1MJj+tG1O7TtnA0z7S8jWaBdT4wjZWbcmkrvQC8nTZ+NW1Mw9pK/CP4p526TB3XpPQBPIZQFqB6AeoFMA7ImsOmSs4EtgqYX4PVWWS7ETYCStObciGhSWwAKIwT4xfsMjJBw3BJHCzkuKMIS2vHFw69aqBKPvd0o+5MoT+vahJyjyXehPeT2yYc0m9CdXlRm9APScwPCFvb+3A9MDCEFMhQUy8

NXNQyYXU3M9vU9G4AbyJ8MlcvtJ7Uhh5gVFJo9hojFNu8NE3FMAioLZKDmj9E1oMMSRIzxMKSzE4pOY9/E2SL9cbEypJCT69ENycTaksPVwiaaaLIKTiI7xPMSEsmSON1ksipMUisIxT0yzPPVxKeko9YOK01Q48dPfs9PXIQM8xlbiJ6CMkviIsyETIYLyTqSYxPhovE1yB8S7PUt0SzSs9j2ojzdWiIcSVI8JOyy1I2+JwEH47SN71dIztzIz3

4zpLzCh3CADbA4AQeCMBiAUCGxBxkqunsirtHgQ2A7RFBgWT+FD0h31SMW2XOsVwNESMQ5gCKDzMdgYKOPdJM092KpOqOTJf1komHWUyZwzegoS+vFHU0yezZcJ0zHkixS3C/3HcPsVfkoDzMyAUzlxPDGgWzKAY6iQ6jXBOIOFPESZgdzL25Ow5PzXB9yAaPlcIs78NNUbvP8KCy/yHJUQgkNCKnCySU+N1KURMGWDLoyQIQCEB9AHLLKUllQXJ

cQRcwOLk8GsuN2azE3VrIPIo4jrJjj0kiAEySE47JJz1f7BZX5zrwSXOFzRc5bMaTPTQjKfjWk2522yzciLy6Tz8cADHIIQOADgBBQPIm4Br8aADeAsgSoDnAjIIYAYB8xCgC0Nrki5Ocgw8s7SWANckQB4JYKTIEFBH9TFwnCigKPNIAY89ZGDyUoiHLISocjJOjzXYWPMncHkjTP9yXEVPPzz1kePNoTtM3oLzycgAvMrzRvBhKpcU8tPMyBh4

PHSKjk80vNbz9AMBGm9GXLvNryoAAvIrg77RrISSW88vMyBR8mWnowQIyfLrz1kLfCSSNaBfOHyK8qIHOgW4VPNYhLmeEzXyC84cBpBt8qCD3ywwHfKoBI87vKnz9AE/NYg74MBJYIS8ofJHyTCYeA1BEhJUGwBEQPkAS9tCCKkYhjRUWFagQCblS/yf8/ACqBXMxqACgxhchkeBcoCMggAjAA6FFy0AbOnoACAJBBhBYOeZLGALlA/PWR28/+hd

AnKBwn9zKQEgGiTyCQcnShiAQUAQAcSNACQLKC4gEaBPoBACPzcATQGCA/MyAFYKlFbOnsgMQXOgBhSQN6w2AooNYBeFpCqKBLUaYiADHhlAAMDZBKgMQtwA3rJsCkKtCjXHxh5CiAAILr8mjE6p6ndA0PCEAMeBDB0oFL3QLFQbIG4LeCpMM71sAIgCYLVsyAF+hvcu+M71hAKADnwnC8EH0A2QKSArBJyAIsVAginkS4KeChIloQCCuwELokaZ

gH5BfoOAHYKXYaIscL9EiECy5GACxAxB3ciMwUJ6SAIgEos1MfH0AH8yMzlUXvBnLRorYJmjVV7nIZVCBeMXIoQB8i/ACMiqMyAEcBmABwpTIcgAYFvB/QfBXAAB3bkF5Bwgd3Ptzz8IAA==
```
%%