---
anti_patterns:
  - description: Bundling several deliverables into one issue with vague completion wording forces reviewers to accept or reject them together and leaves no one able to tell when the issue is done.
    id: issue-pr-etiquette.issue.multi-deliverable-issue-with-uncheckable-done
    name: Multi-deliverable issue with an uncheckable definition of done
    severity: warn
applies_when: a contributor is about to file a bug or feature issue and must decide what single problem the issue owns and how someone else will later be able to tell it is resolved
id: issue-pr-etiquette.issue.converge-on-one-problem-with-testable-acceptance-criteria
severity: warn
stage: issue
tech_stack:
  - github-contribution
title: Converge on One Problem with Testable Acceptance Criteria
---

## When to apply

Before filing a bug or feature issue that someone will track, assign, or schedule, make it clear
which problem you want solved and how another person could tell it is fixed. Keep untracked
questions in the discussion channel they were directed to. If the repository allows a direct PR for
a small change, you do not need to create an issue just to follow this guidance.

## Guidance

Use the title and opening paragraph to describe one problem. Explain what is affected, what you are
leaving out, which other work it depends on, and how a fix must be verified. Write acceptance
criteria as a checklist that someone other than you can test: a command that should succeed, a
document that should exist, or a behavior they should be able to observe.

If part of the work could be reviewed, merged, or reverted independently, give it its own issue and
link it. Start from the [feature issue template](resource:assets/issue-template-feature.md) or the
[bug report template](resource:assets/issue-template-bug.md), removing sections that do not help
explain this problem. Before submitting, make sure every criterion can be checked objectively and
that no paragraph introduces a second piece of work to deliver.

## Anti-pattern

A team files "Improve search" covering ranking quality, the indexing pipeline, and the results UI,
with "search works better" as the only completion wording. The ranking fix lands first, but the
issue cannot close because the UI work never started. Two teams attach their own priorities, and the
acceptance discussion restarts in every review because nobody agreed on how to check "better".

## Why

Reviewers accept an issue, teams schedule its work, and maintainers decide when to close it. Keeping
it to one problem lets them make those decisions together. Testable criteria let maintainers check
whether the work is done instead of negotiating what "done" means; unrelated deliverables can keep
an otherwise resolved issue open and bury acceptance questions in unrelated discussion.

## Exceptions and boundaries

An umbrella issue is legitimate when each child deliverable has its own issue with its own criteria
and the umbrella only tracks them. Exploratory discussion may be broad before it converts into a
tracked issue; convergence is required at conversion time, not before the topic is understood.
Acceptance criteria may reference a spec or design document instead of restating it, but the
checklist itself must still be checkable from the issue.

## Example

A contributor notices that real usage of a tool keeps exposing defects that fixtures never catch.
Instead of filing "improve feedback", they file an issue covering one problem: there is no
privacy-safe channel from real usage back to the maintainers. The boundary excludes storage and
schema choices, and the acceptance criteria are seven checkboxes — each naming a document that must
exist or a distinction the workflow must make — that a maintainer can verify without asking the
author what was meant.
