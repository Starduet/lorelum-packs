---
id: code-review.llm.account-for-all-usage
title: Don't Lose Track of What Each LLM Call Cost
stage: review
severity: critical
tech_stack: [code-review]
applies_when: an LLM provider call, stream, usage ledger, charge, retry, or fallback changes and per-attempt settlement may be lost or duplicated
anti_patterns:
  - id: code-review.llm.lost-or-duplicate-usage
    name: Usage disappears between attempts
    description: Retrying replaces an incurred attempt before its usage is captured, or a repeated settlement charges it twice.
    severity: critical
---

## When to apply

An LLM call can succeed, stop halfway, retry, or fall back to another provider. When the code changes any of those paths, check what gets recorded for every call that may have cost money.

## Guidance

Follow each call from the provider response to the usage record and the price used for it. A retry or fallback may mean there are two calls to account for, even if the user sees only one answer.

Also check what happens when the answer is ready but recording usage or charging fails. Does the user still get the answer? Whether that is allowed depends on the billing and accounting requirements; don't assume either that billing may be discarded or that it must block the response.

The details vary by provider:

- For OpenAI Chat Completions streaming, `stream_options.include_usage` requests an additional usage chunk before `[DONE]`; an interrupted stream may never deliver it. This is endpoint-specific, not a rule for every OpenAI API.
- Anthropic Messages streaming includes initial usage in `message_start` and cumulative output usage in `message_delta`; summing successive cumulative values would overcount.
- A client disconnect can stop consumption before final usage arrives even if the provider has incurred cost. Check whether the server keeps reading, retrieves authoritative usage, estimates under an allowed policy, or reconciles later.
- Fallback attempts may use different models, cached-input rates, currencies, or pricing versions. Associate usage and price with each attempt, not just the final provider.
- Local tokenizer counts are estimates unless the provider contract makes them authoritative; tool input, cache categories, and provider tokenization can differ. Do not silently treat missing usage as zero or an estimate as the provider's exact bill.

## Anti-pattern

A streaming proxy stops reading when the client disconnects. It records zero usage because it never received the final usage event, even though the provider may already have generated billable output. A separate reconciliation process may account for the missing usage; check for one before reporting loss.

## Why

The provider can charge for work even when the user never receives the answer. Looking only at the final response can miss an earlier call or charge for the same call twice.

## Exceptions and boundaries

Do not assume every provider cost must be billed to the customer, that final usage metadata always exists, or that a mandatory financial record may be dropped. An established reconciliation process or per-attempt idempotency may close the apparent gap; inspect it. Non-billing notifications belong to side-effect isolation, not this accounting decision.

## Example

A contract requires recording usage from every provider call, including retryable failures. `call_model` returns both `usage` and `retryable`; the changed handler retries by assigning a second result over the first, then calls `charge(result.usage)` once. Because the first result can contain billable usage and no other code records it, the retry line can cause undercounting. If each call records its usage before returning, overwriting the local result alone is not a finding.
