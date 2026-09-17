---
anti_patterns:
  - description: Adding coverage because a component, branch, or helper changed, without naming the behavior that must remain true, can make an incomplete implementation define its own correctness.
    id: agentic-coding.testing.test-without-protected-contract
    name: Test without a protected contract
    severity: info
applies_when: the agent is selecting tests for new or changed behavior and must decide what requirement, public contract, or domain invariant each proposed test is supposed to protect
id: agentic-coding.testing.anchor-tests-to-requirements
severity: info
stage: testing
tech_stack:
  - agentic-coding
title: Anchor Each Test to a Contract
---

## When to apply

Apply before adding or substantially changing a test, while its purpose is still being chosen. Ask
what promise would be broken if the test failed. This Practice ends once the test has one explicit
contract to protect. Choosing how to observe that contract belongs to assertion design; deciding
whether a past bug deserves a permanent regression test belongs to regression-protection judgment.

## Guidance

1. Name the exact reason for the proposed test before writing it: a sentence in the user request, an
   accepted issue or specification, a published interface, or a necessary rule such as "one user
   cannot read another user's data."
2. Restate that reason as behavior, without naming the current helper or class.
3. Keep the test only when its failure would show that behavior may be broken. If no meaningful
   reason exists, omit the test or label it a temporary investigation instead of treating new code
   as automatically test-worthy.
4. Record the connection in the test name, a nearby comment, or the review explanation.

Stop once the test has one explicit contract to protect; choosing the assertion comes next.

## Anti-pattern

The user asks for retry-safe job submission. The repository already has a queue adapter, and the
change adds a retry helper and status enum. Because each new method is easy to exercise and the
coverage report highlights its branches, the agent writes one test per method. The suite turns
green, but none of the tests protects the user-visible rule that retrying the same job must not
submit it twice.

## Why

Tests outlive the implementation choice that created them. When their purpose comes from current
code structure, they can preserve the wrong design and still look thorough. A test-to-contract
mapping keeps maintenance cost and future failures tied to behavior the project has actually
promised.

## Exceptions and boundaries

Exploratory probes and temporary characterization tests can reveal unknown behavior without
declaring it correct; label them and later retire or promote them deliberately. Safety,
compatibility, and data-integrity invariants may justify coverage even when product prose does not
mention them. Mechanical updates that preserve an already clear mapping need not repeat this
analysis.

## Example

The user asks for uploads to resume after a worker restart without corrupting the file. The
repository now has separate chunk scheduling and retry helpers, but those helpers are implementation
choices. The agent creates one test for "retrying an interrupted chunk does not duplicate stored
bytes" and one for "the upload resumes after process restart," and records those contracts in the
test names. It leaves helper call patterns untested because they are not promises to the user.
