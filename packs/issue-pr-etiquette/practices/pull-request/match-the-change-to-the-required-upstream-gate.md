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

Before writing code, check whether you can open a PR directly or need agreement in an issue or
design document first. Follow the repository's process, especially when other work depends on the
interface or behavior you plan to change.

## Guidance

Read the contributing guide before starting implementation. Changes to public schemas, interfaces,
evaluation behavior, or protocols that other work depends on need an issue where the proposed change
is agreed first. Prepare a design document before implementation too if the repository requires one.

A contained fix that leaves those agreements unchanged may go directly to a PR. Its body must still
explain the root cause, exactly what the fix covers, and how you verified it. If you are unsure
whether an issue or design approval is needed, settle that before writing code; ask in the issue
tracker if necessary. You can proceed once you have completed the required prior steps or
established that the repository does not require them.

## Anti-pattern

An Agent rewires an evaluator's scoring semantics straight into a PR, because the diff is small.
Review stalls on "where was this agreed?" — three downstream suites depend on the old semantics, and
the debate happens line-by-line in a diff instead of in a single-issue design discussion. The
opposite failure also recurs: a typo fix waits weeks behind an issue-approval process meant for
contract changes.

## Why

Prior issue and design requirements let teams agree on changes before downstream work must adapt.
Skipping them moves the design debate into diff review, where reviewers must reconsider scope
alongside the code. Requiring the same process for trivial fixes wastes review time and encourages
contributors to stop following it.

## Exceptions and boundaries

Repositories define their own urgency paths — an urgent revert or hotfix may merge first and file
its issue immediately after, in the order the repository's rules state. Documentation-only fixes
often follow a lighter gate; the contributing guide, not this Practice, defines which. When
contributing somewhere with no stated process, a linked issue for contract-class changes remains the
safe default.

## Example

Before changing how a test harness scores results, a contributor identifies that other work depends
on the scoring behavior. They first file an issue focused on that behavior change and wait for the
issue or design approval the process requires. A README typo the same day goes as a direct PR whose
body states the root cause, the one-file fix boundary, and the rendered-docs check that verified it.
