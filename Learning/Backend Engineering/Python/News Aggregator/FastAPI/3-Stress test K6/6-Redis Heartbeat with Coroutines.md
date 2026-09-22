## K6 
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



  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=5

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=17

    limit_counter{limit:300000}
    ✓ 'count>=0' count=5

    limit_counter{limit:600000}
    ✓ 'count>=0' count=3

    limit_counter{limit:800000}
    ✓ 'count>=0' count=73


  █ TOTAL RESULTS

    checks_total.......: 103     1.109631/s
    checks_succeeded...: 100.00% 103 out of 103
    checks_failed......: 0.00%   0 out of 103

    ✓ status is 200

    CUSTOM
    limit_counter..................: 103   1.109631/s
      { limit:100000 }.............: 5     0.053866/s
      { limit:1000000 }............: 17    0.183143/s
      { limit:300000 }.............: 5     0.053866/s
      { limit:600000 }.............: 3     0.032319/s
      { limit:800000 }.............: 73    0.786438/s

    HTTP
    http_req_duration..............: avg=8.8s min=190.78ms med=4.54s max=38.84s p(90)=18.96s p(95)=22.98s
      { expected_response:true }...: avg=8.8s min=190.78ms med=4.54s max=38.84s p(90)=18.96s p(95)=22.98s
    http_req_failed................: 0.00% 0 out of 103
    http_reqs......................: 103   1.109631/s

    EXECUTION
    iteration_duration.............: avg=8.9s min=291.59ms med=4.65s max=38.94s p(90)=19.07s p(95)=23.09s
    iterations.....................: 103   1.109631/s
    vus............................: 5     min=5        max=10
    vus_max........................: 10    min=10       max=10

    NETWORK
    data_received..................: 18 GB 194 MB/s
    data_sent......................: 10 kB 108 B/s




running (1m32.8s), 00/10 VUs, 103 complete and 0 interrupted iterations
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
    ✓ 'count>=0' count=10

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=19

    limit_counter{limit:300000}
    ✓ 'count>=0' count=3

    limit_counter{limit:600000}
    ✓ 'count>=0' count=6

    limit_counter{limit:800000}
    ✓ 'count>=0' count=88


  █ TOTAL RESULTS

    checks_total.......: 126     1.342773/s
    checks_succeeded...: 100.00% 126 out of 126
    checks_failed......: 0.00%   0 out of 126

    ✓ status is 200

    CUSTOM
    limit_counter..................: 126   1.342773/s
      { limit:100000 }.............: 10    0.106569/s
      { limit:1000000 }............: 19    0.202482/s
      { limit:300000 }.............: 3     0.031971/s
      { limit:600000 }.............: 6     0.063942/s
      { limit:800000 }.............: 88    0.93781/s

    HTTP
    http_req_duration..............: avg=7.26s min=85.97ms  med=4.62s max=32.47s p(90)=17.16s p(95)=21.31s
      { expected_response:true }...: avg=7.26s min=85.97ms  med=4.62s max=32.47s p(90)=17.16s p(95)=21.31s
    http_req_failed................: 0.00% 0 out of 126
    http_reqs......................: 126   1.342773/s

    EXECUTION
    iteration_duration.............: avg=7.36s min=187.16ms med=4.72s max=32.57s p(90)=17.27s p(95)=21.41s
    iterations.....................: 126   1.342773/s
    vus............................: 4     min=4        max=10
    vus_max........................: 10    min=10       max=10

    NETWORK
    data_received..................: 22 GB 229 MB/s
    data_sent......................: 12 kB 131 B/s




running (1m33.8s), 00/10 VUs, 126 complete and 0 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```

![[Pasted image 20260923003407.png]]

- Slow because the serilization and transformation part of rwos for publishedAt was CPU bound task ( for transforming 1_000_000 records ).
- Fixed it by using asyncio.to_thread to make this part hand over to other ( presumably not actual thread ) so we can work with renew_llop co routine.


# After Run

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



  █ THRESHOLDS

    limit_counter{limit:100000}
    ✓ 'count>=0' count=3

    limit_counter{limit:1000000}
    ✓ 'count>=0' count=15

    limit_counter{limit:300000}
    ✓ 'count>=0' count=7

    limit_counter{limit:600000}
    ✓ 'count>=0' count=5

    limit_counter{limit:800000}
    ✓ 'count>=0' count=84


  █ TOTAL RESULTS

    checks_total.......: 114     1.208735/s
    checks_succeeded...: 100.00% 114 out of 114
    checks_failed......: 0.00%   0 out of 114

    ✓ status is 200

    CUSTOM
    limit_counter..................: 114   1.208735/s
      { limit:100000 }.............: 3     0.031809/s
      { limit:1000000 }............: 15    0.159044/s
      { limit:300000 }.............: 7     0.074221/s
      { limit:600000 }.............: 5     0.053015/s
      { limit:800000 }.............: 84    0.890647/s

    HTTP
    http_req_duration..............: avg=8.02s min=66ms     med=6.52s max=25.37s p(90)=18.47s p(95)=22.01s
      { expected_response:true }...: avg=8.02s min=66ms     med=6.52s max=25.37s p(90)=18.47s p(95)=22.01s
    http_req_failed................: 0.00% 0 out of 114
    http_reqs......................: 114   1.208735/s

    EXECUTION
    iteration_duration.............: avg=8.12s min=166.39ms med=6.62s max=25.47s p(90)=18.59s p(95)=22.11s
    iterations.....................: 114   1.208735/s
    vus............................: 2     min=2        max=10
    vus_max........................: 10    min=10       max=10

    NETWORK
    data_received..................: 20 GB 211 MB/s
    data_sent......................: 11 kB 117 B/s




running (1m34.3s), 00/10 VUs, 114 complete and 0 interrupted iterations
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
    ✓ 'count>=0' count=21

    limit_counter{limit:300000}
    ✓ 'count>=0' count=5

    limit_counter{limit:600000}
    ✓ 'count>=0' count=0

    limit_counter{limit:800000}
    ✓ 'count>=0' count=92


  █ TOTAL RESULTS

    checks_total.......: 123     1.307335/s
    checks_succeeded...: 100.00% 123 out of 123
    checks_failed......: 0.00%   0 out of 123

    ✓ status is 200

    CUSTOM
    limit_counter..................: 123   1.307335/s
      { limit:100000 }.............: 5     0.053144/s
      { limit:1000000 }............: 21    0.223204/s
      { limit:300000 }.............: 5     0.053144/s
      { limit:600000 }.............: 0     0/s
      { limit:800000 }.............: 92    0.977844/s

    HTTP
    http_req_duration..............: avg=7.39s min=818.37ms med=5.34s max=23.3s p(90)=15.12s p(95)=17.74s
      { expected_response:true }...: avg=7.39s min=818.37ms med=5.34s max=23.3s p(90)=15.12s p(95)=17.74s
    http_req_failed................: 0.00% 0 out of 123
    http_reqs......................: 123   1.307335/s

    EXECUTION
    iteration_duration.............: avg=7.51s min=919.38ms med=5.44s max=23.4s p(90)=15.23s p(95)=18.66s
    iterations.....................: 123   1.307335/s
    vus............................: 2     min=2        max=10
    vus_max........................: 10    min=10       max=10

    NETWORK
    data_received..................: 22 GB 233 MB/s
    data_sent......................: 12 kB 127 B/s




running (1m34.1s), 00/10 VUs, 123 complete and 0 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```

![[Pasted image 20260923011859.png]]