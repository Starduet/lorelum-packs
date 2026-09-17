---
anti_patterns:
  - description: Turning a salient one-off mistake or rejected experiment into a permanent negative assertion without a durable contract, credible recurrence path, or high-impact risk leaves future maintainers paying for corrective residue.
    id: agentic-coding.testing.memorialized-transient-mistake
    name: Memorialized transient mistake
    severity: warn
applies_when: a failure has been classified or a correction accepted, and the agent must decide whether to add a long-lived regression test, negative assertion, lint rule, or gate that will constrain future changes
id: agentic-coding.testing.justify-regression-protection
severity: warn
stage: testing
tech_stack:
  - agentic-coding
title: Require Evidence for Regression Protection
---

## When to apply

Apply after the failure or correction is understood, before converting it into a permanent test or
gate. The decision is whether recurrence prevention deserves long-term maintenance. It is not the
earlier decision about what caused the failure, and it is not ordinary positive coverage selected
directly from a current requirement.

## Guidance

1. State the failure the proposed permanent test, negative assertion, lint rule, or gate would
   catch.
2. Keep it only with a lasting reason: an explicit promise, a required absence such as "unauthorized
   requests never return data," a reproduced bug that can realistically return through future
   changes, or a high-impact safety, privacy, compatibility, or data-integrity risk. "This just
   happened" is not enough.
3. Choose whether to keep, narrow, make temporary, or omit the protection; for temporary protection,
   record when it can be removed.
4. Observe the smallest stable behavior that catches recurrence without freezing today's helper
   design.

Stop with the reason recorded next to the protection.

## Anti-pattern

The user rejects helper text that an Agent added to one supplied screen and asks to restore the
design. The repository has a simple text-lint mechanism, so adding a global ban for that phrase is
cheap and makes the correction feel complete. The Agent adds the ban even though the user restored
one screen, not a product-wide prohibition, and no shared generator or repeated failure could
reintroduce the text elsewhere.

## Why

Regression tests and gates turn one incident into a standing constraint. A durability check keeps
protections for failures that matter and can recur, while avoiding a suite shaped by the accident of
which Agent mistakes happened most recently.

## Exceptions and boundaries

Unauthorized access, secret exposure, destructive data loss, regulatory violations, and published
compatibility breaks can warrant protection after one credible incident because the failure cost is
high. Temporary safeguards can be appropriate during a migration when their removal condition is
explicit. Do not reject justified protection merely to minimize test count or diff size, and do not
add it before an unresolved failure is classified.

## Example

The user requires payment retries to produce at most one charge. A reproduced bug showed that the
repository's queue serializer dropped the request identifier before redelivery, allowing a duplicate
charge. Because the public payment contract requires idempotency and the serializer is a likely
future refactor point, the agent adds a permanent test that redelivers the saved job and observes
one charge. It does not freeze the current queue helper sequence.
