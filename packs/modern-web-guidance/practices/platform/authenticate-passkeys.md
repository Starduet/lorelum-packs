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

## Establish the trust boundary

This is a returning-user flow; it assumes registration has already associated each credential ID, public key, user handle and relevant authenticator state with an account. Use HTTPS, a configured RP ID valid for the calling origin, and a vetted WebAuthn server library. Do not construct the expected origin or RP ID from request headers or client input. Registration and account recovery need separate verification and threat models.

For each attempt, the options endpoint creates a fresh, high-entropy random challenge and stores it, an expiry, and the requested user-verification (UV) policy in the server-side pre-authentication session. Return the challenge encoded as base64url and the configured `rpId`. For username-free sign-in, `allowCredentials: []` requests discoverable credentials; an account-specific flow instead restricts credentials to those registered to that account. Choose UV according to the account, product and security requirements: `"preferred"` permits an assertion without UV, while `"required"` requires local user verification, such as a PIN or biometric. Persist the requested policy rather than trusting a value returned by the browser. For a username-free request, the account may not yet be known: request `"required"` at that entry point, or after resolving the credential enforce the stricter of the saved request policy and the account's current server-side UV requirement. If that account requires UV and the assertion lacks it, reject and start a fresh required-UV attempt; do not create a session.

The verification endpoint must reject missing, expired, reused or mismatched challenges and atomically consume the attempt so an assertion cannot be replayed. Resolve the returned credential ID against registered credentials, check its account association and, when supplied, the user handle against that account. With the stored public key and authenticator state, have the library verify the signature, challenge, expected origin, RP ID hash, user presence, and UV against the saved request policy and current account requirement. A policy strengthened while the request was pending must be enforced before session issuance; reject and retry if it cannot be met. Apply the library's signature-counter and backup-state guidance; a counter anomaly needs a risk decision, not an assumption that every synced passkey has a strictly increasing counter. Establish or rotate the authenticated session only after all checks succeed. Unknown credentials, invalid assertions, expired attempts and server errors must not create a session.

## Choose interaction paths

An explicitly labelled “Sign in with passkey” button can start `navigator.credentials.get({ publicKey })`. If the product offers conditional mediation, annotate the username input `autocomplete="username webauthn"`, feature-detect the capability and start a conditional request with an `AbortController`. Abort that request before opening an explicit prompt, then rearm it with a **new server attempt** after cancellation if the form remains active. Use the library or supported `PublicKeyCredential.parseRequestOptionsFromJSON()` and `credential.toJSON()` to convert binary fields; serialization helpers do not add authenticator support.

Treat `NotAllowedError` as cancellation or timeout, and `AbortError` as programmatic cancellation; show actionable feedback for unexpected WebAuthn, network and verification errors. If the server deliberately exposes an unknown-credential response, consider its account-enumeration implications. Only on that explicit response, while unauthenticated, optionally call the feature-detected `PublicKeyCredential.signalUnknownCredential({ rpId: publicKey.rpId, credentialId: encoded.id })`: use the server-provided RP ID and base64url ID, not the page hostname or `rawId`. A network failure or generic verification failure must not trigger the signal.

## Verify and stop

Exercise each offered sign-in path and check that the authenticated session belongs to the registered credential's account. Independently try a wrong origin or RP ID, altered signature, unknown credential, mismatched user handle, expired or replayed challenge, and a UV-less assertion when UV was required: each must leave the client unauthenticated. If username-free requests can use preferred UV while some accounts require UV, test that a UV-less assertion for such an account is rejected; likewise test a requirement strengthened while a request is pending if policy can change. Test cancellation, absent optional APIs and a failed verification request; when offering both conditional and button requests, also test overlap. Keep another sign-in or recovery path for unsupported browsers, unavailable authenticators and users without passkeys; never downgrade a required UV policy to make a failed attempt succeed.

Sources: [Passkey Authentication](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/passkey-authentication.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`; [WebAuthn assertion verification](https://www.w3.org/TR/webauthn-3/#sctn-verifying-assertion).
