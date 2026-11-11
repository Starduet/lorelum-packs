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

## Guidance

Exclude irrelevant states in the selector instead of undoing an overbroad rule. For example, a hover rule should not match disabled buttons, regardless of source order. For rules that repeatedly compete by specificity, use cascade layers to express priority and `:where()` for overridable defaults; follow existing project conventions rather than renaming classes.

## Exceptions and boundaries

Normal unlayered author rules outrank layered rules, and `!important` reverses layer order. Adding a layer to an existing stylesheet can therefore change priority: account for existing unlayered rules before migrating. Overrides remain appropriate for genuine specialization.

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
