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

1. List the required behavior and the rules that must stay true — authorization, compatibility, data
   integrity, required errors and limits. Discard any option that misses one.
2. Count what each remaining option adds: new state, indirection, layers, fallbacks, and data passes
   (failure branches count too), rather than lines.
3. Choose the design that adds the fewest responsibilities and is easiest to reverse in the current
   code. Require a present reason for every extra layer, stored state, fallback, or data pass.
4. If a larger option seems necessary, name the concrete condition — security isolation, migration
   safety, published compatibility, measured performance limits, or an approved near-term
   requirement.

Stop with one design and one sentence on why it fully meets the task. A more defensive option is not
automatically sufficient if it rejects supported input or hides an actual failure, and a smaller
diff is not success by itself. A direct typed call can be smaller than a short chain of validation
wrappers, reparsing, and fallback defaults.

## Anti-pattern

The user asks for one discount rule. A roadmap note mentions future pricing rules, and the
repository has a generic pipeline elsewhere. A configurable rule pipeline and plugin boundary
therefore look consistent and future-proof, and their focused tests pass. But the task needs one
rule, so the new contracts and failure modes add maintenance without serving the request.

## Why

New structure creates interactions, failure modes, and maintenance commitments. Choosing less
structure reduces that cost only after every required behavior and protection is preserved.

## Exceptions and boundaries

Do not remove meaningful behavior or protection to reduce line count. If the options place a rule in
different components, decide which component owns that rule before comparing internal designs.

## Example

The user asks for one thumbnail in a supported image format. Two viable designs remain: a small
adapter around the current image operation, and a transform graph. Both satisfy the request, but
only the adapter avoids a new configuration model and extra data passes. The agent chooses the
adapter and keeps the existing metadata preservation and decode-failure reporting; a graph can wait
until configurable, composable transforms are accepted.
