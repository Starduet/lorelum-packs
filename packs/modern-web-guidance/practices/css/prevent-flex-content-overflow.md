---
id: modern-web-guidance.css.prevent-flex-content-overflow
title: Allow Flex Items to Shrink and Wrap
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: a flex row contains long text or items that may exceed the available inline space
anti_patterns:
  - id: modern-web-guidance.css.prevent-flex-content-overflow.counterexample
    name: Allow Flex Items to Shrink and Wrap counterexample
    description: A long URL inside a flex item can force the row wider than its container because the item retains an automatic minimum size.
    severity: warn
---

## When to apply

Apply when a flex row contains long text or items that may exceed the available inline space.

## Guidance

Allow wrapping where appropriate and set `min-inline-size: 0` on the flex item that must shrink; choose a deliberate wrapping or scrolling policy for unbreakable content.

## Anti-pattern

A long URL inside a flex item can force the row wider than its container because the item retains an automatic minimum size.

## Why

The explicit minimum lets the flex item shrink below its content-based minimum; text wrapping controls the content inside it.

## Exceptions and boundaries

Do not hide essential content to conceal overflow. A toolbar that intentionally scrolls may use a scroll container instead of wrapping.

## Example

```css
.row { display: flex; flex-wrap: wrap; gap: 1rem; }
.row > .description { flex: 1 1 15rem; min-inline-size: 0; overflow-wrap: anywhere; }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css-layout.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css-layout.md)
