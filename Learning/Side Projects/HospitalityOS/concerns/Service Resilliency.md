# AI-PMS — Service Resilience & Communication Patterns

> Generated: May 2026 | Internal Reference

---

## Communication Architecture (Clarified)

| Layer | Protocol | Usage |
|---|---|---|
| OTA Inbound | **Webhooks** (HTTP POST) | Booking.com, Airbnb etc. push events to `/webhooks/*` |
| OTA Outbound | **REST HTTP** | `pushAvailability()`, `pushRates()` on adapters — not yet implemented |
| Real-time Monitoring | **SSE / Socket.IO** | IoT sensor data pushed to browser dashboard |
| Frontend ↔ Backend | **GraphQL over HTTP** | All core PMS operations |

---

## What's Already Good ✅

The `eventBus` has genuine resilience for OTA inbound bookings:
- Persists every event to MongoDB **before** processing
- 3 retries with exponential backoff (`2s → 4s → 6s`)
- Dead-letter status tracked in DB (`status: 'failed'`)
- Manual `replay(eventId)` available via GraphQL mutation
- Webhook ACK sent to OTA immediately — correct, prevents OTA retries

---

## What Needs Fixing

### 🔴 Fix 1 — MongoDB connection pool size & resilience (`server.js`)

`maxPoolSize: 2000` is dangerous on a single server — will exhaust DB connections fast. Default should be 10.
Also no reconnect handling — if DB drops, server just hangs silently.

```js
// REPLACE in server.js:
await mongoose.connect(process.env.MONGO_URI, {
  maxPoolSize: 10,
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
});

mongoose.connection.on('disconnected', () => {
  console.error('[DB] MongoDB disconnected — attempting reconnect');
});
mongoose.connection.on('error', (err) => {
  console.error('[DB] MongoDB error:', err);
});
```

---

### 🟡 Fix 2 — Dead-letter alerting (`eventBus.js`)

When an OTA booking fails all 3 retries it silently sits in the DB as `status: 'failed'`. No staff notification, no visibility. Receptionist never knows a booking from Airbnb failed to inject.

```js
// ADD inside the dead-letter else block in subscribe():
} else {
  console.error(`[EventBus] Dead-lettering event ${eventType} after ${MAX_RETRIES} attempts`);
  if (eventId) {
    await ChannelEvent.findByIdAndUpdate(eventId, {
      status: 'failed',
      error: err.message
    });
  }
  // ADD THIS:
  console.error(`[ALERT] Manual intervention needed: Event ${eventId} (${eventType}) failed. Use replay mutation.`);
  // Hook into notification service here when ready
}
```

---

### 🟡 Fix 3 — IoT Gateway startup isolation (`server.js`)

If MQTT broker fails to start, it currently takes down the whole server. IoT monitoring should be optional — core PMS must survive without it.

```js
// REPLACE in server.js:
try {
  IoTGateway.startBroker(1883);
  if (process.env.MQTT_BROKER_URL) {
    IoTGateway.connectToExternalBroker(process.env.MQTT_BROKER_URL);
  }
} catch (err) {
  console.error('[IoT] Gateway failed to start — monitoring disabled:', err.message);
  // Server continues without IoT
}
```

---

## Defer Until Post-MVP

| Thing                          | Why Skip Now                                                   |
| ------------------------------ | -------------------------------------------------------------- |
| Circuit breakers               | No distributed services to protect yet                         |
| gRPC / RPC                     | OTAs dictate the protocol — webhooks + REST is the only option |
| Kafka / external message queue | EventBus handles current volume fine                           |
| Splitting Channel Manager      | Only worth it when OTA volume justifies operational overhead   |
| Per-service health checks      | One `/health` endpoint is enough for now                       |