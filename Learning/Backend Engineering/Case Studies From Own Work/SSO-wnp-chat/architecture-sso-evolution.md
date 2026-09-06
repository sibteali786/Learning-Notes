# WNP ↔ Chat App SSO — Architecture (v1 → v2)

Interactive diagram: `2026-09-06-architecture-sso-evolution.html`

## Components

| Node | Role/color | What it is |
|---|---|---|
| WNP Frontend | user / mint | `apps/web` — iframe host, `use-chat-auth.ts` hook |
| WNP Backend | orch / sky | `apps/backend` — `ChatController.generateInitToken` (HMAC signing), gated by `verifyTokenHybrid` |
| Chat-App-Frontend | embed / amber | `app/embed/page.tsx`, `lib/socket.ts` |
| chat-app-backend | compute / magenta | Socket.IO server, `socketAuthMiddleware`, `SSOTokenService.validateToken` |
| Tenant Store | vector / violet | MongoDB `Tenant` collection (`status`, `isActive`, `sharedSecret`, `registrationToken`) |
| Admin / Ops | seed / orange | `AdminController` / `TenantController` — provisions new tenants |

## Mode toggle: v1 vs v2

- **v1 — Original (postMessage + REST)**: the iframe and parent relay the token over `window.postMessage`, then the chat frontend makes a separate REST call (`POST /tenants/sso/init`) to log in, and only afterwards opens a Socket.IO connection with the resulting JWT. Three independent async hops with no atomic handshake.
- **v2 — Current (Socket.IO handshake)**: the token/signature travel as iframe URL query params, and the chat frontend hands them straight to Socket.IO's `auth` option on connect. The socket connection attempt *is* the login request — one atomic step, success or `connect_error`.

## Flows

### 1. v1 Login — postMessage + REST (mode: v1 only)
1. `chat_fe → wnp_fe`: iframe posts `EMBED_READY`
2. `wnp_fe → chat_fe`: parent posts `INIT_CHAT` with `{token, signature}`
3. `chat_fe → chat_be`: REST `POST /tenants/sso/init`
4. `chat_be → chat_fe`: REST response with JWT
5. `chat_fe → chat_be`: Socket.IO connects afterwards, separately, using the JWT

**Note:** highlights the fragility — three async hops, any of which can be delayed or arrive out of order before the user sees a working chat UI.

### 2. v2 Login — Socket.IO Handshake (mode: v2 only)
1. `wnp_fe → wnp_be`: `GET /api/proxy/chat/init-token` (same-origin proxy, cookies)
2. `wnp_be → wnp_fe`: HMAC-signed token/signature returned (`generateInitToken`)
3. `wnp_fe → chat_fe`: iframe loads with `?ssoToken&ssoSignature` as query params
4. `chat_fe → chat_be`: `io(url, {auth: {ssoToken, ssoSignature}})` — single atomic handshake
5. `chat_be → tenant_db`: `socketAuthMiddleware` → `SSOTokenService.validateToken` — decode, check `exp`, look up **tenant's own** `sharedSecret`, recompute HMAC, **require `isActive && status === "verified"`**
6. `chat_be → chat_fe`: `findOrCreateUser`, JWTs issued, `tenantContext.run()`, emits `authenticated`

### 3. Tenant Registration & the Race Window (mode: v2 only)
1. **Generate** (`admin → chat_be`): `POST /api/admin/tenants/generate-credentials` → `Tenant{status:"pending_registration", isActive:false, sharedSecret, registrationToken (24h)}`
2. **Register** (`wnp_be → chat_be`): `POST /api/tenants/register` → `isActive:true`, `status:"pending_verification"` — **isActive flips true before status is verified**
3. **⚠ Race window** (`chat_fe → chat_be`): any SSO handshake attempted here is rejected by `validateToken`'s `!tenant.isActive || tenant.status !== "verified"` check → `ForbiddenError`. This is the root cause of the observed race condition.
4. **Verify** (`admin → chat_be`): `POST /api/tenants/verify` → `status:"verified"`, `provisionTenant()` runs — window closes, handshakes now succeed

**The fix** did not remove the ordering requirement (a tenant genuinely can't accept SSO before verification) — it made the in-between window fail cleanly: `getTenant` returns `null` instead of throwing, dedicated `ForbiddenError`/`UnauthorizedError` classes replace generic exceptions, and debug logging was added around this exact window.

### 4. Silent Re-auth (v2) — postMessage's surviving job
1. `chat_fe → wnp_fe`: `postMessage CHAT_AUTH_ERROR`
2. `wnp_fe → wnp_be`: silent `GET /api/proxy/chat/init-token`
3. `wnp_fe → chat_fe`: `postMessage CHAT_REAUTH` with fresh `{ssoToken, ssoSignature}` pushed into the already-mounted iframe
4. `chat_fe → chat_be`: socket disconnects and reconnects with the new credentials via the same v2 handshake

postMessage wasn't deleted from the system — it was demoted to this one job: refreshing an already-connected iframe's token without a full remount.

## Key code references

- `whatsnextplease-monolith/apps/backend/api/controller/chat.controller.ts` — `generateInitToken` (HMAC-SHA256 signing)
- `whatsnextplease-monolith/apps/web/hooks/use-chat-auth.ts` — token fetch, iframe URL, silent refresh, `CHAT_REAUTH`
- `chat app/Chat-App-Frontend/app/embed/page.tsx` — reads `ssoToken`/`ssoSignature` from URL, listens for `CHAT_REAUTH`
- `chat app/Chat-App-Frontend/lib/socket.ts` — builds `io(url, {auth})`
- `chat app/chat-app-backend/src/socket/middleware/auth.middleware.ts` — `socketAuthMiddleware`, `io.use(...)`
- `chat app/chat-app-backend/src/services/sso-token.service.ts` — `validateToken`, `findOrCreateUser`
