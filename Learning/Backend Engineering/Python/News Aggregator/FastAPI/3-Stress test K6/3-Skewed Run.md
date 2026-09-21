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
    ✗ 'p(99)<200' p(99)=1.68s


  █ TOTAL RESULTS

    checks_total.......: 145743  966.92677/s
    checks_succeeded...: 100.00% 145743 out of 145743
    checks_failed......: 0.00%   0 out of 145743

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=314.06ms min=1.25ms   med=178.45ms max=4.72s p(90)=768.85ms p(95)=1s
      { expected_response:true }...: avg=314.06ms min=1.25ms   med=178.45ms max=4.72s p(90)=768.85ms p(95)=1s
    http_req_failed................: 0.00%  0 out of 145743
    http_reqs......................: 145743 966.92677/s

    EXECUTION
    iteration_duration.............: avg=423.42ms min=101.48ms med=285.97ms max=4.82s p(90)=890.95ms p(95)=1.13s
    iterations.....................: 145743 966.92677/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 701 MB 4.6 MB/s
    data_sent......................: 14 MB  90 kB/s




running (2m30.7s), 0000/1000 VUs, 145743 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0152] thresholds on metrics 'http_req_duration' have been crossed
```

# For Each Tag Run
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
    ✗ 'p(99)<200' p(99)=1.83s

    region_counter{region:APAC}
    ✓ 'count>=0' count=9539

    region_counter{region:EU}
    ✓ 'count>=0' count=27542

    region_counter{region:LATAM}
    ✓ 'count>=0' count=4034

    region_counter{region:US}
    ✓ 'count>=0' count=95768


  █ TOTAL RESULTS

    checks_total.......: 136883  908.732108/s
    checks_succeeded...: 100.00% 136883 out of 136883
    checks_failed......: 0.00%   0 out of 136883

    ✓ status is 200

    CUSTOM
    region_counter.................: 136883 908.732108/s
      { region:APAC }..............: 9539   63.327043/s
      { region:EU }................: 27542  182.844471/s
      { region:LATAM }.............: 4034   26.78072/s
      { region:US }................: 95768  635.779874/s

    HTTP
    http_req_duration..............: avg=345.32ms min=1.28ms   med=193.98ms max=5.65s p(90)=881.5ms  p(95)=1.14s
      { expected_response:true }...: avg=345.32ms min=1.28ms   med=193.98ms max=5.65s p(90)=881.5ms  p(95)=1.14s
    http_req_failed................: 0.00%  0 out of 136883
    http_reqs......................: 136883 908.732108/s

    EXECUTION
    iteration_duration.............: avg=451.02ms min=101.44ms med=299.16ms max=5.82s p(90)=990.98ms p(95)=1.24s
    iterations.....................: 136883 908.732108/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 663 MB 4.4 MB/s
    data_sent......................: 13 MB  85 kB/s




running (2m30.6s), 0000/1000 VUs, 136883 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0151] thresholds on metrics 'http_req_duration' have been crossed
```


## Different Query 
![[Pasted image 20260917225052.png]]


New run with no limit
![[Pasted image 20260917232941.png]]![[Pasted image 20260917232945.png]]

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
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": request timeout"
WARN[0061] Request Failed                                error="request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": request timeout"
WARN[0061] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0065] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=1000000\": request timeout"
WARN[0075] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"
WARN[0094] Request Failed                                error="Get \"http://localhost:8000/feed/full-scan?limit=800000\": request timeout"


  █ TOTAL RESULTS

    checks_total.......: 35     0.291216/s
    checks_succeeded...: 77.14% 27 out of 35
    checks_failed......: 22.85% 8 out of 35

    ✗ status is 200
      ↳  77% — ✓ 27 / ✗ 8

    HTTP
    http_req_duration..............: avg=23.78s min=882.77ms med=15.77s max=1m0s   p(90)=1m0s   p(95)=1m0s
      { expected_response:true }...: avg=12.92s min=882.77ms med=12.12s max=40.12s p(90)=26.04s p(95)=33.54s
    http_req_failed................: 22.85% 8 out of 35
    http_reqs......................: 35     0.291216/s

    EXECUTION
    iteration_duration.............: avg=23.94s min=983.8ms  med=15.87s max=1m1s   p(90)=1m1s   p(95)=1m1s
    iterations.....................: 35     0.291216/s
    vus............................: 4      min=4       max=10
    vus_max........................: 10     min=10      max=10

    NETWORK
    data_received..................: 2.6 GB 22 MB/s
    data_sent......................: 4.0 kB 33 B/s




running (2m00.2s), 00/10 VUs, 35 complete and 4 interrupted iterations
ramping ✓ [======================================] 10 VUs  1m30s
```

script added 
```js
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    ramping: {
      executor: "constant-vus",
      vus: 10,
      duration: "90s",
    },
  },
};

const BASE_URL = __ENV.BASE_URL || "http://localhost:8000";
const LIMITS = [100_000, 300_000, 600_000, 800_000, 1_000_000];
const MAX_ID = 50_000_000; // matches the seeded row count

export default function () {
  const limit = LIMITS[Math.floor(Math.random() * LIMITS.length)];

  const res = http.get(`${BASE_URL}/feed/full-scan?limit=${limit}`);
  check(res, { "status is 200": (r) => r.status === 200 });
  sleep(0.1);
}
```