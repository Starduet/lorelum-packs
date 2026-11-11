---
id: modern-web-guidance.platform.sanitize-untrusted-html
title: Sanitize Untrusted HTML at the Insertion Boundary
stage: implementation
severity: critical
applies_when: a page must display user-supplied or model-generated markup
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.raw-untrusted-html
    name: Inserting untrusted HTML directly
    severity: critical
    description: Untrusted markup is assigned to an HTML parsing sink without effective sanitization.
---

If markup is not required, insert untrusted content with `textContent`. If limited markup is required, use `element.setHTML()` with an appropriately restrictive sanitizer when supported; it parses, sanitizes, and inserts in context. Feature-detect `Element.prototype.setHTML` and use a maintained sanitizer such as DOMPurify on unsupported browsers, configured to enforce the same allowed elements and attributes. Never fall back to raw `innerHTML`.

Native and library defaults differ: for example DOMPurify normally preserves content of removed elements and allows `aria-*` and `data-*`, while the upstream native example does not. Deliberately align the policies, including treatment of removed wrappers, and check representative malicious and legitimate inputs. With a Trusted Types enforcing CSP, the fallback HTML sink needs an allowed Trusted Types policy and trusted output; native `setHTML()` does not require such a policy. If parsing separately with `Document.parseHTML()`, move sanitized nodes into the document rather than serializing and reparsing them, which can reintroduce mutation XSS.

Client sanitization protects that rendering context only. Apply suitable server-side sanitization for content also rendered in server pages, other clients, or email, and keep policies consistent. Neither a sanitizer nor client checks replace authorization. Support for the native Sanitizer API is limited in the source snapshot, including no Safari support; do not assume presence from browser branding.

Source: [Sanitizing Untrusted HTML](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/sanitize-untrusted-html.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
