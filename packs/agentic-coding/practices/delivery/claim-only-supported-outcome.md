---
anti_patterns:
  - description: Using a broad completion verb because the changed component and focused checks look finished, even though the evidence covers only one artifact state or technical slice of the user capability.
    id: agentic-coding.delivery.capability-inflation
    name: Technical slice inflated to capability
    severity: critical
applies_when: the agent is about to say that work is complete, fixed, accepted, deployed, pushed, or verified, and the available evidence may cover only a narrower artifact state or technical slice
id: agentic-coding.delivery.claim-only-supported-outcome
severity: critical
stage: delivery
tech_stack:
  - agentic-coding
title: Claim Only What the Evidence Proves
---

## When to apply

Apply when writing a completion or status claim from evidence already collected. This Practice
controls what the proven result may be called. It does not decide how to close a missing check, and
it does not choose which remaining risks belong in a handoff.

## Guidance

1. Name the exact artifact state, behavior, environment, and scope that the current evidence covers.
2. Choose a verb and object no broader than those facts: "fixed," "complete," "verified," or
   "deployed" must match what was actually demonstrated.
3. If the work is one component or technical slice of a larger user capability, say so directly
   rather than borrowing the surrounding feature's name.

Stop with one calibrated outcome statement; do not hide a broader implication behind words such as
"likely" or "effectively."

## Anti-pattern

The user asks to repair the worker that replays edits after reconnecting. The repository already has
a larger offline-sync feature, and one queued edit now replays successfully with focused tests
green. Calling the work "offline sync complete" feels natural because that is the surrounding
feature name. But conflict resolution and repeated reconnects were not exercised, so the claim turns
proof of one repaired path into proof of the whole capability.

## Why

Recipients use completion language to decide whether to merge, release, or stop investigating.
Matching the statement to the evidence prevents a true local result from authorizing decisions that
assume untested behavior.

## Exceptions and boundaries

Use the project's formal completion vocabulary when its gates are satisfied, but say when a gate was
not run or covered a different artifact state. When current evidence does cover the full capability,
state that plainly rather than weakening a supported result into vague language.

## Example

The current index passes the accepted relevance cases, but no rollout or failover was performed. The
agent reports "ranking behavior is verified on the current index" — naming the behavior and the
scope — rather than "the search rollout is complete."
