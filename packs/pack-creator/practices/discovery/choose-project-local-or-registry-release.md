---
anti_patterns:
  - description: The author sees that a Pack has a valid pack.yaml and treats the project directory as a publishing target, adding a Registry release or installing it into a user Store even though the guidance is only meant to travel with one repository.
    id: pack-creator.discovery.local-pack-published-too-early
    name: Repository-local Pack treated as a Registry release
    severity: warn
applies_when: a team wants Practices to affect one source tree, and the author must decide whether they belong in that directory's .lorelum layer or in a versioned Registry release
id: pack-creator.discovery.choose-project-local-or-registry-release
severity: warn
stage: discovery
tech_stack:
  - lorelum-pack-authoring
title: Choose a Project Layer or a Registry Release
---

## When to apply

Apply before creating a Pack when the guidance may be useful to more than one person, but it is not
yet clear whether it belongs to one repository or should be installed independently. This decision
selects the distribution boundary. Creating the local files and choosing parent/child precedence
come later.

## Guidance

Use a project-local Pack when its authority, vocabulary, source files, or review boundary belongs to
one source tree and should travel with that tree. Put it under `.lorelum/packs/<pack-name>/` in the
directory where the guidance should begin to apply. It is source content: do not run
`lore pack install`, create a Registry release, or commit index/cache files merely to make it
queryable.

Use a versioned Registry release when the same reviewed Pack must be installed into unrelated
repositories or retained as a reproducible public artifact. That is a separate distribution step:
prepare a version, immutable ref, Registry entry, and supported installation evidence. A local Pack
can later be promoted, but copy its reviewed canonical files into a new release candidate instead of
treating one mutable working tree as a Registry artifact.

State the chosen audience and lifecycle in the Pack README or contribution guidance. Stop when a
reader can tell whether editing the repository files changes the intended source of truth, and
whether a Registry release is deliberately out of scope. For the local starter layout and commands,
see [the project-local Pack guide](resource:references/project-local-packs.md).

## Anti-pattern

A payments service needs three Practices about its own deployment gates, a private staging
environment, and a generated contract file. The team wants them available while editing that
repository. An author creates a Registry entry and tells everyone to install the Pack globally,
because the Pack already has a name and version. The service guidance now depends on a separate
install/update step, can become stale relative to the repository, and may appear in unrelated
projects. The correct boundary is a local `.lorelum/packs/payments-delivery/` Pack; a Registry
release is useful only if the guidance later becomes independently maintained across repositories.

## Why

Project layers make repository-owned guidance immediately available without polluting a user's Store
or turning derived index state into source control. Registry releases solve a different problem:
reproducible distribution of a reviewed immutable artifact.

## Exceptions and boundaries

A repository may intentionally contain a public Pack release candidate, but its local behavior and
its Registry publication are still different facts. A local Pack does not require Git; ordinary
directories use the same `.lorelum` contract. Do not use a local layer to silently replace an
organization-wide release when the broader Pack is the intended authority.

## Example

An infrastructure repository has Terraform modules, a release workflow, and an internal ownership
map that change together. The maintainers create `.lorelum/packs/infrastructure-delivery/` and keep
the Practices in the same pull requests as those files. A platform team later extracts two rules
that apply to every service, reviews them without repository-private assumptions, and publishes a
separate Registry Pack version. The local Pack remains repository-owned; the release is an
independent artifact with its own provenance.
