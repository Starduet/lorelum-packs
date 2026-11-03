---
anti_patterns:
  - description: Rewriting published history mid-review or pushing changes during a formal review round orphans the reviewers' inline evidence and invalidates the conclusions they were forming.
    id: issue-pr-etiquette.pull-request.history-rewritten-mid-review
    name: Published history rewritten mid-review
    severity: warn
applies_when: review feedback has arrived on an open PR, or a formal review round is in progress, and the author must decide how to apply changes without destroying the review's record
id: issue-pr-etiquette.review.address-feedback-with-new-commits-and-freeze-during-review
severity: warn
stage: review
tech_stack:
  - github-contribution
title: Address Feedback with New Commits and Freeze During Review
---

## When to apply

Once others have been asked to review your PR, preserve the history they are reading when you
respond to feedback. If a formal or independent review round is running, also wait until it ends
before changing the branch. A branch nobody has been asked to review yet can still be rewritten.

## Guidance

Address feedback with new commits rather than rewriting commits reviewers have already read. Explain
in each commit which finding it addresses. Keep review-requested fixes separate from unrelated
improvements, and preferably put those improvements in separate PRs.

During a formal review round — an automated pass, an independent review, or a scheduled session —
leave the branch's code unchanged until the round ends. Record findings and queue the fixes instead
of pushing them while the review is running. Rebase or squash only when a reviewer asks or at the
checkpoint the repository defines. Every finding needs either a commit that addresses it or a
written reply explaining why you are not making that change.

## Anti-pattern

Midway through a two-round review, the author force-pushes a "cleaned up" history. Every inline
comment from round one now points at lines missing from the new history. The independent reviewer
must start again, and a finding about a real race condition is lost with its original context. The
final merge carries a defect the review process had already caught.

## Why

Reviewers base findings on a specific commit. Adding commits preserves that version and shows which
fix addresses each finding. Rewriting history removes those references; pushing mid-round means
reviewers may reach conclusions about different versions. Multiple independent rounds need the same
unchanged version if their conclusions are to be compared.

## Exceptions and boundaries

A reviewer may explicitly request a rebase or squash at a defined point — follow the request then,
not before. A branch not yet opened for review is private history and may be rewritten freely.
Urgent fixes that must land while a round runs follow the repository's stated urgency path rather
than silence, and the round is re-run rather than continued against a moved target.

## Example

Round one of a structured review returns six findings. The author fixes five in separate commits
titled `fix: guard snapshot race (review r1-3)` and replies on the sixth explaining why the
suggestion would break a pinned behavior. Round two reviews the frozen result with every finding
either addressed or answered, and signs off in one pass.
