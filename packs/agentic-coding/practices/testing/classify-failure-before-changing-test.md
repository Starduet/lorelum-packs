---
anti_patterns:
  - description: Changing the easiest side of a failed check before deciding whether the defect is in the product, verifier, environment, or pre-existing baseline can erase the only clear evidence of the real problem.
    id: agentic-coding.testing.test-accommodation-before-diagnosis
    name: Test accommodation before diagnosis
    severity: warn
applies_when: a test, lint, type, build, or validation check has failed and the agent is about to change production code, the test, generated files, or configuration without first identifying the source of the disagreement
id: agentic-coding.testing.classify-failure-before-changing-test
severity: warn
stage: testing
tech_stack:
  - agentic-coding
title: Diagnose Failed Checks Before Editing Code or Tests
---

## When to apply

A test, lint, type check, build, or validation has failed, and there is more than one plausible
reason. Before changing the implementation, expected result, fixture, generated output, or tool
configuration, find out which is wrong. It may be the product, an obsolete or incorrect test, the
environment or nondeterministic behavior, a generated file built from different source, or an
unrelated failure that already existed. An external review comment without a reproduced check needs
review-finding validation instead.

## Guidance

1. Reproduce the smallest relevant failure using a known commit, build, or generated file.
2. Read the failed assertion or diagnostic, and compare what happened with the current requirement.
3. Check the environment, inputs, fixtures, and generated files that could change the result, and
   gather only enough evidence to distinguish the leading explanations.
4. Record the cause and the fact that rules out the next most likely explanation.

Choose the fix after diagnosing the failure. If the cause is still unclear, leave production code,
tests, and configuration unchanged and report what remains uncertain. Do not keep editing until the
suite turns green.

## Anti-pattern

The user asks for a visual refresh that preserves keyboard navigation. A nearby UI refactor changes
a snapshot, and the new screen looks polished. Because updating the snapshot is one command and
restores a green suite, the agent accepts it immediately. The refactor also removed a required
keyboard action, so the expectation update deletes the only failure signal before the behavior is
compared with the request.

## Why

A failed check shows a disagreement, not which side is right. Diagnose it so you do not accept a
product bug as the new expected result or change correct behavior to satisfy an outdated test. This
also keeps unrelated failures that already existed out of the current change.

## Exceptions and boundaries

Contain an active security, data-loss, or production incident before full diagnosis when delay
increases harm, while preserving evidence for follow-up. A directly confirmed infrastructure outage
or corrupt generated file can be repaired without reconsidering every possible cause. An approved
requirement change may make a test obsolete, but that approval — not the new implementation output —
is the reason.

## Example

The user asks for a database migration that works from the currently released schema. In the
repository, the migration test passes alone but fails after another database suite. The agent runs
both orders and checks the starting schema version, finding that the earlier suite leaves shared
state behind. A fresh database migrates successfully, so the failure comes from test isolation
rather than the migration or its expected result. Only then does the agent change the shared fixture
cleanup.
