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

A reviewer, another agent, or an analyzer says something is wrong. Before changing code, tests,
documents, or the plan, check whether that claim holds for the current requirement and files. If the
defect is already reproduced, act on it. If only the supporting evidence may be outdated, check
whether that evidence still applies instead.

## Guidance

1. Compare the claim with the current request or specification. Does the requested behavior require
   this change, or would the proposed change conflict with it?
2. Check the current files on the branch; the review may refer to an older diff.
3. Record whether the problem is confirmed, still unconfirmed, or needs a decision from someone
   authorized to change the requirement.
4. Fix a confirmed local problem, gather more evidence for an unconfirmed one, or return to
   requirements for a decision.

Do not edit while the claim is unconfirmed or the change would alter accepted behavior.

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
