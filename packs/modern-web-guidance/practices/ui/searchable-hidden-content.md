---
anti_patterns:
  - description: Search-relevant collapsed content is hidden with display none, so find-in-page cannot reveal it and associated controls never reflect a search reveal.
    id: modern-web-guidance.ui.hidden-content-unsearchable
    name: Searchable content hidden from browser find
    severity: warn
applies_when: hiding non-sensitive page content that users should still be able to find with browser search or fragment navigation
id: modern-web-guidance.ui.searchable-hidden-content
severity: warn
stage: implementation
tech_stack:
  - html
  - javascript
title: Preserve Find-in-Page for Hidden Content
---

Prefer `<details>` for a disclosure whose closed content should be discoverable by browser find. For a custom disclosure or externally controlled panel, use `hidden="until-found"` and listen for `beforematch` on the panel or a containing element. When the browser reveals a match, synchronize its control's `aria-expanded` and any mutually exclusive siblings before the reveal completes.

Do not apply `display: none` or `visibility: hidden` to the until-found panel: that prevents native find from revealing it. Put borders, backgrounds and padding on a child, since the hidden panel can still have a layout box. This is not a secrecy mechanism; never send sensitive data merely because it starts hidden. It is also not a substitute for visually hidden screen-reader text.

The pinned upstream identifies Safari as not supporting `hidden="until-found"`; unsupported browsers treat it as ordinary hidden content and cannot find it. If search access is required, detect `beforematch` support and expose the contents with corresponding control states updated. For mutually exclusive panels, present the contents linearly in the fallback rather than overlapping them. Browser find itself cannot be polyfilled reliably.

Source: [Search hidden content, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-behaviors/search-hidden-content.md).
