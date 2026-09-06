# Hybrid OAuth — Architecture Diagram

Interactive companion to the ["Hybrid OAuth Coexistence"](https://claude.ai/code/artifact/e5c607f8-405c-4816-9991-f4205124e960) report. Covers `HCC/Identity-provider-shared-infra` (shared Keycloak/AWS Cognito identity provider) and `whatsnextplease-monolith` (the app with legacy JWT auth plus the hybrid integration layer added in January 2026).

Open `hybrid-oauth-architecture.html` in a browser. Click a flow tab, then step through with the player controls (or `←`/`→`, `Space` to autoplay). Click any node to jump to the first step it appears in. Toggle **Keycloak** vs **AWS Cognito** with the provider switch (or press `O`) to see how the same flow shape hits a different concrete admin API / token endpoint.

## Components

| Node | Role | What it is |
|---|---|---|
| **Browser** | Client | Next.js frontend (`apps/web`) — the sign-in/sign-up forms and the edge middleware that later decodes a token's role claim (no signature check — that already happened on the backend) |
| **WNP Backend API** | Orchestrator | Express backend (`apps/backend`) — `AuthService` (signin/signup/refreshToken) and `hybrid-auth.middleware.ts` (`verifyTokenHybrid`), the two places all of this logic lives |
| **auth-client** | Token verification | `@HillCountryCoder/auth-client` — one `IAuthService` interface, two implementations: `KeycloakAuthService` (JWKS fetch + RS256 verify) and `CognitoAuthService` (`aws-jwt-verify`). Picked by the `AUTH_PROVIDER` env var via `factory.ts` |
| **IDP admin + token exchange** | Provisioning | `apps/backend/api/services/idp/` — `CognitoAdminService` / `KeycloakAdminService` (create/delete IdP users) plus `TokenExchangeService` (trades a username/password for a real IdP token) |
| **Postgres** | Datastore | `User` / `Client` tables via Prisma — `passwordHash` (now optional) and `cognitoSub` (unique, nullable) are the two columns that make hybrid auth possible |
| **Identity Provider** | External system | Local Keycloak (Docker Compose, realm `hcc-wnp`) in development, or a shared AWS Cognito User Pool (also used by the sibling HCC product) in staging/production |

## Flows

### 1 — Sign-in · unmigrated user (10 steps)
The auto-migration path. A user whose `cognitoSub` is still `NULL` logs in with their existing password; the backend verifies it the old way, then transparently creates the same user in the IdP, stamps `cognitoSub` onto their row inside a Prisma transaction, and exchanges their credentials for a real IdP token — so their very next login (and the response to *this* one) already looks fully migrated. If any IdP step fails, the whole request falls back to a locally-signed 12-hour HS256 JWT instead of failing the login.

### 2 — Sign-in · migrated user (6 steps)
The steady-state path once `cognitoSub` is set: password check against Postgres, then a direct token exchange with the IdP — no admin API call needed. Same legacy-JWT fallback exists if the IdP call fails.

### 3 — Verify request · IdP token (6 steps)
What `verifyTokenHybrid` does on (almost) every protected route: hand the bearer token to `auth-client`, which fetches Keycloak's JWKS (or lets Cognito's SDK verify it), reads the `groups` claim to decide User-vs-Client, and looks the row up by `cognitoSub`.

### 4 — Verify request · legacy fallback (5 steps)
The same middleware, but the IdP validation fails (wrong signing algorithm, token not IdP-issued, or the IdP is simply down) and it falls through to `jwt.verify(token, SECRET)` — HS256, looked up by Postgres primary key instead of `cognitoSub`. Notice which nodes stay dimmed here: **auth-client** and the **external IdP** never get a wire at all in this flow — that's the point. The fallback is fully self-contained.

### 5 — Sign-up · IdP-first (8 steps)
New accounts are never legacy-only. The IdP user is created *first*; the database row is created second, already populated with `cognitoSub`. If the database write fails, the code compensates with `idpAdmin.deleteUser()` to avoid an orphaned IdP account — a best-effort rollback, not a true distributed transaction (a hard crash between the two writes is a known, documented gap).

## Provider mode differences (Keycloak vs Cognito)

| | Keycloak (local dev) | AWS Cognito (staging/prod) |
|---|---|---|
| Verification | JWKS fetch by `kid`, hand-rolled RS256 verify, `azp` claim checked instead of `aud` (audience validation is disabled by default for Keycloak) | `aws-jwt-verify`'s `CognitoJwtVerifier`, tries access token then ID token |
| Admin API | REST calls to the realm admin API (`PUT /admin/realms/hcc-wnp/users`) | AWS SDK commands (`AdminCreateUserCommand`, `AdminAddUserToGroupCommand`) |
| Token endpoint | `POST /realms/hcc-wnp/protocol/openid-connect/token`, `grant_type=password` | `InitiateAuthCommand` with `AuthFlow: USER_PASSWORD_AUTH` |
| Where it runs | Docker Compose container, every developer's machine | One shared User Pool, also used by the sibling HCC product |

## Talking points for a walkthrough

- Toggle to **flow 4** first and ask: "which nodes never light up here?" — it's the clearest way to show that the legacy fallback bypasses the IdP entirely rather than degrading through it.
- Compare **flow 1** vs **flow 2** side by side: the only structural difference is whether the "create user in IdP" hop happens at all — everything after it (token exchange, response) is identical.
- Switch the provider toggle mid-flow on **flow 3** to show that the *shape* of verification never changes — only the concrete protocol call to the identity provider does.
