# Backend Engineering

An unreleased Knowledge Pack for backend engineering decisions. Its Practices apply during design, implementation, and review; use the repository's contracts and actual callers to decide which guidance applies.

For local evaluation, install with `lore pack install --path ./packs/backend-engineering --store-root <isolated-store>`. Query using the actual operation, shared resource, guard, and uncertainty, then read an applicable result with `lore get`. The Pack is not registered or released. Installation and retrieval alone do not establish that an agent uses the guidance or improves review.

## Practices

| Decision | Practice |
| --- | --- |
| Identify the owner of a task and how it stops, reports errors, and joins | [Own task lifetimes](practices/async/own-task-lifetimes.md) |
| Establish what a lock or gate protects and when it releases | [Justify locks and gates](practices/concurrency/justify-locks-and-gates.md) |
| Keep retries and crashes from losing or repeating required effects | [Align effects and acknowledgements](practices/delivery/align-effects-and-acknowledgements.md) |
| Capture usage and settle each provider attempt without double charging | [Account for each attempt](practices/llm/account-for-each-attempt.md) |
| Keep optional failures and delays from controlling the primary result | [Isolate optional work](practices/side-effects/isolate-optional-work.md) |
| Prevent obsolete results from overwriting current state | [Guard current-generation writes](practices/state/guard-current-generation-writes.md) |

See [Sources and synthesis](references/SOURCES.md) for the applicable versions and limits of product-specific guidance.