# Pull request template

Copy this skeleton to the task workspace and fill it in before requesting review; when the
repository provides its own template, that one wins. Write in the repository's collaboration
language; keep commands and identifiers verbatim. After posting, read the saved body back on the
platform and fix any flattened Markdown before requesting review. For the decisions behind each
section, retrieve the `issue-pr-etiquette.pull-request.*` Practices.

**Title:** `<type>(<scope>): <imperative, lowercase subject, ≤72 characters>`

## Summary

One or two sentences: what does this PR do? Include what deliberately does not change when that
could surprise a reviewer. For a direct-fix PR with no linked issue, also state the root cause and
the fix boundary here.

## Linked issue

Closes #<n>

## Type of change

- [ ] 🐛 Bug fix (non-breaking)
- [ ] ✨ New feature (non-breaking)
- [ ] 💥 Breaking change (name the breaking surface)
- [ ] 📚 Docs only
- [ ] 🔧 Refactor / chore

## How was this tested?

The verbatim commands you ran, then the named scenarios you exercised. Paste output where it
carries evidence. "Tested locally" is not a verification statement.

```text
<command>
<command>
```

- <scenario exercised and what it showed>

## Checklist

- [ ] Linked the issue this closes (`Closes #<n>`), or stated the root cause and fix boundary above
- [ ] Design was discussed in the issue / Discussions first if this changes contract-class behavior
- [ ] Added/updated tests for the change
- [ ] Lint, type-check, and tests all pass locally
- [ ] Updated relevant documentation
- [ ] No secrets, credentials, or private info in the diff

## AI assistance and review

- [ ] This PR used AI assistance (describe the scope below)
- [ ] If AI-assisted: an AI review covered the changed behavior; material findings are resolved or
      documented below

<If AI-assisted: which parts the AI drafted or reviewed; what the AI review found; what this branch
changed as a result, and which findings were rejected and why. "Reviewed every line" is not an
acceptance criterion.>

## Notes for reviewers

Where to look first, tricky parts, trade-offs made, and what was deliberately deferred.
