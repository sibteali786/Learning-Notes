# AI-PMS — Apollo Client Analysis & Fixes

> Generated: May 2026 | Internal Reference

---

## Setup Summary

```
apolloClient.js
├── httpLink        → GraphQL over HTTP POST
├── authLink        → attaches JWT to every request
├── errorLink       → logs GraphQL + network errors
├── InMemoryCache   → client-side cache (Property, Room, Booking, Package)
└── No WebSocketLink → no GraphQL subscriptions (Socket.IO handles real-time)
```

Apollo handles data fetching. Socket.IO handles push events. Clean separation — keep it that way.

---

## What Needs Fixing

### 🔴 Fix 1 — Replace Polling with Socket.IO for Channel Events

Polling is doing real-time's job in two places:

```js
// channel-manager/page.jsx
pollInterval: 10000,   // channel events — every 10s
pollInterval: 30000,   // sync status   — every 30s

// dashboard/page.jsx
pollInterval: 60000,   // metrics — every 60s
```

**Why this matters at scale:**

```
10 hotels, 1 open browser tab each
→ channel events polling every 10s
→ 60 requests/min hitting GraphQL server
→ most returning empty — pure waste

100 hotels → 600 req/min just for "is there anything new?"
```

**Fix:** Use the Socket.IO connection already in place for channel event updates. Apollo fetches initial data on load; Socket.IO triggers a `refetch()` when something actually changes.

```js
// Pattern to follow in channel-manager/page.jsx:
// 1. Remove pollInterval from useQuery
const { data, refetch } = useQuery(GET_CHANNEL_EVENTS, {
  variables: { propertyId: selectedPropertyId },
  // pollInterval: 10000  ← REMOVE
});

// 2. Listen for Socket.IO push instead
useEffect(() => {
  socket.on('channel:event:new', () => refetch());
  return () => socket.off('channel:event:new');
}, [refetch]);
```

---

### 🟡 Fix 2 — Clear Apollo Cache on Logout (`auth.js`)

`InMemoryCache` is a singleton for the browser session. If a user logs out and another logs in on the same tab (or if you later support org-switching), cached data from the previous session persists.

One line fix — add to logout handler:

```js
// In auth.js or useAuthStore logout action:
import client from '@/lib/apolloClient';

export const signOut = async () => {
  // ... existing logout logic
  await client.clearStore(); // wipes InMemoryCache completely
};
```

---

## Verdict on Apollo for This Project

|Concern|Verdict|
|---|---|
|GraphQL data fetching|✅ Correct choice, keep it|
|Cache config for multi-tenancy|🟡 Add `client.clearStore()` on logout|
|Polling for real-time data|🔴 Replace with Socket.IO for channel events feed|
|Apollo Subscriptions (WebSocket)?|❌ Redundant — Socket.IO already covers real-time|
|Replace Apollo entirely?|❌ Not justified|

## Future (Post-MVP)

| Feature                      | What to Use                                        |
| ---------------------------- | -------------------------------------------------- |
| Push notifications           | Web Push API / FCM — not Apollo                    |
| Offline support              | Apollo Persist Cache — add later                   |
| Webhook-triggered UI updates | Socket.IO emit → `refetch()` — already the pattern |