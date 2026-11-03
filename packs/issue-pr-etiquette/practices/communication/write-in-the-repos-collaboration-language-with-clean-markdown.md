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

When writing an issue, PR body, review comment, or important status comment, check whether the
repository declares a working language in its contributing guide or governing documents. Use that
language for your explanation so collaborators can read it without translating. Quoted logs, code,
and upstream documents keep their original language.

## Guidance

Write the prose in the repository's declared collaboration language — for example, a repository
whose contributing guide says collaborator-facing posts default to Chinese unless the user requests
otherwise. Keep file paths, commands, code identifiers, error messages, and untranslatable proper
nouns in their original form instead of translating them. Break longer posts into Markdown headings,
paragraphs, and lists where they help reviewers find a section or quote a specific line. A short
comment can stay short. The post is ready when readers fluent in the declared language can find its
sections quickly and search every identifier in its original spelling.

## Anti-pattern

In a Chinese-default repository, an Agent files an English PR body because the diff is in English,
and alternates languages sentence by sentence inside one paragraph. Reviewers slow down on every
line, one critical caveat about a breaking change is missed in the unfamiliar prose, and a later
search for the Chinese term everyone used in discussion finds nothing.

## Why

The declared language is the one the whole team reads fluently; writing in it lowers the cost of
every review that follows. Keeping identifiers in their original spelling lets readers search for
them in code and docs, inspect their history, and follow references without translating them back.

## Exceptions and boundaries

A user's explicit request for another language overrides the default for that conversation. Upstream
communities with their own norms keep their own language. Multi-paragraph posts justify headings and
lists; a two-sentence comment needs neither. Quoted material keeps its source language, clearly
marked as quotation.

## Example

A contributor files a defect issue in Chinese: the title and every explanatory paragraph are
Chinese, while `npm test`, the file path `src/validate/resources.ts`, and the error
`ENOENT: no such file or directory` stay verbatim. A reviewer scans the headings, greps the
identifier, and lands in the right file on the first try.
