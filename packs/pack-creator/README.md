# Pack Creator

`pack-creator@0.2.0` is an unreleased, domain-neutral Knowledge Pack for creating Lorelum Packs whose Practices can be retrieved independently, understood by humans, evaluated without confusing format success with semantic or behavioral quality, and supplemented with safely routed Pack-native resources.

Canonical English · [简体中文 companion](./i18n/zh-CN/README.md)

## Scope

Use this Pack when defining a new Pack, splitting domain guidance into Practices, writing triggers and examples, reviewing overlap, designing retrieval fixtures, adding references/assets/scripts, localizing content for human review, or preparing a versioned Registry release.

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

## Release history

- `0.1.0` is the published first release.
- `0.2.0` is an unreleased candidate. It must receive a new immutable `pack-creator-v0.2.0` ref and Registry entry after canonical content, localization, fixtures, and the resource evidence chain are reviewed. No local validation result authorizes an installability claim.

## Candidate evidence status

The following statements intentionally keep evidence layers separate for the local `0.2.0` candidate:

- **Structure:** the current Lorelum source CLI completed `lore validate` for this Pack on September 15, 2026: 23 canonical Practices, 23 current Chinese companions, and no Pack diagnostics. This proves the current directory/link structure only.
- **Content review:** the new and changed Practices received an authoring review for standalone trigger, action, reason, exception, stop condition, and resource-consumption boundary. Maintainer or domain-expert approval remains a release gate; this is not a claim that the guidance is generally correct.
- **Installation and resource readback:** not yet run through the public Registry. The current `0.2.0` source has no immutable `pack-creator-v0.2.0` ref or Registry release entry, so it must not be described as installable or resource-preserved remotely.
- **Retrieval selection:** the fixture catalog and resource-backed workflow state selection hypotheses, but no retrieval run has evaluated them.
- **Downstream Agent behavior:** not run. No claim is made that an Agent will choose, copy, or execute these resources correctly.

See [SOURCES.md](./SOURCES.md) for provenance and synthesis boundaries.
