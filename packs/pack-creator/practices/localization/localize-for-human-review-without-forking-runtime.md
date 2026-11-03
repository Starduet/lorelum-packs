---
anti_patterns:
  - description: Editing localized IDs, triggers, decisions, or release behavior independently to improve one language creates two competing Pack meanings that can drift and retrieve differently.
    id: pack-creator.localization.localized-runtime-fork
    name: Localized copy becomes a second runtime Pack
    severity: warn
applies_when: canonical Practices are being translated for human readers, and the author must make the localized text natural and reviewable while keeping one canonical runtime identity and decision meaning
id: pack-creator.localization.localize-for-human-review-without-forking-runtime
severity: warn
stage: localization
tech_stack:
  - lorelum-pack-authoring
title: Localize for Human Review without Forking Runtime Meaning
---

## When to apply

When adding or updating a translation, make it easy for reviewers in that language to understand the
same guidance. Do not let it become a second Pack with different rules: the canonical Practice IDs,
files used at runtime, and intended decisions must remain the shared reference.

## Guidance

Translate the decision, not the English word order. Preserve the Practice and anti-pattern
identities, trigger conditions, required action, stopping point, exceptions, causal reason, and
example relationships. Replace an idiom or unfamiliar term with natural language in the target
language when the meaning stays the same. Follow the repository's localization layout: companions
correspond to canonical IDs but do not need copies of runtime frontmatter. Keep them outside the
canonical runtime input, and record which canonical revision each translation represents. Have a
target-language reviewer check readability and meaning against the canonical file. Stop when every
localized Practice is current, reviewable, and traceable to one canonical Practice; do not add
language-specific runtime rules merely to make the translation feel more useful.

## Anti-pattern

A compliance Pack is translated for regional reviewers. The canonical Practice says to retain
customer records for the period defined by the applicable policy and to escalate conflicting rules.
A local reviewer asks for a concrete number, and the translator knows that one business unit
commonly uses seven years. Adding “seven years” only to the translation seems helpful and saves a
policy lookup. It also creates a second rule that can outlive the business-unit policy and
contradict the canonical trigger for other users.

## Why

Natural translation helps people spot unclear guidance and domain mistakes. If translated files
instead supply their own runtime rules, the same Practice ID can tell readers to make different
decisions, with no single source in which to fix them.

## Exceptions and boundaries

A localized note may explain a term, regulation name, or example for readers when it is clearly
marked as non-canonical context and does not change the decision. A market-specific rule that should
affect runtime behavior belongs in its own canonical Practice or Pack with an explicit trigger, not
in a translation. This Practice does not require literal sentence alignment.

## Example

A database-operations Pack uses the English phrase “fail closed” in a Practice about restoring
access controls after recovery. The Chinese reviewer finds a literal translation unclear. The
translator rewrites it as a concrete instruction: if the permission state cannot be verified, keep
access denied and ask an operator to resolve it. The Practice and anti-pattern IDs stay unchanged,
the example preserves the same recovery sequence, and the localization record points to the reviewed
canonical revision. No localized file is added to the runtime Pack root.
