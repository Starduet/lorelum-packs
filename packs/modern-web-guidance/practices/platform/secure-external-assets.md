---
id: modern-web-guidance.platform.secure-external-assets
title: Pin and Verify External Script and Stylesheet Bytes
stage: implementation
severity: critical
applies_when: a page loads an immutable third-party script or stylesheet across origins
tech_stack:
  - html
  - web
anti_patterns:
  - id: modern-web-guidance.platform.unverified-third-party-asset
    name: Loading an unverified third-party asset
    severity: critical
    description: A mutable CDN URL executes third-party bytes without an independently obtained integrity digest.
---

Pin external scripts and stylesheets to immutable versioned URLs and generate a Subresource Integrity digest from known-good local bytes at build or release time, or use the publisher's trusted digest. Put the digest in `integrity`, choose `crossorigin="anonymous"` for public assets and require the CDN to return a suitable CORS header. Set a deliberate referrer policy, such as `no-referrer` for a third-party asset. A mismatch blocks the resource; update the pinned URL and digest together when upgrading.

Computing the expected hash from the same live response being verified provides no independent protection. CSP and integrity protect different boundaries: an allowed script is not made safe by an origin allowlist alone, and SRI does not replace CSP. If a vendor insists on mutable bytes, SRI cannot pin that resource; prefer a pinned alternative or assess isolation and CSP rather than claiming equivalent integrity protection.

HTML script and stylesheet SRI is broadly supported in the upstream snapshot. CSS `url()` integrity modifiers have much narrower support; a plain-URL fallback is unverified, so do not claim cross-browser integrity for it. Where verification is mandatory, prefer an integrity-protected HTML stylesheet link or a trusted same-origin asset delivery strategy. Verify browser and CDN behavior for the deployed targets.

Source: [Secure external subresources with Subresource Integrity, CORS, and Referrer Policy](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/secure-external-subresources.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
