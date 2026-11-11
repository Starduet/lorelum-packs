---
anti_patterns:
  - description: A tooltip arrow is fixed to its original side after viewport collision handling flips the tooltip, making the arrow point away from its trigger.
    id: modern-web-guidance.ui.tooltip-arrow-stale-after-flip
    name: Tooltip arrow ignores collision fallback
    severity: warn
applies_when: positioning an anchored tooltip that may flip around its trigger near a viewport edge and has a directional arrow
id: modern-web-guidance.ui.tooltip-flip-indicator
severity: warn
stage: implementation
tech_stack:
  - css
  - accessibility
title: Keep Tooltip Indicators Consistent with Anchor Flips
---

Use anchor positioning with logical `position-try-fallbacks`, such as `flip-block`, to choose an alternate side when the preferred side overflows. If an arrow is needed, make it decorative and change its side and direction to match the active fallback. Set `container-type: anchored` on the positioned element and use `@container anchored(fallback: flip-block)` to style a descendant or pseudo-element; a container query cannot style its own container, so use an inner wrapper for its background or margins.

At the pinned upstream version, anchored container queries are limited to Chromium-based browsers. Hide the directional arrow unless `@supports (container-type: anchored)` succeeds; the tooltip text must remain usable without it. Anchor positioning and popover support are separate dependencies: provide an ordinary usable placement and an invocation/dismissal fallback or conditional polyfill for target browsers lacking them. Do not assume a centered polyfilled popover is anchored. Ensure the tooltip does not obscure keyboard-focused controls; reposition or dismiss it when no longer relevant. Associate descriptive tooltip text with its trigger and ensure it is accessible without a mouse.

Source: [Position Aware Tooltips, v1.0.0, commit 4dd9683](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/ui-atoms/position-aware-tooltips.md).
