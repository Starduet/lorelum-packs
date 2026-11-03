---
anti_patterns:
  - description: The agent maximizes the number or breadth of convenient checks because they create visible confidence, while none observes the boundary where the required behavior can actually fail.
    id: agentic-coding.planning.check-volume-evidence-plan
    name: Check-volume evidence plan
    severity: warn
applies_when: acceptance conditions are known and implementation is about to begin, but the agent has not chosen observations that can distinguish success from plausible failure at an appropriate cost
id: agentic-coding.planning.plan-sufficient-evidence
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Plan the Minimum Sufficient Evidence
---

## When to apply

Once the acceptance requirements and overall amount of engineering work are clear, decide how you
will tell whether each required behavior works, before coding starts. Choose checks that can catch
the failures that matter, and know when a cheap check stops representing real use. If checks have
already run, compare their results with the requirements instead of starting a new evidence plan.

## Guidance

1. For each required behavior, describe a plausible mistake that could survive implementation:
   charging twice, for example, or exporting an archive that the intended consumer cannot open.
2. Choose the least expensive check that can tell correct behavior from that mistake. Say which
   check to run, where to run it, and what behavior to observe.
3. Note what the check does not cover and what would make a stronger check necessary.
4. Use focused checks to rule out bad approaches early. Use integration checks, a representative
   environment, or human review when cheaper checks cannot show what happens there.
5. If there is no feasible way to verify a requirement, get its owner's decision before coding. They
   may provide a way to gather the evidence, narrow or defer the requirement, remove it from scope,
   or accept that it cannot be verified and record the risk. Merely noting the gap does not let you
   proceed as though the requirement can be verified.

Planning is complete when each requirement has a sufficient check or a recorded owner decision about
its limits. Writing "not verified" without that decision is not enough.

When updating a plan, add checks for new risks and unresolved gaps. Reuse earlier results that still
apply to the current code or output and environment. An edit does not automatically require the
whole suite, a benchmark, or a formal risk report. If a frequently executed operation now does more
work, measure at a scale that can show whether its cost matters; do not run a benchmark just to
complete a checklist. Testing inputs the producer cannot generate says nothing about failures that
can actually occur. More checks or defensive branches do not, by themselves, prove better quality.

## Anti-pattern

An export plan includes unit tests, static checks, and opening the files by hand. All are convenient
and can pass, but nobody tries the archive in the independent consumer required to support it. The
plan counts checks without checking compatibility where it can fail.

## Why

A useful check rules out a mistake that could really happen. Choosing the cheapest check that does
so avoids unnecessary work without dropping stronger checks when they can change the decision.

## Exceptions and boundaries

Audits, certification, safety cases, or release policy may require more evidence. Exploratory
evidence cannot support a production claim or a claim that the complete feature works.

## Example

A payment retry must not create a duplicate charge. The plan pairs focused state-transition tests
for the retry rules with one integration observation against a test payment endpoint for gateway
idempotency, and records the blind spot: the real gateway's retry behavior. It escalates to a
controlled staging check only if that behavior differs from the test endpoint.
