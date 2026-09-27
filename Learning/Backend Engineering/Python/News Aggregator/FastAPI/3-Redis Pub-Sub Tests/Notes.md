## Test 1
```bash
➜  news_aggregator git:(main) ✗ for i in 1 2; do
  curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n" \
    "http://localhost:8000/feed/full-scan?limit=800000" &
done
wait
[2] 515950
[3] 515951
req2 status=200 time=7.821855s
[3]  + 515951 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
req1 status=200 time=8.284125s
[2]  + 515950 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
```

## For long runing 
```bash
feed_redis     | 99:C 27 Sep 2026 17:48:40.498 * Fork CoW for RDB: current 0 MB, peak 0 MB, feed_redis     | 1:M 27 Sep 2026 17:48:40.509 * Background saving terminated with success
feed_postgres  | 2026-09-27 17:50:24.188 UTC [27] LOG:  checkpoint starting: time
feed_postgres  | 2026-09-27 17:50:24.188 UTC [27] LOG:  checkpoint starting: time
feed_api       | [2026-09-27 17:50:41 +0000] [11] [ERROR] Exception in ASGI application
feed_api       | [2026-09-27 17:50:41 +0000] [11] [ERROR] Exception in ASGI application
feed_api       | Traceback (most recent call last):
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 676, in send_packed_command
feed_api       |     await self._writer.drain()
feed_api       |   File "/usr/local/lib/python3.12/asyncio/streams.py", line 392, in drain
feed_api       |     await self._protocol._drain_helper()

feed_api       | Traceback (most recent call last):
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 676, in send_packed_command
feed_api       |     await self._writer.drain()
feed_api       |   File "/usr/local/lib/python3.12/asyncio/streams.py", line 392, in drain
feed_api       |     await self._protocol._drain_helper()
feed_api       |   File "/usr/local/lib/python3.12/asyncio/streams.py", line 172, in _drain_helper
feed_api       |     await waiter
feed_api       |   File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 1102, in _write_sendmsg
feed_api       |     nbytes = self._sock.sendmsg(self._get_sendmsg_buffer())
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       | ConnectionResetError: [Errno 104] Connection reset by peer
feed_api       |
feed_api       | The above exception was the direct cause of the following exception:
feed_api       |
feed_api       | Traceback (most recent call last):
feed_api       |   File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 416, in run_asgi
feed_api       |     result = await app(  # type: ignore[func-returns-value]
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 63, in __call__
feed_api       |     return await self.app(scope, receive, send)
feed_api       |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1163, in __call__
feed_api       |     await super().__call__(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 96, in __call__
feed_api       |     await self.middleware_stack(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
feed_api       |     await self.app(scope, receive, _send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
feed_api       |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
feed_api       |     await app(scope, receive, sender)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
feed_api       |     await self.app(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 670, in __call__
feed_api       |     await self.middleware_stack(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 2734, in app
feed_api       |     await route.handle(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 1281, in handle
feed_api       |     await super().handle(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 280, in handle
feed_api       |     await self.app(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 158, in app
feed_api       |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
feed_api       |     await app(scope, receive, sender)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 144, in app
feed_api       |     response = await f(request)
feed_api       |                ^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 706, in app
feed_api       |     raw_response = await run_endpoint_function(
feed_api       |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 352, in run_endpoint_function
feed_api       |     return await dependant.call(**values)
feed_api       |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/app/main.py", line 164, in getFullScanFeed
feed_api       |     await redis_client.set(key, json_serialized, ex=20)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/client.py", l

feed_api       |     result = await conn.retry.call_with_retry(
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/retry.py", line 81, in call_with_retry
feed_api       |     raise error
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/retry.py", line 69, in call_with_retry
feed_api       |     return await do()
feed_api       |            ^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/client.py", line 722, in _send_command_parse_response
feed_api       |     await conn.send_command(*args)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 700, in send_command
feed_api       |     await self.send_packed_command(
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 687, in send_packed_command
feed_api       |     raise ConnectionError(
feed_api       |   File "/usr/local/lib/python3.12/asyncio/streams.py", line 172, in _drain_helpereset by peer.
feed_api       |     await waiter
feed_api       |   File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 1102, in _write_sendmsg
feed_api       |     nbytes = self._sock.sendmsg(self._get_sendmsg_buffer())
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       | ConnectionResetError: [Errno 104] Connection reset by peer
feed_api       |
feed_api       | The above exception was the direct cause of the following exception:
feed_api       |
feed_api       | Traceback (most recent call last):
feed_api       |   File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 416, in run_asgi
feed_api       |     result = await app(  # type: ignore[func-returns-value]
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 63, in __call__
feed_api       |     return await self.app(scope, receive, send)
feed_api       |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1163, in __call__
feed_api       |     await super().__call__(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 96, in __call__
feed_api       |     await self.middleware_stack(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
feed_api       |     await self.app(scope, receive, _send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
feed_api       |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
feed_api       |     await app(scope, receive, sender)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
feed_api       |     await self.app(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 670, in __call__
feed_api       |     await self.middleware_stack(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 2734, in app
feed_api       |     await route.handle(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 1281, in handle
feed_api       |     await super().handle(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 280, in handle
feed_api       |     await self.app(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 158, in app
feed_api       |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
feed_api       |     raise exc
feed_api       |   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
feed_api       |     await app(scope, receive, sender)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 144, in app
feed_api       |     response = await f(request)
feed_api       |                ^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 706, in app
feed_api       |     raw_response = await run_endpoint_function(
feed_api       |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 352, in run_endpoint_function
feed_api       |     return await dependant.call(**values)
feed_api       |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/app/main.py", line 164, in getFullScanFeed
feed_api       |     await redis_client.set(key, json_serialized, ex=20)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/client.py", line 782, in execute_command
feed_api       |     result = await conn.retry.call_with_retry(
feed_api       |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/retry.py", line 81, in call_with_retry
feed_api       |     raise error
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/retry.py", line 69, in call_with_retry
feed_api       |     return await do()
feed_api       |            ^^^^^^^^^^
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/client.py", line 722, in _send_command_parse_response
feed_api       |     await conn.send_command(*args)
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 700, in send_command
feed_api       |     await self.send_packed_command(
feed_api       |   File "/usr/local/lib/python3.12/site-packages/redis/asyncio/connection.py", line 687, in send_packed_command
feed_api       |     raise ConnectionError(
feed_api       | redis.exceptions.ConnectionError: Error 104 while writing to socket. Connection reset by peer.
```

```bash
➜  news_aggregator git:(main) ✗ docker exec feed_redis redis-cli DEL fullscan:limit:3000000 fullscan:lock:limit:3000000
0
➜  news_aggregator git:(main) ✗ curl -s -o /dev/null -w "single status=%{http_code} time=%{time_total}s\n" \
  "http://localhost:8000/feed/full-scan?limit=3000000"
single status=500 time=25.661250s
➜  news_aggregator git:(main) ✗


➜  news_aggregator git:(main) ✗ for i in 1 2; do
  curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n" \
    "http://localhost:8000/feed/full-scan?limit=3000000" &
done
wait
[2] 524615
[3] 524616
req2 status=500 time=26.494166s
[3]  + 524616 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
req1 status=500 time=60.107911s
[2]  + 524615 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
➜  news_aggregator git:(main) ✗
```

```bash
➜  news_aggregator git:(main) ✗ docker logs --since 5m feed_api 2>&1 | grep -iE "never awaited|Traceback|Error"
[2026-09-27 17:50:41 +0000] [11] [ERROR] Exception in ASGI application
Traceback (most recent call last):
ConnectionResetError: [Errno 104] Connection reset by peer
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    raise error
    raise ConnectionError(
redis.exceptions.ConnectionError: Error 104 while writing to socket. Connection reset by peer.
[2026-09-27 17:52:23 +0000] [8] [ERROR] Exception in ASGI application
Traceback (most recent call last):
ConnectionResetError: [Errno 104] Connection reset by peer
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    raise error
    raise ConnectionError(
redis.exceptions.ConnectionError: Error 104 while writing to socket. Connection reset by peer.
[2026-09-27 17:52:57 +0000] [11] [ERROR] Exception in ASGI application
Traceback (most recent call last):
ConnectionResetError: [Errno 104] Connection reset by peer
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
  File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
    raise error
    raise ConnectionError(
redis.exceptions.ConnectionError: Error 104 while writing to socket. Connection reset by peer.
```

### Debug
```bash
Size of response for 800k
➜  news_aggregator git:(main) ✗ docker exec feed_redis redis-cli STRLEN fullscan:limit:800000
181403292 bytes for 800K respons string
or 181.403292 MB

- Redis supports max 512Mb so its far below that
```

- Works for 2M becuase bytes per row is 181,403,292 / 800,000 ≈ 227 bytes 
- 3M rows: 3,000,000 × 227 ≈ 680 MB, over the 512 MB (536,870,912 bytes) limit, which is why Redis dropped the connection
```bash
➜  news_aggregator git:(main) ✗ docker exec feed_redis redis-cli DEL fullscan:limit:2000000 fullscan:lock:limit:2000000
0
➜  news_aggregator git:(main) ✗ for i in 1 2; do
  curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n" \
    "http://localhost:8000/feed/full-scan?limit=2000000" &
done
wait
[2] 581143
[3] 581144
req2 status=200 time=19.228681s
[3]  + 581144 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
req1 status=200 time=20.013757s
[2]  + 581143 done       curl -s -o /dev/null -w "req$i status=%{http_code} time=%{time_total}s\n"
➜  news_aggregator git:(main) ✗
```