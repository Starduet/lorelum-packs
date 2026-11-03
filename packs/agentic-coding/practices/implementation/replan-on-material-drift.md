---
anti_patterns:
  - description: Treating each newly discovered dependency, fallback, state change, or I/O step as a small implementation detail until the delivered behavior, risks, and required checks no longer match the accepted plan.
    id: agentic-coding.implementation.drift-normalization
    name: Drift normalization
    severity: warn
applies_when: coding has revealed an unplanned dependency, public behavior, stored state, I/O path, risk, or verification need that changes the accepted scope, and the agent is about to continue under the old plan
id: agentic-coding.implementation.replan-on-material-drift
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Replan When New Facts Change the Work
---

## When to apply

While coding, you discover an unplanned dependency, public behavior, stored state, I/O path, risk,
or verification need. Revisit the plan if this changes what you will deliver, who may depend on it,
how it can fail, or what must be checked. A helper rename, routine file split, or local adjustment
with the same scope and risk does not need replanning. If the plan already approves a kind of public
behavior and only its exact values are unclear, confirm those values instead.

## Guidance

1. Pause the affected implementation instead of continuing as if nothing had changed.
2. Compare the discovery with the agreed scope, risks, stopping condition, and planned checks.
   Explain what changes in the delivery, dependencies, possible failures, or verification.
3. Choose one response: bring the implementation back within the plan, update the plan and its
   checks, or ask for authorization before continuing.
4. Record the revised plan and use it when you resume.

Stop replanning when one current plan says what you will build and verify, and accounts for what you
discovered while coding.

## Anti-pattern

The user asks for a download endpoint that returns an account export. A large fixture exceeds the
response limit, so the agent adds a temporary file, then a retry queue, then background cleanup.
Each small addition fixes the next focused test and seems faster than stopping to redesign the
endpoint. The endpoint quietly grows into a stateful background job with its own queue and cleanup
storage that the accepted plan never included, bringing new failure and recovery behavior the
accepted work never covered.

## Why

A plan ties the promised scope to known risks and checks. When those facts change, continuing
silently creates new commitments while testing and review still judge the old work.

## Exceptions and boundaries

Contain an active security or data-loss incident immediately when delay increases harm, then update
the plan as soon as it is safe. Do not invoke this Practice for harmless mechanical details or use
it to reopen settled scope without a new fact that changes delivery, risk, or verification.

## Example

A migration checker was planned as read-only, but corrupted records reveal that useful completion
would require writes and rollback. The agent pauses, keeps the current change to a read-only report,
and asks whether repair should become a separately authorized migration with new safety evidence.
