---
anti_patterns:
  - description: The agent acts on a plausible finding because fixing it seems safer than challenging a reviewer, allowing stale, mis-scoped, or requirement-conflicting advice to become product behavior.
    id: agentic-coding.review.finding-as-fact
    name: Finding treated as fact
    severity: warn
applies_when: a human, agent, analyzer, or review has raised a finding, and the agent is about to change the current artifact without first establishing whether the finding is true and in scope
id: agentic-coding.review.validate-findings-before-action
severity: warn
stage: review
tech_stack:
  - agentic-coding
title: Validate Findings Before Taking Action
---

## When to apply

Apply before an external finding drives a code, test, document, or plan change. Decide whether that
finding is true for the current requirement and artifact. If the defect is already reproduced, act
on it. If only the finding's supporting evidence may be stale, evaluate evidence freshness instead.

## Guidance

1. Compare the finding with the current request or specification: does the requested behavior
   actually conflict with, or require, this change?
2. Check the current artifact on the branch — the finding may cite an older diff.
3. Mark the finding confirmed, unconfirmed, or requiring an authority decision.
4. Choose only the route that status permits: local fix, gather more evidence, or return to
   requirements.

Do not edit while the finding is unconfirmed or the change would alter accepted behavior.

## Anti-pattern

A reviewer recommends removing keyboard navigation because focused pointer tests pass and the event
handling looks complex. Deleting it would simplify the component and keep the visible tests green,
but the accepted accessibility requirement explicitly includes keyboard use. The plausible
simplification conflicts with that requirement.

## Why

A finding is a claim, not a fact. Checking it preserves useful review input without letting
confidence, stale context, or preference for smaller code override the task.

## Exceptions and boundaries

Contain an exploitable security issue or destructive failure immediately when delay increases harm,
then validate before making containment permanent. A maintainer decision that changes scope is new
authority, not a technical finding.

## Example

A review says a cache key ignores locale and may return text in the wrong language. The agent checks
the current branch and finds locale was added during a later refactor; the finding cites the older
diff. It marks the finding unconfirmed for the current artifact and makes no code change.
