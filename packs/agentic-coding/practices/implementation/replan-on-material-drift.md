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

Apply when a discovery during coding changes what will be delivered, who may depend on it, how
failure can occur, or what must be checked. A renamed helper, routine file split, or local
adjustment covered by the same scope and risk is a near miss. If the plan already authorizes a kind
of public behavior and only its exact values are unclear, confirm those values instead of reopening
the whole task.

## Guidance

1. Pause the affected implementation; do not code through the discrepancy.
2. Compare the new fact with the accepted scope, risks, stopping condition, and planned checks, and
   name what changed — delivery, dependencies, failure modes, or verification needs.
3. Choose one response: narrow the implementation back to the plan, update the plan and its checks,
   or ask for authorization before continuing.
4. Record the updated plan and resume from it.

Stop when one current plan states what will be built and verified and matches the facts coding
revealed.

## Anti-pattern

The user asks for a download endpoint that returns an account export. A large fixture exceeds the
response limit, so the agent adds a temporary file, then a retry queue, then background cleanup.
Each small addition fixes the next focused test and seems faster than stopping to redesign the
endpoint. Together they turn a synchronous download into a stateful background job with new failure
and recovery behavior that the accepted work never covered.

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
