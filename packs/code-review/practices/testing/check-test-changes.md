---
id: code-review.testing.check-test-changes
title: Check What the Changed Tests Actually Protect
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a diff adds, removes, skips, or changes tests, assertions, fixtures, mocks, or test configuration for changed behavior
anti_patterns:
  - id: code-review.testing.test-no-longer-protects-behavior
    name: A test passes without checking the promised result
    description: A changed assertion or fixture allows a real regression to pass unnoticed.
    severity: warn
---

## When to apply

A change modifies tests or test setup. Check whether the tests still catch failures that matter to callers, especially when the production behavior changes too.

## Guidance

Start with the behavior the test is supposed to protect. Follow the input through the code under test and ask what a broken result would look like. Then check whether the changed assertion would actually fail for that result. A green test is not enough if it never reaches the behavior or if its mock supplies the answer being asserted.

Look closely at changes that:

- Delete or skip a test, replace an exact contract assertion with `not null` or `not throws`, or catch the error the test was supposed to detect.
- Mock the same method whose behavior the test is meant to verify, or configure a mock to return the expected output without exercising the real decision.
- Start asynchronous work without awaiting its completion, so assertions or failures can happen after the test has already passed.
- Use fixed sleeps, shared state, wall-clock time, or real network services where scheduling or another test can change the outcome.
- Change fixtures so a previously reachable boundary or failure is no longer exercised, or rely on a test order that a full suite does not guarantee.

Report a concrete regression the changed test would miss, a false failure it could produce, or a required test removed by the change. Check the rest of the suite before claiming the behavior has no coverage. Stop once the affected behavior and its actual coverage are clear.

## Anti-pattern

A test for denied access used to send a request after revocation and assert a forbidden response. The diff replaces that assertion with a check that the response object exists. A successful response now passes the test, so the protection the caller relies on is gone.

## Why

A test can pass while the behavior it was meant to protect is broken. It can also fail on a harmless refactor if it checks private helper calls rather than the result callers rely on.

## Exceptions and boundaries

Don't demand tests for every changed line or report missing coverage without a concrete required behavior or failure. Exact calls, ordering, timing, or bytes may be the contract, such as a published protocol or a limit on duplicate charges. A separate integration test may already cover the affected path; inspect it before reporting a gap. This Practice reviews test changes; it does not turn implementation details into required assertions.

## Example

An API promises not to charge twice after a retry. The changed test mocks the entire payment service to return an existing receipt, then asserts that receipt was returned. The retry and charge logic never runs. If no other test covers duplicate charges, report that the test no longer checks the promised behavior. If an independent test exercises the real retry against a deterministic payment boundary and checks one charge, the mock alone is not evidence of a coverage gap.
