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

Apply when one concrete detail is not settled, but either reasonable choice is safe, local, and easy
to replace. The uncertainty must not change user-visible product meaning, a public contract, a
security boundary, or an irreversible operation. Those higher-impact choices require confirmation
before coding. If authoritative sources disagree, resolve which source controls instead of recording
a temporary assumption.

## Guidance

1. Record the temporary interpretation in one line at the point of choice: what you will assume for
   now and why either reading is reasonable.
2. Mark the exact code the choice affects — one serializer, one importer — and keep dependent work
   inside that boundary without deriving new requirements from the assumption.
3. Name the review condition: the source, owner answer, or observation that will confirm or replace
   the choice.
4. When new evidence disproves the assumption, change the bounded implementation instead of
   preserving the guess as compatibility behavior.

Stop when another engineer can find, review, and replace the choice without replaying the
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
