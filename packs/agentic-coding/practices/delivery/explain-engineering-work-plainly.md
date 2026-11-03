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

Use this when a developer can read the report but still cannot tell what the code does, why the
change helps, or what remains unknown. Explain which component acts, what it changes, and what
happens as a result. Keep technical terms that express a useful distinction, explaining unfamiliar
project shorthand where needed. A shorter slogan is not a clearer explanation.

## Guidance

1. Replace labels such as "coordination landed" or "the lifecycle is closed" with what actually
   happens: which component reads, writes, waits for, rejects, or returns what, and how that changes
   behavior. Name the responsible component when it is known; do not invent a cause or owner.
2. Explain for this reader. Keep useful terms such as transaction, token, revision, or rollback.
   Explain an unfamiliar abbreviation or project name where it first matters, without teaching a
   specialist common basics. Keep code, paths, commands, quoted errors, and source destinations
   exactly as given.

   If only part of a structured reply may change, copy the protected values unchanged and rewrite
   only the permitted text. Before sending, compare those values and the requested output shape with
   the source; do not translate them or add punctuation.

3. Separate actions or conditions when putting them in one sentence hides their relationship. Keep
   each condition beside the result it limits. Say whether a change is proposed, implemented, or
   observed to work. A failed check is not merely an untested case. "Not yet shown to meet the
   requirement" does not mean "cannot meet it." Clear prose must not turn an unknown into a fact.
4. Compare the rewrite with the source facts. Keep identifiers, quantities, units, environments,
   comparison bases, exceptions, negations, and uncertainty. Remove padded verbs, inflated success
   claims, and repeated explanations, not facts needed to judge the result. If the mechanism is
   unknown, describe the observation and what is missing rather than supplying a plausible story.

You have explained enough when the reader understands what happens differently and why it matters,
or exactly what remains unknown. Shorter wording alone is not a better explanation.

## Anti-pattern

The report says "concurrency credential lifecycle coordination is complete." A developer cannot tell
whether the change serializes requests, shares a refresh result, or retries failures. Replacing it
with "login is fixed" is shorter but even less precise. Say that simultaneous callers wait for one
refresh and reuse its result, if that is what the code does, then retain the actual verification
boundary.

## Why

To judge correctness and choose the next step, a developer needs to know how the change works.
Describing the component's actions connects the code to its behavior. An abstract label can sound
convincing while hiding an explanation that is wrong or has not been checked.

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
