---
anti_patterns:
  - description: Catching broad failures and cascading through retries, alternate sources, empty values, or defaults without a defined recoverable condition and caller-visible meaning.
    id: agentic-coding.implementation.fallback-cascade-hides-failure
    name: Fallback cascade hides the failure
    severity: warn
applies_when: a failed operation is about to gain retries, defaults, alternate sources, degraded results, or catch-and-continue wrappers, and the agent must decide whether that recovery preserves the caller's promised outcome
id: agentic-coding.implementation.make-recovery-behavior-explicit
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Give Recovery One Owner and an Explicit Outcome
---

## When to apply

Apply before adding or retaining a fallback, retry, or error-swallowing wrapper. Decide which known
failure can recover and what the caller receives afterward. Deciding where to validate incoming data
is a different question; a valid input can still encounter an unavailable dependency.

## Guidance

Start with the normal success and failure contract. Name the specific recoverable condition, the
component that owns recovery, and the usable result or preserved state it can produce. Prefer
propagating the established error when no accepted recovery exists. Do not invent success by
replacing malformed data, denied access, or a failed write with an empty collection or default.

For a retry, establish why another attempt can succeed, whether replay can duplicate an effect, and
one total attempt or time budget. Check existing client, job, and caller retries before adding any;
avoid multiplying their budgets. For a fallback, establish source equivalence or the explicitly
accepted degradation, its limit, and how callers learn any material difference. Ordinary defaults
for absent optional input need no recovery framework when the contract already defines them.

Keep error translation at the interface that owns it and preserve the actionable cause. Let the
recovery operation depend only on prerequisites needed to complete that operation safely. Stop when
one owner, eligible failures, a bounded recovery, and the final observable result are clear. If no
recovery is required, retain the direct failure and a usable next step at the user-facing boundary.

## Anti-pattern

A dashboard must show the current number of failed jobs. Its HTTP client allows three attempts, the
service makes up to three whole client calls, and a wrapper falls back from stale cache to an empty
list on any exception. The code looks resilient and rarely shows an error. During an outage it makes
nine requests and then reports zero failures; operators cannot distinguish a healthy system from
missing data, and an unrelated decoding bug is hidden by the same path.

## Why

Recovery is additional product behavior with its own failure modes. An unqualified fallback can turn
detectable failure into false success, while nested retries multiply delay and load. One explicit
owner makes the result understandable and the budget enforceable.

## Exceptions and boundaries

An accepted offline mode, stale-read policy, compatibility path, or default for an absent optional
setting is useful behavior, not automatically excess. Keep its stated limits and verify its outcome.
Independent retries can remain when they cover different operations and fit an established overall
budget. A timeout after a possibly committed write needs idempotency or outcome reconciliation, not
a blind replay. A mandatory audit or integrity failure cannot become success through fallback.

## Example

A status page may show a snapshot up to five minutes old during a transport outage. Its data client
owns one bounded retry; the page uses the timestamped cache only for that known failure and labels
the stale result. Expired cache, permission errors, and invalid payloads remain explicit failures.
Separately, a local process-stop command must work when that process's business API is incompatible:
it retains the identity checks needed to stop the intended process, but does not require a
successful business query merely to enable recovery. Neither path needs a chain of general-purpose
fallbacks.
