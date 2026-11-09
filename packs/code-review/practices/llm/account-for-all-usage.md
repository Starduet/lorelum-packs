---
id: code-review.llm.account-for-all-usage
title: Trace Usage and Settlement Across LLM Attempts
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a changed LLM call can retry, fall back, stream partially, or alter how provider usage is recorded or settled
anti_patterns:
  - id: code-review.llm.lost-or-duplicate-usage
    name: Usage disappears between attempts
    description: Retrying replaces an incurred attempt before its usage is captured, or a repeated settlement charges it twice.
    severity: warn
---

## When to apply

A diff changes an LLM invocation, response stream, retry or fallback, usage collection, or billing. Determine what happens to each attempt, including attempts whose response is not delivered to the caller.

## Guidance

1. Trace each provider attempt from dispatch through success, error, cancellation, partial stream, and final usage capture. Find the provider's actual guarantees for billable failed calls and usage metadata; a cancelled response is not proof of zero cost.
2. Follow usage into the ledger, customer charge, reconciliation, and deduplication mechanisms. On retry or fallback, identify which attempt each record represents and whether ambiguous completion can repeat it.
3. Check the business, accounting, and compliance contract for required durability, permitted estimates, and recovery. Separately trace whether settlement failure or delay changes an otherwise successful LLM response. A recoverable settlement may be independent, while a required durable record may legitimately gate success.
4. Report a reachable discrepancy between that contract and the changed path, including the affected attempt and consequence. Stop when all relevant terminal paths and their existing safeguards are accounted for.

## Anti-pattern

A retry replaces a response object before the only billing call reads its usage. The first failed attempt may have incurred tokens, so billing only the last response can omit a real charge. Conversely, reporting a lost charge without checking a helper that already records each attempt would be a false positive.

## Why

One user request can produce several provider attempts, and a response failure does not necessarily reverse provider work. Treating the last result as the only attempt loses the relationship between incurred usage and settlement.

## Exceptions and boundaries

Do not assume every provider cost must be billed to the customer, that final usage metadata always exists, or that a mandatory financial record may be dropped. An established reconciliation process or per-attempt idempotency may close the apparent gap; inspect it. Non-billing notifications belong to side-effect isolation, not this accounting decision.

## Example

A contract requires recording usage from every provider call, including retryable failures. `call_model` returns both `usage` and `retryable`; the changed handler retries by assigning a second result over the first, then calls `charge(result.usage)` once. Because the first result can contain billable usage and no other code records it, the retry line can cause undercounting. If each call records its usage before returning, overwriting the local result alone is not a finding.

Before conducting a review, explicitly load the [review execution contract and workflow](resource:references/review-workflow.md); retrieval does not load it. The designated reviewer makes the substantive judgment.
