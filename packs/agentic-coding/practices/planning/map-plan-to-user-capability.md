---
anti_patterns:
  - description: The agent treats a set of finishable components or layers as the complete capability because each has a clear task, leaving a cross-layer behavior or required rule with no owner.
    id: agentic-coding.planning.component-completion-substitution
    name: Component completion substitution
    severity: warn
applies_when: a plan that spans interfaces, services, storage, or other boundaries is about to be finalized, and nobody has traced its tasks end to end against the complete requested behavior path
id: agentic-coding.planning.map-plan-to-user-capability
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Map the Plan to User Capability
---

## When to apply

Before finalizing a plan that crosses interfaces, services, storage, policies, or other boundaries,
check whether its tasks cover the whole operation the user asked for. An internal refactor needs the
same check for behavior that must stay unchanged. If implementation is already finished, compare the
collected evidence with acceptance instead.

## Guidance

1. Start with the action the requester described and the result they expect to see. Follow the task
   list from one to the other.
2. Walk through the entry point, service handoffs, state changes, and applicable rules until you
   reach that result. Building the screen or API alone does not finish the operation.
3. Match each step to a task in the plan. Identify required steps that nobody has planned to do.
4. Add the missing work, or explicitly say that the promised delivery covers less. Finishing each
   listed component does not prove that all the necessary work was listed.

You are done when the plan connects the starting action to the result, with no unexplained missing
step that the promised behavior requires.

## Anti-pattern

An inventory-transfer plan includes a request endpoint and a confirmation screen, both
straightforward to build and test. It omits stock reservation between them because that
responsibility sits in another service. Every listed task can finish while two operators still
oversell the same stock.

## Why

A task list can make each component look complete while leaving the handoffs between them unbuilt.
Walking the whole operation reveals those gaps before an incomplete implementation makes them
expensive to fix.

## Exceptions and boundaries

A partial delivery can cover less than the full operation if that limit is explicit. For
infrastructure or refactoring, follow the operational behavior that must be preserved; do not invent
a user just to fit the exercise.

## Example

A password-reset task enters a repository that already has token creation and validation, making a
token-only plan look nearly complete. The agent maps request, message delivery, token validation,
password update, and required session invalidation to secure account recovery. The update and
invalidation steps have no task, so it adds them before coding instead of calling the token service
the whole capability.
