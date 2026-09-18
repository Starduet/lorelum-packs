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

Apply after acceptance is clear and the task's overall engineering depth has been chosen, but before
coding starts. Decide how each must will be demonstrated and where cheap evidence stops being
representative. If checks have already run and their coverage is being reconciled with acceptance,
map the evidence instead.

## Guidance

1. List each acceptance must next to the plausible failure an implementer could ship while believing
   it works: a duplicate charge, an archive the independent consumer cannot open.
2. For each must, choose the lowest-cost observation that actually distinguishes success from that
   failure: which check, run where, watching which boundary.
3. Record each observation's scope and blind spot, and the trigger that would demand stronger
   evidence.
4. Use focused checks to reject bad approaches early; reserve integration, a representative
   environment, or human review for boundaries cheaper checks cannot represent.
5. If no feasible evidence supports a must, get a decision from the requirement owner before
   implementation begins: add the missing evidence route (for example a new environment), narrow or
   defer the must, remove it from the committed scope, or accept it as unverifiable with the risk
   recorded. Recording the gap alone does not authorize implementing the must as if it could be
   verified.

Stop when every must has a sufficient evidence route or a recorded owner decision — narrowed,
deferred, de-committed, or accepted as unverifiable with its risk. A declared gap alone is not a
stop.

## Anti-pattern

An export plan lists unit tests, static checks, and manual file inspection. They are convenient and
all can pass, but none opens the archive in the independent consumer named by the compatibility
requirement. Check volume substitutes for evidence at the only boundary that matters.

## Why

Evidence tied to a plausible failure shows what a pass rules out. The cheapest sufficient route
avoids ceremony while preserving stronger checks where they can change the decision.

## Exceptions and boundaries

Audits, certification, safety cases, or release policy may require more evidence. Exploratory
evidence cannot support a production claim or a claim that the complete feature works.

## Example

A payment retry must not create a duplicate charge. The plan pairs focused state-transition tests
for the retry rules with one integration observation against a test payment endpoint for gateway
idempotency, and records the blind spot: the real gateway's retry behavior. It escalates to a
controlled staging check only if that behavior differs from the test endpoint.
