---
anti_patterns:
  - description: Updating content behind an old version or tag because the change looks minor breaks reproducible installs, while vague source claims prevent reviewers from separating documented facts from author synthesis.
    id: pack-creator.release.mutable-release-with-blurred-provenance
    name: Existing release rewritten as a correction
    severity: warn
applies_when: canonical Pack content or its release sources have changed and the maintainer must decide how to publish a reproducible version without rewriting an existing release or overstating where the guidance came from
id: pack-creator.release.preserve-versioned-content-and-provenance
severity: warn
stage: release
tech_stack:
  - lorelum-pack-authoring
title: Publish Changed Content as a Traceable New Version
---

## When to apply

Apply when accepted canonical content is ready to become a release, or when already released content
needs correction. The decision is which immutable version will contain the exact files and how
reviewers can trace each important rule to a public source, observed recurring need, or clearly
labeled author synthesis. Whether the release can actually be installed is a separate verification
step.

## Guidance

Freeze the release candidate at one repository commit. If canonical guidance changed after an
existing release, choose a new version and new release ref instead of moving the old tag or
replacing its files. Update the Registry entry and human release notes to point to that version only
when the release object is ready. Record provenance at enough detail for a reviewer to distinguish
source-explicit requirements, observations of recurring failures, and the author’s generalized
judgment; do not describe synthesis as measured effectiveness. Preserve source links and the version
boundary even when a correction changes only wording or resource bytes, because wording can change
retrieval and a resource-only change still changes the selected artifact. Record whether a release
changes canonical Practice content, only `references/`/`assets/`/`scripts/` bytes, or both. Stop
when the version, commit, release ref, canonical files, resource tree, and provenance record
identify one reproducible object. Installation proof comes next.

## Anti-pattern

A network-security Pack already has version `1.0.0` tagged. A maintainer learns that one TLS
Practice recommends an obsolete cipher and fixes a single paragraph. Creating a new version,
Registry row, and release note feels heavy for such a small diff, so moving the old tag seems like
harmless correction. The old install can now produce different guidance on different days, and the
updated source note says only “industry best practice,” hiding whether the rule came from current
vendor documentation or author judgment.

## Why

Pack content changes Agent decisions, so an old version must continue to mean the same bytes and
guidance. A resource-only update can change the reference, asset, or script the next retrieval
locates even when a Practice digest remains stable. Clear provenance lets reviewers assess the basis
and limits of a rule without mistaking a reasonable synthesis for published evidence that the Pack
works.

## Exceptions and boundaries

Unreleased drafts may change in place when no Registry release or immutable ref promises
reproducibility. A broken tag or accidentally exposed secret requires repository governance and
incident handling; do not preserve harmful data merely for immutability. Provenance need not cite
every ordinary sentence, but material claims and synthesis boundaries must be reviewable. A
versioned release object does not prove semantic quality or installability.

## Example

An operations Pack updates its incident-severity guidance after the organization publishes a new
public response policy and maintainers observe that two existing Practices retrieve for the same
escalation decision. The author revises the trigger boundary, cites the policy for the explicit
response times, labels the split between the two Practices as Pack-authoring synthesis, and
publishes the files at a new commit and version. The old tag remains unchanged, so previous installs
stay reproducible while reviewers can see which parts came from policy and which came from design
judgment.
