---
anti_patterns:
  - description: Rechecking or normalizing the same established fact in every layer without a new input, mutation, caller, or failure mode, creating divergent rules and rejecting valid work.
    id: agentic-coding.implementation.defensive-check-per-layer
    name: A defensive check in every layer
    severity: warn
applies_when: a fact is checked or normalized across adapters, internal HTTP handoffs, services, or storage, and the agent must assign its owning boundary and determine which established results remain valid at later locations
id: agentic-coding.implementation.validate-at-the-owning-boundary
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Validate at the Boundary That Owns the Fact
---

## When to apply

The same input passes through an adapter, service, and storage layer, and you need to decide where
to check it — or whether to check it again later. Follow that actual path, not every package.
Deciding whether a proposed check adds enough protection for its cost belongs to
`justify-added-checks`. Choosing a retry or fallback after a known failure is a recovery decision.

## Guidance

1. Follow only the relevant input or state through its handoffs. For each check, explain what
   failure can happen there or which mandatory contract requires it, what the check proves, where
   you can first trust that result, and which component must keep it valid.
2. Check external input shape at entry. Apply business rules in the component that owns the relevant
   state. Convert to the agreed representation once, where that conversion belongs, then pass the
   result through ordinary internal calls. Use an internal type to express what has been checked
   where practical; a cast alone proves nothing.
3. Before checking again, identify what could make the earlier result invalid here: another entry
   point, untrusted deserialization, a transformation, concurrent mutation, expired authorization,
   or independently required protection. Keep the check only if such a condition exists. A new
   function, layer, or package name does not by itself create a new boundary.
4. Pass already-checked results through calls that do not change them, and retain checks at
   genuinely different boundaries. Remove duplicate internal work; do not add caches, trusted flags,
   or locks just to keep doing it.

Stop when it is clear who is responsible for each guarantee and only the checks needed on the actual
path remain. A short explanation in the existing design or review is enough.

When an internal producer is controlled, rely on what its contract and actual production path
guarantee about its output. Crossing a process boundary or making a local HTTP call does not alone
make that output untrusted. Keep decoding, authentication, protocol matching, and request–response
correlation where needed, without treating them as reasons to repeat the full business-schema check.
A representation conversion needs checks for failures it can introduce, not every problem an
arbitrary object could have.

Do not make the production path guard by default against other internal code violating its own types
and contract. Prefer types, producer contract tests, and necessary development assertions. A mock
that invents output the producer cannot emit does not justify a downstream guard. Preserve tests for
reachable external input, real corruption, and supported recovery.

After JSON has been decoded and validated, if no new values have been introduced, checking for
cycles, Symbols, or arbitrary object prototypes adds no guarantee. Keep adapters that actually
handle a conversion or lifecycle; different boundaries need not share one validator. An earlier
check does not cover later file changes or a new caller that can bypass the checked path.

Preserve external input validation, model/native integration quality checks, publication integrity,
transaction and snapshot consistency, authentication, process ownership, and regeneration of corrupt
derived caches. Change an accepted checking contract through its normal change process before
removing its required checks.

## Anti-pattern

An HTTP adapter parses a quantity into a positive integer. A service, domain helper, and repository
each accept that typed value, but independently parse, clamp, and reject it because each module is
meant to be robust. Their limits later drift: the adapter accepts a bulk order while a hidden helper
silently clamps it. Every layer has tests, yet a valid request is changed after acceptance and the
caller cannot tell which rule defines the order.

## Why

A check adds value when it establishes a fact that can actually be false there. Repeating an already
established fact creates more rule owners, failure paths, and maintenance without improving the
guarantee. Distinct boundaries can still need distinct protections even when they inspect the same
field.

## Exceptions and boundaries

An API and CLI may each validate raw input before sharing a typed domain call. A database uniqueness
constraint remains necessary when a preflight check cannot prevent concurrent inserts. A worker
deserializing a queued message has a new input boundary; an unchanged object passed to a private
helper does not. Encoding for HTML output solves a different problem from parsing input.

Use confirmed deployment and caller facts when sizing authorization. An internal service behind an
enforced gateway need not recreate an identity platform for every helper; a bypassable gateway or
cross-tenant operation can require its own authorization decision. Retain separately justified
defense in depth and explicit policy requirements. Before removing existing checks, establish their
callers and contract; this Practice does not authorize changing accepted behavior by itself.

## Example

An inventory service accepts orders through an HTTP endpoint and a CSV import. Each adapter parses
its raw quantity and creates the same typed command. The domain service checks current available
stock, and the database atomically prevents competing reservations from overselling. The agent keeps
those distinct checks and removes a proposed third string parser in the repository: no string or
unchecked caller can reach it. A stock change still gets checked at the mutation boundary, while the
parsed quantity is passed through without another normalization policy.
