---
id: modern-web-guidance.platform.authenticate-passkeys
title: Verify Passkey Assertions on the Server
stage: implementation
severity: critical
applies_when: implementing returning-user passkey sign-in with WebAuthn
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.trust-client-passkey-result
    name: Trusting an unverified passkey assertion
    severity: critical
    description: A client-reported credential or verification preference is accepted as proof of authentication without server verification.
---

Use a vetted WebAuthn server library. For each sign-in, generate a fresh cryptographically random challenge and store it with the requested user-verification policy in the server session. Before establishing a session, verify the assertion against that challenge, the expected origin and configured relying-party ID, the registered credential public key, and the stored verification requirement. The client must not be able to weaken that requirement.

For a username-free flow, an empty `allowCredentials` requests discoverable credentials. Offer an explicit passkey button and, where supported, conditional mediation on an input annotated `autocomplete="username webauthn"`. Abort a pending conditional request before starting an explicit prompt; rearm it when appropriate. Distinguish expected cancellation from verification or network failures.

Keep an appropriate sign-in or recovery path for users without a usable passkey or supported authenticator. Feature detection or a serialization polyfill cannot create authenticator support. This guidance covers returning-user authentication; registration and recovery require their own server-side verification and threat model.

Source: [Passkey Authentication](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/passkey-authentication.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
