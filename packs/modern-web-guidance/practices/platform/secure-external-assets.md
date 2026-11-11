---
id: modern-web-guidance.platform.secure-external-assets
title: Pin and Verify External Script and Stylesheet Bytes
stage: implementation
severity: critical
applies_when: adding or upgrading a third-party script or stylesheet loaded directly by a page
tech_stack:
  - html
  - web
anti_patterns:
  - id: modern-web-guidance.platform.unverified-third-party-asset
    name: Loading an unverified third-party asset
    severity: critical
    description: A mutable CDN URL executes third-party bytes without an independently obtained integrity digest.
---

First decide whether the page needs the third-party code at all: a script executes with the page's privileges. For a public, version-pinned CDN script or stylesheet whose bytes are known in advance, add an `integrity` digest generated from known-good release bytes or obtained independently from the publisher. Use `crossorigin="anonymous"` and ensure the CDN serves a matching CORS header; update the URL and digest together. Choose a referrer policy appropriate to the third party.

For example, when upgrading a pinned library, generate its new digest from the verified release, deploy it with the new URL, and check that the resource loads with CORS and that a mismatched digest is blocked. Hashing the live response against itself does not establish trust.

SRI verifies bytes, not whether the verified code is trustworthy; CSP and isolation address different risks. A mutable vendor tag cannot be pinned this way: prefer a pinned alternative or explicitly assess isolation and CSP rather than claiming equivalent integrity. CSS `url()` integrity support is narrower than HTML script and stylesheet SRI; an unverified fallback does not enforce integrity.

Source: [Secure external subresources with Subresource Integrity, CORS, and Referrer Policy](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/secure-external-subresources.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
