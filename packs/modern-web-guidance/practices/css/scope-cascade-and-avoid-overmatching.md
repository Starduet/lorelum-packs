---
id: modern-web-guidance.css.scope-cascade-and-avoid-overmatching
title: Make Cascade Priority and Selector Intent Explicit
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: designing CSS rules that otherwise require specificity escalation or reset overrides
anti_patterns:
  - id: modern-web-guidance.css.scope-cascade-and-avoid-overmatching.counterexample
    name: Make Cascade Priority and Selector Intent Explicit counterexample
    description: A generic hover rule followed by a disabled override becomes incorrect when the rules are reordered.
    severity: warn
---

## When to apply

Apply when designing CSS rules that otherwise require specificity escalation or reset overrides.

## Guidance

Declare cascade layer order up front, use `:where()` for low-specificity defaults, and exclude states that should never match with `:not()`. Use scoped boundaries where nested subtrees must be excluded or proximity matters.

## Anti-pattern

A generic hover rule followed by a disabled override becomes incorrect when the rules are reordered.

## Why

Non-overlapping selectors express the intended state, while layers separate priority from selector specificity.

## Exceptions and boundaries

Unlayered normal author rules outrank layered normal author rules; important declarations reverse layer order. `@scope` is progressive enhancement: supply a functional selector fallback when outside the target matrix. Existing BEM conventions need not be renamed.

## Example

```css
@layer base, components;
@layer components {
  button:hover:not(:disabled) { background: royalblue; }
}
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [css.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/css.md)
