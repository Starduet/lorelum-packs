---
anti_patterns:
  - description: Responding to a correction by creating permanent tests, rules, or documentation against the rejected behavior, even though the user only restored the earlier requirement and did not establish a new prohibition.
    id: agentic-coding.correction.correction-overreach
    name: Correction promoted to prohibition
    severity: warn
applies_when: an authorized user correction, accepted scope change, or rejection of unrequested behavior has made part of the current work obsolete, and the agent is about to continue from the old interpretation
id: agentic-coding.correction.restore-authoritative-baseline
severity: warn
stage: correction
tech_stack:
  - agentic-coding
title: Reset the Work After a Confirmed Correction
---

## When to apply

Apply after an authorized person or accepted specification has corrected the current direction.
Remove the old interpretation wherever it still shapes the goal, plan, code, tests, or
documentation. If sources still conflict, first resolve which source controls. An unverified review
comment is also not a confirmed correction.

## Guidance

1. Re-read the correction and the current request or specification, and state the corrected
   direction in one sentence.
2. Identify the assumptions and artifacts whose only basis was the rejected interpretation — goal
   sentences, plan items, code, tests, documentation — and remove or revise them.
3. Preserve behavior and protection that have an independent requirement or risk basis; a correction
   is not permission to discard the entire implementation.
4. Do not convert the rejection into a new permanent test, rule, or ban unless the authorized source
   explicitly establishes one.

Stop with one current statement of the requested work that separates restored scope from any
genuinely new scope introduced by the correction.

## Anti-pattern

The user asks to remove helper text that the agent added without a design source. The agent removes
it, then adds a negative test, a comment, and a design rule forbidding helper text on every similar
screen. The response feels protective, but it turns one cleanup into a new product contract the user
never requested.

## Why

Corrections fail when obsolete reasoning survives in plans, tests, or documentation. Resetting all
affected work removes that influence without making the opposite mistake: turning one rejected
experiment into a lasting prohibition.

## Exceptions and boundaries

A correction can establish a new durable contract when the authorized source explicitly says so.
Safety, privacy, compliance, data integrity, or compatibility may also provide an independent reason
for lasting protection.

## Example

The user clarifies that the requested status is an on-screen badge, not the weekly email the agent
inferred from an adjacent feature. The agent removes the scheduler, email code, and email-specific
tests, keeps the badge, and records no general ban on future notification work.
