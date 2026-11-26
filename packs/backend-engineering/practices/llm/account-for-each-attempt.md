---
id: backend-engineering.llm.account-for-each-attempt
title: Account for Each LLM Provider Attempt
stage: design
severity: warn
tech_stack: [backend]
applies_when: designing provider calls, streaming, retry or fallback, usage capture, reconciliation, or settlement
anti_patterns:
  - id: backend-engineering.llm.lost-or-duplicate-usage
    name: Lose an attempt or settle it twice
    description: A retry replaces an incurred attempt before its usage is recorded, or repeated settlement charges for the same usage twice.
    severity: warn
---

## Decision

Keep the logical operation and its provider attempts separate. Record each retry or fallback under its own stable attempt identity, linked to the operation. Associate the usage and its provenance with the provider, model, applicable price version and currency. Provider cost, the customer charge, and internal audit are separate records or decisions; the provider can incur cost even when the customer is not charged.

## Capture what actually arrives

Trace completion, partial output, provider error, cancellation, and client disconnect. A client that stops reading can miss usage even though the provider has already done billable work. Preserve any partial usage and distinguish it from final usage, missing usage, and estimates. Do not silently record missing usage as zero or present a local tokenizer estimate as authoritative. Check which units the provider reports, including cache or tool categories where applicable.

- OpenAI Chat Completions: `stream_options.include_usage` requests an extra usage chunk before `[DONE]`; an interrupted stream may not deliver it. This does not establish the behavior of the Responses API.
- Anthropic Messages streaming: `message_delta.usage` token counts are cumulative. Use the reported totals for the relevant scope rather than adding the snapshots; for true deltas, accumulate each event once. Recheck the usage scope at model boundaries for provider-managed fallback and inspect what the actual SDK exposes.

## Settle without charging twice

Decide from the business and audit contract whether to capture usage synchronously, hand it off durably, apply a labeled estimate under an explicit policy, or reconcile against provider records when available. Confirm that any handoff persists enough information to recover an attempt whose final usage never arrived. Use a stable settlement key with an atomic duplicate check or equivalent idempotency guarantee; a replay must not create another charge. Reconcile corrections without treating an updated total as another attempt.

For example, a stream fails after generating output and fallback returns a complete answer. Recording only the successful response hides the original attempt. Keep the failed attempt with the usage actually observed and reconcile it as required. If a per-attempt ledger and reconciliation already cover it, replacing a local response variable is not evidence of lost usage. Usage metadata alone is not an invoice.
