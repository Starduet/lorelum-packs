---
anti_patterns:
  - description: Preserving source jargon because it sounds authoritative, even though readers and translators cannot map the words to one observable action or object.
    id: pack-creator.authoring.abstract-language-as-precision
    name: Abstract language mistaken for precision
    severity: warn
applies_when: a Practice uses abstract nouns, compressed jargon, or coined terms where the author could name the actual person, artifact, action, or observable state
id: pack-creator.authoring.prefer-plain-language-and-concrete-referents
severity: warn
stage: authoring
tech_stack:
  - lorelum-pack-authoring
title: Use Plain Words for Concrete Things
---

## When to apply

If a first-time reader would have to decode your wording before knowing what to do, revise the
sentence. Check not only unfamiliar terms but also passages that classify the problem or compare
other Practices before explaining the reader's situation. This review concerns how you explain the
guidance; whether its reason is correct and its Example has enough facts are separate questions.

## Guidance

Start with the situation the reader can recognize and the action that helps. Say who needs to do
what, to which file, data, or system, and what result they should look for. A category label may
help index content, but it does not replace that explanation. Keep distinctions between related
Practices where they affect the choice, after explaining the useful action. If a necessary technical
term would be unfamiliar, clarify it where it appears, then use it consistently. Prefer an ordinary
sentence to a coined label followed by a definition; no separate introduction or summary is
required. Stop when readers and translators can understand the situation, action, and expected
result without guessing what the words refer to.

## Anti-pattern

An operations Pack turns incident guidance into "operationalize the observability posture through
telemetry harmonization." The phrase resembles the policy source and therefore feels precise and
defensible. But it does not say whether the engineer should align field names, sampling rates, alert
thresholds, or dashboards, so different readers and translations produce different actions while
preserving the same impressive words.

## Why

Readers can act on a description of their situation and what to do about it. Abstract labels can
hide different interpretations, weakening both retrieval matching and human review across languages.

## Exceptions and boundaries

Keep standard domain terms when practitioners use them consistently and the distinction matters.
Legal or regulatory wording may need to remain exact, but explain the operational object or action
it governs. Do not replace precise technical language with a longer but equally vague paraphrase.

## Example

A compliance Pack helps reviewers decide whether an exception is auditable. Its source requires the
request, approver, and governing policy version to be recorded. Instead of "retain sufficient
exception provenance," the author writes, "Record who requested and approved the exception and which
policy version allowed it." Reviewers can check each fact, and no new compliance rule was invented.
