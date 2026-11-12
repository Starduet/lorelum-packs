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

## Choose the boundary and policy

Treat user input, external service responses and generated content as untrusted even if stored in your database. For plain text, use `textContent` or the framework's escaped text rendering. Parse HTML only when the product needs markup; choose allowed elements, attributes and URL schemes for that particular display context. Sanitization is not authorization and does not make a string safe for JavaScript, CSS or a different HTML context.

The example below is deliberately limited to paragraphs and emphasis, with **no links, images, attributes, CSS, SVG or forms**. If the product needs links, specify and test an appropriate URL scheme and attribute policy separately; do not infer that this policy covers them. Native `setHTML()` performs context-aware parsing, sanitization and insertion. A maintained fallback must enforce the same intended policy; its defaults are not interchangeable with native defaults.

```js
let purifier;
async function renderComment(element, untrustedHTML) {
  const elements = ['p', 'b', 'i', 'strong', 'em'];
  if ('setHTML' in Element.prototype) {
    element.setHTML(untrustedHTML, {
      sanitizer: { elements, attributes: [] },
    });
    return;
  }

  purifier ??= import('dompurify').then(m => m.default ?? m);
  const DOMPurify = await purifier;
  element.innerHTML = DOMPurify.sanitize(untrustedHTML, {
    ALLOWED_TAGS: [...elements, '#text'],
    ALLOWED_ATTR: [],
    ALLOW_ARIA_ATTR: false,
    ALLOW_DATA_ATTR: false,
    KEEP_CONTENT: false,
    RETURN_TRUSTED_TYPE: true,
  });
}
```

This assumes a browser application with a bundler resolving a maintained DOMPurify dependency. Under Trusted Types enforcement, allow the DOMPurify policy name in the `trusted-types` CSP and use trusted output as shown; verify compatibility with the installed version and existing policy configuration. If import, policy creation or sanitization fails, leave the content unrendered or show it via `textContent`, never assign the original HTML. Consider request ordering if multiple asynchronous renders target the same element.

Native restricted configurations remove disallowed elements **and their contents**; DOMPurify normally preserves content and permits `data-*` and `aria-*`, hence the explicit fallback options. Native `replaceWithChildrenElements` has no direct equivalent in this fallback; do not add it and assume matching behavior. Neither the configuration nor the fallback should be relaxed to preserve unsafe content. Avoid `setHTMLUnsafe()` for this boundary.

## Verify both paths

Force each path in supported target browsers and compare the resulting DOM, not just a serialized string: allowed `<p><strong>hello</strong></p>` remains; `<script>`, event handlers, disallowed wrappers and their contents, attributes, links and dangerous URLs cannot execute or survive this policy. Include malformed and nested markup and verify no alert, navigation or unexpected network request occurs. Test with Trusted Types enforcement enabled as deployed, and test a failed fallback load. If output differs in a security-relevant way, stop and fix the policy before release.

If using `Document.parseHTML()` for inspection, move sanitized nodes into the target rather than serializing and reparsing them, which can reintroduce mutation XSS. Client-side sanitization protects only that rendering context: independently protect server-rendered pages, email and other consumers with policies appropriate to those contexts.

Source: [Sanitizing Untrusted HTML](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/security/sanitize-untrusted-html.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
