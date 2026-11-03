---
anti_patterns:
  - description: Placing a shared rule in the component where the symptom is easiest to fix rather than in the component responsible for the rule, allowing other callers to bypass it or implement it differently.
    id: agentic-coding.implementation.invariant-in-wrong-owner
    name: Invariant in the wrong owner
    severity: warn
applies_when: a change crosses a domain, layer, package, service, or repository boundary, and the agent must decide which component should own a rule that must remain consistent across more than one caller or entry point
id: agentic-coding.implementation.preserve-responsibility-boundaries
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Put Shared Rules in the Responsible Component
---

## When to apply

Several callers, interfaces, or layers must obey the same rule, and you need to decide where to
enforce it. If the component responsible for the rule is already clear and you are only changing its
internals, there is no need to revisit that choice. Decide who is responsible here; choosing a new
architecture or the simplest implementation inside that component is a separate task.

## Guidance

1. Describe the rule in one sentence, such as "reservations must not exceed available stock" or
   "invoice totals use this rounding rule."
2. List every entry point that depends on it: screens, API paths, batch importers, other services.
3. Put the final decision in the component already responsible for the relevant data or policy.
   Other layers may translate input, output, or presentation, but they must not redefine the rule.
4. If no existing component can reasonably take responsibility for the rule, pause for an
   architectural decision rather than putting it in the easiest file to edit.

Stop with one responsible component and a clear instruction for callers.

## Anti-pattern

The user asks a new checkout screen to show the final invoice total. The screen already has every
line item, so calculating and rounding the total there avoids a service change and makes the UI
tests pass quickly. But refunds and API-created orders still use the pricing component's different
rounding rule, so the same invoice can have two totals.

## Why

A rule enforced by the responsible component has one meaning for every entry point. Putting it in a
convenient caller ties the rule to one flow, so other callers can bypass it or recreate it
differently.

## Exceptions and boundaries

Different input or trust boundaries may need to check the same field. Each check must address
something that could actually be wrong at that point and uphold, not redefine, the authoritative
rule. Passing an unchanged validated value through another internal layer does not create that need.
A database constraint can still be necessary to prevent concurrent changes after input validation.
Performance-driven duplication needs evidence and a strategy for keeping results consistent. If the
requirement intentionally moves ownership or splits a domain, treat that as an architectural change
with migration consequences.

## Example

The repository creates stock reservations through both an API and a batch importer. Available stock
is maintained by the inventory component, so the agent puts the no-overselling check there and lets
each caller translate its own input. Both entry points now receive the same reservation decision
without copying stock arithmetic.
