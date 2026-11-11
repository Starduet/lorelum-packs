---
id: modern-web-guidance.css.use-logical-properties-for-flow
title: Use Logical Properties for Flow-Relative Layout
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: setting spacing, sizing, or position that should follow text direction or writing mode
anti_patterns:
  - id: modern-web-guidance.css.use-logical-properties-for-flow.counterexample
    name: Use Logical Properties for Flow-Relative Layout counterexample
    description: Hardcoding left margins for a navigation label makes spacing appear on the wrong side in right-to-left text.
    severity: warn
---

## When to apply

Apply when setting spacing, sizing, or position that should follow text direction or writing mode.

## Guidance

Use inline and block dimensions and start/end spacing where the design should follow writing direction. Keep physical directions for effects whose direction is intentionally fixed.

## Anti-pattern

Hardcoding left margins for a navigation label makes spacing appear on the wrong side in right-to-left text.

## Why

Logical properties express the relationship to content flow instead of assuming a left-to-right horizontal page.

## Exceptions and boundaries

Do not mechanically replace a physical direction that must remain physical, such as a directional diagram. Supply physical fallbacks when required by the supported browser matrix.

## Example

```css
.icon { margin-inline-end: 0.5rem; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css.md)
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
