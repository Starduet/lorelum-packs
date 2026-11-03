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

Before requesting review on any PR, check that the diff contains nothing private. Do the same before
publishing a post that quotes logs or data. Even if you only suspect a value might be private, find
out before publishing it.

## Guidance

Scan every added line for access tokens, API keys, passwords, connection strings, internal
hostnames, customer identifiers, and real personal data; also scan quoted logs, fixture files, and
example output, which leak as easily as config. Replace real values with synthetic placeholders
(`internal.example`, `user-1234`, `ssh-key-ed25519-REPLACED`) and load secrets from the environment
or the platform's secret store. If a secret has already been pushed anywhere public, treat it as
leaked: rotate it first, then follow the repository's removal process — rewriting history does not
unpublish what crawlers already copied. Finish the check only when you can explain why each
suspicious-looking string in the diff is synthetic or already public.

## Anti-pattern

To make a failing integration test reproducible, a contributor pastes the real internal endpoint and
a working token into the fixture. The PR is public; automated crawlers read it within the hour. The
token is rotated a day later, but the internal hostname and topology sit in caches and forks
forever, and the incident costs more goodwill than the test ever saved.

## Why

A published diff can remain in crawlers, mirrors, and forks after deletion or force-push. Removing
sensitive values before posting also protects the people in the data: customer identifiers and
personal records can outlive the bug they illustrated. Checking the diff before publication avoids
exposure that later removal cannot undo.

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
