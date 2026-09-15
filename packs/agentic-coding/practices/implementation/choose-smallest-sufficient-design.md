---
anti_patterns:
  - description: Choosing extra layers, configuration, stored state, or data passes because nearby code or roadmap hints make future variants feel likely, even though a less complex design already protects everything the current task requires.
    id: agentic-coding.implementation.architecture-for-possibility
    name: Architecture for possibility
    severity: warn
applies_when: two or more implementation designs can satisfy the required behavior, and the agent must choose how much new abstraction, state, indirection, or I/O the current change actually needs
id: agentic-coding.implementation.choose-smallest-sufficient-design
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Choose the Least Complex Design That Fully Works
---

## When to apply

Apply after viable options are understood and before choosing a structure. This Practice compares
designs that can all meet the requirement. It does not decide whether the repository, a dependency,
or the runtime already provides the needed behavior. If only one option meets the behavior, safety,
or compatibility requirements, there is no design-size choice to make.

## Guidance

List the required behavior and rules that must stay true, such as authorization, compatibility, or
data integrity. Discard any option that misses them. From the rest, choose the design that adds the
fewest responsibilities and is easiest to reverse in the current code. Require a present reason for
every extra layer, stored state, fallback, or data pass. Stop with one design and why it fully meets
the task. Count data passes and failure branches as complexity too: a direct typed call can be
smaller than a short chain of validation wrappers, reparsing, and fallback defaults. A more
defensive option is not automatically sufficient if it rejects supported input or hides an actual
failure.

## Anti-pattern

The user asks for one discount rule. A roadmap note mentions future pricing rules, and the
repository has a generic pipeline elsewhere. A configurable rule pipeline and plugin boundary
therefore look consistent and future-proof, and their focused tests pass. But the task needs one
rule, so the new contracts and failure modes add maintenance without serving the request.

## Why

New structure creates interactions, failure modes, and maintenance commitments. Choosing less
structure reduces that cost only after every required behavior and protection is preserved; a
smaller diff is not success by itself.

## Exceptions and boundaries

Security isolation, migration safety, published compatibility, measured performance limits, or an
approved near-term requirement may make the larger option the smallest sufficient design. Do not
remove meaningful behavior or protection to reduce line count. Name the concrete condition that
requires the larger option; a general desire for robustness is insufficient. If the options place a
rule in different components, decide which component owns that rule before comparing internal
designs.

## Example

The user asks for one thumbnail in a supported image format. The current image operation preserves
metadata and reports decode failures correctly. A small adapter and a transform graph could both
work, but only the adapter avoids a new configuration model. The agent chooses it and keeps the
existing protections; a graph can wait until configurable, composable transforms are accepted.
