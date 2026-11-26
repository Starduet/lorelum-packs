# Code Review

An unreleased, lightweight Knowledge Pack for reviewing changes in repository context. Its five Practices cover backend and UI navigation, task completion boundaries, changed tests, and logging. Findings require reachable scenarios, relevant contracts, and concrete consequences.

## Review entry point

For an explicit review request, resolve the installed Pack with `lore pack list code-review` and use its [workflow](resource:references/review-workflow.md). The optional `review-tools.py prepare --scope scope.json [--focus "user request"]` produces a prompt for the host to pass to the designated reviewer. A focus prioritizes a question without changing the review target. Installation does not load guidance or select a model; the host owns reviewer dispatch.

For an explicit request to consult domain guidance, use `prepare --guidance requested` and the `guidance` helper. With `--record`, the helper saves full JSON and prints concise candidates or the selected Practice as Markdown for the same reviewer. For a repository-evidence-only request, use `--guidance source-only`. Ordinary reviews keep the default `manual` mode.

## Use

From the same candidate checkout, install CR into an isolated Store. Install either companion into that same Store when its domain is relevant; neither is required for CR:

```sh
lore pack install --path ./packs/code-review --store-root <isolated-store>
lore pack install --path ./packs/backend-engineering --store-root <isolated-store>
lore pack install --path ./packs/frontend-engineering --store-root <isolated-store>
```

Pin the checkout revision when evaluating this combination. For React-specific guidance, optionally install `react-web-craft@0.1.1` from the official Registry into the same Store. Reading a navigation Practice does not establish that any companion is installed.

Use navigation to identify distinct changed behavior paths, then query for the domain decisions that need guidance using the observed mechanism, without a review-stage filter. Check each match against the repository's actual contracts. Adding a domain Practice does not require editing CR navigation.

The [review tools](resource:scripts/review-tools.py) are optional Python and Git tools for scope capture, bounded reads, and mechanical location and coverage checks. The [workflow](resource:references/review-workflow.md) documents their commands and fields. Installation, indexing, and retrieval do not run the script. It cannot decide findings, infer review coverage, or verify reviewer identity.

This candidate is not registered or released. Installation and retrieval do not prove that a
reviewer will find real defects. [Sources](./SOURCES.md) records the references used to write the
Practices.
