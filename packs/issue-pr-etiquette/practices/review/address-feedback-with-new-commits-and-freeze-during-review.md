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

Apply whenever responding to review feedback on a PR others are reviewing, and whenever a formal or
independent review round is running against the branch. The decision is how changes reach the branch
and when. Do not apply to a branch nobody has been asked to review yet.

## Guidance

Respond to feedback by adding commits to the branch, not by rewriting the history reviewers have
already read; each commit should state which finding it addresses. Keep a review-requested fix and
any unrelated improvement in separate commits, and prefer separate PRs for the unrelated ones. When
the repository runs a formal review round — an automated pass, an independent reviewer, a scheduled
session — freeze code changes on the branch until the round concludes: record findings and queue
fixes instead of pushing them mid-round. Rebase or squash only when the reviewer asks for it or at
the repository's defined checkpoint. Stop when every finding has either a commit that addresses it
or a written reply saying why not.

## Anti-pattern

Midway through a two-round review, the author force-pushes a "cleaned up" history. Every inline
comment from round one is orphaned, pointing at lines that no longer exist; the independent reviewer
restarts from zero, and one of the orphaned findings — a real race condition — is lost in the
rewrite. The final merge carries a defect the review process had already caught.

## Why

Review evidence attaches to the commit state reviewers read. New commits extend that record so each
finding stays traceable to its fix; rewriting destroys the mapping, and mid-round changes invalidate
the round's conclusions, so the process pays for review it cannot use. The cost compounds when
multiple independent rounds must agree on one frozen state.

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
