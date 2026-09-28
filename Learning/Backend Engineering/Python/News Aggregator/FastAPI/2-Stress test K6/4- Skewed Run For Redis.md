# Before![[Pasted image 20260919210212.png]]![[Pasted image 20260919210219.png]]![[Pasted image 20260919210237.png]]

```bash
➜  news_aggregator git:(main) ✗ k6 run --env BASE_URL=http://localhost:8000 k6/load_test_deep_pagination.js

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/


     execution: local
        script: k6/load_test_deep_pagination.js
        output: -

     scenarios: (100.00%) 1 scenario, 10 max VUs, 2m0s max duration (incl. graceful stop):
              * ramping: 10 looping VUs for 1m30s (gracefulStop: 30s)

WARN[0043] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0043] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0043] Request Failed                                error="unexpected EOF"
WARN[0043] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0043] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0043] Request Failed                                error="unexpected EOF"
WARN[0074] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0090] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0090] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0090] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0090] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0090] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"


  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=2

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=3

    limit_counter{limit:300000}
    ✓ 'count>=0' count=3

    limit_counter{limit:600000}
    ✓ 'count>=0' count=0

    limit_counter{limit:800000}
    ✓ 'count>=0' count=23


  █ TOTAL RESULTS

    checks_total.......: 31     0.292597/s
    checks_succeeded...: 61.29% 19 out of 31
    checks_failed......: 38.70% 12 out of 31

    ✗ status is 200
      ↳  61% — ✓ 19 / ✗ 12

    CUSTOM
    limit_counter..................: 31     0.292597/s
      { limit:100000 }.............: 2      0.018877/s
      { limit:1000000 }............: 3      0.028316/s
      { limit:300000 }.............: 3      0.028316/s
      { limit:600000 }.............: 0      0/s
      { limit:800000 }.............: 23     0.217088/s

    HTTP
    http_req_duration..............: avg=30.27s min=2.41s med=28.1s  max=1m0s   p(90)=47.62s p(95)=47.62s
      { expected_response:true }...: avg=20.17s min=2.41s med=21.62s max=46.47s p(90)=29.42s p(95)=34.23s
    http_req_failed................: 38.70% 12 out of 31
    http_reqs......................: 31     0.292597/s

    EXECUTION
    iteration_duration.............: avg=30.37s min=2.51s med=28.2s  max=1m0s   p(90)=47.72s p(95)=47.72s
    iterations.....................: 31     0.292597/s
    vus............................: 1      min=1        max=10
    vus_max........................: 10     min=10       max=10

    NETWORK
    data_received..................: 2.7 GB 25 MB/s
    data_sent......................: 3.2 kB 30 B/s




running (1m45.9s), 00/10 VUs, 31 complete and 0 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```

# After Adding Redis
![[Pasted image 20260919233246.png]]![[Pasted image 20260919233251.png]]![[Pasted image 20260919233304.png]]![[Pasted image 20260919233339.png]]

docker logs
```bash
feed_api       | [2026-09-19 18:33:10 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:9)
feed_api       | [2026-09-19 18:33:10 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:9)
feed_postgres  | 2026-09-19 18:33:14.667 UTC [1805] LOG:  could not receive data from client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:14.667 UTC [1805] LOG:  could not receive data from client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:14.678 UTC [1736] LOG:  could not receive data from client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:14.678 UTC [1736] LOG:  could not receive data from client: Connection reset by peer
feed_api       | [2026-09-19 18:33:14 +0000] [1] [ERROR] Worker (pid:9) was sent code 134!
feed_api       | [2026-09-19 18:33:14 +0000] [1] [ERROR] Worker (pid:9) was sent code 134!
feed_api       | [2026-09-19 18:33:14 +0000] [21] [INFO] Booting worker with pid: 21
feed_api       | [2026-09-19 18:33:14 +0000] [21] [INFO] Booting worker with pid: 21
feed_api       | [2026-09-19 18:33:17 +0000] [21] [INFO] Started server process [21]
feed_api       | [2026-09-19 18:33:17 +0000] [21] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:17 +0000] [21] [INFO] Started server process [21]
feed_api       | [2026-09-19 18:33:17 +0000] [21] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:18 +0000] [21] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:18 +0000] [21] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:24 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:7)
feed_api       | [2026-09-19 18:33:24 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:7)
feed_postgres  | 2026-09-19 18:33:25.484 UTC [1803] LOG:  could not receive data from client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:25.484 UTC [1803] LOG:  could not receive data from client: Connection reset by peer
feed_api       | [2026-09-19 18:33:25 +0000] [1] [ERROR] Worker (pid:7) was sent code 134!
feed_api       | [2026-09-19 18:33:25 +0000] [1] [ERROR] Worker (pid:7) was sent code 134!
feed_api       | [2026-09-19 18:33:25 +0000] [26] [INFO] Booting worker with pid: 26
feed_api       | [2026-09-19 18:33:25 +0000] [26] [INFO] Booting worker with pid: 26
feed_api       | [2026-09-19 18:33:27 +0000] [26] [INFO] Started server process [26]
feed_api       | [2026-09-19 18:33:27 +0000] [26] [INFO] Started server process [26]
feed_api       | [2026-09-19 18:33:27 +0000] [26] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:27 +0000] [26] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:27 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:8)
feed_api       | [2026-09-19 18:33:27 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:8)
feed_api       | [2026-09-19 18:33:28 +0000] [26] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:28 +0000] [26] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:28 +0000] [1] [ERROR] Worker (pid:8) was sent code 134!
feed_api       | [2026-09-19 18:33:28 +0000] [1] [ERROR] Worker (pid:8) was sent code 134!
feed_postgres  | 2026-09-19 18:33:28.445 UTC [1809] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:28.445 UTC [1809] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:33:28.445 UTC [1809] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:28.445 UTC [1809] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:33:28.448 UTC [1809] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:33:28.448 UTC [1809] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:33:28.448 UTC [1809] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:33:28.448 UTC [1809] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_api       | [2026-09-19 18:33:28 +0000] [29] [INFO] Booting worker with pid: 29
feed_api       | [2026-09-19 18:33:28 +0000] [29] [INFO] Booting worker with pid: 29
feed_api       | [2026-09-19 18:33:29 +0000] [29] [INFO] Started server process [29]
feed_api       | [2026-09-19 18:33:29 +0000] [29] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:29 +0000] [29] [INFO] Started server process [29]
feed_api       | [2026-09-19 18:33:29 +0000] [29] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:33:30 +0000] [29] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:30 +0000] [29] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:33:58 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:6)
feed_api       | [2026-09-19 18:33:58 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:6)
feed_postgres  | 2026-09-19 18:33:59.848 UTC [1867] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:59.848 UTC [1867] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:33:59.851 UTC [1867] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:33:59.851 UTC [1867] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_api       | [2026-09-19 18:33:59 +0000] [1] [ERROR] Worker (pid:6) was sent code 134!
feed_api       | [2026-09-19 18:33:59 +0000] [34] [INFO] Booting worker with pid: 34
feed_api       | [2026-09-19 18:33:59 +0000] [1] [ERROR] Worker (pid:6) was sent code 134!
feed_api       | [2026-09-19 18:33:59 +0000] [34] [INFO] Booting worker with pid: 34

feed_postgres  | 2026-09-19 18:33:59.848 UTC [1867] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:33:59.848 UTC [1867] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:33:59.851 UTC [1867] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:33:59.851 UTC [1867] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Started server process [34]
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Started server process [34]
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:34:01 +0000] [34] [INFO] Application startup complete.

feed_api       | [2026-09-19 18:34:14 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:26)
feed_postgres  | 2026-09-19 18:34:14.905 UTC [27] LOG:  checkpoint starting: time
feed_postgres  | 2026-09-19 18:34:14.905 UTC [27] LOG:  checkpoint starting: time
feed_postgres  | 2026-09-19 18:34:15.308 UTC [27] LOG:  checkpoint complete: wrote 1 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.159 s, sync=0.038 s, total=0.452 s; sync files=2, longest=0.019 s, average=0.019 s; distance=0 kB, estimate=21 kB; lsn=5/4C7C5308, redo lsn=5/4C7C5278
feed_postgres  | 2026-09-19 18:34:15.308 UTC [27] LOG:  checkpoint complete: wrote 1 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.159 s, sync=0.038 s, total=0.452 s; sync files=2, longest=0.019 s, average=0.019 s; distance=0 kB, estimate=21 kB; lsn=5/4C7C5308, redo lsn=5/4C7C5278
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] LOG:  could not send data to client: Connection reset by peer
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] FATAL:  connection to client lost
feed_postgres  | 2026-09-19 18:34:16.152 UTC [1893] STATEMENT:
feed_postgres  |                SELECT a.id, a.title, a.url, p.name AS "publisherName", a.category, a.region, a.published_at AS "publishedAt"
feed_postgres  |                FROM article a JOIN
feed_postgres  |                publisher p on p.id = a.publisher_id ORDER BY a.id DESC LIMIT $1
feed_postgres  |
feed_api       | [2026-09-19 18:34:16 +0000] [1] [ERROR] Worker (pid:26) was sent SIGKILL! Perhaps out of memory?
feed_api       | [2026-09-19 18:34:16 +0000] [1] [ERROR] Worker (pid:26) was sent SIGKILL! Perhaps out of memory?
feed_api       | [2026-09-19 18:34:16 +0000] [37] [INFO] Booting worker with pid: 37
feed_api       | [2026-09-19 18:34:16 +0000] [37] [INFO] Booting worker with pid: 37
feed_api       | [2026-09-19 18:34:18 +0000] [37] [INFO] Started server process [37]
feed_api       | [2026-09-19 18:34:18 +0000] [37] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:34:18 +0000] [37] [INFO] Started server process [37]
feed_api       | [2026-09-19 18:34:18 +0000] [37] [INFO] Waiting for application startup.
feed_api       | [2026-09-19 18:34:19 +0000] [37] [INFO] Application startup complete.
feed_api       | [2026-09-19 18:34:19 +0000] [37] [INFO] Application startup complete.
```


k6 

```bash

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/


     execution: local
        script: k6/load_test_deep_pagination.js
        output: -

     scenarios: (100.00%) 1 scenario, 10 max VUs, 2m0s max duration (incl. graceful stop):
              * ramping: 10 looping VUs for 1m30s (gracefulStop: 30s)

WARN[0037] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0037] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0037] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0047] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0047] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0047] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0050] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0050] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0050] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0050] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0082] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0082] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0098] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0098] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": EOF"
WARN[0098] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": EOF"
WARN[0111] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"


  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=1

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=6

    limit_counter{limit:300000}
    ✓ 'count>=0' count=1

    limit_counter{limit:600000}
    ✓ 'count>=0' count=2

    limit_counter{limit:800000}
    ✓ 'count>=0' count=16


  █ TOTAL RESULTS

    checks_total.......: 24     0.199998/s
    checks_succeeded...: 33.33% 8 out of 24
    checks_failed......: 66.66% 16 out of 24

    ✗ status is 200
      ↳  33% — ✓ 8 / ✗ 16

    CUSTOM
    limit_counter..................: 26     0.216664/s
      { limit:100000 }.............: 1      0.008333/s
      { limit:1000000 }............: 6      0.049999/s
      { limit:300000 }.............: 1      0.008333/s
      { limit:600000 }.............: 2      0.016666/s
      { limit:800000 }.............: 16     0.133332/s

    HTTP
    http_req_duration..............: avg=41.8s  min=4.97s med=47.23s max=1m0s   p(90)=52.06s p(95)=54.67s
      { expected_response:true }...: avg=32.53s min=4.97s med=33.65s max=54.98s p(90)=53.5s  p(95)=54.24s
    http_req_failed................: 66.66% 16 out of 24
    http_reqs......................: 24     0.199998/s

    EXECUTION
    iteration_duration.............: avg=41.97s min=5.07s med=47.34s max=1m0s   p(90)=52.19s p(95)=54.77s
    iterations.....................: 24     0.199998/s
    vus............................: 2      min=2        max=10
    vus_max........................: 10     min=10       max=10

    NETWORK
    data_received..................: 1.2 GB 9.8 MB/s
    data_sent......................: 2.7 kB 23 B/s




running (2m00.0s), 00/10 VUs, 24 complete and 2 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```

Results are worse ? but why 
- because of problem of Thundering Herd

## after reducing Virtual Users to 2 from 10 concurrent

```bash
feed_postgres  | 2026-09-19 18:49:15.028 UTC [27] LOG:  checkpoint starting: time
feed_postgres  | 2026-09-19 18:49:15.028 UTC [27] LOG:  checkpoint starting: time
feed_postgres  | 2026-09-19 18:49:15.270 UTC [27] LOG:  checkpoint complete: wrote 2 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.121 s, sync=0.032 s, total=0.242 s; sync files=2, longest=0.020 s, average=0.016 s; distance=0 kB, estimate=16 kB; lsn=5/4C7C5A98, redo lsn=5/4C7C5A40
feed_postgres  | 2026-09-19 18:49:15.270 UTC [27] LOG:  checkpoint complete: wrote 2 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.121 s, sync=0.032 s, total=0.242 s; sync files=2, longest=0.020 s, average=0.016 s; distance=0 kB, estimate=16 kB; lsn=5/4C7C5A98, redo lsn=5/4C7C5A40
rss_poller     | Polling BBC World....
rss_poller     | Polling BBC World....
rss_poller     |   -> 24 entries processed
rss_poller     | Polling Reuters World....
rss_poller     |   -> 24 entries processed
rss_poller     | Polling Reuters World....
rss_poller     |   -> 0 entries processed
rss_poller     |   -> 0 entries processed
rss_poller     | Polling TechCrunch....
rss_poller     | Polling TechCrunch....

rss_poller     |   -> 20 entries processed
rss_poller     |   -> 20 entries processed
rss_poller     | Polling Hacker News....
rss_poller     |   -> 20 entries processed
rss_poller     |   -> 20 entries processed
```

k6
```bash

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/


     execution: local
        script: k6/load_test_deep_pagination.js
        output: -

     scenarios: (100.00%) 1 scenario, 2 max VUs, 2m0s max duration (incl. graceful stop):
              * ramping: 2 looping VUs for 1m30s (gracefulStop: 30s)



  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=3

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=9

    limit_counter{limit:300000}
    ✓ 'count>=0' count=5

    limit_counter{limit:600000}
    ✓ 'count>=0' count=5

    limit_counter{limit:800000}
    ✓ 'count>=0' count=41


  █ TOTAL RESULTS

    checks_total.......: 63      0.647749/s
    checks_succeeded...: 100.00% 63 out of 63
    checks_failed......: 0.00%   0 out of 63

    ✓ status is 200

    CUSTOM
    limit_counter..................: 63     0.647749/s
      { limit:100000 }.............: 3      0.030845/s
      { limit:1000000 }............: 9      0.092536/s
      { limit:300000 }.............: 5      0.051409/s
      { limit:600000 }.............: 5      0.051409/s
      { limit:800000 }.............: 41     0.421551/s

    HTTP
    http_req_duration..............: avg=2.87s min=327.35ms med=913.53ms max=14.06s p(90)=10.13s p(95)=10.61s
      { expected_response:true }...: avg=2.87s min=327.35ms med=913.53ms max=14.06s p(90)=10.13s p(95)=10.61s
    http_req_failed................: 0.00%  0 out of 63
    http_reqs......................: 63     0.647749/s

    EXECUTION
    iteration_duration.............: avg=2.97s min=428.28ms med=1.01s    max=14.16s p(90)=10.24s p(95)=10.71s
    iterations.....................: 63     0.647749/s
    vus............................: 1      min=1       max=2
    vus_max........................: 2      min=2       max=2

    NETWORK
    data_received..................: 11 GB  109 MB/s
    data_sent......................: 6.1 kB 63 B/s




running (1m37.3s), 0/2 VUs, 63 complete and 0 interrupted iterations
ramping ✓ [======================================] 2 VUs  1m30s
```