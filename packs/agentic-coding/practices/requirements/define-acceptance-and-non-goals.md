---
anti_patterns:
  - description: The agent judges completion by a clean-looking diff, reusable architecture, or passing local checks instead of the required behaviors, so optional platform work can be added or a required path can be removed.
    id: agentic-coding.requirements.artifact-count-acceptance
    name: Artifact-count acceptance
    severity: warn
applies_when: the requested result is clear, but the agent is about to plan implementation without stating which behaviors must work and which likely extensions are not part of the task
id: agentic-coding.requirements.define-acceptance-and-non-goals
severity: warn
stage: requirements
tech_stack:
  - agentic-coding
title: Define Acceptance and Explicit Non-goals
---

## When to apply

Apply after the requested result is clear and before implementation work is chosen. State both what
must work and the most plausible adjacent work that is not required. If the requested result is
still unclear, define the user goal first.

## Guidance

Write a short "done when" list using behavior a caller can observe. Then write a "not part of this
task" list for nearby extensions a capable engineer might reasonably add. Keep required behavior
even when removing it would shrink the diff. Exclude optional infrastructure even when it would make
the design more general. Stop when the two lists let a reviewer distinguish complete work from
missing behavior and scope expansion. Include any material failure or degraded outcome callers must
distinguish: unavailable is not empty, rejected is not saved, and stale is not current. Establish
the actual callers and deployment constraints when they change acceptance; do not silently add a
public, hostile, multi-tenant, or always-offline scenario to a task that does not require it.

## Anti-pattern

The installer needs a default official registry and an explicit custom repository registry. Because
the Git acquisition code is already being changed, a generic locator layer, automatic mirror
fallback, caching, and authentication hooks look like efficient future-proofing. A later cleanup
makes the opposite mistake: it removes custom-registry support to minimize the patch. Both choices
optimize the shape of the implementation instead of the requested install behaviors.

## Why

Without an explicit behavior boundary, "more reusable" and "smaller diff" can both look like
quality. Completion conditions protect required capability; non-goals prevent attractive platform
work from becoming a current commitment.

## Exceptions and boundaries

Checks required by the supported inputs, governing policy, or accepted contract remain part of
completion even when not listed individually. Name that basis rather than treating "robustness" or
"security" as an unlimited exception. A later authorized requirement may add a non-goal, but future
possibility alone does not.

## Example

For this installer, write: "Done when an install with no override resolves the official registry,
and an install with an explicit repository uses that custom registry." Write: "Not part of this
task: automatic mirror fallback, authentication plugins, multi-registry aggregation, generic file or
HTTP locators, and registry caching." Verification must cover both required paths; it need not build
or permanently forbid the non-goals.
