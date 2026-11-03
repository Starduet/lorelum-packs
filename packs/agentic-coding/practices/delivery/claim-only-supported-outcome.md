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

Before saying that work is complete, check exactly what you have demonstrated. A fix to one
component or a passing check in one environment may not prove that the whole feature works. This
rule is about how to report the result, not how to fill gaps in testing or which remaining risks to
hand over.

## Guidance

1. Identify what was checked, the state of the code or output, what it did, and the environment in
   which it ran.
2. Use "fixed," "complete," "verified," or "deployed" only for the result you actually demonstrated.
   If the checks cover one component or part of a feature, name that part rather than claiming the
   whole feature.

Once you have an accurate statement of that result, stop refining the claim. Adding "likely" or
"effectively" does not justify implying that more work is complete than the evidence shows.

## Anti-pattern

The user asks to repair the worker that replays edits after reconnecting. The repository already has
a larger offline-sync feature, and one queued edit now replays successfully with focused tests
green. Calling the work "offline sync complete" feels natural because that is the surrounding
feature name. But conflict resolution and repeated reconnects were not exercised, so the claim turns
proof of one repaired path into proof of the whole capability.

## Why

People may merge, release, or stop investigating based on this report. If a local fix is described
as a completed feature, they may rely on behavior that nobody checked.

## Exceptions and boundaries

Use the project's own completion terms when their conditions have been met. Mention any check that
was not run or ran against a different version or state. If the evidence proves that the full
feature works, say so directly; there is no need to make a supported result sound uncertain.

## Example

The current index passes the accepted relevance cases, but no rollout or failover was performed. The
agent reports "ranking behavior is verified on the current index" — naming the behavior and the
scope — rather than "the search rollout is complete."
