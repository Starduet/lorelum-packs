# Pack resource review checklist

Copy this checklist into the release or review record and complete only the rows applicable to the
Pack. It distinguishes observations; checked rows must not be summarized as evidence for unchecked
layers.

## Structure

- [ ] `lore validate <pack-root>` completed and the result, Pack revision, and diagnostics are recorded.
- [ ] Canonical Practice metadata has the runtime-required `id`, `title`, `stage`, `tech_stack`, and `applies_when`; any structured anti-pattern has `id`, `name`, `description`, and `severity`. Practice-level `severity` is optional in the format.
- [ ] The body contains what the particular decision needs, without a prescribed set or order of headings, examples, explanations, exceptions, or stopping conditions. Remove material that does not help the decision.
- [ ] `applies_when` states the applicability condition; the body need not repeat it. Localized companions mirror the Practice paths without copying runtime YAML metadata.
- [ ] Every linked `resource:` target is in `references/`, `assets/`, or `scripts/` and has a clear task-time purpose in its Practice.
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

### Domain Packs used in code review

- [ ] Install the candidate and the Code Review Pack into the same isolated Store. Verify
  installation and read a representative Practice separately from the review run.
- [ ] Use a pinned, representative change and run an ordinary review without preloading a
  Practice, suggesting a query, or requesting explicit guidance. Record the change, Pack
  revisions, reviewer model, the question it asks, the candidates offered, and whether an
  applicable full Practice reached the reviewer before its conclusion. Record incomplete runs
  and provider failures separately.

If the reviewer asks the right question but cannot retrieve useful guidance, inspect the domain
Practice and retrieval. Consider changing CR navigation only when reviewers repeatedly overlook
the underlying behavior and never ask the question. Adding a Pack does not by itself require a
navigation update.

Report this run separately from structural validation. If automated, run it on demand and
report the observed results; do not make model output or provider availability a merge gate.
