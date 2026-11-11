---
id: modern-web-guidance.platform.sanitize-untrusted-html
title: Sanitize Untrusted HTML at the Insertion Boundary
stage: implementation
severity: critical
applies_when: displaying untrusted text or rich HTML from users, external services, or generated content
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.raw-untrusted-html
    name: Inserting untrusted HTML directly
    severity: critical
    description: Untrusted markup is assigned to an HTML parsing sink without effective sanitization.
---

Choose the rendering boundary before choosing an API. For text, use `textContent` or the framework's escaped text rendering. Only parse HTML when the product actually needs markup; for example, a comment preview that permits bold and links needs a restrictive allowlist, not raw `innerHTML`.

For rich HTML, sanitize at the insertion boundary with `Element.setHTML()` where supported, or a maintained sanitizer such as DOMPurify where it is not. Define allowed elements, attributes and URL schemes for the use case; align native and fallback policies rather than assuming their defaults match. Never use raw untrusted HTML as the fallback. If Trusted Types are enforced, configure the fallback to return trusted output under an allowed policy.

If separately parsing sanitized HTML, move the resulting nodes into the document instead of serializing and reparsing them, which can reintroduce mutation XSS. Check representative legitimate and malicious inputs in each supported path. Client-side sanitization protects only that rendering context: also protect server-rendered pages, email and other consumers. It does not replace authorization.

Source: [Sanitizing Untrusted HTML](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/sanitize-untrusted-html.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
