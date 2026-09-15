# Pack resource authoring guide

Use this reference after a Practice already contains the trigger, action, direct reason, exceptions,
and stopping point for its immediate decision. It summarizes how a Pack may provide additional
materials without turning those materials into a second workflow or an execution authority.

## Canonical tree

```text
<pack-root>/
├── pack.yaml
├── practices/
├── decisions.yaml                 # optional
├── references/                    # optional
├── assets/                        # optional
├── scripts/                       # optional
└── i18n/                          # authoring-only companions
```

`references/`, `assets/`, and `scripts/` can contain nested ordinary files. They remain part of the
immutable Pack artifact, are not independent retrieval candidates, and do not need a global
attachment manifest. A Practice’s Markdown body gives the task-specific route.

## Resource links

Use an ordinary Markdown link whose target is a Pack-root-relative `resource:` path:

```markdown
[migration compatibility matrix](resource:references/migration-compatibility.md)
[migration-plan template](resource:assets/migration-plan.md)
[read-only schema diff](resource:scripts/schema-diff.py)
```

The path must start with `references/`, `assets/`, or `scripts/` and point to a regular file in the
same Pack. Do not use a sibling-relative path, a Pack-name alias, a Store path, `..`, a symlink,
query, fragment, or ordinary web URL as a resource target. Normal Markdown links retain their usual
meaning.

## Consumption boundary

- Read a reference only when the linking Practice says its additional detail is needed.
- Copy an asset to the caller’s task destination before changing it.
- Run a script only with current-task authorization, named inputs, and expected output. Installation,
  validation, discovery, retrieval, indexing, and recovery do not run Pack scripts.

The link is guidance about when to use a resource, not a file-access allowlist. A user who explicitly
selects a Pack can browse its returned Pack root. A caller must obtain that root through the public
CLI result rather than reconstructing the local Store layout.

## Validation and evidence

`lore validate <pack-root>` reports resource-directory safety and invalid or missing `resource:`
targets. It does not execute scripts, install dependencies, read credentials, connect to a network,
or require every helper file to have a direct link. Use the resource review checklist for release
evidence, but keep format validity, installability, retrieval selection, script behavior, and Agent
behavior as separate claims.
