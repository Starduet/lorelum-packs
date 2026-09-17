---
anti_patterns:
  - description: The agent treats the source that is newest, most detailed, or easiest to implement as authoritative without checking its status, turning stale behavior or an unconfirmed interpretation into a requirement.
    id: agentic-coding.requirements.promote-convenient-source
    name: Convenient source promotion
    severity: warn
applies_when: two or more governing sources for the same behavior disagree — request, spec or contract, decision record, plan, README, code, or tests — and one of them is about to be treated as the intended behavior
id: agentic-coding.requirements.resolve-source-authority
severity: warn
stage: requirements
tech_stack:
  - agentic-coding
title: Resolve Authority Across Conflicting Sources
---

## When to apply

Apply when two or more already relevant sources imply different intended behavior and the next
decision needs one baseline: the current request, an applicable repository instruction, an adopted
spec or active contract, a decision record with a stated status, a README, a plan, code and tests,
history, or a conversation summary. Do not search the repository for possible disagreement. If the
known sources already agree and the open question is reuse of existing code, inspect the
implementation instead.

## Guidance

1. Isolate the disputed behavior to one sentence, for example how long order records are kept.
2. State each known source's role: defines current behavior, records an accepted constraint,
   proposes future work, preserves history, or only shows the current artifact. An adopted spec or
   active contract controls; a detailed README or passing tests only show what exists today; a plan
   or prototype describes work that may not be accepted.
3. Decide which source wins from status, not from detail, recency, or implementation convenience:
   use the repository's stated authority rules, explicit adoption or supersession, and authorized
   corrections.
4. Record the controlling source and what the other sources still prove, so a reviewer can retrace
   the decision.

If no rule resolves a material conflict — the suite asserts one behavior, the decision record says
another, and a maintainer comment disagrees with both — ask the user or responsible maintainer
before coding. Stop when one named source defines the disputed behavior and every other source is
labeled with its role.

## Anti-pattern

An adopted policy keeps audit records for seven years, while an older cleanup job and its passing
tests delete them after one. Because the cleanup job already runs and its tests are green, keeping
it looks safer than reopening the decision. Passing tests show an existing artifact; they cannot
outweigh an adopted policy about intended retention.

## Why

Sources serve different roles. Separating authority from proposal, navigation, history, and
observation prevents a convenient existing artifact or a detailed explanation from becoming the
target without approval.

## Exceptions and boundaries

A safety or data-protection rule may override a product instruction when governing policy explicitly
grants that precedence. A local repository instruction changes an inherited rule only when its scope
and relationship to that rule are explicit; directory proximity alone does not grant an override.
Record the scope of any override. This Practice chooses which source defines intent, not the
implementation design or a broad repository-reading plan.

## Example

The accepted migration plan says existing customer identifiers must remain stable, while the current
prototype and its tests generate replacements, and the prototype's README agrees with the tests. The
agent must pick which document to follow. It records the accepted plan as the controlling source and
the prototype plus its tests as unfinished state, and does not preserve replacement identifiers
unless that behavior is separately approved.
