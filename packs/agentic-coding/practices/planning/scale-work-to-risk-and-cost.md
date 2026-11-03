---
anti_patterns:
  - description: The agent applies the same heavy or light delivery template to every task because it is familiar, wasting effort on reversible changes or omitting protection from changes with costly failure modes.
    id: agentic-coding.planning.uniform-engineering-ceremony
    name: Uniform engineering ceremony
    severity: warn
applies_when: an implementation approach has been selected, and the agent is about to set its investigation, validation, review, and recovery depth without weighing affected users, reversibility, uncertainty, and failure cost
id: agentic-coding.planning.scale-work-to-risk-and-cost
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Scale Work to Risk and Cost
---

## When to apply

After choosing an approach, decide how much investigation, checking, review, and recovery
preparation it needs. How many users or systems could be affected? Can you undo the change? What is
still unknown, and what would recovery cost?

Set that overall effort first; then choose the checks for individual acceptance requirements. If
implementation has already exposed new facts about risk or scope, revisit the plan from those facts
instead.

## Guidance

1. Identify what could realistically go wrong: who would be affected, which data or security,
   compatibility, or operational problems could follow, and whether the change can be undone.
2. Use the number of affected users, reversibility, unknowns, and cost of failure to choose the
   effort. A reversible color change and a live schema migration should not both get the same
   single-test sign-off.
3. Give each safeguard a reason: a specific failure it prevents or a policy that requires it. Remove
   process with no such reason. Count its costs too: rejecting valid work, reporting errors later,
   extra configuration, preventing upgrades or repairs, and ongoing maintenance.
4. Before settling the effort, investigate any unknown risk that could change the decision, or run a
   small, focused experiment. Say what is still unknown and which result would change the plan.

You have enough when every safeguard has a reason and you can explain in one sentence how much
verification and recovery preparation this change needs. Reporting a recoverable failure clearly may
need less machinery than a fallback that returns a different result.

## Anti-pattern

The team's last project was an authorization migration, so the agent copies its rollout plan, broad
regression suite, and rollback checklist onto a reversible styling correction. Later, the same
familiar "focused test" template is applied to a schema change that can strand live data. The
uniform process looks consistent while being wrong in both directions.

## Why

Spend effort where failure would matter most. A low-cost, reversible change need not carry the
process of a dangerous migration; a change that can lose data should not be rushed to save a check.

## Exceptions and boundaries

Follow required organizational reviews and checks even when the local risk is low. Investigate
unknown security, privacy, or data-loss risks if the answer could materially change the decision.
Keep that investigation focused; uncertainty does not justify listing endless hypothetical
attackers, corruption scenarios, or recovery systems.

## Example

Changing a webhook signature format can break every existing receiver and block deliveries. The plan
therefore includes old-and-new compatibility checks, a representative consumer test, a staged
cutover, and a rollback route. Those safeguards are justified by the number of existing receivers
affected, not by a rule that every request change needs the same ceremony. For the reversible color
fix in the same sprint, one focused check and review are enough.
