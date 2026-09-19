```bash

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/


     execution: local
        script: k6/load_test.js
        output: -

     scenarios: (100.00%) 1 scenario, 1000 max VUs, 3m0s max duration (incl. graceful stop):
              * ramping: Up to 1000 looping VUs for 2m30s over 5 stages (gracefulRampDown: 30s, gracefulStop: 30s)



  █ THRESHOLDS

    http_req_duration
    ✗ 'p(99)<200' p(99)=1.67s


  █ TOTAL RESULTS

    checks_total.......: 146417  971.979887/s
    checks_succeeded...: 100.00% 146417 out of 146417
    checks_failed......: 0.00%   0 out of 146417

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=317.79ms min=1.31ms   med=173.9ms  max=4.9s p(90)=783.4ms  p(95)=1.02s
      { expected_response:true }...: avg=317.79ms min=1.31ms   med=173.9ms  max=4.9s p(90)=783.4ms  p(95)=1.02s
    http_req_failed................: 0.00%  0 out of 146417
    http_reqs......................: 146417 971.979887/s

    EXECUTION
    iteration_duration.............: avg=421.63ms min=101.53ms med=278.57ms max=5s   p(90)=887.38ms p(95)=1.13s
    iterations.....................: 146417 971.979887/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 660 MB 4.4 MB/s
    data_sent......................: 14 MB  92 kB/s




running (2m30.6s), 0000/1000 VUs, 146417 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0151] thresholds on metrics 'http_req_duration' have been crossed
```


