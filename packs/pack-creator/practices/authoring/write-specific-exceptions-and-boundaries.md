---
anti_patterns:
  - description: Listing broad concerns such as performance, security, or business need because they sound comprehensive, without stating a condition that a reader can recognize and apply.
    id: pack-creator.authoring.blanket-exception-list
    name: Blanket exceptions that weaken the rule
    severity: warn
applies_when: a Practice has a default rule and an observable condition changes, limits, or transfers that rule in a way readers need to know
id: pack-creator.authoring.write-specific-exceptions-and-boundaries
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Name Specific Exceptions and Boundaries
---

## When to apply

When a condition materially changes or limits the default action, explain it so readers can
recognize it. Do not invent exceptions or require a separate section when none is needed.

## Guidance

For each relevant exception, name the observable condition and explain how the default changes.
Identify protections that must remain and similar cases that still follow the default when those
facts matter. Delete categories that cannot be tested from available facts; do not aim to cover
every imaginable edge case.

## Anti-pattern

A frontend Pack recommends using the design system's standard interactive components. To avoid
sounding rigid, the author adds, "unless performance, accessibility, security, or business needs
require otherwise." The list feels balanced and acknowledges real concerns, but none of the terms
says when a custom component is justified or which keyboard and focus protections must remain. Any
preference can now be presented as an exception.

## Why

A specific boundary preserves the strength of the default while allowing justified departures. Vague
exception categories make the rule optional precisely when pressure makes a shortcut attractive.

## Exceptions and boundaries

Some Practices have no known exception; do not invent one to fill the section. A controlling law or
published contract may define a broad category, but cite the concrete condition it imposes. If an
exception creates a separate recurring decision, give it its own Practice instead of embedding a
second rule here.

## Example

An operations Pack recommends retrying transient job failures. Its boundary says not to retry an
operation that can create a second external charge unless the provider accepts an idempotency key or
the system has a verified compensating action. A timeout before any external request still follows
the default. The conditions are observable, and the data-integrity protection remains explicit.
