---
anti_patterns:
  - description: Choosing a plausible interpretation because it unblocks coding, then letting code, tests, and later tasks treat it as confirmed behavior without recording its limited scope or review condition.
    id: agentic-coding.implementation.silent-assumption
    name: Silent assumption
    severity: warn
applies_when: one implementation detail remains uncertain, and the agent is about to use a temporary interpretation that is low-impact, reversible, and does not change a public contract, security boundary, or irreversible operation
id: agentic-coding.implementation.surface-unconfirmed-assumptions
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Make Safe Temporary Assumptions Explicit
---

## When to apply

An implementation detail is still unanswered, but either reasonable choice would be safe, local, and
easy to replace. You can proceed with a clearly recorded temporary choice. Do not do this if the
choice changes user-visible product meaning, a public contract, a security boundary, or an
irreversible operation; confirm those decisions before coding. If authoritative sources disagree,
resolve which source to follow rather than writing down an assumption.

## Guidance

1. Record the temporary interpretation in one line at the point of choice: what you will assume for
   now and why either reading is reasonable.
2. Mark exactly which code it affects — one serializer or importer, for example. Keep work that
   depends on the choice there, and do not turn the assumption into a new requirement.
3. Say what will settle the question: a source, an answer from the responsible person, or an
   observation that would confirm or replace the choice.
4. If new evidence disproves it, change that local implementation. Do not keep the guess merely as
   compatibility behavior.

Stop when another engineer can find, review, and replace the choice without repeating your
investigation.

## Anti-pattern

The user asks for one new importer. Its sample records omit a blank description, while the shared
model accepts both an omitted value and an empty string. Using an empty string in the importer is
quick and harmless there, so the agent also changes the shared serializer and its tests for
consistency. A local temporary choice has now spread across every importer and looks like an
accepted data contract.

## Why

Code and tests can make an undocumented choice look settled. Recording the uncertainty keeps it
visible and limits how far it can spread while still allowing safe progress.

## Exceptions and boundaries

Do not use this Practice to bypass conflicting requirements or a decision that needs product,
security, legal, or operational approval. Details already settled by repository convention need no
extra record.

## Example

Sample payloads omit whether an empty optional label should be absent or an empty string, and the
current parser accepts both. The agent records "omit the field for now" next to the one serializer
that reads it, explains that both forms currently pass, and names an accepted schema clarification
from the schema owner as the review condition. No other serializer or test is changed to match the
guess.
