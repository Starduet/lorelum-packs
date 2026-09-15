---
anti_patterns:
  - description: Starting implementation before classifying the change against the repository's gates lands contract changes in a diff review where design debate is most expensive, or buries trivial fixes under heavyweight process.
    id: issue-pr-etiquette.pull-request.gate-classification-skipped
    name: Change started before its gate was classified
    severity: warn
applies_when: work on a change is about to start, and the contributor must decide whether the repository's process requires a prior issue or design alignment, or whether the change may go directly to a pull request
id: issue-pr-etiquette.pull-request.match-the-change-to-the-required-upstream-gate
severity: warn
stage: pull-request
tech_stack:
  - github-contribution
title: Match the Change to the Required Upstream Gate
---

## When to apply

Apply before writing code, when the change's class is known: does it alter a contract, interface, or
semantics that other work depends on, or is it a contained fix that does not. The decision is which
upstream gate the repository's process demands for that class.

## Guidance

Check the repository's contributing guide for what triggers a prior issue or a design artifact.
Changes that alter what other work depends on — public schemas, interfaces, evaluation semantics,
protocols — get a converging issue first, and a design artifact where the process requires one,
before implementation. Contained fixes that change no contract may go directly to a PR, but the
direct route carries its own duty: the PR body must state the root cause, the fix boundary, and how
the fix was verified. When the class is unclear, classify before writing code — asking in the issue
tracker is cheaper than re-review. Stop once the change has one gate and the artifact that gate
requires exists or is deliberately not required.

## Anti-pattern

An Agent rewires an evaluator's scoring semantics straight into a PR, because the diff is small.
Review stalls on "where was this agreed?" — three downstream suites depend on the old semantics, and
the debate happens line-by-line in a diff instead of in a single-issue design discussion. The
opposite failure also recurs: a typo fix waits weeks behind an issue-approval process meant for
contract changes.

## Why

Gates are placed where downstream work depends on stability; skipping one moves the design debate
into the most expensive venue, a diff review, and every reviewer re-litigates scope. Applying heavy
gates to trivial fixes spends the same review capacity on nothing, which is how mandatory processes
get quietly abandoned.

## Exceptions and boundaries

Repositories define their own urgency paths — an urgent revert or hotfix may merge first and file
its issue immediately after, in the order the repository's rules state. Documentation-only fixes
often follow a lighter gate; the contributing guide, not this Practice, defines which. When
contributing somewhere with no stated process, a linked issue for contract-class changes remains the
safe default.

## Example

Before changing how a test harness scores results, a contributor classifies the change: scoring
semantics is contract-class, so they first file an issue converging on the single behavior change
and wait for the validated change artifact the process requires. A README typo the same day goes as
a direct PR whose body states the root cause, the one-file fix boundary, and the rendered-docs check
that verified it.
