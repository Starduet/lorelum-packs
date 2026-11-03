---
anti_patterns:
  - description: Requesting review on a post that was never read back risks headings, lists, and checkboxes having been flattened in the saved copy, silently changing what reviewers act on.
    id: issue-pr-etiquette.communication.unread-back-post-requested-for-review
    name: Review requested on an unverified saved post
    severity: warn
applies_when: an issue or PR has just been created or its body edited, and the author is about to request review or merge
id: issue-pr-etiquette.communication.read-back-your-post-before-requesting-review
severity: warn
stage: communication
tech_stack:
  - github-contribution
title: Read Back Your Post before Requesting Review
---

## When to apply

After creating an issue, opening or editing a PR body, or posting an important status comment, read
the saved post before asking for review, approval, or merge. Check the platform's rendered copy, not
just your local draft or a live preview: saving or pasting can change how the post appears.

## Guidance

Reopen the saved post on the platform and read it as a reviewer would. Verify that headings rendered
as headings, lists kept their items and indentation, line breaks and blank lines survived,
checkboxes render as checkboxes, code blocks stayed fenced, and tables kept their columns. Check
that nothing was flattened into one paragraph by a paste or an editor that stripped newlines. Fix
defects in the platform editor, save, and read back again. Request review only after one pass shows
the rendered post intact. Once it accurately presents what you wrote, you do not need to keep
re-editing its style.

## Anti-pattern

An Agent composes a long PR body in a local editor and pastes it into the web form. The paste
collapses the acceptance checklist into a single prose line and merges two headings. The author
requests review immediately; two reviewers read different things — one treats the checklist as
informal prose — and the misunderstanding surfaces only after an argument about scope in the review
thread.

## Why

Reviewers and future readers act on the saved, rendered post, not the draft. Formatting damage can
hide requirements: a checkbox rendered as prose no longer marks a checklist item, and a heading
rendered as body text makes its section harder to find. Reading back checks that the published post
still presents what the author wrote.

## Exceptions and boundaries

A one-line edit of an already-verified post needs only a spot check of the edited region. Platforms
that render from an editable source the author re-reads in place may satisfy the read back within
that view, as long as what is checked is the saved rendering. This checks whether the post was saved
and displayed correctly, not whether its argument is sound. For help with the content, use the
Practices about issue structure and PR bodies.

## Example

After filing a proposal issue, the author reopens it and notices the acceptance checklist rendered
as three run-on lines because the draft used hyphens the platform did not convert. They edit the
body into proper checkbox syntax, save, read back once more, and only then mention the issue in the
maintainer channel.
