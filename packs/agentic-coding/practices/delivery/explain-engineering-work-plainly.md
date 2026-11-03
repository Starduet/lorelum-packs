---
anti_patterns:
  - description: Replacing an explanation of what the code does with abstract engineering labels, unexplained project shorthand, or polished claims that hide the actual mechanism and its limits.
    id: agentic-coding.delivery.labels-instead-of-mechanism
    name: Labels instead of an engineering explanation
    severity: warn
applies_when: an agent's engineering explanation or work report uses abstract labels, project jargon, or tangled sentences that prevent a developer from understanding what the code does, why a change helps, or what remains uncertain
id: agentic-coding.delivery.explain-engineering-work-plainly
severity: warn
stage: delivery
tech_stack:
  - agentic-coding
title: Explain Engineering Work with Concrete Actions
---

## When to apply

Use this when explaining a diagnosis, design choice, implementation, or result to a developer and
the words hide what actually happens. Name the component, action, affected state, and consequence.
Keep technical terms that carry a real distinction, and explain unfamiliar project shorthand where
it matters. Clear engineering language preserves the mechanism instead of replacing it with a
slogan.

## Guidance

1. Replace labels such as "coordination landed" or "the lifecycle is closed" with what a component
   actually reads, writes, waits for, rejects, or returns, and why that changes the observed
   behavior. Name the responsible component when it is known; do not invent a cause or owner.
2. Match the developer's knowledge. Keep useful terms such as transaction, token, revision, or
   rollback. Explain an unfamiliar abbreviation or local concept at first use, not every common
   engineering term. Preserve exact code, paths, commands, quoted errors, and source destinations.
3. Split sentences when several actions or conditions hide their relationship. Keep a condition
   beside the effect it limits. Distinguish an observed result, a proposed mechanism, and an
   untested hypothesis instead of letting a fluent causal sentence merge them.
4. Compare the rewrite with the source facts. Preserve identifiers, quantities, units, environments,
   comparison bases, exceptions, negations, and uncertainty. Remove padded verbs, inflated success
   language, and repeated explanations. If the mechanism is not known, state the observation and the
   unknown; do not fill the gap with plausible technical prose.

Stop when the developer can explain what the component does differently and why it matters, or
identify exactly what is not yet known. Fewer words alone are not proof of a better explanation.

## Anti-pattern

The report says "concurrency credential lifecycle coordination is complete." A developer cannot tell
whether the change serializes requests, shares a refresh result, or retries failures. Replacing it
with "login is fixed" is shorter but even less precise. Say that simultaneous callers wait for one
refresh and reuse its result, if that is what the code does, then retain the actual verification
boundary.

## Why

A developer needs the mechanism to review correctness and make the next decision. Concrete component
actions let them connect code changes to behavior; abstract labels can sound complete while
concealing a wrong or unproven explanation.

## Exceptions and boundaries

Do not teach a specialist familiar basics or force casual slang into an engineering discussion. Keep
exact specifications, quotations, and requested output schemas intact. This Practice governs replies
to developers, not a broad rewrite of code, comments, documentation, or existing Practices. It does
not require fixed sentence lengths, a vocabulary blacklist, or an AI-detector target.

Use `agentic-coding.delivery.lead-with-engineering-conclusion` when understandable sentences bury
the answer. `agentic-coding.delivery.claim-only-supported-outcome` and
`agentic-coding.delivery.report-material-residuals` still decide the supported result and required
remaining issues. `pack-creator.authoring.prefer-plain-language-and-concrete-referents` governs
writing reusable Practices, not reporting the current engineering task.

## Example

The source says a worker retains the highest locally edited revision and advances the saved revision
only to the acknowledged revision. Instead of "the persistence lifecycle now converges," write "When
revision 12 finishes saving, the worker marks revision 12 as saved. Edits from revision 13 stay
pending." Do not turn that mechanism into a guarantee that crashes or multi-device edits are handled
when those cases have not been established.

Read the
[Chinese engineering before-and-after examples](resource:references/engineering-communication.md)
when checking whether a rewrite still says what the source facts support.
