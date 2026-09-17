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

Apply after the reason for a test is known and before choosing what it will inspect. Identify who or
what relies on the protected behavior: a user, API caller, persisted reader, external consumer, or
intentionally stable internal interface. This Practice selects the observation boundary; it does not
decide whether the behavior deserves a test in the first place.

## Guidance

1. Drive the behavior with a controlled input and inspect the smallest result the real user or
   caller can rely on: a return value, saved record, protocol message, permission decision, or file
   bytes.
2. Check enough detail to distinguish success from the likely failure, but do not reconstruct the
   private route taken to get there.
3. Assert the distinct outcomes callers must see: a denied request stays denied, stale data is
   identified when required, and exhausted retries return the defined failure.
4. If the result cannot currently be observed, expose the smallest legitimate read or test through
   the nearest stable interface instead of inspecting private state.

Stop when the assertion would still pass after an internal refactor that preserves the promised
behavior. A promised attempt budget or non-duplication guarantee is observable behavior; do not
require every internal layer to call the same validator, or maintain tests for impossible internal
states solely to justify defensive code.

## Anti-pattern

The user requires revoked access to stop working on the next request. The repository uses an
authorization cache, and a refactor moves invalidation between two helpers. Because helper order is
easy to mock and produces a fast deterministic test, the agent checks that invalidation runs before
lookup. The test can pass while the next request still receives a cached allow decision, and it will
fail if a later design removes the cache while correctly denying access.

## Why

An assertion is useful when its failure means the protected promise may be broken. Stable
observations provide that signal. Incidental assertions spend maintenance effort on code shape, can
miss the user-visible defect, and produce evidence that is difficult to connect to acceptance.

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
