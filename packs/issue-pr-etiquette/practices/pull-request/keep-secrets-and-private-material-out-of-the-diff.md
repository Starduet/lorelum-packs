---
anti_patterns:
  - description: Posting a diff that carries credentials or private material publishes it to crawlers and caches permanently, and later deletion or force-push does not unpublish it.
    id: issue-pr-etiquette.pull-request.secrets-in-the-diff
    name: Secrets or private material in the diff
    severity: warn
applies_when: a change touches configuration, logging, fixtures, test data, example output, or material copied from a private system, and the diff is about to be published for review
id: issue-pr-etiquette.pull-request.keep-secrets-and-private-material-out-of-the-diff
severity: warn
stage: pull-request
tech_stack:
  - github-contribution
title: Keep Secrets and Private Material out of the Diff
---

## When to apply

Apply as the final check before requesting review on any PR, and while drafting any public post that
quotes logs or data. The decision is whether the diff and quoted material are publishable as
written. Suspicion alone is enough to apply — verifying a suspicion belongs to the fix, not the
check.

## Guidance

Scan every added line for access tokens, API keys, passwords, connection strings, internal
hostnames, customer identifiers, and real personal data; also scan quoted logs, fixture files, and
example output, which leak as easily as config. Replace real values with synthetic placeholders
(`internal.example`, `user-1234`, `ssh-key-ed25519-REPLACED`) and load secrets from the environment
or the platform's secret store. If a secret has already been pushed anywhere public, treat it as
leaked: rotate it first, then follow the repository's removal process — rewriting history does not
unpublish what crawlers already copied. Stop when you can explain each suspicious-looking string in
the diff as synthetic or public.

## Anti-pattern

To make a failing integration test reproducible, a contributor pastes the real internal endpoint and
a working token into the fixture. The PR is public; automated crawlers read it within the hour. The
token is rotated a day later, but the internal hostname and topology sit in caches and forks
forever, and the incident costs more goodwill than the test ever saved.

## Why

A published diff is copied immediately and permanently by crawlers, mirrors, and forks — deletion
and force-push do not recall it. Sanitization also protects the people in the data: customer
identifiers and personal records in fixtures outlive the bug they illustrated. The final-line check
is cheap; every downstream consequence is not.

## Exceptions and boundaries

Identifiers that are public by design — public documentation URLs, published example values,
already-public package names — stay as written. A reference to a secret, such as an environment
variable name or a secret-store key, is not a secret and belongs in the diff; only the value does
not. Private-review channels reduce exposure but do not change the check, because the material
usually becomes public on merge anyway.

## Example

Before requesting review, the author rereads the diff and spots a real internal hostname in a pasted
error message. They replace it with `internal.example`, swap the fixture token for a synthetic one,
confirm the test still reproduces with the placeholder, and note the sanitization in the PR body's
checklist item. The PR goes up clean.
