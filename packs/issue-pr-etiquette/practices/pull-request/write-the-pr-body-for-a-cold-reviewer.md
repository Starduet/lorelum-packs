---
anti_patterns:
  - description: A PR body that assumes the reviewer shares the author's context forces review to become archaeology, so scope and verification get argued line-by-line in the diff.
    id: issue-pr-etiquette.pull-request.context-dependent-pr-body
    name: PR body that assumes shared context
    severity: warn
applies_when: a PR is about to be opened, and the author must write a body from which a reviewer with none of the author's context can verify the change without asking a question first
id: issue-pr-etiquette.pull-request.write-the-pr-body-for-a-cold-reviewer
severity: warn
stage: pull-request
tech_stack:
  - github-contribution
title: Write the PR Body for a Cold Reviewer
---

## When to apply

Apply when opening any PR, and again when its body needs updating after significant changes. The
decision is what the body contains so that review starts from verification rather than
reconstruction. Start from the [pull request template](resource:assets/pull-request-template.md)
when the repository provides none.

## Guidance

Write for a reviewer who has not read the issue thread, the chat discussion, or your local attempts.
Include: a summary saying what changed and what deliberately did not change; the linked issue the PR
resolves; the type of change, naming the breaking surface when there is one; how it was tested — the
verbatim commands you ran plus the named scenarios you exercised, not a summary adjective like
"tested locally"; the checklist the repository's template asks for; and notes for reviewers stating
design intent and what was deliberately deferred. For a direct-fix PR with no issue, the body
additionally carries the root cause, the fix boundary, and the verification — those duties cannot be
delegated to a linked discussion. Stop when a cold reader can answer "what does this claim to do,
and how do I check it" from the body alone.

## Anti-pattern

The PR body reads "As discussed" and "See title". The reviewer opens a two-hundred-line diff with no
statement of intended behavior, discovers a breaking JSON field change by accident, and spends the
review reverse-engineering scope instead of checking it. The approval, when it comes, certifies the
reviewer's reconstruction — not the author's intent.

## Why

A reviewer's first questions are what the change claims and how to verify it. A self-contained body
converts review from archaeology into checking stated claims against a diff, catches scope
misunderstanding before approval rather than after merge, and preserves the verification evidence
for the future reader who finds this PR from the history.

## Exceptions and boundaries

A one-file fix still needs one sentence of summary and one sentence of verification; small is not
exempt, only shorter. Very large ports may link a design document for depth, but the body must still
summarize the change and its verification in its own words. The template sections are a floor, not a
ceiling — add sections the change needs, and drop none that the repository requires.

## Example

A PR adding a resource protocol opens with a two-paragraph summary including one sentence on what
resources deliberately do not affect, links `Closes #161`, checks the new-feature and breaking boxes
with a note naming the required field, lists the five verbatim commands from `bun test` to
`git diff --check`, walks six named regression scenarios, and closes with notes telling reviewers
which design decisions are out of scope. Review of the diff starts in the first hour.
