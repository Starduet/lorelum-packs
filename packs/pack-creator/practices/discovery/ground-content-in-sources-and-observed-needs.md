---
anti_patterns:
  - description: The author turns one repository pattern or memorable incident into general guidance because it is concrete and easy to teach, while hiding the limit of the evidence and making a local response look universally authoritative.
    id: pack-creator.discovery.unsourced-synthesis-as-rule
    name: Unsourced synthesis presented as a rule
    severity: warn
applies_when: candidate guidance is about to become Pack content, but its basis in a governing source, documented behavior, or recurring observed failure has not been recorded
id: pack-creator.discovery.ground-content-in-sources-and-observed-needs
severity: warn
stage: discovery
tech_stack:
  - lorelum-pack-authoring
title: Ground Content in Sources and Observed Needs
---

## When to apply

Before adding a rule to the Pack, ask what supports it: an authoritative standard, a product
contract, documented platform behavior, or failures that recur in reviews or incidents. Make that
basis clear. A rule built from those sources is not, by that fact alone, proven to improve retrieval
or downstream behavior.

## Guidance

For each candidate, record the source or observed need, what it directly supports, and what the
author is adding by synthesis. Check important factual claims against current material and preserve
meaningful conflicts instead of blending them into certainty. When private incidents motivate the
rule, publish a sanitized mechanism and a truthful provenance category rather than private details.
Remove or clearly qualify guidance whose basis cannot be found. Stop when every material rule has a
traceable reason and its evidence limit is visible.

## Anti-pattern

An operations Pack should help engineers choose safe responses to external-service failures. One
postmortem says a retry recovered a delayed DNS lookup, and the repository already has a three-retry
helper, so "retry every external call three times" looks practical and consistent with local code.
The author promotes it to a general Practice without checking provider contracts showing that
several write operations are not idempotent. The rule can now duplicate real actions while appearing
incident-tested. The better decision is to limit the guidance to the behavior the sources support
and mark any wider retry policy as unconfirmed synthesis.

## Why

Recording the basis of a rule lets reviewers distinguish a requirement, an observed pattern, and an
author's generalization. Without that distinction, a plausible local lesson can appear more
authoritative than its sources justify.

## Exceptions and boundaries

Novel domains may have little public documentation. Repeated, sanitized observations can still
support useful guidance when their limits are explicit. Common knowledge does not need ceremonial
citation for every sentence, but consequential claims about safety, compatibility, compliance, or
platform behavior need a checkable basis.

## Example

A software-supply-chain Pack should help release engineers decide whether an artifact is trustworthy
enough to deploy. For a Practice about artifact verification, the author cites the organization's
accepted signing policy for the required signature and identity checks, then cites sanitized
incident reviews showing that teams often verified a checksum from the same compromised location.
The Practice adds a synthesized recommendation to use an independently trusted metadata channel and
labels that recommendation as review-derived rather than claiming the incidents proved one universal
tool or workflow.
