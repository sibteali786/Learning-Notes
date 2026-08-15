```
RDB is a Redis backup file created at intervals. It captures the whole Redis dataset at one moment, so a crash can lose changes made after the last snapshot. AOF is a log that records each write command, so Redis can replay the log after restarting. fsync means forcing written data from the operating system’s memory onto disk. With default AOF settings, Redis does that about once per second, so the newest second of acknowledged writes may be lost in a crash.
```


## Sorted Sets
```bash
➜  ~ docker exec -it redis-local redis-cli
127.0.0.1:6379> ZADD leaderboard 100 "alice"
(integer) 1
127.0.0.1:6379> ZADD leaderboard 250 "bob"
(integer) 1
127.0.0.1:6379> ZADD leaderboard 180 "carol"
(integer) 1
127.0.0.1:6379> ZRANGE leaderboard 0 -1 WITHSCORES
1) "alice"
2) "100"
3) "carol"
4) "180"
5) "bob"
6) "250"
127.0.0.1:6379> ZRANGE leaderboard 0 WITHSCORES
(error) ERR value is not an integer or out of range
127.0.0.1:6379> ZRANGE leaderboard 0 1 WITHSCORES
7) "alice"
8) "100"
9) "carol"
10) "180"
127.0.0.1:6379> ZRANGE leaderboard 1 WITHSCORES
(error) ERR value is not an integer or out of range
127.0.0.1:6379> ZRANGE leaderboard 1 2 WITHSCORES
11) "carol"
12) "180"
13) "bob"
14) "250"
127.0.0.1:6379> ZRANGE leaderboard 1 -1 WITHSCORES
15) "carol"
16) "180"
17) "bob"
18) "250"
127.0.0.1:6379> ZRANGE leaderboard 0 -1 WITHSCORES
19) "alice"
20) "100"
21) "carol"
22) "180"
23) "bob"
24) "250"
127.0.0.1:6379> ZREVRANGE leaderboard 0 -1 WITHSCORES
25) "bob"
26) "250"
27) "carol"
28) "180"
29) "alice"
30) "100"
127.0.0.1:6379> ZRANK leaderboard carol
(integer) 1
127.0.0.1:6379> ZREVRANGE leaderboard 0 -1 WITHSCORES
31) "bob"
32) "250"
33) "carol"
34) "180"
35) "alice"
36) "100"
127.0.0.1:6379> ZRANK leaderboard carol
(integer) 1
127.0.0.1:6379> ZREVRANGE leaderboard 0 -1 WITHSCORES
37) "bob"
38) "250"
39) "carol"
40) "180"
41) "alice"
42) "100"
127.0.0.1:6379> ZREVRANGE leaderboard 0 -1
43) "bob"
44) "carol"
45) "alice"
127.0.0.1:6379> ZRANK leaderboard carol
(integer) 1
127.0.0.1:6379> ZRANK leaderboard alice
(integer) 0
127.0.0.1:6379> ZRANK leaderboard bob
(integer) 2
127.0.0.1:6379>
```

### For a cache you'll configure an eviction policy like allkeys-lru so Redis discards the least-recently-used keys to make room. Redis approximates LRU by sampling keys rather than tracking exact order, which is plenty for a cache.
Redis does not remember the exact last-used time for every key. When it needs memory, it checks a small random sample of keys and evicts the least recently used key from that sample. This is faster and uses less memory than maintaining a perfect order for millions of keys, and it is usually close enough for cache eviction.

### Fencing Token

A fencing token is a version number attached to each lock owner. The database accepts writes only from the newest version.

```
Lock service grants A token 10
A pauses before writing

A's lock expires
Lock service grants B token 11
B writes with token 11  → database stores last_token = 11

A wakes up and writes with token 10
Database rejects it     → 10 is older than 11
```

For instance, each write can require WHERE last_token < :token. This prevents an old lock holder from overwriting newer data after its lock has expired.

![[redis_geosearch_grid_vs_radius.svg]]