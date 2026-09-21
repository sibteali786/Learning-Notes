docker stats for feed_api 
![[Pasted image 20260908122650.png]]![[Pasted image 20260908122705.png]]![[Pasted image 20260908122717.png]]



after 4 workers added
![[Pasted image 20260908125301.png]]![[Pasted image 20260908125311.png]]

## TOP ( utlitiy for each worjer CPU usage)

![[Pasted image 20260910160003.png]]![[Pasted image 20260910160013.png]]![[Pasted image 20260910160037.png]]![[Pasted image 20260910160054.png]]

#### K6 Run for this 
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
    ✗ 'p(99)<200' p(99)=1.51s


  █ TOTAL RESULTS

    checks_total.......: 160883  1068.803438/s
    checks_succeeded...: 100.00% 160883 out of 160883
    checks_failed......: 0.00%   0 out of 160883

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=276.11ms min=1.27ms   med=148.18ms max=5.43s p(90)=690.78ms p(95)=926.73ms
      { expected_response:true }...: avg=276.11ms min=1.27ms   med=148.18ms max=5.43s p(90)=690.78ms p(95)=926.73ms
    http_req_failed................: 0.00%  0 out of 160883
    http_reqs......................: 160883 1068.803438/s

    EXECUTION
    iteration_duration.............: avg=383.19ms min=101.51ms med=255.4ms  max=5.53s p(90)=806.02ms p(95)=1.04s
    iterations.....................: 160883 1068.803438/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 683 MB 4.5 MB/s
    data_sent......................: 15 MB  101 kB/s




running (2m30.5s), 0000/1000 VUs, 160883 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0152] thresholds on metrics 'http_req_duration' have been crossed
```


## Gunicorn with --access-logfile flag
- Will save file inside docker to study it 
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

RUN mkdir -p /var/log/gunicorn && chown -R www-data:www-data /var/log/gunicorn

EXPOSE 8000
CMD ["gunicorn", "--access-logfile", "/var/log/gunicorn/access.log", "main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4", "--bind", "0.0.0.0:8000"]

```

k6 run
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
    ✗ 'p(99)<200' p(99)=1.61s


  █ TOTAL RESULTS

    checks_total.......: 154758  1027.523805/s
    checks_succeeded...: 100.00% 154758 out of 154758
    checks_failed......: 0.00%   0 out of 154758

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=296.63ms min=1.38ms  med=145.04ms max=6.02s p(90)=725.13ms p(95)=992.33ms
      { expected_response:true }...: avg=296.63ms min=1.38ms  med=145.04ms max=6.02s p(90)=725.13ms p(95)=992.33ms
    http_req_failed................: 0.00%  0 out of 154758
    http_reqs......................: 154758 1027.523805/s

    EXECUTION
    iteration_duration.............: avg=398.96ms min=101.6ms med=248.29ms max=6.16s p(90)=828.6ms  p(95)=1.09s
    iterations.....................: 154758 1027.523805/s
    vus............................: 998    min=1           max=998
    vus_max........................: 1000   min=1000        max=1000

    NETWORK
    data_received..................: 657 MB 4.4 MB/s
    data_sent......................: 15 MB  97 kB/s




running (2m30.6s), 0000/1000 VUs, 154758 complete and 0 interrupted iterations
ramping ✓ [======================================] 0000/1000 VUs  2m30s
ERRO[0151] thresholds on metrics 'http_req_duration' have been crossed
```


## Py-spy for profiling gunicorn

![[Pasted image 20260910173927.png]]![[Pasted image 20260910173934.png]]![[Pasted image 20260910173944.png]]![[Pasted image 20260910173954.png]]![[Pasted image 20260910174017.png]]![[Pasted image 20260910174039.png]]![[Pasted image 20260910174056.png]]![[Pasted image 20260910174138.png]]