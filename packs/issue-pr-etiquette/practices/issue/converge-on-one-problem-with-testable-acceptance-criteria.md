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

Apply before submitting an issue that will be tracked, assigned, or scheduled. The decision is what
single problem the issue owns, what sits outside it, and what observable result counts as resolved.
Do not apply to untracked questions already routed to a discussion channel, or to changes small
enough that the repository's process allows a direct pull request.

## Guidance

State one problem in the title and opening paragraph. Name its boundary (what is affected and what
is explicitly not), its dependencies on other work, and the verification requirements a fix must
satisfy. Write acceptance criteria as a checklist where each item is testable by someone who is not
the author: a command that should succeed, a document that should exist, a behavior that should be
observable. Split out anything that could be reviewed, merged, or reverted independently — file it
as its own issue and link it. Start from the
[feature issue template](resource:assets/issue-template-feature.md) or the
[bug report template](resource:assets/issue-template-bug.md) and remove sections that do not serve
the single problem. Stop when every criterion is objectively checkable and no paragraph of the body
introduces a second deliverable.

## Anti-pattern

A team files "Improve search" covering ranking quality, the indexing pipeline, and the results UI,
with "search works better" as the only completion wording. The ranking fix lands first, but the
issue cannot close because the UI work never started. Two teams attach their own priorities, and the
acceptance discussion restarts in every review because nobody agreed on what "better" observes.

## Why

An issue is the unit reviewers accept, schedulers sequence, and maintainers close. A single problem
keeps that unit reviewable, and testable criteria make closure a check instead of a negotiation;
mixed deliverables block partial progress and bury the acceptance question inside unrelated
discussion.

## Exceptions and boundaries

An umbrella issue is legitimate when each child deliverable has its own issue with its own criteria
and the umbrella only tracks them. Exploratory discussion may be broad before it converts into a
tracked issue; convergence is required at conversion time, not before the topic is understood.
Acceptance criteria may reference a spec or design document instead of restating it, but the
checklist itself must still be checkable from the issue.

## Example

A contributor notices that real usage of a tool keeps exposing defects that fixtures never catch.
Instead of filing "improve feedback", they file an issue owning one problem: there is no
privacy-safe channel from real usage back to the maintainers. The boundary excludes storage and
schema choices, and the acceptance criteria are seven checkboxes — each naming a document that must
exist or a distinction the workflow must make — that a maintainer can verify without asking the
author what was meant.
