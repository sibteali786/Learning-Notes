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

WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"


  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=2

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=6

    limit_counter{limit:300000}
    ✓ 'count>=0' count=4

    limit_counter{limit:600000}
    ✓ 'count>=0' count=2

    limit_counter{limit:800000}
    ✓ 'count>=0' count=30


  █ TOTAL RESULTS

    checks_total.......: 44     0.441508/s
    checks_succeeded...: 88.63% 39 out of 44
    checks_failed......: 11.36% 5 out of 44

    ✗ status is 200
      ↳  88% — ✓ 39 / ✗ 5

    CUSTOM
    limit_counter..................: 44     0.441508/s
      { limit:100000 }.............: 2      0.020069/s
      { limit:1000000 }............: 6      0.060206/s
      { limit:300000 }.............: 4      0.040137/s
      { limit:600000 }.............: 2      0.020069/s
      { limit:800000 }.............: 30     0.301028/s

    HTTP
    http_req_duration..............: avg=21.98s min=348.1ms  med=13.89s max=1m0s   p(90)=57.76s p(95)=1m0s
      { expected_response:true }...: avg=17.04s min=348.1ms  med=9.5s   max=51.45s p(90)=44.77s p(95)=46.24s
    http_req_failed................: 11.36% 5 out of 44
    http_reqs......................: 44     0.441508/s

    EXECUTION
    iteration_duration.............: avg=22.14s min=448.39ms med=13.99s max=1m0s   p(90)=58.13s p(95)=1m0s
    iterations.....................: 44     0.441508/s
    vus............................: 2      min=2       max=10
    vus_max........................: 10     min=10      max=10

    NETWORK
    data_received..................: 6.5 GB 65 MB/s
    data_sent......................: 4.3 kB 43 B/s




running (1m39.7s), 00/10 VUs, 44 complete and 0 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
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



  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=5

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=14

    limit_counter{limit:300000}
    ✓ 'count>=0' count=9

    limit_counter{limit:600000}
    ✓ 'count>=0' count=3

    limit_counter{limit:800000}
    ✓ 'count>=0' count=51


  █ TOTAL RESULTS

    checks_total.......: 82      0.828038/s
    checks_succeeded...: 100.00% 82 out of 82
    checks_failed......: 0.00%   0 out of 82

    ✓ status is 200

    CUSTOM
    limit_counter..................: 82     0.828038/s
      { limit:100000 }.............: 5      0.05049/s
      { limit:1000000 }............: 14     0.141372/s
      { limit:300000 }.............: 9      0.090882/s
      { limit:600000 }.............: 3      0.030294/s
      { limit:800000 }.............: 51     0.514999/s

    HTTP
    http_req_duration..............: avg=11.38s min=480.22ms med=10.4s  max=42.81s p(90)=24.21s p(95)=26.36s
      { expected_response:true }...: avg=11.38s min=480.22ms med=10.4s  max=42.81s p(90)=24.21s p(95)=26.36s
    http_req_failed................: 0.00%  0 out of 82
    http_reqs......................: 82     0.828038/s

    EXECUTION
    iteration_duration.............: avg=11.53s min=581.53ms med=10.53s max=42.91s p(90)=24.59s p(95)=26.46s
    iterations.....................: 82     0.828038/s
    vus............................: 1      min=1       max=10
    vus_max........................: 10     min=10      max=10

    NETWORK
    data_received..................: 14 GB  137 MB/s
    data_sent......................: 8.0 kB 81 B/s




running (1m39.0s), 00/10 VUs, 82 complete and 0 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```