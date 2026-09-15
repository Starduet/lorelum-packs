---
anti_patterns:
  - description: Presenting AI-drafted work as unaided, or claiming blanket line-by-line verification instead of recording what the AI review actually found, misprices the review evidence the repository depends on.
    id: issue-pr-etiquette.review.undisclosed-or-unsubstantiated-ai-involvement
    name: Undisclosed or unsubstantiated AI involvement
    severity: warn
applies_when: AI tools materially helped draft a change, its tests, or its review, and the PR body is being written or AI review findings are being handled
id: issue-pr-etiquette.review.disclose-ai-assistance-and-its-review-findings
severity: warn
stage: review
tech_stack:
  - github-contribution
title: Disclose AI Assistance and Its Review Findings
---

## When to apply

Apply when preparing a PR where an AI tool wrote or materially reshaped code, tests, or prose, or
where an AI review pass ran over the change. The decision is what the PR records about that
involvement. Do not apply to incidental spell-check or autocomplete below the threshold any relevant
policy names.

## Guidance

Declare the assistance where the repository asks for it — the template checkbox or section — and
state its scope concretely: which parts the AI drafted, which it only polished. When an AI review
ran, record in the PR body what it found and what this branch changed as a result; name the
findings, including the ones you rejected and why. Do not offer "every line was reviewed" as
evidence: verification claims state what was checked and how, and blanket assurance is not an
acceptance criterion anywhere. Verify AI-suggested changes yourself before adopting them — the
disclosure covers your judgment, not the tool's. Stop when a reader can tell what the AI
contributed, what it found, and what you did about it.

## Anti-pattern

An Agent drafts a PR and checks no disclosure box, describing the body as fully hand-verified. After
merge, a defect appears that matches, almost word for word, a finding in an AI review that was run
and ignored. The repository learns its review evidence was mispriced, and every later claim from
that contributor carries a discount.

## Why

Reviewers weigh evidence by its provenance. Knowing which parts are AI-drafted tells them where to
look hardest; recorded AI findings are actionable review signal, while blanket "reviewed" claims are
unverifiable and — when contradicted by an ignored finding — destroy trust far beyond the one PR.
Honest disclosure lets the repository calibrate its process instead of discovering its gaps in an
incident.

## Exceptions and boundaries

Incidental assistance below the policy's threshold — spelling, formatting, import completion — needs
no disclosure. A repository without any AI policy still gets the substance: record material AI
review findings in the body even where no checkbox exists. Disclosure describes provenance; it is
not an apology and does not reduce the author's ownership of every merged line.

## Example

A PR body's assistance section checks the AI box, states the AI drafted the validator and the author
rewrote the error mapping, then lists five concrete findings from the AI review — four fixed in
commits it links, one rejected with the reason. A reviewer reads the section, spends their attention
on the rewritten parts, and cites the recorded findings as part of the approval.
