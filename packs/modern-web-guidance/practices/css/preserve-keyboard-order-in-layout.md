---
id: modern-web-guidance.css.preserve-keyboard-order-in-layout
title: Preserve DOM Order in Visual Layout
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: using flex or grid to arrange interactive controls
anti_patterns:
  - id: modern-web-guidance.css.preserve-keyboard-order-in-layout.counterexample
    name: Preserve DOM Order in Visual Layout counterexample
    description: Using `order`, reversed flex direction, or dense grid packing to rearrange links can make focus jump unpredictably.
    severity: warn
---

## When to apply

Apply when using flex or grid to arrange interactive controls.

## Guidance

Keep the visual sequence of interactive elements aligned with document and keyboard focus order; arrange the DOM in the intended reading sequence.

## Anti-pattern

Using `order`, reversed flex direction, or dense grid packing to rearrange links can make focus jump unpredictably.

## Why

Visual rearrangement does not change DOM reading order or sequential keyboard navigation.

## Exceptions and boundaries

Decorative non-interactive items may use reordering when meaning is unchanged. Verify responsive variants as well as the default layout.

## Example

```html
<nav aria-label="Actions"><a href="/edit">Edit</a> <a href="/share">Share</a></nav>
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
