---
anti_patterns:
  - description: A simple FAQ is rebuilt with clickable divs, custom keyboard handlers and an exclusive open state that prevents comparing answers.
    id: modern-web-guidance.ui.custom-disclosure-by-default
    name: Rebuilding ordinary disclosure controls
    severity: warn
applies_when: building an accordion or a set of independently expandable sections with labeled disclosure controls
id: modern-web-guidance.ui.native-accordion-disclosures
severity: warn
stage: implementation
tech_stack:
  - html
  - accessibility
title: Use Native Disclosures for Accordions
---

Use adjacent `<details>` elements with a `<summary>` for each ordinary disclosure. Group them under a named section when they form a distinct section, but avoid adding a landmark for every small group. Keep multiple items open by default so users can compare content and avoid unexpected viewport shifts. Do not add arrow-key navigation: users may need those keys to scroll long content.

```html
<section aria-labelledby="faq">
  <h2 id="faq">Frequently asked questions</h2>
  <details><summary>How do I reset my password?</summary><p>Use the reset link on the sign-in page.</p></details>
  <details><summary>How do I change my email?</summary><p>Open account settings.</p></details>
</section>
```

If exclusivity is a real requirement, use a shared `name` only on the intended group and check target-browser support; use a scripted fallback if exclusivity is essential. Avoid putting headings inside `summary`: some screen readers expose the summary as a button and lose the heading. If each item needs a navigable heading, use a custom heading containing a button, synchronize `aria-expanded` and visibility, and support keyboard activation. Search-driven reveals must also update the state of custom controls. Optional disclosure animation must not prevent operation without animation and should respect reduced-motion preferences.

Source: [Accordion, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-components/accordion.md).
