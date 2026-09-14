---
anti_patterns:
  - description: Reading additional code, tests, documentation, logs, or neighboring implementations for general familiarity after the target and direct evidence already resolve the next decision wastes context and can hide the source that actually matters.
    id: agentic-coding.implementation.familiarity-driven-exploration
    name: Familiarity-driven exploration
    severity: warn
applies_when: the target file, symbol, or behavior is known, but the agent is about to inspect additional code, tests, configuration, documentation, logs, or analogous modules without naming a current decision that their contents could change
id: agentic-coding.implementation.limit-investigation-to-current-decision
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Limit Investigation to the Current Decision
---

## When to apply

Apply after the Agent has located the target file, symbol, or behavior and is considering more
repository exploration for general familiarity. Use it before opening another source whose result is
not tied to a concrete choice. Locating an unknown target is a near miss: find the target first. A
known conflict about intended behavior belongs to source-authority resolution instead.

## Guidance

Name the next unresolved decision before opening another source. Read a code file, test,
configuration, document, log, or neighboring implementation only when it could change the edit
location, responsible owner, required behavior, focused verification, or the choice to replan.
Follow one unresolved dependency at a time and update the decision after each direct observation.
When the evidence reveals a material new public surface, shared state, risk, or verification need,
stop local investigation and replan from that fact. Do not treat broad familiarity, file count, or
an exhaustive caller map as evidence. Stop when the target behavior, direct owner, edit boundary,
and focused verification path are clear, and no next source can change one of them.

## Anti-pattern

The user asks to change a settings-page save button from gray to blue. The Agent finds the page,
sees that the button uses one shared variant, and locates the color token that variant reads. Rather
than deciding whether the token's meaning permits a local override or a shared change, it opens
every Button consumer, old theme migrations, unrelated page styles, broad end-to-end suites, and
architecture notes. The extra material changes no color decision, consumes context, and obscures the
two sources that actually define the edit.

## Why

Investigation is useful only when it can alter the next decision. Reading sources that cannot do so
turns uncertainty into delay, wastes context, and makes irrelevant observations compete with the
small set of facts needed for a correct change.

## Exceptions and boundaries

Follow applicable instructions already supplied by the working environment. Do not manually scan a
repository for possible instruction files merely to recreate an unknown discovery mechanism. A
safety, security, data, compatibility, migration, release, or explicitly requested audit may require
more investigation, but each additional source must still answer a named boundary question. If the
target cannot be located, search for it; if a direct source shows a broader change than accepted,
use replanning rather than continuing an expanding exploration.

## Example

A user asks to correct a currency label in an invoice preview. The Agent locates the preview
component, sees that the label comes from a shared formatter, and reads that formatter plus its
focused test. The formatter already receives a locale-aware currency code, so the Agent corrects the
one label mapping and runs the formatter test. It does not inspect every invoice consumer or the
historical billing migration. If the formatter instead reveals a persisted currency-code mismatch,
the Agent stops and replans because the task is no longer a local label correction.
