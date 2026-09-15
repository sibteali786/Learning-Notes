"""
Loads the `students` table from Postgres into Redis as hashes:
  key = student:{id}
  fields = g, firstname, lastname, dob

pip install psycopg2-binary redis
"""

import time
import psycopg2
import redis

PG_DSN = "dbname=postgres user=postgres password=postgres host=localhost port=5432"
REDIS_HOST = "localhost"
REDIS_PORT = 6379

BATCH_SIZE = 5000          # rows per pipeline flush
CURSOR_FETCH_SIZE = 5000   # rows pulled from Postgres per round trip


def main():
    pg = psycopg2.connect(PG_DSN)
    # server-side (named) cursor so we don't try to pull all 10M rows into
    # Python memory at once
    pg_cur = pg.cursor(name="students_stream")
    pg_cur.itersize = CURSOR_FETCH_SIZE
    pg_cur.execute("SELECT id, g, firstname, lastname, dob FROM students")

    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    pipe = r.pipeline(transaction=False)

    start = time.time()
    total = 0
    batch_count = 0

    for row in pg_cur:
        student_id, g, firstname, lastname, dob = row
        key = f"student:{student_id}"
        pipe.hset(
            key,
            mapping={
                "g": g,
                "firstname": firstname or "",
                "lastname": lastname or "",
                "dob": str(dob),
            },
        )
        # maintain the sorted-set range index alongside the hash, for the
        # range-query benchmark step
        pipe.zadd("grade_index", {student_id: g})

        batch_count += 1
        total += 1

        if batch_count >= BATCH_SIZE:
            pipe.execute()
            pipe = r.pipeline(transaction=False)
            batch_count = 0

        if total % 500_000 == 0:
            elapsed = time.time() - start
            rate = total / elapsed
            print(f"  {total:,} rows loaded ({rate:,.0f} rows/sec)")

    if batch_count > 0:
        pipe.execute()

    elapsed = time.time() - start
    print(f"\nDone. Loaded {total:,} rows into Redis in {elapsed:.1f}s "
          f"({total / elapsed:,.0f} rows/sec)")

    pg_cur.close()
    pg.close()


if __name__ == "__main__":
    main()
