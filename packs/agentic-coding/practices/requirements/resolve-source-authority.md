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

The request says one thing, but a specification, README, plan, or test says another. Before choosing
which behavior to implement, find out which source is meant to decide it. Relevant sources can also
include repository instructions, active contracts, decision records, code, history, and conversation
summaries. Work from disagreements you already know about; do not search the repository for possible
ones. If those sources agree and you only need to know whether existing code is reusable, inspect
that implementation instead.

## Guidance

1. Describe the disputed behavior in one sentence, for example how long order records are kept.
2. Read each known source's declared status to find out what it tells you: what should happen now,
   which constraint was accepted, what is only proposed, what happened in the past, or what the code
   currently does. File type alone does not decide this. Follow an adopted spec or active contract,
   including a README explicitly adopted as the repository's contract. An unadopted README or
   passing tests only show what exists today; a plan or prototype may describe unaccepted work.
3. Use the repository's authority rules, explicit adoption or replacement of earlier decisions, and
   authorized corrections to resolve the disagreement. More detail, a newer date, or easier
   implementation does not give a source priority.
4. Record which source decides the behavior and what the others still establish, so a reviewer can
   retrace the choice.

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

A proposal, a historical note, and a test of existing code do not necessarily tell you what the
product should do. Checking their status prevents a convenient implementation or detailed
explanation from becoming a requirement without approval.

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
