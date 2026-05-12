```table-of-contents
```
# Back-end
## Repository Snapshot

This is a **TypeScript Node.js backend** for a real-time chat system with REST + WebSocket support, tenant isolation, and presence tracking.

## Tech Stack

- **Runtime/API:** `Node.js`, `Express`, `TypeScript`
- **Database:** `MongoDB` with `Mongoose`
- **Cache/realtime infra:** `Redis`, `Socket.IO`
- **Auth/security:** `jsonwebtoken` (JWT), `bcrypt`, `express-rate-limit`, `zod`
- **Storage/media:** AWS S3 SDK (`@aws-sdk/client-s3`, presigner)
- **Logging/testing/dev:** `winston`, `vitest`, `eslint`, `nodemon`, `ts-node`
- **Local infra:** `docker-compose` spins up `mongodb`, `mongo_express`, `redis`

## Routes (Count + Structure)

Mounted under `app.use("/api", routes)` in `src/server.ts`, plus top-level `/health`.

- **Total HTTP endpoints found:** **67**
  - **66** under `/api/*`
  - **1** top-level `/health`

Main route groups under `src/routes/index.ts`:

- `/api/auth` → 9 endpoints
- `/api/direct-messages` → 8
- `/api/users` → 2
- `/api/channels` → 15
- `/api/messages` (reactions) → 3
- `/api/attachments` → 5
- `/api/presence` → 12 (from `src/presence/routes/presence.routes.ts`)
- `/api/tenants` → 9
- `/api/admin` → 3

Note: `src/routes/health.routes.ts` exists, but isn’t wired in `src/routes/index.ts`; health is served directly in `src/server.ts` via `/health`.

## Services Used

### Internal service layer (`src/services`)

Key services include:

- `auth.service`
- `user.service`
- `tenant.service`
- `channel.service`
- `direct-message.service`
- `message.service`
- `message-reaction.service`
- `attachment.service`
- `file-validation.service`
- `s3.service`
- `sso-token.service`
- `unread-messages.service`

Also separate presence-domain services under `src/presence/services`, plus infra services like DB init, Redis client, logger, and service locator.

### External backing services

- MongoDB (primary data)
- Redis (presence/realtime support)
- AWS S3 (attachments/media)
- Socket.IO server for realtime events

## Multi-Tenant (Simple Explanation)

Multi-tenancy is enforced by a combination of:

- **Tenant context propagation** via `AsyncLocalStorage` in `src/plugins/tenantPlugin.ts`
- **Automatic query scoping** using `tenantIsolationPlugin` (injects `tenantId` into Mongoose queries and blocks queries without tenant context)
- **Auth middleware tenant binding** in `src/common/middlewares/auth.middleware.ts` (sets `tenantContext` from authenticated user)
- **Explicit context execution** with `runInTenantContext(...)` for services, controllers, sockets, and background jobs

In short: once a user is authenticated, tenant ID is carried in context, and DB operations are automatically constrained to that tenant.

## Middlewares In Place

Global in `src/server.ts`:

- `cors(...)` with configured origin checks
- `express.json()`
- `express.urlencoded(...)`
- `errorMiddleware` (centralized error handling)

Common middlewares in `src/common/middlewares`:

- `authMiddleware` (JWT auth + user lookup + tenant context)
- `validateRequest` (Zod request validation)
- `errorMiddleware` (maps Zod/Mongo/Redis/custom errors to responses)
- `sso_authentication.middleware` (`verifySSOToken`, SSO token validation flow)

Socket layer:

- `socketAuthMiddleware` in `src/socket/middleware/auth.middleware.ts` (JWT/SSO auth for sockets + tenant context)

If you want, I can also give you:
- a **public vs protected routes breakdown**
- a **controller-to-service dependency map**
- or a **“new developer onboarding” path** (what to read first in order).


# Frontend
Here’s a concise project overview based on the codebase.

## Stack

- **Framework:** Next.js (App Router) + React + TypeScript
- **Styling/UI:** Tailwind CSS, Radix/shadcn-style components, `next-themes`
- **State/Data:**
  - TanStack Query for server data
  - Zustand (with persist/immer) for auth/session client state
- **Forms/Validation:** React Hook Form + Zod
- **API layer:** Axios-based REST client (`NEXT_PUBLIC_API_URL`)
- **Realtime:** Socket.IO client (not native WebSocket directly)
- **Editor:** Plate.js rich text editor
- **Supabase:** not used in this frontend codebase

## How many pages/routes

It currently has **11 App Router pages** (`app/**/page.tsx`):

- `/login`
- `/register`
- `/chat`
- `/chat/new`
- `/chat/channel/[id]`
- `/chat/dm/[id]`
- `/chat/settings`
- `/chat/settings/profile`
- `/chat/settings/appearance`
- `/chat/settings/security`
- `/embed`

There are links for a few routes that don’t currently exist as pages (like mentions/starred and some settings subsections).

## Channels and Direct Messages

- The app supports both **channels** and **DMs**.
- Data model distinguishes message context with optional `channelId` vs `directMessageId`.
- **Channel flow:** channel list + channel detail page + channel message hooks.
- **DM flow:** DM list + DM detail page + “new chat” flow that can start a DM from first message.
- Sidebar and conversation list combine these into chat navigation.

## Auth flow

- Email/password **register/login** pages call custom auth hooks.
- On success, user is redirected to `/chat`.
- Auth tokens (`token` + `refreshToken`) are stored in cookies.
- Axios interceptor:
  - attaches bearer token
  - handles 401 refresh flow
  - retries queued requests after refresh
- Auth state is also persisted in Zustand for client hydration.
- Route protection uses `middleware.ts`:
  - protects `/chat*` and `/`
  - allows `/login`, `/register`, `/embed`
  - checks token existence/expiry
- There is also a custom **SSO-style token/signature flow** used by embed context.

## Realtime / WebSocket

- Realtime is implemented with **Socket.IO** (`lib/socket.ts`).
- Used for:
  - new/edit message events (channels + DMs)
  - join/leave room events
  - unread count updates
  - presence/online status updates
- Reconnect strategy exists:
  - retries on connection errors (with auth-aware handling)
  - socket reconnect is triggered after auth restore
  - presence UI shows status/retry behavior

If you want, I can also give you a **feature map by file** (which hook/component handles each specific behavior).


# Backend Folder Structure
```plaintext
.
├── cdk_chat
│   ├── bin
│   │   └── cdk_chat.ts
│   ├── cdk.context.json
│   ├── cdk.json
│   ├── jest.config.js
│   ├── lib
│   │   ├── app.ts
│   │   ├── cdk_chat-stack.ts
│   │   ├── config.ts
│   │   ├── stacks
│   │   │   └── backend-stack.ts
│   │   └── stage.ts
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   ├── test
│   │   └── cdk_chat.test.ts
│   └── tsconfig.json
├── deployment-guide.md
├── deployment.md
├── deploy.sh
├── deploy-to-ecr.sh
├── dist
│   ├── common
│   │   ├── database
│   │   │   ├── connection.js
│   │   │   ├── connection.js.map
│   │   │   ├── init.js
│   │   │   └── init.js.map
│   │   ├── environment.js
│   │   ├── environment.js.map
│   │   ├── errors
│   │   │   ├── app-errors.js
│   │   │   ├── app-errors.js.map
│   │   │   ├── base-error.js
│   │   │   ├── base-error.js.map
│   │   │   ├── constants.js
│   │   │   ├── constants.js.map
│   │   │   ├── error-handler.js
│   │   │   ├── error-handler.js.map
│   │   │   ├── index.js
│   │   │   ├── index.js.map
│   │   │   ├── mongodb-error-mapper.js
│   │   │   ├── mongodb-error-mapper.js.map
│   │   │   ├── redis-error.js
│   │   │   ├── redis-error.js.map
│   │   │   ├── types.js
│   │   │   └── types.js.map
│   │   ├── logger.js
│   │   ├── logger.js.map
│   │   ├── middlewares
│   │   │   ├── auth.middleware.js
│   │   │   ├── auth.middleware.js.map
│   │   │   ├── error.middleware.js
│   │   │   ├── error.middleware.js.map
│   │   │   ├── index.js
│   │   │   ├── index.js.map
│   │   │   ├── sso_authentication.middleware.js
│   │   │   ├── sso_authentication.middleware.js.map
│   │   │   ├── __tests__
│   │   │   │   ├── auth.middleware.test.js
│   │   │   │   └── auth.middleware.test.js.map
│   │   │   ├── validation.middleware.js
│   │   │   └── validation.middleware.js.map
│   │   ├── redis
│   │   │   ├── client.js
│   │   │   └── client.js.map
│   │   ├── service-locator.js
│   │   ├── service-locator.js.map
│   │   └── types
│   │       ├── auth.type.js
│   │       ├── auth.type.js.map
│   │       ├── index.js
│   │       ├── index.js.map
│   │       ├── socket.types.js
│   │       ├── socket.types.js.map
│   │       ├── user.types.js
│   │       └── user.types.js.map
│   ├── constants
│   │   ├── files.js
│   │   ├── files.js.map
│   │   ├── index.js
│   │   └── index.js.map
│   ├── controllers
│   │   ├── admin.controller.js
│   │   ├── admin.controller.js.map
│   │   ├── attachment.controller.js
│   │   ├── attachment.controller.js.map
│   │   ├── auth.controller.js
│   │   ├── auth.controller.js.map
│   │   ├── channel.controller.js
│   │   ├── channel.controller.js.map
│   │   ├── direct-message.controller.js
│   │   ├── direct-message.controller.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message-reaction.controller.js
│   │   ├── message-reaction.controller.js.map
│   │   ├── tenant.controller.js
│   │   ├── tenant.controller.js.map
│   │   ├── __tests__
│   │   │   ├── attachment.controller.test.js
│   │   │   ├── attachment.controller.test.js.map
│   │   │   ├── auth.controller.test.js
│   │   │   ├── auth.controller.test.js.map
│   │   │   ├── direct-message.controller.test.js
│   │   │   ├── direct-message.controller.test.js.map
│   │   │   ├── message-reaction.controller.test.js
│   │   │   ├── message-reaction.controller.test.js.map
│   │   │   ├── user.controller.test.js
│   │   │   └── user.controller.test.js.map
│   │   ├── user.controller.js
│   │   └── user.controller.js.map
│   ├── models
│   │   ├── attachment.model.js
│   │   ├── attachment.model.js.map
│   │   ├── channel-member.model.js
│   │   ├── channel-member.model.js.map
│   │   ├── channel.model.js
│   │   ├── channel.model.js.map
│   │   ├── direct-message.model.js
│   │   ├── direct-message.model.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message.model.js
│   │   ├── message.model.js.map
│   │   ├── refresh-token.model.js
│   │   ├── refresh-token.model.js.map
│   │   ├── tenant.model.js
│   │   ├── tenant.model.js.map
│   │   ├── thread.model.js
│   │   ├── thread.model.js.map
│   │   ├── user.model.js
│   │   └── user.model.js.map
│   ├── plugins
│   │   ├── tenantPlugin.js
│   │   └── tenantPlugin.js.map
│   ├── presence
│   │   ├── constants.js
│   │   ├── constants.js.map
│   │   ├── controllers
│   │   │   ├── presence.controller.js
│   │   │   └── presence.controller.js.map
│   │   ├── models
│   │   │   ├── index.js
│   │   │   ├── index.js.map
│   │   │   ├── presence-history.model.js
│   │   │   ├── presence-history.model.js.map
│   │   │   ├── user-connection.model.js
│   │   │   └── user-connection.model.js.map
│   │   ├── presence-manager.js
│   │   ├── presence-manager.js.map
│   │   ├── routes
│   │   │   ├── presence.routes.js
│   │   │   └── presence.routes.js.map
│   │   ├── services
│   │   │   ├── connection.service.js
│   │   │   ├── connection.service.js.map
│   │   │   ├── index.js
│   │   │   ├── index.js.map
│   │   │   ├── presence-history.service.js
│   │   │   └── presence-history.service.js.map
│   │   └── socket
│   │       ├── presence.handler.js
│   │       └── presence.handler.js.map
│   ├── repositories
│   │   ├── attachment.repository.js
│   │   ├── attachment.repository.js.map
│   │   ├── base.repository.js
│   │   ├── base.repository.js.map
│   │   ├── channel-member.repository.js
│   │   ├── channel-member.repository.js.map
│   │   ├── channel.repository.js
│   │   ├── channel.repository.js.map
│   │   ├── direct-message.repository.js
│   │   ├── direct-message.repository.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message.repository.js
│   │   ├── message.repository.js.map
│   │   ├── __tests__
│   │   │   ├── attachment.repository.test.js
│   │   │   └── attachment.repository.test.js.map
│   │   ├── thread.repository.js
│   │   ├── thread.repository.js.map
│   │   ├── user.repository.js
│   │   └── user.repository.js.map
│   ├── routes
│   │   ├── admin.routes.js
│   │   ├── admin.routes.js.map
│   │   ├── attachment.routes.js
│   │   ├── attachment.routes.js.map
│   │   ├── auth.routes.js
│   │   ├── auth.routes.js.map
│   │   ├── channel.routes.js
│   │   ├── channel.routes.js.map
│   │   ├── direct-message.routes.js
│   │   ├── direct-message.routes.js.map
│   │   ├── health.routes.js
│   │   ├── health.routes.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message-reaction.routes.js
│   │   ├── message-reaction.routes.js.map
│   │   ├── tenant.routes.js
│   │   ├── tenant.routes.js.map
│   │   ├── user.routes.js
│   │   └── user.routes.js.map
│   ├── scripts
│   │   ├── seed-database.js
│   │   ├── seed-database.js.map
│   │   ├── tenant-migrations.js
│   │   └── tenant-migrations.js.map
│   ├── server.js
│   ├── server.js.map
│   ├── services
│   │   ├── attachment.service.js
│   │   ├── attachment.service.js.map
│   │   ├── auth.service.js
│   │   ├── auth.service.js.map
│   │   ├── channel.service.js
│   │   ├── channel.service.js.map
│   │   ├── direct-message.service.js
│   │   ├── direct-message.service.js.map
│   │   ├── file-validation.service.js
│   │   ├── file-validation.service.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message-reaction.service.js
│   │   ├── message-reaction.service.js.map
│   │   ├── message.service.js
│   │   ├── message.service.js.map
│   │   ├── s3.service.js
│   │   ├── s3.service.js.map
│   │   ├── sso-token.service.js
│   │   ├── sso-token.service.js.map
│   │   ├── tenant.service.js
│   │   ├── tenant.service.js.map
│   │   ├── __tests__
│   │   │   ├── attachment.service.test.js
│   │   │   ├── attachment.service.test.js.map
│   │   │   ├── auth.service.test.js
│   │   │   ├── auth.service.test.js.map
│   │   │   ├── direct-message.service.test.js
│   │   │   ├── direct-message.service.test.js.map
│   │   │   ├── message-reaction.service.test.js
│   │   │   ├── message-reaction.service.test.js.map
│   │   │   ├── message.service.test.js
│   │   │   ├── message.service.test.js.map
│   │   │   ├── s3.service.test.js
│   │   │   ├── s3.service.test.js.map
│   │   │   ├── user.service.test.js
│   │   │   └── user.service.test.js.map
│   │   ├── unread-messages.service.js
│   │   ├── unread-messages.service.js.map
│   │   ├── user.service.js
│   │   ├── user.service.js.map
│   │   └── validation
│   │       ├── auth.validation.js
│   │       ├── auth.validation.js.map
│   │       ├── message.validation.js
│   │       └── message.validation.js.map
│   ├── socket
│   │   ├── attachment.handler.js
│   │   ├── attachment.handler.js.map
│   │   ├── channel.handler.js
│   │   ├── channel.handler.js.map
│   │   ├── direct-message.handler.js
│   │   ├── direct-message.handler.js.map
│   │   ├── index.js
│   │   ├── index.js.map
│   │   ├── message-reaction.handler.js
│   │   ├── message-reaction.handler.js.map
│   │   └── middleware
│   │       ├── auth.middleware.js
│   │       ├── auth.middleware.js.map
│   │       └── __tests__
│   │           ├── auth.middleware.test.js
│   │           └── auth.middleware.test.js.map
│   └── tests
│       ├── helpers
│       │   ├── attachment-test-helper.js
│       │   ├── attachment-test-helper.js.map
│       │   ├── aws-mock-helper.js
│       │   ├── aws-mock-helper.js.map
│       │   ├── performance-helper.js
│       │   ├── performance-helper.js.map
│       │   ├── test-app.js
│       │   ├── test-app.js.map
│       │   ├── test-database.js
│       │   └── test-database.js.map
│       ├── integration
│       │   ├── auth
│       │   │   ├── authentication.test.js
│       │   │   ├── authentication.test.js.map
│       │   │   ├── login.test.js
│       │   │   ├── login.test.js.map
│       │   │   ├── registration.test.js
│       │   │   └── registration.test.js.map
│       │   ├── direct-message
│       │   │   ├── direct-message.test.js
│       │   │   └── direct-message.test.js.map
│       │   ├── fixtures
│       │   │   ├── auth-fixtures.js
│       │   │   ├── auth-fixtures.js.map
│       │   │   ├── repository-fixtures.js
│       │   │   └── repository-fixtures.js.map
│       │   ├── performance
│       │   │   ├── attachment.performance.test.js
│       │   │   └── attachment.performance.test.js.map
│       │   ├── real-data
│       │   │   ├── attachment.real.test.js
│       │   │   └── attachment.real.test.js.map
│       │   ├── repositories
│       │   │   ├── base-repository.test.js
│       │   │   ├── base-repository.test.js.map
│       │   │   ├── direct-message.repository.test.js
│       │   │   ├── direct-message.repository.test.js.map
│       │   │   ├── message.repository.test.js
│       │   │   ├── message.repository.test.js.map
│       │   │   ├── user-repository.test.js
│       │   │   └── user-repository.test.js.map
│       │   ├── routes
│       │   │   ├── message-reaction.routes.test.js
│       │   │   └── message-reaction.routes.test.js.map
│       │   ├── setup.js
│       │   ├── setup.js.map
│       │   └── socket
│       │       ├── direct-message-socket.test.js
│       │       └── direct-message-socket.test.js.map
│       ├── message-reaction.handler.test.js
│       └── message-reaction.handler.test.js.map
├── docker-compose.yaml
├── docker-deploy.sh
├── Dockerfile
├── eslint.config.mjs
├── logs
│   ├── combined.log
│   └── error.log
├── package.json
├── package-lock.json
├── public
│   └── favicon.ico
├── README.md
├── scripts
│   ├── clear-logs.mjs
│   ├── migrate-phase2.ts
│   ├── open-mongo-express.mjs
│   └── test-runner.sh
├── src
│   ├── common
│   │   ├── database
│   │   │   ├── connection.ts
│   │   │   └── init.ts
│   │   ├── environment.ts
│   │   ├── errors
│   │   │   ├── app-errors.ts
│   │   │   ├── base-error.ts
│   │   │   ├── constants.ts
│   │   │   ├── error-handler.ts
│   │   │   ├── index.ts
│   │   │   ├── mongodb-error-mapper.ts
│   │   │   ├── redis-error.ts
│   │   │   └── types.ts
│   │   ├── logger.ts
│   │   ├── middlewares
│   │   │   ├── auth.middleware.ts
│   │   │   ├── error.middleware.ts
│   │   │   ├── index.ts
│   │   │   ├── sso_authentication.middleware.ts
│   │   │   ├── __tests__
│   │   │   │   └── auth.middleware.test.ts
│   │   │   └── validation.middleware.ts
│   │   ├── redis
│   │   │   └── client.ts
│   │   ├── service-locator.ts
│   │   └── types
│   │       ├── auth.type.ts
│   │       ├── index.ts
│   │       ├── socket.types.ts
│   │       └── user.types.ts
│   ├── constants
│   │   ├── files.ts
│   │   └── index.ts
│   ├── controllers
│   │   ├── admin.controller.ts
│   │   ├── attachment.controller.ts
│   │   ├── auth.controller.ts
│   │   ├── channel.controller.ts
│   │   ├── direct-message.controller.ts
│   │   ├── index.ts
│   │   ├── message-reaction.controller.ts
│   │   ├── tenant.controller.ts
│   │   ├── __tests__
│   │   │   ├── attachment.controller.test.ts
│   │   │   ├── auth.controller.test.ts
│   │   │   ├── direct-message.controller.test.ts
│   │   │   ├── message-reaction.controller.test.ts
│   │   │   └── user.controller.test.ts
│   │   └── user.controller.ts
│   ├── models
│   │   ├── attachment.model.ts
│   │   ├── channel-member.model.ts
│   │   ├── channel.model.ts
│   │   ├── direct-message.model.ts
│   │   ├── index.ts
│   │   ├── message.model.ts
│   │   ├── refresh-token.model.ts
│   │   ├── tenant.model.ts
│   │   ├── thread.model.ts
│   │   └── user.model.ts
│   ├── plugins
│   │   └── tenantPlugin.ts
│   ├── presence
│   │   ├── constants.ts
│   │   ├── controllers
│   │   │   └── presence.controller.ts
│   │   ├── models
│   │   │   ├── index.ts
│   │   │   ├── presence-history.model.ts
│   │   │   └── user-connection.model.ts
│   │   ├── presence-manager.ts
│   │   ├── routes
│   │   │   └── presence.routes.ts
│   │   ├── services
│   │   │   ├── connection.service.ts
│   │   │   ├── index.ts
│   │   │   └── presence-history.service.ts
│   │   └── socket
│   │       └── presence.handler.ts
│   ├── repositories
│   │   ├── attachment.repository.ts
│   │   ├── base.repository.ts
│   │   ├── channel-member.repository.ts
│   │   ├── channel.repository.ts
│   │   ├── direct-message.repository.ts
│   │   ├── index.ts
│   │   ├── message.repository.ts
│   │   ├── __tests__
│   │   │   └── attachment.repository.test.ts
│   │   ├── thread.repository.ts
│   │   └── user.repository.ts
│   ├── routes
│   │   ├── admin.routes.ts
│   │   ├── attachment.routes.ts
│   │   ├── auth.routes.ts
│   │   ├── channel.routes.ts
│   │   ├── direct-message.routes.ts
│   │   ├── health.routes.ts
│   │   ├── index.ts
│   │   ├── message-reaction.routes.ts
│   │   ├── tenant.routes.ts
│   │   └── user.routes.ts
│   ├── scripts
│   │   ├── seed-database.ts
│   │   └── tenant-migrations.ts
│   ├── server.ts
│   ├── services
│   │   ├── attachment.service.ts
│   │   ├── auth.service.ts
│   │   ├── channel.service.ts
│   │   ├── direct-message.service.ts
│   │   ├── file-validation.service.ts
│   │   ├── index.ts
│   │   ├── message-reaction.service.ts
│   │   ├── message.service.ts
│   │   ├── s3.service.ts
│   │   ├── sso-token.service.ts
│   │   ├── tenant.service.ts
│   │   ├── __tests__
│   │   │   ├── attachment.service.test.ts
│   │   │   ├── auth.service.test.ts
│   │   │   ├── direct-message.service.test.ts
│   │   │   ├── message-reaction.service.test.ts
│   │   │   ├── message.service.test.ts
│   │   │   ├── s3.service.test.ts
│   │   │   └── user.service.test.ts
│   │   ├── unread-messages.service.ts
│   │   ├── user.service.ts
│   │   └── validation
│   │       ├── auth.validation.ts
│   │       └── message.validation.ts
│   ├── socket
│   │   ├── attachment.handler.ts
│   │   ├── channel.handler.ts
│   │   ├── direct-message.handler.ts
│   │   ├── index.ts
│   │   ├── message-reaction.handler.ts
│   │   └── middleware
│   │       ├── auth.middleware.ts
│   │       └── __tests__
│   │           └── auth.middleware.test.ts
│   └── tests
│       ├── helpers
│       │   ├── attachment-test-helper.ts
│       │   ├── aws-mock-helper.ts
│       │   ├── performance-helper.ts
│       │   ├── test-app.ts
│       │   └── test-database.ts
│       ├── integration
│       │   ├── auth
│       │   │   ├── authentication.test.ts
│       │   │   ├── login.test.ts
│       │   │   └── registration.test.ts
│       │   ├── direct-message
│       │   │   └── direct-message.test.ts
│       │   ├── fixtures
│       │   │   ├── auth-fixtures.ts
│       │   │   └── repository-fixtures.ts
│       │   ├── performance
│       │   │   └── attachment.performance.test.ts
│       │   ├── real-data
│       │   │   └── attachment.real.test.ts
│       │   ├── repositories
│       │   │   ├── base-repository.test.ts
│       │   │   ├── direct-message.repository.test.ts
│       │   │   ├── message.repository.test.ts
│       │   │   └── user-repository.test.ts
│       │   ├── routes
│       │   │   └── message-reaction.routes.test.ts
│       │   ├── setup.ts
│       │   └── socket
│       │       └── direct-message-socket.test.ts
│       └── message-reaction.handler.test.ts
├── tsconfig.json
└── vitest.config.ts

89 directories, 439 files
```


# Frontend folder structure
```bash
.
├── app
│   ├── (auth)
│   │   ├── layout.tsx
│   │   ├── login
│   │   │   └── page.tsx
│   │   └── register
│   │       └── page.tsx
│   ├── chat
│   │   ├── channel
│   │   │   └── [id]
│   │   │       └── page.tsx
│   │   ├── dm
│   │   │   └── [id]
│   │   │       └── page.tsx
│   │   ├── layout.tsx
│   │   ├── new
│   │   │   └── page.tsx
│   │   ├── page.tsx
│   │   └── settings
│   │       ├── appearance
│   │       │   └── page.tsx
│   │       ├── layout.tsx
│   │       ├── page.tsx
│   │       ├── profile
│   │       │   └── page.tsx
│   │       └── security
│   │           ├── page.tsx
│   │           └── securitySettingsPage.tsx
│   ├── embed
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── error.tsx
│   ├── favicon.ico
│   ├── globals.css
│   ├── layout.tsx
│   └── not-found.tsx
├── components
│   ├── api-error.tsx
│   ├── chat
│   │   ├── AttachmentDisplay.tsx
│   │   ├── AttachmentPreview.tsx
│   │   ├── ChannelList.tsx
│   │   ├── ChannelMembersDrawer.tsx
│   │   ├── ChannelWindow.tsx
│   │   ├── ChatDashboard.tsx
│   │   ├── ChatMessage.tsx
│   │   ├── ChatSidebar.tsx
│   │   ├── ChatWindow.tsx
│   │   ├── ConversationList.tsx
│   │   ├── CreateChannelDialog.tsx
│   │   ├── DirectMessageList.tsx
│   │   ├── EmptyState.tsx
│   │   ├── FileUploadDropzone.tsx
│   │   ├── MediaViewer.tsx
│   │   ├── MessageDate.tsx
│   │   ├── MessageReactionMenu.tsx
│   │   ├── MessageReactions.tsx
│   │   ├── RichTextEditor.tsx
│   │   ├── RichTextRenderer.tsx
│   │   ├── TopBar.tsx
│   │   └── UnreadBadge.tsx
│   ├── DocumentTitleUpdater.tsx
│   ├── editor
│   │   ├── editor-kit.tsx
│   │   ├── plugins
│   │   │   ├── basic-blocks-base-kit.tsx
│   │   │   ├── basic-blocks-kit.tsx
│   │   │   ├── basic-marks-base-kit.tsx
│   │   │   ├── basic-marks-kit.tsx
│   │   │   ├── code-block-base-kit.tsx
│   │   │   ├── code-block-kit.tsx
│   │   │   └── fixed-toolbar-kit.tsx
│   │   └── renderer-kit.tsx
│   ├── error-boundary.tsx
│   ├── NavUser.tsx
│   ├── PasswordStrengthMeter.tsx
│   ├── presence
│   │   ├── ConnectionStatus.tsx
│   │   ├── index.ts
│   │   ├── OnlineUsersList.tsx
│   │   ├── PresenceAwareAvatar.tsx
│   │   ├── PresenceIndicator.tsx
│   │   ├── StatusSelector.tsx
│   │   └── UserActivityStatus.tsx
│   ├── SessionExpiredAlert.tsx
│   ├── sessionManagement.tsx
│   ├── theme-toggle.tsx
│   └── ui
│       ├── alert-dialog.tsx
│       ├── alert.tsx
│       ├── avatar.tsx
│       ├── badge.tsx
│       ├── blockquote-node-static.tsx
│       ├── blockquote-node.tsx
│       ├── button.tsx
│       ├── card.tsx
│       ├── checkbox.tsx
│       ├── code-block-node-static.tsx
│       ├── code-block-node.tsx
│       ├── code-node-static.tsx
│       ├── code-node.tsx
│       ├── command.tsx
│       ├── dialog.tsx
│       ├── dropdown-menu.tsx
│       ├── editor-static.tsx
│       ├── editor.tsx
│       ├── fixed-toolbar-buttons.tsx
│       ├── fixed-toolbar.tsx
│       ├── form.tsx
│       ├── heading-node-static.tsx
│       ├── heading-node.tsx
│       ├── highlight-node-static.tsx
│       ├── highlight-node.tsx
│       ├── hr-node-static.tsx
│       ├── hr-node.tsx
│       ├── input.tsx
│       ├── kbd-node-static.tsx
│       ├── kbd-node.tsx
│       ├── label.tsx
│       ├── mark-toolbar-button.tsx
│       ├── multi-select.tsx
│       ├── paragraph-node-static.tsx
│       ├── paragraph-node.tsx
│       ├── popover.tsx
│       ├── progress.tsx
│       ├── scroll-area.tsx
│       ├── select.tsx
│       ├── separator.tsx
│       ├── sheet.tsx
│       ├── skeleton.tsx
│       ├── slider.tsx
│       ├── sonner.tsx
│       ├── switch.tsx
│       ├── tabs.tsx
│       ├── textarea.tsx
│       ├── toolbar.tsx
│       └── tooltip.tsx
├── components.json
├── contexts
│   └── ReactionContext.tsx
├── eslint.config.mjs
├── hooks
│   ├── use-async.ts
│   ├── use-attachments.ts
│   ├── use-auth-persistence.ts
│   ├── use-auth.ts
│   ├── use-channels.ts
│   ├── use-chat.ts
│   ├── use-direct-message-users.ts
│   ├── use-file-upload.ts
│   ├── use-hydration.ts
│   ├── use-message-editing.ts
│   ├── use-message-reaction.ts
│   ├── use-messenger-integration.ts
│   ├── use-presence-indicator.ts
│   ├── use-presence.ts
│   ├── use-reaction.ts
│   ├── use-refresh-token.ts
│   ├── use-sso-auth.ts
│   └── use-unread.ts
├── lib
│   ├── api.ts
│   ├── attachment.service.ts
│   ├── errors
│   │   ├── base-error.ts
│   │   ├── error-classes.ts
│   │   ├── factory.ts
│   │   ├── index.ts
│   │   ├── toast-error-handler.ts
│   │   └── types.ts
│   ├── file-upload.service.ts
│   ├── presence-api.ts
│   ├── socket.ts
│   ├── utils.ts
│   └── validators.ts
├── middleware.ts
├── next.config.ts
├── next-env.d.ts
├── package.json
├── package-lock.json
├── postcss.config.mjs
├── providers
│   ├── auth-proivder.tsx
│   ├── chat-messenger-provider.tsx
│   ├── error-providers.tsx
│   ├── presence-provider.tsx
│   ├── query-provider.tsx
│   ├── socket-provider.tsx
│   └── theme-provider.tsx
├── public
│   ├── file.svg
│   ├── globe.svg
│   ├── next.svg
│   ├── vercel.svg
│   └── window.svg
├── README.md
├── store
│   └── auth-store.ts
├── tsconfig.json
├── types
│   ├── attachment.ts
│   ├── chat.ts
│   ├── presence.ts
│   ├── tenant.ts
│   └── user.ts
└── utils
    ├── ChatAppMessenger.ts
    ├── constants
    │   ├── debug.ts
    │   └── file.ts
    ├── date-utils.ts
    ├── passwordStrength.ts
    └── rich-text.ts

32 directories, 182 files
```