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

Before a delivery or handoff, decide which known, unresolved issues could change what the recipient
does next, whether they release, or how they recover. Explain those issues rather than repeating the
results already proved. If nothing important remains, do not invent an issues section; just describe
the completed work accurately.

## Guidance

1. Gather the known work still unfinished, risks, departures from the plan, and behavior not yet
   checked.
2. Keep the items that could change the recipient's next action, release decision, or recovery plan.
3. For each, explain the current effect and enough about reproduction, mitigation, or rollback for
   someone to act.

Once the recipient can choose the next step without retracing your investigation, stop. Leave out
the process history, harmless warnings, and discarded approaches.

## Anti-pattern

The user asks to finish a dependency upgrade. Two consumers still use the old interface, but the
agent also encountered several harmless warnings and discarded many hypotheses while debugging. To
demonstrate thoroughness, the handoff lists every command and dead end. The important decision,
whether the two remaining consumers block release or need compatibility support, is buried in
process history.

## Why

The next person needs to know what still matters, not everything that happened. A long work log can
hide the release blocker. A short explanation of the impact and recovery option helps them continue
without mistaking a detailed history for complete work.

## Exceptions and boundaries

Regulated, forensic, incident, or audit work may require a complete retained log. Keep that archive,
but separate it from the operational handoff. A transient failure that was reproduced, explained,
and cleared belongs in the handoff only when recurrence or uncertainty can still change the next
action.

## Example

A handoff states that peak-load behavior was not exercised, explains that connection saturation
could delay requests, and identifies the safe concurrency setting to restore if latency rises. It
omits unrelated failed searches and superseded tuning experiments.
