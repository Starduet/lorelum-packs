---
anti_patterns:
  - description: Including every explored path, harmless warning, and transient failure to demonstrate diligence, thereby burying the unresolved facts that could change the recipient's next action or release decision.
    id: agentic-coding.delivery.residual-log-dump
    name: Investigation log instead of decision-relevant issues
    severity: critical
applies_when: delivery or handoff is imminent, at least one known limitation, risk, plan deviation, or unfinished item could change the recipient's next decision, and the agent must decide what to report
id: agentic-coding.delivery.report-material-residuals
severity: critical
stage: delivery
tech_stack:
  - agentic-coding
title: Report Only Remaining Issues That Matter
---

## When to apply

Apply when something known but unresolved could change the recipient's next action, release
decision, or recovery plan. This Practice reports what remains; it does not restate what the
evidence already proves. If nothing important remains, do not invent an issues section — calibrate
the completion wording instead.

## Guidance

1. List the known but unresolved items: unfinished work, risks, plan deviations, untested behavior.
2. Select only the ones that can change the recipient's next action, release decision, or recovery
   plan.
3. For each selected item, state its current impact and the smallest reproduction, mitigation, or
   rollback fact needed to act.

Stop when the recipient can choose the next step without replaying the investigation; omit the
process history, harmless warnings, and dead ends.

## Anti-pattern

The user asks to finish a dependency upgrade. Two consumers still use the old interface, but the
agent also encountered several harmless warnings and discarded many hypotheses while debugging. To
demonstrate thoroughness, the handoff lists every command and dead end. The important decision,
whether the two remaining consumers block release or need compatibility support, is buried in
process history.

## Why

Decision-relevant issues preserve continuity between owners. Process history consumes attention and
can hide the actual blocker, while a concise impact and recovery note lets the next owner act
without mistaking verbosity for completeness.

## Exceptions and boundaries

Regulated, forensic, incident, or audit work may require a complete retained log. Keep that archive,
but separate it from the operational handoff. A transient failure that was reproduced, explained,
and cleared belongs in the handoff only when recurrence or uncertainty can still change the next
action.

## Example

A handoff states that peak-load behavior was not exercised, explains that connection saturation
could delay requests, and identifies the safe concurrency setting to restore if latency rises. It
omits unrelated failed searches and superseded tuning experiments.
