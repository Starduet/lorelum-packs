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

Use a vetted WebAuthn server library. Generate a fresh cryptographically random challenge and save it and the requested user-verification policy in the server session. Set the configured relying-party ID in request options; for a discoverable-credential flow, an empty `allowCredentials` allows account selection. Verify the returned assertion against the stored challenge, expected origin and RP ID, credential public key, and stored verification requirement before establishing a session. Do not let the client relax the server's requested verification policy.

Offer a passkey button and, when supported, conditional mediation on an input annotated with `autocomplete="username webauthn"`. Abort a pending conditional request before starting the explicit prompt and restore it as appropriate afterward. Handle cancellation separately from verification or network errors. Keep another permitted sign-in or recovery path for unsupported devices and users without a usable passkey; a serialization polyfill cannot create authenticator support.

If using `signalUnknownCredential`, feature-detect it and call only for an unauthenticated user after the server explicitly identifies an unknown credential. Pass the server-provided RP ID and base64url credential ID, not a hostname-derived RP ID or raw buffer. Signaling support is limited in the source snapshot and omission must not block sign-in. Consider account-enumeration implications of endpoint error responses in the actual product threat model.

Source: [Passkey Authentication](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/passkey-authentication.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
