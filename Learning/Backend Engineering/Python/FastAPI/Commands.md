```sql
feed_engine=# WITH duplicate_rows AS (
feed_engine(# SELECT id, ROW_NUMBER() OVER (PARTITION BY url ORDER BY id) AS row_num FROM article
feed_engine(# )
feed_engine-# DELETE FROM article
feed_engine-# WHERE id IN (SELECT id FROM duplicate_rows WHERE row_num > 1);
DELETE 418
feed_engine=# ALTER TABLE article ADD CONSTRAINT uq_url UNIQUE (url);
ALTER TABLE
feed_engine=# ^C
feed_engine=# exit
```
