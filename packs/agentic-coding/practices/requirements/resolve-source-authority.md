---
anti_patterns:
  - description: The agent treats the source that is newest, most detailed, or easiest to implement as authoritative without checking its status, turning stale behavior or an unconfirmed interpretation into a requirement.
    id: agentic-coding.requirements.promote-convenient-source
    name: Convenient source promotion
    severity: warn
applies_when: applicable repository instructions, a current contract, a decision record, code, tests, plans, summaries, or prior decisions disagree, and one of them is about to define intended behavior
id: agentic-coding.requirements.resolve-source-authority
severity: warn
stage: requirements
tech_stack:
  - agentic-coding
title: Resolve Authority Across Conflicting Sources
---

## When to apply

Apply when two or more already relevant sources imply different intended behavior and the next
decision needs one baseline. Sources can include the current request, an applicable repository
instruction, an active contract, a decision record with a stated status, a README or directory
index, a plan, code and tests, history, and a conversation summary. Do not search the repository for
possible disagreement. If the known sources agree and the question is reuse, inspect the
implementation instead.

## Guidance

Isolate the disputed behavior. For each known source, state whether it defines the current behavior,
explains an accepted architectural constraint, proposes future work, preserves history, or only
shows the current artifact. Use the repository's stated authority rules, explicit adoption or
supersession, and an authorized correction to choose the controlling source; detail and recency
alone are not enough. A README or directory index may orient the reader without creating a contract;
code and tests normally show what exists; a plan or proposed decision may describe work not yet
accepted. Record what controls the behavior and what the other sources still prove. If no rule
resolves a material choice, ask the user or responsible maintainer before coding it.

## Anti-pattern

A README and current tests describe a bulk-refund endpoint, while the active API contract omits it
and a proposed plan schedules it for a later stage. The endpoint already has a convenient handler,
so retaining it looks safer than reopening the decision. The code and README show an existing
artifact, but they cannot turn proposed work into a current contract.

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
prototype and its tests generate replacements. Keeping the tested prototype would be cheaper, but
the agent records the accepted plan as authority and the prototype as unfinished state. It does not
open unrelated migration modules or preserve replacement identifiers unless that behavior is
separately approved.
