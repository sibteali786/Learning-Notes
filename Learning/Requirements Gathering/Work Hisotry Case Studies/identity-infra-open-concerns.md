# Identity Infrastructure — Open Concerns & "Why Not Yet"

Honest gaps in the identity-provider-shared-infra system, framed for interview use. Each one is real, not hidden — the goal is to have a ready, credible answer rather than get caught flat-footed.

---

## 1. No token expiry hardening
**Concern:** Neither Cognito nor Keycloak has custom token lifetimes configured — both run on platform defaults (Cognito: 1hr access/ID, 30d refresh; Keycloak: 5min access, 30min SSO session idle).

**Why not yet:** This is an internal tool with a small, known user base (WNP + HCC Admin staff/clients), not a public-facing consumer product — the risk profile of a leaked long-lived token is lower than it would be at scale, and platform defaults are reasonable, vendor-tested starting points rather than arbitrary. It wasn't prioritized because nothing has surfaced a concrete incident tied to token lifetime.

**What I'd do next:** Set explicit, shorter access-token lifetimes with silent refresh, especially for the Cognito WNP client which supports direct password/SRP grants (higher exposure than pure hosted-UI redirect flows).

---

## 2. No brute-force protection / account lockout
**Concern:** Cognito's `AdvancedSecurityMode` (risk-based adaptive auth) isn't enabled; Keycloak's realm export has no `bruteForceProtected` flag set.

**Why not yet:** Same reasoning as above — small, largely known user base, not internet-facing signup at scale. Both platforms support this as a native toggle, so it's a config change away, not a build project — it was simply never turned on because it hasn't been needed yet, not because it's hard.

**What I'd do next:** Enable `bruteForceProtected` on Keycloak and Cognito's `AdvancedSecurityMode` — low effort, meaningful defense-in-depth, worth doing regardless of current risk level.

---

## 3. No Secrets Manager / SSM — plain env vars for runtime config
**Concern:** `COGNITO_USER_POOL_ID`, `COGNITO_CLIENT_ID`, `COGNITO_DOMAIN`, `KEYCLOAK_URL/REALM/CLIENT_ID` are all plain environment variables, no secret-store indirection.

**Why not yet:** None of these values are actually secret — they're public-facing OAuth configuration (pool IDs, client IDs, domains are visible in browser network requests during login anyway). There's no client secret in this system at all (see #5), so there's genuinely nothing sensitive being passed via env vars here. Using Secrets Manager for non-secret config would add operational overhead without a real security benefit.

**What I'd do next:** No change needed for current values. If a future integration introduces an actual secret (API key, service credential), that's the trigger to add Secrets Manager — not before.

---

## 4. No CI/CD for CDK deploys — fully manual
**Concern:** `cdk deploy --context environment=staging/production` is run by hand; no pipeline, no approval gate, no drift detection.

**Why not yet:** Identity infrastructure changes are infrequent and deliberately high-stakes — a manual deploy step is arguably a *feature* here, not a gap: it forces a human to consciously trigger changes to shared auth infra that both apps depend on, rather than an automated pipeline pushing IdP changes on every merge. This wasn't an oversight so much as an implicit "don't automate the scary part yet" choice.

**What I'd do next:** If deploy frequency increases, add a pipeline with a required manual approval step (not full automation) — preserves the "human in the loop" property while removing manual CLI-command risk (wrong context flag, wrong AWS profile, etc.).

---

## 5. No client secret on any OAuth client
**Concern:** All four clients (WNP/HCC × Keycloak/Cognito) are public clients with no secret — nothing beyond the redirect-URI allow-list protects client identity, and there's no client-credentials/service-account flow.

**Why not yet:** This is correct behavior, not a gap — all four clients are browser-based SPA/SSR apps using the authorization-code flow, which is exactly the case public clients (no secret) are designed for. Adding a secret to a browser-exposed client would provide false security (the secret would be extractable from client-side code) while adding complexity.

**What I'd do next:** No change needed unless a server-to-server integration is added later, at which point a dedicated client-credentials client (with a real secret, never exposed to a browser) would be the right addition — not retrofitting a secret onto the existing public clients.

---

## 6. Cognito role mapping incomplete relative to Keycloak
**Concern:** Keycloak has an explicit protocol mapper wiring `wnp_role` into ID/access tokens on every client. Cognito has the custom attribute defined on the User Pool, but no Pre-Token-Generation Lambda or equivalent explicit mapper — the claim isn't being actively set/read the same way.

**Why not yet:** This is a genuine, currently-open inconsistency between the two IdP implementations — not a deliberate design choice, unlike most items above. Likely explanation: `wnp_role` was built out Keycloak-first (matches the audience-bug investigation timeline, which was also Keycloak-specific) and the Cognito equivalent wasn't finished in the same pass.

**What I'd do next:** Add a Pre-Token-Generation Lambda trigger on the Cognito User Pool to mirror the Keycloak protocol mapper behavior — this is the one item on this list that's an actual to-do, not an accepted tradeoff. Worth being upfront about this distinction in an interview: five of these six are deliberate risk-based decisions, this one is unfinished work.

---

## 7. Staging Cognito still whitelists `localhost` callback URLs
**Concern:** The staging Cognito pool's redirect-URI allow-list includes `localhost:3000`/`localhost:3001` alongside real staging domains — broadens the trusted-redirect surface of a pool used by real (if staging) users.

**Why not yet:** Practical convenience — lets developers point local dev builds at staging Cognito without needing a second, throwaway Cognito pool just for that purpose. Staging environments generally carry a lower bar than production (which correctly has no `localhost` entries).

**What I'd do next:** If staging ever holds anything resembling real user data (not just test accounts), tighten this — but as long as staging is purely synthetic test data, the convenience trade is reasonable.

---

## Summary framing for interviews
Of these seven, **six are deliberate, risk-calibrated decisions** appropriate for an internal tool at its current scale — not oversights. **One (#6, Cognito role mapping)** is genuinely unfinished work. Being able to draw that distinction clearly — knowing which gaps are accepted tradeoffs versus which are actual to-dos — is itself the point of this document.
