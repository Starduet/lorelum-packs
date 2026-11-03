# Pack resource review checklist

Copy this checklist into the release or review record and complete only the rows applicable to the
Pack. It distinguishes observations; checked rows must not be summarized as evidence for unchecked
layers.

## Structure

- [ ] `lore validate <pack-root>` completed and the result, Pack revision, and diagnostics are recorded.
- [ ] Canonical Practice metadata has the runtime-required `id`, `title`, `stage`, `tech_stack`, and `applies_when`; any structured anti-pattern has `id`, `name`, `description`, and `severity`. Practice-level `severity` is optional in the format.
- [ ] Each Practice follows this Pack's existing six-section authoring pattern: When to apply, Guidance, Anti-pattern, Why, Exceptions and boundaries, and Example. This is an authoring check, not a claim that all six headings are runtime-required.
- [ ] The existing applicability field and section state the condition; no additional summary or introduction is required. Localized companions mirror the Practice paths without copying runtime YAML metadata.
- [ ] Every linked `resource:` target is in `references/`, `assets/`, or `scripts/` and has a clear task-time purpose in its Practice.
- [ ] The Practice still contains the immediate trigger, action, reason, exceptions, and stopping point.
- [ ] Resource files and directories meet repository safety and size rules; any unlinked helper or grouped asset is intentional.

## Selected artifact and installation

- [ ] The exact version, immutable ref, and registry entry were recorded.
- [ ] A supported isolated installation preserved a representative linked reference or asset at the locator returned for the selected Pack/Practice.
- [ ] No claim says that local directory validation alone proves remote materialization or release availability.

## Script execution, if applicable

- [ ] The task explicitly authorized execution, with inputs, expected output, and host constraints recorded.
- [ ] Script behavior was observed separately from format validation and installation.
- [ ] No script was treated as an install hook or as an automatic capability granted by the Pack.

## Retrieval and downstream use

- [ ] Representative queries checked that the Practice, rather than a neighboring one, is selected when its resource is needed.
- [ ] A downstream Agent task, if run, records the exact Practice/resource revision and observed outcome.
- [ ] The release or review statement names only the evidence layers actually observed.
