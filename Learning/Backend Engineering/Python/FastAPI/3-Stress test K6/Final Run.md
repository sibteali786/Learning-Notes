```bash
➜  news_aggregator git:(main) ✗ k6 run --env BASE_URL=http://localhost:8000 k6/load_test.js

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
    ✗ 'p(99)<200' p(99)=1.42s


  █ TOTAL RESULTS

    checks_total.......: 167766  1114.451474/s
    checks_succeeded...: 100.00% 167766 out of 167766
    checks_failed......: 0.00%   0 out of 167766

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=260.71ms min=1.2ms    med=133.16ms max=3.6s p(90)=654.58ms p(95)=865.03ms
      { expected_response:true }...: avg=260.71ms min=1.2ms    med=133.16ms max=3.6s p(90)=654.58ms p(95)=865.03ms
    http_req_failed................: 0.00%  0 out of 167766
    http_reqs......................: 167766 1114.451474/s

    EXECUTION
    iteration_duration.............: avg=367.64ms min=101.37ms med=239.14ms max=3.8s p(90)=770.74ms p(95)=981.91ms
    iterations.....................: 167766 1114.451474/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 712 MB 4.7 MB/s
    data_sent......................: 16 MB  105 kB/s




running (2m30.5s), 0000/1000 VUs, 167766 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0151] thresholds on metrics 'http_req_duration' have been crossed
➜  news_aggregator git:(main) ✗
```
