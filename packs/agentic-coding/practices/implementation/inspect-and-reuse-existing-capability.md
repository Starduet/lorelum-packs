---
anti_patterns:
  - description: Implementing a familiar utility from memory because it looks quick and locally testable, before checking the repository or its dependencies for an existing contract with important edge-case behavior.
    id: agentic-coding.implementation.reflexive-reimplementation
    name: Reflexive reimplementation
    severity: warn
applies_when: implementation is about to add a helper or mechanism, and the agent has not yet determined whether a nearby module, declared dependency, or the runtime already provides the required behavior under the current constraints
id: agentic-coding.implementation.inspect-and-reuse-existing-capability
severity: warn
stage: implementation
tech_stack:
  - agentic-coding
title: Check What Already Exists Before Building
---

## When to apply

Apply immediately before creating a helper, adapter, parser, cache, retry policy, or similar
mechanism that could plausibly exist nearby. If current evidence already shows that the behavior is
intentionally new or that existing options fail a required constraint, stop searching and design the
new code.

## Guidance

1. Open the module where the behavior belongs and the closest candidate capability inside it.
2. Read one representative caller or test of that candidate only if it can change whether the
   candidate preserves a required semantic, compatibility, or failure constraint.
3. Check the one declared dependency or runtime facility most likely to provide the behavior.
4. Decide between direct reuse, a small adaptation, and a new implementation, and record the
   specific mismatch that rules out each closer option.

Stop as soon as the evidence supports one choice; do not catalog every vaguely similar helper,
caller, or test.

## Anti-pattern

The user asks for imported links to be normalized before storage. A short helper is easy to write,
matches the examples, and passes the new focused tests. Under deadline pressure, the agent builds it
without checking a declared dependency already used by another importer. That dependency also
handles encoded separators, host casing, and platform-specific paths, so the repository now has two
normalization rules that disagree on real inputs.

## Why

Existing code often carries compatibility rules, failure behavior, and maintenance ownership that
are not obvious from its name. Checking before building avoids parallel contracts and limits new
code to the part the current requirement truly lacks.

## Exceptions and boundaries

Do not reuse code merely because its name looks right. A security boundary, license restriction,
unsupported environment, unstable API, or demonstrated semantic mismatch can justify new code. Once
reuse has been accepted or ruled out, choosing among multiple feasible designs is a separate
decision.

## Example

A scheduling change needs to detect whether a new booking overlaps an existing one, including
bookings that share an endpoint. Before writing its own function, the agent opens the scheduling
module and finds a tested overlap function with exactly those endpoint rules, and reuses it
directly. No second definition of overlap enters the repository.
