---
anti_patterns:
  - description: Sending only a task label, file path, or generic quality rule forces the delegated agent to reconstruct decisions it never saw, so it can produce polished and valid work that repeats an already rejected interpretation.
    id: agentic-coding.context.instructions-without-decisions
    name: Instructions without decision context
    severity: warn
applies_when: another agent is about to receive a bounded task that requires judgment about scope, tradeoffs, or quality, and important user corrections or accepted decisions are not visible in the files the agent will inspect
id: agentic-coding.context.give-delegated-agents-decision-context
severity: warn
stage: context
tech_stack:
  - agentic-coding
title: Give Delegated Agents the Context They Need to Decide
---

## When to apply

Apply before delegating work that requires the receiving agent to make the same scope or quality
judgments as the sender. Use it when decisive information lives in conversation, earlier review, or
several sources the receiver would not know to inspect. A mechanical task with fully specified input
and output is a near miss and needs only those instructions.

## Guidance

1. State the requested outcome and the user request or specification that controls it.
2. List the repository facts the receiver cannot discover from the task name alone: relevant state,
   required constraints, non-goals, and the accepted or rejected decisions that shape the work.
   Include the reason for a rejection when the receiver might otherwise repeat that locally
   reasonable choice.
3. Define the boundary of the delegation: the files or symbols in scope, the result to return, the
   checks the receiver owns, and which discoveries require escalation.
4. Link to large sources instead of copying their full contents.

Stop when the receiving agent can explain what it must decide, what it must preserve, and what it
must not silently reinterpret.

## Anti-pattern

The user and main agent agree that Pack examples must show mistakes a capable Agent could
realistically make, and they explicitly reject a scheduler example as confusing and artificial. The
main agent then delegates the rewrite with only "read the authoring plan and improve the
requirements Practices." The plan mentions realism but not the rejected example or why it failed.
The delegated agent polishes the scheduler wording and returns schema-valid files, repeating the
decision the user had already overturned.

## Why

Delegation removes conversation history to save time and context, but judgment depends on more than
the task name. A decision-focused packet preserves the reasons that distinguish an acceptable result
from a plausible wrong one without making every agent replay the full parent task.

## Exceptions and boundaries

Do not manufacture a long brief for a rename, exact text replacement, or other mechanical task whose
choices are already closed. Do not paste the entire transcript, raw logs, secrets, or unrelated
exploration into the packet; excess context can hide the same decisions the packet is meant to
preserve. The receiving agent still validates current files and evidence rather than treating the
packet as proof that the repository has not changed.

## Example

Before delegating a CLI installer change, the main agent states: "Default installation must use the
official registry, and an explicit custom registry must also work. Reuse the existing Pack validator
and materializer. Do not add arbitrary URL sources, automatic mirror fallback, an authentication
plugin system, or a new cache. Preserve current input budgets and typed errors. Return the changed
files, focused tests, and any contract change you believe is unavoidable." The receiver has enough
context to keep required extensibility without inventing a general source platform.
