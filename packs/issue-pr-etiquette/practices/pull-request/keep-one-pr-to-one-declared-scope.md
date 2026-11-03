---
anti_patterns:
  - description: Folding adjacent improvements into the change being reviewed packages unrelated risk under one approval, so reviewers must accept everything to get anything.
    id: issue-pr-etiquette.pull-request.drive-by-changes-folded-in
    name: Drive-by changes folded into the declared scope
    severity: warn
applies_when: a PR is being assembled and its diff, or the temptation while working, risks covering more than the single change the PR title declares
id: issue-pr-etiquette.pull-request.keep-one-pr-to-one-declared-scope
severity: warn
stage: pull-request
tech_stack:
  - github-contribution
title: Keep One PR to One Declared Scope
---

## When to apply

When preparing a PR, check whether everything in the diff belongs to the change described by its
title. Do this again if you find another problem worth fixing along the way. A mechanical change
across the repository can still be one change; touching many files is not itself a reason to split
it.

## Guidance

Use the title to say what this PR changes. For each changed block, ask whether it should go away if
the PR is reverted. Leave out unrelated typos, stale tests, or refactors you found along the way;
submit each separately, however small. If the repository expects one issue per PR, link exactly the
issue this PR resolves and leave the others for other PRs.

If another problem prevents this change from working, fix only what is needed to unblock it and file
the rest separately. Keep the diff to work that reviewers can approve together and maintainers can
revert together without also undoing an unrelated improvement.

## Anti-pattern

While fixing an off-by-one error, a contributor also reformats the surrounding module and bumps a
dependency that "was asking for it". The PR now carries three risks; the reviewer who approves the
bug fix approves all three, a later regression cannot be bisected to one change, and reverting the
dependency bump would tear out the bug fix with it.

## Why

Keeping one scope lets reviewers approve a change without also accepting unrelated work. It also
lets maintainers revert or cherry-pick it independently and trace a regression to the change that
caused it. Mixed scopes force those decisions together even when the failures are unrelated.

## Exceptions and boundaries

A mechanical sweep — formatting, a rename, a codemod — is legitimate as one PR when its title
declares exactly that mechanical scope. Changes that cannot compile or behave apart, such as an API
and its in-repo callers, are one scope despite touching many files. A tiny follow-up may ride along
only when the repository's convention explicitly allows it, and then it is named in the body.

## Example

Mid-fix, the author notices a misspelled log message and a stale comment in a neighboring file. They
finish the fix at minus twelve plus four lines, then open two one-line PRs for the typo and the
comment, each with its own verification sentence. All three review in minutes; a later revert of the
fix touches nothing else.
