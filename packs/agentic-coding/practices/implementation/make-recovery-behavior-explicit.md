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

Before adding or keeping retries, fallbacks, or code that catches an error and continues, decide
which failures can actually recover and what the caller should receive. Validating incoming data is
a separate question: even valid input can fail when a dependency is unavailable.

## Guidance

1. First say what the caller normally receives when the operation succeeds and when it fails.
2. Identify the known failure that another attempt or fallback can resolve. Make one component
   responsible for that recovery.
3. Say which result or saved state remains usable afterward, and how callers will learn any
   important difference from a successful operation returning fresh data.
4. Before retrying, explain why another attempt may succeed and whether it could repeat a side
   effect. Set one total limit on attempts or time. Check retries already made by the client, job,
   and caller so that their limits do not multiply.
5. Before falling back to another source, show that it gives an equivalent result or that the
   reduced result and its limits have been explicitly accepted. Otherwise, return the established
   error. Never disguise malformed data, denied access, or a failed write as an empty collection or
   default value.

Translate errors at the interface responsible for doing so, keeping the cause callers need in order
to act. Require only the prerequisites needed to perform the recovery safely. A default already
specified for missing optional input does not need a recovery framework.

You are done when it is clear which component recovers which failures, how far it may retry or fall
back, and what the caller will see. If recovery is not needed, report the failure directly at the
user-facing interface and give a usable next step.

## Anti-pattern

A dashboard must show the current number of failed jobs. Its HTTP client allows three attempts, the
service makes up to three whole client calls, and a wrapper falls back from stale cache to an empty
list on any exception. The code looks resilient and rarely shows an error. During an outage it makes
nine requests and then reports zero failures; operators cannot distinguish a healthy system from
missing data, and an unrelated decoding bug is hidden by the same path.

## Why

A fallback changes what the product does when something fails, and can fail in its own right.
Returning a default for every error can make a broken system look healthy. Retrying at several
layers multiplies delay and load. Giving recovery one owner makes its result and limits clear.

## Exceptions and boundaries

Keep accepted offline behavior, older-data read policies, compatibility paths, and defaults for
missing optional settings. They are not automatically unnecessary; preserve their limits and check
their results. Separate retries may stay if they cover different operations and fit the total
budget.

If a write may already have committed before a timeout, do not blindly replay it. Use idempotency or
reconcile what happened first. A required audit or integrity check that failed must remain a
failure, not become success through fallback.

## Example

A status page may show a snapshot up to five minutes old during a transport outage. Its data client
owns one bounded retry; the page uses the timestamped cache only for that known failure and labels
the stale outcome. Expired cache, permission errors, and invalid payloads remain explicit failures.
Separately, a local process-stop command must work when that process's business API is incompatible:
it retains the identity checks needed to stop the intended process, but does not require a
successful business query merely to enable recovery. Neither path needs a chain of general-purpose
fallbacks.
