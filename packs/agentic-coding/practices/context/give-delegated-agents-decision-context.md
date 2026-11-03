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

You are handing work to another agent, but some decisions it needs are only in your conversation or
an earlier review. Explain those decisions before it has to judge scope or quality for itself.
Include decisive information from sources it would not know to inspect. A mechanical task with fully
specified input and output needs only those instructions, not an extra brief.

## Guidance

1. Say what result is needed and which user request or specification defines it.
2. Explain the repository facts the task name will not tell the receiver: relevant current state,
   required constraints, non-goals, and decisions already accepted or rejected. If a rejected choice
   would still look sensible to the receiver, include why it was rejected.
3. Specify the files or symbols it may work on, what it should return, which checks it owns, and
   which discoveries it must bring back to you.
4. Link to large sources instead of copying them in full.

Stop when the receiving agent can tell what it must decide, what it must preserve, and what it
cannot silently reinterpret.

## Anti-pattern

The user and main agent agree that Pack examples must show mistakes a capable Agent could
realistically make, and they explicitly reject a scheduler example as confusing and artificial. The
main agent then delegates the rewrite with only "read the authoring plan and improve the
requirements Practices." The plan mentions realism but not the rejected example or why it failed.
The delegated agent polishes the scheduler wording and returns schema-valid files, repeating the
decision the user had already overturned.

## Why

Another agent usually does not receive your conversation history. Without the reasons behind earlier
decisions, it can do careful work and still repeat a choice the user rejected. Give it those reasons
without making it read the whole parent task.

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
