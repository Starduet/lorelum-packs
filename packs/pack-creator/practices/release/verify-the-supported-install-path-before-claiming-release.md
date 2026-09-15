---
anti_patterns:
  - description: Treating a valid local directory, green schema check, or documented install command as proof of release skips the remote Registry and materialization path that users actually depend on.
    id: pack-creator.release.local-validation-as-release-proof
    name: Local validation reported as a published release
    severity: warn
applies_when: a versioned Pack is about to be described as published or installable, and the maintainer must verify the actual Registry, release ref, source materialization, decoding, and installation path users are expected to run
id: pack-creator.release.verify-the-supported-install-path-before-claiming-release
severity: warn
stage: release
tech_stack:
  - lorelum-pack-authoring
title: Verify the Supported Install Path before Claiming Release
---

## When to apply

Apply after an immutable release candidate and Registry entry exist, before saying the Pack is
published, installable, or available through the supported command. The decision is whether the
complete supported distribution chain works for that exact version. Content quality, retrieval
behavior, and downstream usefulness require separate evidence.

## Guidance

Use an isolated destination and the same public install path users are told to use. Resolve the Pack
through the intended Registry repository, confirm the selected version and release ref, materialize
only the supported Pack files, pass the Pack decoder and validation gate, install into the intended
store, and read back the installed Pack identity and expected Practice IDs. Record the resolved
commit, version, command or API path, environment, and result. Fail the release claim when the
Registry points to a missing or movable ref, the remote source differs from the reviewed candidate,
materialization omits files, decoding fails, or the installed identity is wrong. Stop after one
representative supported path succeeds for the exact release, plus any additional platform checks
the release policy requires; do not turn repeated installs into a semantic-quality score.

When the release contains Pack-native resources, retrieve one Practice that links a representative
file and resolve that target from its returned Pack root. Record the target and observed file bytes
or digest. This establishes selected-artifact preservation only; it does not execute a script or
prove retrieval quality.

## Anti-pattern

An author prepares an incident-alerting Pack. The local directory validates, all files appear in the
catalog, and the README shows the official install command. The release deadline is near, and
creating the tag after merge seems routine, so the author announces that `0.1.0` is installable. The
Registry ref was mistyped and does not exist remotely. Every local content check remains green, but
a user cannot materialize the Pack through the documented path.

## Why

Users install a released Pack through more than its local directory. Registry resolution, the
immutable ref, remote object retrieval, decoding, and store installation can fail independently.
Exercising that chain supports an installability claim and nothing broader.

## Exceptions and boundaries

A private or offline Registry may require its own supported environment and credentials; verify that
documented path without exposing secrets. A draft may be described as locally valid before a release
ref exists when the limitation is explicit. Successful installation does not show that the Practices
are clear, retrieve for the right queries, or improve Agent decisions, and the number of installed
entries does not prove coverage.

## Example

A frontend-performance Pack has passed human review and is tagged for release. In a clean temporary
store, the maintainer installs it through the official Registry name rather than from the working
tree. The result resolves the reviewed commit and version, materializes the expected canonical
paths, passes decoding, and reads back the Pack ID and Practice IDs. The maintainer records that
evidence and then claims the version is installable, while keeping separate statements for semantic
review and retrieval tests.
