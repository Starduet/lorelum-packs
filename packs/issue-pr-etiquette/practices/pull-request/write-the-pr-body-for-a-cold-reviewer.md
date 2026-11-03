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

When opening a PR, explain what changed and how to check it for someone who has not followed your
work. Update that explanation when the change itself changes significantly. If the repository has no
template, start from the [pull request template](resource:assets/pull-request-template.md).

## Guidance

Write for a reviewer who has not read the issue thread, the chat discussion, or your local attempts.
Include:

- A summary of what changed and what deliberately did not change.
- The linked issue the PR resolves.
- The type of change, naming any interface or behavior that breaks compatibility.
- How you tested it: the exact commands you ran and the named scenarios you checked, not just
  "tested locally".
- The checklist required by the repository's template.
- Notes explaining design intent and what was deliberately deferred.

If you are submitting a direct fix without an issue, explain the root cause, exactly what the fix
covers, and how you verified it in the body itself; a link to a discussion is not enough. A reviewer
with no prior context should be able to tell what you claim the PR does and how to check that claim.

## Anti-pattern

The PR body reads "As discussed" and "See title". The reviewer opens a two-hundred-line diff with no
statement of intended behavior, discovers a breaking JSON field change by accident, and spends the
review reverse-engineering scope instead of checking it. The approval, when it comes, certifies the
reviewer's reconstruction — not the author's intent.

## Why

A reviewer's first questions are what the change claims and how to verify it. A self-contained body
lets them compare those claims with the diff instead of reconstructing the author's intent. It
exposes scope misunderstandings before approval and preserves verification evidence for future
readers who find the PR through the history.

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
