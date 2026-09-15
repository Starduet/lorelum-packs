---
anti_patterns:
  - description: The agent optimizes for fewer lines or files because a smaller diff looks disciplined, removing required behavior or protection while retaining conventional additions that have no present purpose.
    id: agentic-coding.review.deletion-as-success
    name: Deletion as success metric
    severity: warn
applies_when: a completed implementation diff is about to be committed or handed off, and its added files, abstractions, fallbacks, interfaces, I/O, tests, or documents have not been checked for a current reason to remain
id: agentic-coding.review.run-subtractive-review-before-commit
severity: warn
stage: review
tech_stack:
  - agentic-coding
title: Remove Unneeded Changes Before Commit
---

## When to apply

Apply when the completed diff can be judged as a whole, immediately before commit or handoff. This
checks necessity across the diff; it does not choose the original design or respond to an
unvalidated finding.

## Guidance

For each material addition, name the requirement, risk, contract, or dependency that justifies it.
Remove additions with no present reason, merge duplicates, and reuse suitable existing code.
Preserve required behavior, migration support, and safeguards. Stop with the smallest diff that
still satisfies the request and its risks. If a deletion changes behavior, verify the revised state
before commit. For a path touched by the diff, follow one representative value and one failure
through its layers. Challenge repeated parsing, normalization, authorization, catch-and-default
wrappers, and nested retries: each needs a distinct condition and owner. Check whether a shared
guard unnecessarily blocks status, stop, upgrade, or repair. Limit this trace to the changed
behavior; subtractive review is not an invitation to audit the entire repository.

## Anti-pattern

At final review, an upstream route guard makes a service-level authorization check look redundant,
and a recovery marker has no happy-path reader. To shrink the diff, the agent removes both while
keeping a familiar wrapper and duplicate parser. Focused route tests stay green, but another caller
can reach the service directly and interrupted work can no longer recover.

## Why

Locally reasonable additions are easier to judge together in the final diff. Subtractive review
removes unsupported maintenance cost without treating minimality as correctness.

## Exceptions and boundaries

Keep migration, compatibility, security, audit, or rollback code when a current contract or rollout
requires it. Ask the responsible authority before changing an accepted architecture or public
contract.

## Example

A task adds chunked image upload to a repository that already has a media-type validator. Before
commit, the agent removes an unused progress abstraction and duplicate media-type helper, reuses the
validator, and keeps the chunk-size cap and partial-file cleanup required by the upload contract. It
reruns the affected upload checks after deletion.
