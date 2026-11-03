---
anti_patterns:
  - description: Listing broad concerns such as performance, security, or business need because they sound comprehensive, without stating a condition that a reader can recognize and apply.
    id: pack-creator.authoring.blanket-exception-list
    name: Blanket exceptions that weaken the rule
    severity: warn
applies_when: a Practice has a useful default rule and the author must state the observable conditions that change, limit, or transfer that rule
id: pack-creator.authoring.write-specific-exceptions-and-boundaries
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Name Specific Exceptions and Boundaries
---

## When to apply

Once the default action is clear, explain when readers should depart from it, limit it, or use
another rule instead. Give them conditions they can recognize. Do not use Exceptions and boundaries
to broaden the trigger or add a second workflow.

## Guidance

For each exception, name the observable condition, explain how the default changes, and identify any
protection that must remain. State near misses that look similar but still follow the default.
Delete categories that cannot be tested from available facts. Stop when each listed exception could
change a concrete decision; do not aim to cover every imaginable edge case.

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
