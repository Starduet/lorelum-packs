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

If AI wrote or substantially reshaped your code, tests, or prose, explain that contribution in the
PR. If you ran an AI review, record what it found and how you responded. Incidental spell-check or
autocomplete below the relevant policy's threshold does not need this disclosure.

## Guidance

Use the repository's disclosure checkbox or section, and say which parts AI drafted and which it
only polished. If an AI review ran, describe its findings in the PR body and what you changed in
response. Include findings you rejected and explain why.

Do not use "every line was reviewed" as evidence. Say what you checked and how so readers have
something they can verify. Check AI-suggested changes yourself before adopting them; you remain
responsible for the work. The PR should make clear what AI contributed, what it found, and what you
did about it.

## Anti-pattern

An Agent drafts a PR and checks no disclosure box, describing the body as fully hand-verified. After
merge, a defect appears that matches, almost word for word, a finding in an AI review that was run
and ignored. Reviewers discover that the claimed verification omitted a known finding, and have less
reason to trust the contributor's later claims.

## Why

Reviewers need to know how the work and its evidence were produced. Knowing which parts are
AI-drafted helps them decide where to inspect closely. Recorded findings give them specific problems
and responses to check; "every line was reviewed" does not. An ignored finding that later causes a
defect undermines trust in that claim. Honest disclosure lets maintainers adjust review before an
incident reveals the gap.

## Exceptions and boundaries

Incidental assistance below the policy's threshold — spelling, formatting, import completion — needs
no disclosure. A repository without any AI policy still gets the substance: record material AI
review findings in the body even where no checkbox exists. Disclosure tells readers how the work was
produced; it does not grant permission that repository policy withholds. It is not an apology and
does not reduce the author's responsibility for every merged line.

## Example

A PR body's assistance section checks the AI box, states the AI drafted the validator and the author
rewrote the error mapping, then lists five concrete findings from the AI review — four fixed in
commits it links, one rejected with the reason. A reviewer reads the section, spends their attention
on the rewritten parts, and cites the recorded findings as part of the approval.
