---
anti_patterns:
  - description: The agent promotes an abstraction, fallback, feature, or guardrail into required work because it could help later, increasing current cost and maintenance without a present requirement or evidenced risk.
    id: agentic-coding.planning.future-value-scope-promotion
    name: Future-value scope promotion
    severity: warn
applies_when: candidate plan items are about to become commitments, and one or more are supported only by generic practice, possible future use, or visible output
id: agentic-coding.planning.admit-only-currently-justified-work
severity: warn
stage: planning
tech_stack:
  - agentic-coding
title: Commit Only Work With a Current Reason
---

## When to apply

Apply while deciding which proposed items belong in the committed plan. The trigger is a plausible
item with no clear present reason. This decides plan scope, not which variant of an approved public
surface may later be exposed.

## Guidance

Label each candidate required, optional, out of scope, or unresolved. Required work must support
current acceptance, an evidenced risk, behavior already promised to callers, or an approved
expansion. A useful idea without that support stays optional and cannot block the required path. If
authority is missing, leave the item unresolved and ask. Stop when every committed item has a
present reason. Apply the same admission rule to validation, authorization, retries, and fallback
work: identify the reachable failure or explicit policy, the current protection, and the remaining
gap. "Another layer of safety" alone is not a gap. Do not require a separate risk document when a
brief explanation settles a small change.

## Anti-pattern

A task requires installation from one configured repository registry. Because the loader already
accepts a string, arbitrary file and network locators look like a cheap, future-proof extension.
Adding them to the required plan silently creates new validation, security, and compatibility
obligations that no current requirement supports.

## Why

An optional idea is cheapest to defer while it is still a plan item. Once code, tests, and consumers
depend on it, removal becomes a compatibility decision.

## Exceptions and boundaries

A governing contract or evidenced security, privacy, data-integrity, compatibility, or compliance
risk can require work the feature request does not name. Explain the actual exposure and
consequence; the category label alone cannot promote hypothetical work into a requirement. Optional
improvements may still be recorded without becoming commitments.

## Example

A task requires email alerts for failed jobs, and the repository already contains an unused
multi-channel interface that makes SMS and push look cheap. The plan marks failure detection, email
delivery, and unsubscribe handling as required; SMS and push are out of scope; consolidating two
email templates is optional. The existing interface is not enough to make extra channels current
work.
