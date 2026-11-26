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

## Decide what can be pinned

First decide whether the page needs the third-party resource: a script runs with the page's privileges. SRI checks that fetched bytes match an expected digest; it does not establish that those bytes are benign, isolate the script, or verify resources it subsequently loads. Review the publisher and release independently, and use CSP and isolation for their distinct purposes.

When a third-party script or stylesheet can be served at an immutable version-pinned or content-addressed URL, use SRI where supported by the project's target browsers and security requirements. Obtain the publisher's authenticated digest, or verify the release through a trusted independent channel and hash the known-good local file at release time:

```sh
printf 'sha384-%s\n' "$(openssl dgst -sha384 -binary app.min.js | openssl base64 -A)"
```

Hashing whatever the CDN returns at runtime against itself is not verification. Copy the authenticated or independently calculated digest into the HTML alongside the exact pinned URL; this template applies to an anonymous public CDN whose CORS response permits the requesting origin:

```html
<script src="https://cdn.example.com/ui@2.4.0/app.min.js"
        integrity="sha384-REPLACE-WITH-VERIFIED-RELEASE-DIGEST"
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

Replace the template digest with the actual digest before deployment; the placeholder intentionally cannot validate an asset. Apply integrity metadata to an external `<link rel="stylesheet">` when using SRI and ensure relevant preloads use matching URL, CORS mode and integrity metadata. Anonymous cross-origin SRI requires a CORS-readable response, such as `Access-Control-Allow-Origin: *`; credentialed assets need a matching origin and credentials-enabled CORS instead. Choose a document-level referrer policy for requests without a per-element policy, and adjust the example's `no-referrer` to the project's privacy and integration needs. For a legitimate set of known byte variants, list their independently verified same-algorithm digests separated by spaces; any matching digest of the strongest listed algorithm is accepted.

## Deploy and diagnose without bypassing integrity

When using SRI, update URL and digest together. In supported target browsers, check that the verified release loads and the expected script behavior or stylesheet appears. In a controlled test, substitute an incorrect valid digest and confirm the script does not execute or the stylesheet is not applied; for cross-origin resources, also check that missing or incorrect CORS headers block the load. Distinguish hash mismatch, CORS, CDN failure and CSP blocking before remediation. A CDN transformation, changed bytes, cache or stale HTML can cause a mismatch: investigate the actual release and deploy a verified URL/digest pair, or roll back both. Never remove `integrity` or dynamically trust the failed response merely to restore service.

SRI on a stylesheet does not verify its `@import`, fonts or images. Prefer a pinned HTML stylesheet link over `@import` when cross-browser stylesheet SRI is required. CSS `url()` integrity modifiers have narrower browser support; check actual target support and test mismatch blocking. A plain URL fallback may retain functionality but is **unverified**, and an unverified font in the same `src` list can load after the verified source fails. If integrity is mandatory in unsupported browsers, do not load that external resource there; use a controlled alternative instead. For mutable vendor tags, prefer a pinned alternative; otherwise explicitly assess the risk and isolate or restrict the integration with sandboxing and CSP, without presenting those controls as equivalent to byte integrity.

Source: [Secure external subresources with Subresource Integrity, CORS, and Referrer Policy](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/secure-external-subresources.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
