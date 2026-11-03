---
anti_patterns:
  - description: The author preserves separate, familiar rules because they came from different sources, even though readers describe both with the same query and cannot tell which action applies.
    id: pack-creator.design.neighbor-collision-by-label
    name: Familiar labels hide a retrieval collision
    severity: warn
applies_when: two or more atomic Practice drafts appear relevant to the same realistic query, and the author must distinguish their triggers and actions or merge them
id: pack-creator.design.separate-neighboring-triggers
severity: warn
stage: design
tech_stack:
  - lorelum-pack-authoring
title: Separate Practices That Compete for the Same Query
---

## When to apply

When two separate Practice drafts both look like answers to the same request, compare what each
would tell the reader to do. Titles and subject areas are not enough to distinguish them. This is
the check to make after splitting a draft that covered several independently useful decisions.

## Guidance

Write a realistic request and a paraphrase for each draft. Try the first draft's request against the
second: it should be a close but unsuitable match, and vice versa. Explain what fact changes which
action is appropriate. Revise the trigger, title, and guidance until someone reading them for the
first time can choose the right Practice for each case. If there is no meaningful difference, merge
the drafts or reconsider what each should answer instead of relying on subtle wording. Stop when
both are selected only because both decisions really need attention, not because either could answer
the same question.

## Anti-pattern

A web-security Pack should help developers choose the right control for untrusted data. It contains
"Validate User Input" from an API guide and "Sanitize User Input" from a frontend review checklist.
Both say they apply when handling untrusted text, and keeping the familiar labels seems easier for
reviewers than challenging the sources. A developer asking how to safely display a profile name
retrieves both, one recommending rejection and the other vague cleaning, without learning that
output encoding at the HTML sink is the needed decision. The author should distinguish
trust-boundary validation from context-specific output encoding, or merge the entries if the Pack
cannot sustain that boundary.

## Why

Even files that each answer one question can be poor retrieval targets when their selection
conditions are indistinguishable. Naming when one applies but its neighbor does not reduces
irrelevant retrieval and conflicting actions.

## Exceptions and boundaries

Two Practices may correctly retrieve together when a situation contains two separate decisions. That
is not a collision if each Practice owns a different action and remains useful. Domain terms can
stay in titles when readers actually use them, but labels alone cannot carry the boundary.

## Example

A database-performance Pack should help engineers decide how to improve slow queries without adding
unjustified indexes. It has one Practice for deciding whether a new index is justified by a
recurring query pattern and another for checking the execution plan after an index or query changes.
A request proposing an index before implementation selects the first; a report that an existing
indexed query became slow selects the second. The author states those moments and actions
explicitly. A broad request covering both design and regression may retrieve both because both
decisions are present.
