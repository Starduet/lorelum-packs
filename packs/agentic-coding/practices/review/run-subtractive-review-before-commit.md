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

The implementation is finished and you are about to commit or hand it off. Read the whole diff and
ask which additions the task actually needs. This final review does not replace choosing the
original design or checking whether a reported finding is true.

## Guidance

1. Read the completed diff as a whole and list its substantial additions: files, abstractions,
   fallbacks, interfaces, I/O, tests, and documents.
2. Explain which requirement, risk, contract, or dependency makes each addition necessary now.
   Remove those without a reason, merge duplicates, and reuse suitable existing code.
3. Preserve required behavior, migration support, and safeguards. Keep migration, compatibility,
   security, audit, or rollback code when a current contract or rollout requires it.
4. If a deletion changes behavior, verify the revised state before commit: follow one representative
   value and one failure through the layers of a path the diff touches.
5. Look closely at repeated parsing, normalization, authorization, catch-and-default wrappers, and
   nested retries. Each needs its own condition that can occur and a responsible component. Check
   whether a shared guard needlessly blocks status, stop, upgrade, or repair.
6. Before removing a shared guard, authorization, migration, or recovery protection, list its
   current callers and entry points. Verify one path per distinct trust boundary (see Validate at
   the Boundary That Owns the Fact). One representative path is not enough when other entrances
   depend on the check.

Limit the trace to the changed behavior; subtractive review is not an invitation to audit the entire
repository. Stop with the smallest diff that still satisfies the request and its risks.

## Anti-pattern

At final review, an upstream route guard makes a service-level authorization check look redundant,
and a recovery marker has no happy-path reader. To shrink the diff, the agent removes both while
keeping a familiar wrapper and duplicate parser. Focused route tests stay green, but another caller
can reach the service directly and interrupted work can no longer recover.

## Why

An addition that seemed useful in one file may be unnecessary when you see the whole change. Remove
that maintenance work, but do not mistake a smaller diff for a correct one.

## Exceptions and boundaries

Ask the responsible authority before changing an accepted architecture or public contract.

## Example

A task adds chunked image upload to a repository that already has a media-type validator. Before
commit, the agent removes an unused progress abstraction and duplicate media-type helper, reuses the
validator, and keeps the chunk-size cap and partial-file cleanup required by the upload contract. It
reruns the affected upload checks after deletion.
