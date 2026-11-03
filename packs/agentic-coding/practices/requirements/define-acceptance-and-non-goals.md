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

You know what result the user wants, but have not yet chosen the implementation work. Write down
what must work at the end and which likely extras are not part of the task. If the result itself is
still unclear, clarify the user goal first.

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

Both a more reusable design and a smaller diff can look like improvements while missing the task.
Completion conditions keep required behavior from being cut; explicit non-goals keep attractive
extra features from becoming promises you now have to deliver.

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
