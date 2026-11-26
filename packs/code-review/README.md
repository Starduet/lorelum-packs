# Code Review

An unreleased, lightweight Knowledge Pack for reviewing changes in repository context. Its five Practices cover backend and UI navigation, task completion boundaries, changed tests, and logging. Findings require reachable scenarios, relevant contracts, and concrete consequences.

## Review entry point

Resolve the installed Pack with `lore pack list code-review` and give its [workflow](resource:references/review-workflow.md), the user's request, and the authorized review scope to the designated reviewer. Use the host's existing diff and source tools. Installation does not load the workflow or select a model.

For an explicit request to consult domain guidance, the [delivery helper](resource:scripts/guidance.py) presents concise candidates and returns only the full Markdown body selected by the reviewer. It saves the complete records separately. The host does not invoke it for ordinary or repository-evidence-only review.

## Use

From the same candidate checkout, install CR into an isolated Store. Install either companion into that same Store when its domain is relevant; neither is required for CR:

```sh
lore pack install --path ./packs/code-review --store-root <isolated-store>
lore pack install --path ./packs/backend-engineering --store-root <isolated-store>
lore pack install --path ./packs/frontend-engineering --store-root <isolated-store>
```

Pin the checkout revision when evaluating this combination. For React-specific guidance, optionally install `react-web-craft@0.1.1` from the official Registry into the same Store. Reading a navigation Practice does not establish that any companion is installed.

Use navigation to identify distinct changed behavior paths, then query for the domain decisions that need guidance using the observed mechanism, without a review-stage filter. Check each match against the repository's actual contracts. Adding a domain Practice does not require editing CR navigation.

This candidate is not registered or released. Installation and retrieval do not prove that a
reviewer will find real defects. [Sources](./SOURCES.md) records the references used to write the
Practices.
