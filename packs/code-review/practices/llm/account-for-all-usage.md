---
id: code-review.llm.account-for-all-usage
title: Trace Usage and Settlement Across LLM Attempts
stage: review
severity: critical
tech_stack: [code-review]
applies_when: a changed LLM call can retry, fall back, stream partially, or alter how provider usage is recorded or settled
anti_patterns:
  - id: code-review.llm.lost-or-duplicate-usage
    name: Usage disappears between attempts
    description: Retrying replaces an incurred attempt before its usage is captured, or a repeated settlement charges it twice.
    severity: critical
---

## When to apply

A diff changes an LLM invocation, response stream, retry or fallback, usage collection, or billing. Determine what happens to each attempt, including attempts whose response is not delivered to the caller.

## Guidance

1. Trace each provider attempt from dispatch through success, error, cancellation, partial stream, and final usage capture. Find the provider's actual guarantees for billable failed calls and usage metadata; a cancelled response is not proof of zero cost.
2. Follow usage into the ledger, customer charge, reconciliation, and deduplication mechanisms. On retry or fallback, identify which attempt each record represents and whether ambiguous completion can repeat it.
3. Check the business, accounting, and compliance contract for required durability, permitted estimates, and recovery. Separately trace whether settlement failure or delay changes an otherwise successful LLM response. A recoverable settlement may be independent, while a required durable record may legitimately gate success.
4. Report a reachable discrepancy between that contract and the changed path, including the affected attempt and consequence. Stop when all relevant terminal paths and their existing safeguards are accounted for.

Provider and transport details change which evidence exists:

- For OpenAI Chat Completions streaming, `stream_options.include_usage` requests an additional usage chunk before `[DONE]`; an interrupted stream may never deliver it. This is endpoint-specific, not a rule for every OpenAI API.
- Anthropic Messages streaming includes initial usage in `message_start` and cumulative output usage in `message_delta`; summing successive cumulative values would overcount.
- A client disconnect can stop consumption before final usage arrives even if the provider has incurred cost. Check whether the server keeps reading, retrieves authoritative usage, estimates under an allowed policy, or reconciles later.
- Fallback attempts may use different models, cached-input rates, currencies, or pricing versions. Associate usage and price with each attempt, not just the final provider.
- Local tokenizer counts are estimates unless the provider contract makes them authoritative; tool input, cache categories, and provider tokenization can differ. Do not silently treat missing usage as zero or an estimate as the provider's exact bill.

## Anti-pattern

A streaming proxy disconnects as soon as the client leaves and persists zero usage because no final usage event arrived. The provider can already have generated billable output; zero is not evidence of zero usage. An approved reconciliation process may instead account for it later.

## Why

One user request can produce several provider attempts, and a response failure does not necessarily reverse provider work. Treating the last result as the only attempt loses the relationship between incurred usage and settlement.

## Exceptions and boundaries

Do not assume every provider cost must be billed to the customer, that final usage metadata always exists, or that a mandatory financial record may be dropped. An established reconciliation process or per-attempt idempotency may close the apparent gap; inspect it. Non-billing notifications belong to side-effect isolation, not this accounting decision.

## Example

A contract requires recording usage from every provider call, including retryable failures. `call_model` returns both `usage` and `retryable`; the changed handler retries by assigning a second result over the first, then calls `charge(result.usage)` once. Because the first result can contain billable usage and no other code records it, the retry line can cause undercounting. If each call records its usage before returning, overwriting the local result alone is not a finding.
