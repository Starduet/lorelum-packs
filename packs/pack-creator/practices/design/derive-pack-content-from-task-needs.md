---
anti_patterns:
  - description: The author copies the structure and level of detail of an existing Pack into a new domain without checking what its users actually need, leaving out task-specific knowledge while packaging generic instructions the model already knows.
    id: pack-creator.design.copy-pack-shape-without-task-evidence
    name: Existing Pack shape substituted for task evidence
    severity: warn
applies_when: defining or substantially revising a Pack and deciding what knowledge to include, how to organize it, and how to assess whether it helps its intended tasks
id: pack-creator.design.derive-pack-content-from-task-needs
severity: warn
stage: design
tech_stack:
  - lorelum-pack-authoring
title: Derive Pack Content from Task Needs
---

## When to apply

Use this when shaping a Pack for a real task or revisiting one whose content does not clearly help its intended users. Do not start by selecting a predefined Pack type or copying another Pack's structure.

## Guidance

Start with representative requests and the decisions or actions the user needs at the moment the guidance will be used. Identify what a capable model can already do and what it cannot reliably infer without the relevant domain, project, source, or version-specific knowledge. Ground proposed guidance in concrete task evidence and authoritative material; identify missing evidence rather than inventing facts or parameters.

Use the considerations that actually distinguish this task, not a mandatory questionnaire. For example:

- **Knowledge and sources:** Is the needed information a stable principle, a local constraint, a detailed procedure, or a fact tied to a particular source or version? Preserve its scope and provenance, and keep changeable details traceable to their source.
- **Moment of use:** What request or decision should retrieve the guidance, and what context must the reader have then? Keep the information needed for that decision accessible without assuming an earlier Practice was read.
- **Decision coupling:** Can choices arise independently, or would separating them lose necessary context? Give independently needed decisions distinct triggers; keep inseparable reasoning together. Use a linked resource for supplementary detail when it helps, not as a substitute for essential guidance.
- **Error cost:** What could go wrong, and how consequential is it? Supply the explanation, evidence, checks, boundaries, or examples needed to make that decision safely; do not impose the same depth on every Practice.

Choose content, detail, and organization from these observations rather than from the headings above. Evaluate with representative tasks, including neighboring or out-of-scope requests: check whether the right guidance is found, whether its evidence and scope support the choice, and whether it changes the resulting behavior usefully compared with working without the Pack. Treat format validation, retrieval, and behavioral evidence as separate claims; note what has not been evaluated.

For contrasting, non-exhaustive applications, consult [task-shaped Pack design examples](resource:references/task-shaped-pack-design.md) when the tradeoffs in content or organization are unclear.

## Anti-pattern

An author copies a previous Pack's checklist, file boundaries, and detail level into a new domain because the old Pack was useful. The new tasks need a version-specific constraint and a coupled decision absent from that checklist, while much of the copied advice restates general model capability. The Pack can be well formatted yet fail to provide the knowledge needed at the decision point.

## Why

A Pack adds value by making relevant knowledge available when it changes a real decision. Different tasks need different evidence, granularity, and organization; a familiar layout alone does not establish any of them.

## Exceptions and boundaries

An existing Pack can suggest questions or a reusable structure when task evidence supports it. Not every consideration applies to every task, and a simple decision may need only concise guidance. Do not add runtime type fields, a fixed body template, or required answers to these considerations.

## Example

For a team choosing a data-retention policy, the author examines actual policy decisions and their governing sources. If the retention period is not established by those sources, the Practice tells the reader to obtain the applicable requirement rather than invent a number. The author separates independently triggered choices only where each remains understandable, and evaluates representative decisions against the available evidence.
