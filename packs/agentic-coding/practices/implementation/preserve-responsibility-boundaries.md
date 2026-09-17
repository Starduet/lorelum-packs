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

Apply when the same rule must hold across multiple callers, interfaces, or layers and it is unclear
where the rule belongs. A local detail inside the component already responsible for the rule is a
near miss. This Practice chooses the responsible component; it does not redesign the architecture or
choose the least complex implementation inside that component.

## Guidance

1. State the rule that must stay true in one sentence — the no-overselling invariant, the rounding
   rule for invoice totals.
2. List every entry point that depends on it: screens, API paths, batch importers, other services.
3. Put the final decision in the component already responsible for the relevant data or policy.
   Other layers may translate input, output, or presentation, but they must not redefine the rule.
4. If no current component can own the rule honestly, pause for an architectural decision instead of
   choosing the easiest file to edit.

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

Distinct input or trust boundaries may need checks of the same field, but each must establish a fact
that can be false there and must reinforce rather than redefine the authoritative rule. Passing an
unchanged validated value through another internal layer does not create that need. A database
constraint guarding concurrent mutation can remain necessary after input validation.
Performance-driven duplication needs evidence and a strategy for keeping results consistent. If the
requirement intentionally moves ownership or splits a domain, treat that as an architectural change
with migration consequences.

## Example

The repository creates stock reservations through both an API and a batch importer. Available stock
is maintained by the inventory component, so the agent puts the no-overselling check there and lets
each caller translate its own input. Both entry points now receive the same reservation decision
without copying stock arithmetic.
