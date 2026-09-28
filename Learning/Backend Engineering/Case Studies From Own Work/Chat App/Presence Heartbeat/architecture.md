# Online presence via Redis heartbeats: architecture

Companion to `architecture.html` (interactive) and `2026-09-24-explanation-redis-heartbeat-presence.html` (long-form explainer).

**Core rule:** the browser renews a 60 s Redis lease every 30 s. If two renewals are missed, the user is marked offline and the change is broadcast.

## Components

| Node | Where | Role |
|---|---|---|
| Alice's browser | `Chat-App-Frontend/providers/presence-provider.tsx` | Emits `authenticate_presence`, then `heartbeat {status}` every 30 s while authenticated. Holds a reducer with `userPresence` and `onlineUsers`. |
| Bob & other clients | `hooks/use-presence.ts`, `hooks/use-presence-indicator.ts`, `components/presence/*` | Listen for `user_online`, `user_offline`, `status_changed` and `presence_update`. Merge real-time data with React Query REST data (60 s refetch). Render dots. |
| presence.handler | `chat-app-backend/src/presence/socket/presence.handler.ts` | Socket events: `authenticate_presence`, `heartbeat`, `change_status`, `get_presence`, `get_online_users`, `disconnect`. `setupPresenceBroadcasting` maps manager events to `io.emit`. |
| REST /presence/* | `src/presence/routes/presence.routes.ts` and the controller | Fallback for when the socket is not authenticated. Also serves history, analytics and admin endpoints. |
| PresenceManager | `src/presence/presence-manager.ts` | Singleton (ServiceLocator), an EventEmitter. `processHeartbeat`, `setUserOffline`, `getBulkPresence`, `getOnlineUsers`, and a 60 s cleanup interval. |
| Offline timers | inside PresenceManager | `Map<userId, setTimeout(60s)>`, reset on each beat. When it fires, it calls `setUserOffline`. |
| Redis | `presence:{tenantId}:{userId}` | JSON `{userId, tenantId, status, lastSeen, deviceInfo}`. TTL 60 s while online, 24 h once offline (for "last seen"). |
| MongoDB | `UserConnection`, `PresenceHistory` | Contacts used for targeted `presence_update`, and session start, end and duration for analytics. Jobs delete history older than 90 days (daily) and close orphaned sessions (hourly). |

## Flows

1. **Come online:** browser → `authenticate_presence {status}` → `processHeartbeat` → `GET` (nil, so the user was offline) → `SETEX … 60` → arm timer → open a PresenceHistory session → emit `userOnline` → `io.emit("user_online")`.
2. **Heartbeat (every 30 s):** `heartbeat {status}` → `processHeartbeat` → `GET` + `SETEX 60` → reset timer → acknowledge. No broadcast unless the status changed.
3. **Change status:** `change_status {busy}` (validated with Zod) → `processHeartbeat` → the status-changed branch runs → `UserConnection.find` → `statusChanged` + `broadcastPresence` → `status_changed` to everyone and `presence_update` to each contact's room.
4. **Clean disconnect:** `disconnect` → `setUserOffline` → `SETEX … 86400 {offline}` → clear timer → `endSession` → `user_offline`.
5. **Silent drop:** the timer fires after 60 s → `setUserOffline(userId, tenantId)`.
   - *As built (since 4be4784):* `tenantId` is `this.tenantId`, which is `undefined`. The lookup reads `presence:undefined:alice` and gets nil, so nothing happens. The real key expires silently through its TTL, and peers find out only on their next REST refetch (up to 60 s later).
   - *Fixed:* pass the `tenantId` argument. This writes the offline record and broadcasts `user_offline`.
6. **Read presence:** `POST /presence/bulk` (or socket `get_presence`) → `getBulkPresence` → `MULTI GET ×N`. The online list uses `SCAN MATCH presence:{tenant}:*`. A missing key means offline.

## Modes in the diagram

- **As built:** current code. `PresenceManager` uses `this.tenantId` (undefined) in `resetOfflineTimer` and in the status-change broadcast.
- **Fixed:** those two call sites use the `tenantId` parameter.

## Known issues

- `this.tenantId` is undefined (see flow 5). This is a two-line fix in `processHeartbeat`.
- `io.emit` broadcasts are not scoped to a tenant.
- With multiple tabs, closing one tab marks the user offline until the next heartbeat.
- Offline timers live in one process's memory, so they break with several backend instances.
- `UserConnection` is only filled through `POST /presence/connections`, so targeted `presence_update` rarely reaches anyone.
- The backend `PRESENCE_STATUS` has `WORK` and the frontend's doesn't.

## Commit trail

Backend: `f79b5d4` module added, `e767ca0` ServiceLocator, `f3e885a`/`2b0a367` bulk parsing fixes, `d4d5dfa` server-side interval removed (client-driven heartbeat), `24d8971` tenant-scoped keys, `4be4784` constructor tenantId removed (bug).
Frontend: `57333c2` provider, hooks, UI; `8b37190`/`49a2c02` live online list; `aea85eb` send current status on authenticate; `a5ba524`/`93b252d`/`3d47c42` online list refinements.
