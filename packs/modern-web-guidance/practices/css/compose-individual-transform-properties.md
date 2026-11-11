---
id: modern-web-guidance.css.compose-individual-transform-properties
title: Compose Independent Transform Properties
severity: warn
stage: implementation
tech_stack:
  - css
applies_when: separate states or animations need to change translation, rotation, or scale independently
anti_patterns:
  - id: modern-web-guidance.css.compose-individual-transform-properties.counterexample
    name: Compose Independent Transform Properties counterexample
    description: "A hover rule that sets `transform: scale(...)` can erase the base `transform: translate(...)`."
    severity: warn
---

## When to apply

Apply when separate states or animations need to change translation, rotation, or scale independently.

## Guidance

Use `translate`, `rotate`, and `scale` for independent effects rather than replacing a full `transform` chain whenever one state changes. Set an identity value in the base state for a transform property that changes on interaction, so its stacking context and containing block do not appear only on hover.

## Anti-pattern

A hover rule that sets `transform: scale(...)` can erase the base `transform: translate(...)`.

## Why

Individual properties can be changed independently without restating unrelated transformations.

## Exceptions and boundaries

Individual transforms have a defined composition order, which can differ from an existing transform list; verify the visual result when migrating. Keep a complete `transform` fallback if the browser target lacks individual properties.

## Example

```css
.badge { translate: 0 -0.2rem; scale: 1; }
.badge:hover { scale: 1.05; }
@media (prefers-reduced-motion: reduce) { .badge { transition: none; } }
```

## Sources

Upstream GoogleChrome/modern-web-guidance v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`:
- [individual-transform-properties.md](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/css/individual-transform-properties.md)
