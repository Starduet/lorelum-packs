# Pack Creator

`pack-creator@0.2.0` is an unreleased, domain-neutral Knowledge Pack for creating Lorelum Packs whose Practices can be retrieved independently, understood by humans, used as repository-local project layers or versioned releases, evaluated without confusing format success with semantic or behavioral quality, and supplemented with safely routed Pack-native resources.

Canonical English · [简体中文 companion](./i18n/zh-CN/README.md)

## Scope

Use this Pack when defining a new Pack, deciding whether it is repository-local or a versioned release, splitting domain guidance into Practices, writing triggers and examples, reviewing overlap, designing retrieval fixtures, adding references/assets/scripts, localizing content for human review, or preparing a Registry release.

The Practices apply to Packs about any engineering or product domain. Examples may use security, databases, frontend work, operations, compliance, or Pack infrastructure, but no example defines a mandatory Pack workflow.

## Non-goals

This Pack is not a schema reference, Markdown tutorial, retrieval engine implementation guide, task manager, automatic quality scorer, script runner, or permission system. It does not prescribe a fixed Practice count, directory taxonomy beyond the public Pack contract, or one release process for every repository. Passing validation or installing successfully does not by itself prove that a Pack retrieves useful guidance, preserves a remote resource artifact, or improves Agent behavior.

## Pack-native resources

Use `references/` for additional material to read, `assets/` for files to copy before editing, and
`scripts/` for helpers that a current task may explicitly run. A Practice uses normal Markdown such
as `[review checklist](resource:assets/resource-review-checklist.md)` to explain when the material
is useful. Resources are supplementary: the retrieved Practice still owns the trigger, action,
reason, exceptions, and stopping point.

Read [the resource authoring guide](resource:references/pack-resources.md) after that immediate
decision is already complete. The bundled [inventory helper](resource:scripts/inspect-resources.py)
only lists regular files for a human review; it does not validate, install, or execute Pack content.

## Repository-local Packs

Repository-owned guidance lives under `.lorelum/packs/<pack-name>/`, where a normal `pack.yaml` and canonical `practices/` tree are discovered from the working directory. Use `lore init` once to create the layer config without overwriting an existing file. Parent and child layers inherit by default; a child same-ID Practice overrides only that ID, while parent-only Practices remain active. Derived query artifacts stay in the user cache and must not be committed under `.lorelum`.

Read [the project-local Pack guide](resource:references/project-local-packs.md) for the starter tree and verification sequence. A local Pack does not need `lore pack install`, a Registry entry, or a tag. Registry publication is for a separately versioned Pack that must be installed into unrelated repositories.

## Release history

- `0.1.0` is the published first release.
- `0.2.0` is an unreleased candidate. Its Registry descriptor names `pack-creator-v0.2.0`, which must be created at the reviewed merge commit after canonical content, localization, fixtures, and local-layer evidence are reviewed. No local validation result authorizes an installability claim.

## Candidate evidence status

The following statements intentionally keep evidence layers separate for the local `0.2.0` candidate:

- **Structure:** the current Lorelum source CLI completed `lore validate` for this Pack on September 16, 2026: 27 canonical Practices, 27 current Chinese companions, and no Pack diagnostics. This proves the current directory/link structure only.
- **Content review:** the new and changed Practices received an authoring review for standalone trigger, action, reason, exception, stop condition, and resource-consumption boundary. Maintainer or domain-expert approval remains a release gate; this is not a claim that the guidance is generally correct.
- **Installation and resource readback:** not yet run through the public Registry. The candidate Registry descriptor is not an immutable ref or installation result, so it must not be described as installable or resource-preserved remotely.
- **Retrieval selection:** the fixture catalog and resource-backed workflow state selection hypotheses, but no retrieval run has evaluated them.
- **Downstream Agent behavior:** not run. No claim is made that an Agent will choose, copy, or execute these resources correctly.

See [SOURCES.md](./SOURCES.md) for provenance and synthesis boundaries.
