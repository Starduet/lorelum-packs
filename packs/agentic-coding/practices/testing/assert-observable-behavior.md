---
anti_patterns:
  - description: Asserting convenient private state, call order, markup shape, or helper boundaries that are not contractual makes harmless refactoring look like a broken promise while the real outcome may remain untested.
    id: agentic-coding.testing.incidental-implementation-assertion
    name: Incidental implementation assertion
    severity: info
applies_when: a test already has a protected requirement or invariant, and the agent must choose an assertion boundary that distinguishes the promised outcome from incidental implementation details
id: agentic-coding.testing.assert-observable-behavior
severity: info
stage: testing
tech_stack:
  - agentic-coding
title: Assert Observable or Stable Behavior
---

## When to apply

You know why a test is needed, but still need to choose what it should inspect. Check the result
relied on by a user, API caller, reader of saved data, external consumer, or deliberately stable
internal interface. This is about where to observe the behavior, not whether it deserves a test.

## Guidance

1. Drive the behavior with a controlled input and inspect the smallest result the real user or
   caller can rely on: a return value, saved record, protocol message, permission decision, or file
   bytes.
2. Check enough detail to distinguish success from the likely failure, but do not reconstruct the
   private route taken to get there.
3. Assert the distinct outcomes callers must see: a denied request stays denied, stale data is
   identified when required, and exhausted retries return the defined failure.
4. If there is no way to observe the result yet, add the smallest legitimate way to read it or test
   it through the nearest stable interface, rather than inspecting private state.

Stop when changing the internals without changing the promised behavior would leave the assertion
passing. A promised limit on attempts or a guarantee against duplicate work is observable behavior
too. Do not require every internal layer to call the same validator, or test impossible internal
states merely to justify defensive code.

## Anti-pattern

The user requires revoked access to stop working on the next request. The repository uses an
authorization cache, and a refactor moves invalidation between two helpers. Because helper order is
easy to mock and produces a fast deterministic test, the agent checks that invalidation runs before
lookup. The test can pass while the next request still receives a cached allow decision, and it will
fail if a later design removes the cache while correctly denying access.

## Why

When a useful assertion fails, it means the promised behavior may be broken. Checking stable results
gives that signal. Checking incidental implementation details can miss the real defect and make
harmless refactors expensive, while proving little about the acceptance criteria.

## Exceptions and boundaries

Exact bytes, syntax trees, protocol fields, event order, timing bounds, or serialization shape
should be asserted when those details are published, compatibility-sensitive, or safety-relevant.
Focused unit tests may target an internal API that the project deliberately treats as stable.
"Observable" does not mean vague: retain exactness whenever exactness is part of the promise.

## Example

The user requires revoked access to stop working immediately. The repository exposes a supported
request path and an administration path for revocation. The agent grants access, confirms one
request succeeds, revokes access, then sends another request through the supported path and verifies
denial. It does not inspect a cache flag or helper order because the user relies on the denial, not
the cache design.
