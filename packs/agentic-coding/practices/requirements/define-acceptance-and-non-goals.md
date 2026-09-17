---
anti_patterns:
  - description: The agent judges completion by a clean-looking diff, reusable architecture, or passing local checks instead of the required behaviors, so optional platform work can be added or a required path can be removed.
    id: agentic-coding.requirements.artifact-count-acceptance
    name: Artifact-count acceptance
    severity: warn
applies_when: the requested result is clear and implementation is about to be planned, but no current list states which behaviors must work at completion and which tempting extensions sit outside it
id: agentic-coding.requirements.define-acceptance-and-non-goals
severity: warn
stage: requirements
tech_stack:
  - agentic-coding
title: Define Acceptance and Explicit Non-goals
---

## When to apply

Apply once the outcome sentence is agreed and before implementation work is chosen. State both what
must work and the most plausible adjacent work that is not required. If the requested result is
still unclear, define the user goal first.

## Guidance

1. Write a "done when" list of behaviors a caller can observe, for example "an install with no
   override resolves the official registry; an install with an explicit repository uses that custom
   registry." These are the checks that must pass before the task can be called done.
2. Write a "not part of this task" list of tempting adjacent features a capable engineer might
   reasonably add — mirrors, caching, a plug-in system, generic locators — and name each one
   explicitly outside the task.
3. Distinguish outcomes callers must tell apart: unavailable is not empty, rejected is not saved,
   and stale is not current. Add each missing distinction to the done-when list.
4. Check both lists against the request: keep required behavior even when removing it would shrink
   the diff, and exclude optional infrastructure even when it would make the design more general.
5. Establish the actual callers and deployment constraints when they change acceptance; do not
   silently add a public, hostile, multi-tenant, or always-offline scenario to a task that does not
   require it.

Stop when the two lists let a reviewer separate complete work from missing behavior and from scope
expansion.

## Anti-pattern

The installer needs a default official registry and an explicit repository registry. Because the Git
acquisition code is already being changed, a generic locator layer, automatic mirror fallback,
caching, and authentication hooks look like efficient future-proofing. A later cleanup makes the
opposite mistake: it removes the custom-registry support to minimize the patch. Both choices
optimize the shape of the implementation instead of the required install behaviors.

## Why

Without an explicit behavior boundary, "more reusable" and "smaller diff" can both look like
quality. Completion conditions protect required capability; non-goals keep attractive platform work
from becoming a current commitment.

## Exceptions and boundaries

Checks required by the supported inputs, governing policy, or accepted contract remain part of
completion even when not listed individually. Name that basis rather than treating "robustness" or
"security" as an unlimited exception. A later authorized requirement may add a non-goal, but future
possibility alone does not.

## Example

While building the new loader, the agent is tempted to add mirrors, caching, and a plug-in system.
It writes: "Done when an install with no override resolves the official registry, and an install
with an explicit repository uses that custom registry." It writes: "Not part of this task: automatic
mirror fallback, authentication plugins, multi-registry aggregation, generic file or HTTP locators,
and registry caching." Verification must cover both required paths; it need not build or permanently
forbid the non-goals.
