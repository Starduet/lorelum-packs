---
id: code-review.testing.check-test-changes
title: Check Whether Changed Tests Still Catch Real Failures
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a diff adds, removes, skips, or changes tests, assertions, fixtures, mocks, or test configuration
anti_patterns:
  - id: code-review.testing.test-no-longer-protects-behavior
    name: A passing test no longer checks the behavior
    description: A changed assertion, mock, or fixture allows a concrete regression to pass unnoticed.
    severity: warn
---

Identify the behavior the changed test is meant to protect, then follow the test input through the real decision and ask whether a plausible wrong result would fail the assertion. Check whether a mock supplies the answer, an asynchronous assertion runs after the test ends, or a removed or skipped case was the only coverage of a required behavior.

Report the specific regression or false failure, not a preference for more tests or stronger-looking assertions. Inspect other coverage before claiming a gap. Exact calls, timing, or bytes can be a contract; otherwise avoid treating implementation details as required behavior.
