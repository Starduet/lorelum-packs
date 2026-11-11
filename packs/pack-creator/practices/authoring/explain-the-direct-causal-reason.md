---
anti_patterns:
  - description: Explaining a rule with broad ideals or remote business value because they sound important, while omitting the immediate mechanism that makes the action necessary.
    id: pack-creator.authoring.distant-rationale
    name: Distant benefit used as the rationale
    severity: warn
applies_when: readers need a direct explanation of the consequence of following or ignoring a Practice's action to make the decision
id: pack-creator.authoring.explain-the-direct-causal-reason
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Explain the Immediate Cause and Effect
---

## When to apply

When readers know what to do but need to understand why it matters, explain the direct consequence
of doing it or leaving it undone. No separate reason section is required.

## Guidance

Explain what happens if the reader takes or omits the action, starting with the first important
change in system behavior or in the decision, then say why it affects the outcome. Keep the causal
chain short and supported by the scenario or source. Remove mission statements and benefits that
could describe almost any good Practice. Stop when the reason helps readers recognize a similar
situation where the rule does not apply, or judge whether an exception is justified.

## Anti-pattern

A database Pack requires large indexes to be built with an online method. The source records show
that blocking index creation held write locks and delayed orders. Because the Pack supports a
high-level reliability program, the author writes only that "reliable data platforms protect
customer trust and business continuity." The statement is true and persuasive, but it does not
explain the lock mechanism, so readers cannot tell why this index operation differs from a harmless
metadata change.

## Why

The immediate cause lets readers transfer a rule to new situations and identify when its conditions
are absent. A distant benefit may motivate agreement but cannot guide the technical decision.

## Exceptions and boundaries

Some policy rules are justified by an external obligation rather than a technical mechanism. Name
the controlling obligation and the direct compliance consequence instead of inventing engineering
causality. Do not extend the chain beyond what the source supports.

## Example

A security Pack says to verify a token's audience before accepting it. It explains: "Audience
verification prevents a token issued for another service from being accepted by this service." That
direct effect explains both the action and its security boundary; a generic claim that validation
"improves trust" would not.
