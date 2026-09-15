---
anti_patterns:
  - description: The agent applies the same heavy or light delivery template to every task because it is familiar, wasting effort on reversible changes or omitting protection from changes with costly failure modes.
    id: agentic-coding.planning.uniform-engineering-ceremony
    name: Uniform engineering ceremony
    severity: warn
applies_when: an implementation approach has been selected, before the agent commits its investigation, validation, review, and recovery depth without considering how many users or systems failure can affect, reversibility, uncertainty, and failure cost
id: agentic-coding.planning.scale-work-to-risk-and-cost
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Scale Work to Risk and Cost
---

## When to apply

Apply when setting the initial engineering depth for a chosen approach. Consider how many users or
systems failure can affect, whether the change can be reversed, what remains unknown, and recovery
cost. This sets the overall depth of investigation, validation, review, and recovery preparation;
choosing the observation for each acceptance condition is the next evidence-planning decision. If
implementation has already revealed new risk or scope, replan from those facts instead.

## Guidance

Identify credible harm to users, data, security, compatibility, or operations. Choose a proportional
level of investigation, validation, review, and recovery preparation. Connect each safeguard to a
failure mode or mandatory policy, and remove ceremony that has no such reason. If a material risk is
unknown, investigate it or run a bounded probe first. Stop when every safeguard has a reason in the
actual failure profile. Include the safeguard's own costs: false rejection, slower failure,
additional configuration, blocked upgrade or repair, and maintenance. A recoverable failure with a
clear message may need less machinery than a fallback that changes the result.

## Anti-pattern

The team's last project was an authorization migration, so the agent copies its rollout plan, broad
regression suite, and rollback checklist onto a reversible styling correction. Later, the same
familiar "focused test" template is applied to a schema change that can strand live data. The
uniform process looks consistent while being wrong in both directions.

## Why

Proportional investment directs effort toward failures that matter. It avoids both overdesign on
cheap changes and false economy when failure is expensive or hard to reverse.

## Exceptions and boundaries

Organizational policy may require a review or check regardless of local risk. Unknown security,
privacy, or data-loss exposure calls for a bounded investigation when it could materially change the
decision. Name the unresolved fact and what result would change the plan; stop when that fact is
settled or hand off the specific remaining decision. Uncertainty is not permission to enumerate
unlimited hypothetical attackers, corruption modes, or recovery frameworks.

## Example

Changing a webhook signature format can break every existing receiver and block deliveries. The plan
therefore includes old-and-new compatibility checks, a representative consumer test, a staged
cutover, and a rollback route. Those safeguards are justified by the number of existing receivers
affected, not by a rule that every request change needs the same ceremony.
