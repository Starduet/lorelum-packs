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

Apply while assembling a PR and whenever work uncovers an adjacent problem worth fixing. The
decision is whether each changed hunk belongs to the change the PR title declares. Do not apply to a
mechanical repository-wide change, which is itself one declared scope.

## Guidance

Make the PR title declare one scope, then hold every hunk to it: a hunk belongs only if reverting
the PR should remove it. Resist folding in the small things found along the way — the unrelated
typo, the stale test, the tempting refactor — and file each as its own change, however tiny. Where
the repository convention is one issue per PR, link exactly the issue this PR resolves and leave
sibling issues to sibling PRs. If a discovered problem blocks the current change, fix the minimum
that unblocks and file the rest. Stop when the diff reads as one reviewable unit whose removal or
revert is a single decision.

## Anti-pattern

While fixing an off-by-one error, a contributor also reformats the surrounding module and bumps a
dependency that "was asking for it". The PR now carries three risks; the reviewer who approves the
bug fix approves all three, a later regression cannot be bisected to one change, and reverting the
dependency bump would tear out the bug fix with it.

## Why

Review, revert, bisect, and cherry-pick all operate at PR granularity. A single scope means one
approval covers one risk, one revert is one decision, and history stays attributable; mixed scope
silently converts every approval into a package deal and couples unrelated failures together.

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
