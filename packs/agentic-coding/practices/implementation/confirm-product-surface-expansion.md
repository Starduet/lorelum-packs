---
anti_patterns:
  - description: Expanding an authorized surface into additional values, modes, or extension points because the internal implementation is already generic, thereby creating public compatibility and maintenance obligations that were never accepted.
    id: agentic-coding.implementation.speculative-public-surface
    name: Speculative public surface
    severity: warn
applies_when: accepted scope authorizes a long-lived UI control, API, configuration value, stored value, public export, source type, or extension category, but the agent is about to expose an exact variant that the accepted scope does not define
id: agentic-coding.implementation.confirm-product-surface-expansion
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Confirm What Users Can Depend On
---

## When to apply

Apply before making a new UI option, API value, configuration key, stored value, export, source
type, or extension point dependable outside its implementation. The general kind of feature is
already authorized; the exact public values or behaviors are not. A completely unplanned feature
that changes scope, risk, or verification needs requires replanning. An internal abstraction that
exposes nothing new is only a design choice.

## Guidance

1. Read the user request, accepted issue, or current specification that authorizes the feature, and
   list the exact values and behaviors it names.
2. Compare that list with what users, integrations, stored data, or downstream code could rely on
   after this change — event names, headers, modes, tokens, configuration keys.
3. Expose only what the source supports. Keep ambiguous variants private, or ask for a decision
   before publishing them.
4. Record the source of any broader obligation: an existing published contract, approved migration,
   or explicit platform requirement may authorize more variants than the immediate feature needs.

Stop with one explicit list of the public values or behaviors admitted now. Approval of one event,
setting, or source type never authorizes arbitrary extensibility.

## Anti-pattern

The user asks integrations to receive one order-shipped webhook. The repository's event dispatcher
already accepts arbitrary event names and headers, so exposing that generic shape looks cleaner than
adding one narrow event, and the requested case still passes. But publishing every name, custom
header, and plugin hook commits the product to behavior the user never asked for.

## Why

Once users, integrations, stored data, or downstream code rely on a value or behavior, removing or
changing it becomes expensive. Confirming the exact boundary prevents a generic internal
implementation from silently defining product policy.

## Exceptions and boundaries

This Practice does not forbid a future-friendly internal design; it limits what becomes externally
dependable now.

## Example

The accepted design asks for a display-density setting with compact and comfortable modes. The
component can accept arbitrary spacing tokens, but no user request or specification makes those
tokens public. The agent exposes only the two named modes and keeps custom tokens internal until a
product decision authorizes them.
