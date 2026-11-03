---
anti_patterns:
  - description: Merging or deleting Practices merely to reduce file count can erase different decision moments, while leaving concise but generic guidance that retrieves broadly and helps with neither decision.
    id: pack-creator.review.shorter-pack-as-better-pack
    name: Shorter Pack treated as a better Pack
    severity: warn
applies_when: a draft Pack has complete Practices, and the author must remove generic advice, repeated rules, artificial examples, or unnecessary ceremony without erasing distinctions that should retrieve separately
id: pack-creator.review.run-subtractive-content-review
severity: warn
stage: review
tech_stack:
  - lorelum-pack-authoring
title: Remove Content That Does Not Change a Decision
---

## When to apply

Once the draft covers the decisions you intended, remove what does not help readers choose or act,
before translation and release make revisions more costly. Do not aim for the fewest files. Guidance
still needs to stay separate when its trigger, action, exception, or consequence of failure differs.

## Guidance

Read each Practice as if it were retrieved alone. Delete a sentence when removing it does not change
the action, judgment, stopping point, exception, or reason. Remove introductions that only praise
good engineering, examples that hide the relevant relationships, repeated warnings already stated
more specifically elsewhere, and tool ceremony that the decision does not require. Compare
neighboring Practices before merging them: keep both when a realistic query should select one but
not the other, and sharpen that difference in their `applies_when` and Guidance. Stop when every
remaining part affects a decision and every Practice answers a different need when retrieved. Do not
keep deleting just to reduce word or file counts.

## Anti-pattern

An author is preparing a database-reliability Pack for review. The repository has separate Practices
for verifying backups before release and restoring service during an incident. Reviewers say the
Pack feels long, and both files mention restoration, so merging them into “test backups and
restores” looks like a clean reduction. The merge removes the different timing, evidence, and
stopping conditions: a release-planning query and an active-recovery query now retrieve the same
generic paragraph, and neither gets the action it needs.

## Why

Generic and repeated content competes for retrieval attention without changing behavior. But a
smaller file count is not evidence of better content. Subtractive review improves the Pack only when
it removes noise while preserving differences that let the right Practice answer the right decision.

## Exceptions and boundaries

Brief context may stay when a cold reader needs it to understand the action or exception. Two
Practices may intentionally repeat a necessary fact if each must work alone, but they should not
duplicate the same decision. This review does not decide whether the Pack covers the right domain
decisions in the first place, and it does not replace retrieval evaluation with contrasting queries.

## Example

A frontend-accessibility Pack has one Practice for choosing keyboard focus after a modal opens and
another for announcing asynchronous validation errors to assistive technology. Both drafts repeat a
paragraph saying to “test accessibility carefully,” and each includes setup steps for one test
runner. The author deletes the generic paragraph and runner-specific ceremony, keeps the two
Practices because their triggers and user effects differ, and rewrites each example around its own
observable decision. Review stops when no remaining sentence is decorative and the two files still
answer different queries.
