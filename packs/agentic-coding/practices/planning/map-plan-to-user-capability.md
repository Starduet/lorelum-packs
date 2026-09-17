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

Apply when a plan spans interfaces, services, storage, policies, or other boundaries and may miss
part of the requested path. For an internal refactor, map the behavior that must remain unchanged.
If implementation is finished and collected results must be compared with acceptance, map evidence
instead.

## Guidance

1. Name the initiating action and the observable result the requester described, then read the task
   list as a path from one to the other, end to end.
2. Walk each step of that path: entry point, service handoffs, state changes, policies, and the
   result the user observes. Screens and the API are stops on the path, not the destination.
3. Assign each step to a task in the plan, and list required steps that no task covers.
4. For every uncovered step, add the missing responsibility to the plan, or narrow the promised
   capability explicitly. Layer completion does not prove the path is whole.

Stop when the map joins up with no unexplained required gap between the action and the result.

## Anti-pattern

An inventory-transfer plan includes a request endpoint and a confirmation screen, both
straightforward to build and test. It omits stock reservation between them because that
responsibility sits in another service. Every listed task can finish while two operators still
oversell the same stock.

## Why

Technical task lists reward local completion. An actor-to-result map exposes missing handoffs before
partial implementation makes them expensive to repair.

## Exceptions and boundaries

A planned partial delivery may cover only part of the capability when that limit is explicit.
Infrastructure and refactoring work should map to the operational behavior they preserve rather than
inventing a fictional user.

## Example

A password-reset task enters a repository that already has token creation and validation, making a
token-only plan look nearly complete. The agent maps request, message delivery, token validation,
password update, and required session invalidation to secure account recovery. The update and
invalidation steps have no task, so it adds them before coding instead of calling the token service
the whole capability.
