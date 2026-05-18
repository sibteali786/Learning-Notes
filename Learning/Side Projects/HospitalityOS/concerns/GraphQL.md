# AI-PMS — GraphQL, TimescaleDB & Redis Analysis

> Generated: May 2026 | Internal Reference

---

## GraphQL

### Verdict: Keep It — Two Issues to Fix

---

### 🔴 Fix 1 — N+1 Queries (Present Now)

No DataLoader anywhere in the codebase. Every booking list page triggers:

```
1 (list query) + 20 × 3 (room + property + package populate) = 61 DB calls per page load
```

Invisible at small scale. Becomes the bottleneck at 50+ concurrent users.

**Fix:** Add DataLoader for frequently populated relations.

```js
// NEW: lib/dataloaders.js
const DataLoader = require('dataloader');
const { Room } = require('../models/Room');
const { Property } = require('../models/Property');

const createRoomLoader = () => new DataLoader(async (ids) => {
  const rooms = await Room.find({ _id: { $in: ids } }).lean();
  const map = Object.fromEntries(rooms.map(r => [r._id.toString(), r]));
  return ids.map(id => map[id.toString()] || null);
});

const createPropertyLoader = () => new DataLoader(async (ids) => {
  const props = await Property.find({ _id: { $in: ids } }).lean();
  const map = Object.fromEntries(props.map(p => [p._id.toString(), p]));
  return ids.map(id => map[id.toString()] || null);
});

module.exports = { createRoomLoader, createPropertyLoader };
```

```js
// In server.js Apollo context — create per-request loaders:
context: async ({ req }) => ({
  userId,
  req,
  loaders: {
    room: createRoomLoader(),
    property: createPropertyLoader(),
  }
})
```

---

### 🟡 Fix 2 — No Query Depth Limit (Pre-Public Exposure)

No depth or complexity limits configured. A single deeply nested query can hang the server. Not urgent for internal alpha testers but must be in place before any public access.

```bash
npm install graphql-depth-limit
```

```js
// In server.js ApolloServer config — add validationRules:
const depthLimit = require('graphql-depth-limit');

const apolloServer = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [depthLimit(7)],  // adjust based on deepest legitimate query
  // ...rest of config
});
```

---

### Should We Switch to PostgreSQL?

**No — not for MVP, not as a full migration.**

MongoDB is a correct fit for what this system stores: heterogeneous OTA payloads, nested guest data, flexible property configs. Where it shows weakness (complex finance reporting, cross-collection joins) the answer is MongoDB aggregation pipelines — not a migration.

The PostgreSQL question becomes real only if heavy analytics/reporting is built later. At that point a **separate read replica or analytics DB** is the right move, not migrating the entire core.

---

## TimescaleDB

### Verdict: Correct Tool, Correctly Isolated — Two Fixes Needed

Used exclusively for IoT sensor readings (`sensor_readings` hypertable). `time_bucket()` aggregations, trend data, anomaly detection — all correct usage. Fully isolated from MongoDB with its own `pg` Pool.

---

### 🔴 Fix 1 — SQL Injection via String Interpolation

`hours` and `days` parameters are interpolated directly into SQL strings:

```js
// VULNERABLE in timescaleDB.js:
`WHERE time >= NOW() - INTERVAL '${hours} hours'`
`WHERE time < NOW() - INTERVAL '${days} days'`
```

If these values ever reach user input, it's injectable.

```js
// REPLACE with parameterized intervals:

// calculateAverage:
const queryText = `
  SELECT AVG(value) as average
  FROM sensor_readings
  WHERE property_id = $1
    AND metric_type = $2
    AND time >= NOW() - ($3 * INTERVAL '1 hour');
`;
return query(queryText, [propertyId, metricType, hours]);

// deleteOldData:
const queryText = `
  DELETE FROM sensor_readings
  WHERE time < NOW() - ($1 * INTERVAL '1 day');
`;
return query(queryText, [days]);
```

---

### 🟡 Fix 2 — `initialize()` Never Called at Startup

TimescaleDB pool is created lazily on first route hit. If `eventProcessor` or any monitoring service calls it before a route triggers initialization, it throws `TimescaleDB not initialized`.

```js
// ADD in server.js alongside mongoose.connect():
const TimescaleDB = require('./monitoring/database/timescaleDB');
TimescaleDB.initialize();
```

---

## Redis

### Verdict: Correct Uses — Consolidate Into One Client

Used for: IoT device status cache, security event feed, push notification subscriptions, notification settings. All appropriate — fast ephemeral state that doesn't need DB persistence.

---

### 🔴 Fix — 3 Separate Instances → 1 Shared Client

Three files each open their own TCP connection to Redis:

```js
// sensor.controller.js      → new Redis(process.env.REDIS_URL)
// monitoring.controller.js  → new Redis(process.env.REDIS_URL)
// notificationService.js    → new Redis(process.env.REDIS_URL)
```

```js
// NEW: config/redisClient.js
const Redis = require('ioredis');

const redis = new Redis(process.env.REDIS_URL, {
  retryStrategy: (times) => Math.min(times * 50, 2000),
  maxRetriesPerRequest: 3,
});

redis.on('error', (err) => console.error('[Redis] Error:', err));
redis.on('connect', () => console.log('✅ Redis connected'));

module.exports = redis;
```

```js
// REPLACE in every file that instantiates Redis:
// FROM: const redis = new Redis(process.env.REDIS_URL);
// TO:
const redis = require('../../config/redisClient');
```

---

## Summary

| Tech            | Verdict        | Priority                                                   |
| --------------- | -------------- | ---------------------------------------------------------- |
| **GraphQL**     | ✅ Keep         | 🔴 Add DataLoader · 🟡 Add depth limit before public       |
| **MongoDB**     | ✅ Keep for MVP | Don't migrate; aggregation pipelines cover reporting needs |
| **TimescaleDB** | ✅ Correct fit  | 🔴 Fix SQL injection · 🟡 Call `initialize()` at startup   |
| **Redis**       | ✅ Correct uses | 🔴 Consolidate 3 instances into one shared client          |