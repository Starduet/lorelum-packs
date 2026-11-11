---
id: modern-web-guidance.css.derive-parent-styles-from-descendants
title: Derive Parent Styles from Descendant State
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: styling a container based on a child’s state or presence
anti_patterns:
  - id: modern-web-guidance.css.derive-parent-styles-from-descendants.counterexample
    name: Derive Parent Styles from Descendant State counterexample
    description: Mirroring a checkbox state into a parent class with JavaScript creates a second state that can get out of sync.
    severity: warn
---

## When to apply

Apply when styling a container based on a child’s state or presence.

## Guidance

Use a narrowly anchored `:has()` selector for presentation driven by actual descendant state, such as checked controls or the presence of an image. Use `:user-invalid` when an error should appear after user interaction.

## Anti-pattern

Mirroring a checkbox state into a parent class with JavaScript creates a second state that can get out of sync.

## Why

The selector reads the real DOM state directly, avoiding duplicated presentation state.

## Exceptions and boundaries

Do not nest `:has()` or put pseudo-elements inside it. If older target browsers need the visual state, provide a state class or equivalent fallback; do not rely on color alone for validation or treat styling as a substitute for accessible error text.

## Example

```css
.field:has(input:user-invalid) { outline: 2px solid firebrick; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [child-state-based-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/child-state-based-styling.md)
- [content-based-styling.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/content-based-styling.md)
- [style-parent-with-has.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/style-parent-with-has.md)
