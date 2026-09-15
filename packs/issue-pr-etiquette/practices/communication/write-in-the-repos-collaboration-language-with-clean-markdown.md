---
anti_patterns:
  - description: Writing collaborator-facing posts in a language or structure the repository does not read fluently raises the cost of every review and buries critical caveats in hard-to-scan prose.
    id: issue-pr-etiquette.communication.mixed-language-unscannable-post
    name: Mixed-language post that reviewers cannot scan
    severity: warn
applies_when: a contributor is writing an issue, PR body, review comment, or significant status comment that collaborators will read, and must choose the language and the Markdown structure of the post
id: issue-pr-etiquette.communication.write-in-the-repos-collaboration-language-with-clean-markdown
severity: warn
stage: communication
tech_stack:
  - github-contribution
title: Write in the Repository's Collaboration Language with Clean Markdown
---

## When to apply

Apply when composing any collaborator-facing post on a repository that declares a working language
in its contributing guide or governing documents. The decision is which language the prose uses and
how the post is structured for a cold reader. Do not apply to content whose language is fixed by the
artifact itself, such as quoted log output, code, or upstream documents.

## Guidance

Write the prose in the repository's declared collaboration language — in the Lorelum repositories,
issue and PR titles, bodies, reviews, and significant status comments default to Chinese unless the
user explicitly asks for another language. Keep file paths, commands, code identifiers, error
messages, and untranslatable proper nouns in their original form instead of translating them.
Structure the post with Markdown headings, paragraphs, and lists so a reviewer can scan sections and
quote a specific line; one dense wall of text is a structure choice, and usually the wrong one. Stop
when a native reader of the declared language can locate any section of the post in seconds and
every identifier remains searchable in its original spelling.

## Anti-pattern

In a Chinese-default repository, an Agent files an English PR body because the diff is in English,
and alternates languages sentence by sentence inside one paragraph. Reviewers slow down on every
line, one critical caveat about a breaking change is missed in the unfamiliar prose, and a later
search for the Chinese term everyone used in discussion finds nothing.

## Why

The declared language is the one the whole team reads fluently; writing in it lowers the cost of
every review that follows. Identifiers kept in their original spelling stay greppable in code and
docs, while translated identifiers silently break search, blame, and cross-referencing.

## Exceptions and boundaries

A user's explicit request for another language overrides the default for that conversation. Upstream
communities with their own norms keep their own language. Multi-paragraph posts justify headings and
lists; a two-sentence comment needs neither. Quoted material keeps its source language, clearly
marked as quotation.

## Example

A contributor files a defect issue in Chinese: the title and every explanatory paragraph are
Chinese, while `lore pack install`, the file path `packages/format/src/validate/resources.ts`, and
the error `ENOENT: no such file or directory` stay verbatim. A reviewer scans the headings, greps
the identifier, and lands in the right file on the first try.
