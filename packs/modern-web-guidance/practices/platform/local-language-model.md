---
id: modern-web-guidance.platform.local-language-model
title: Gate On-Device Language Models by Availability
stage: implementation
severity: warn
applies_when: using the browser Prompt API for an on-device language-model feature
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.assume-local-model-ready
    name: Assuming the local model is ready
    severity: warn
    description: A page starts a model download without user activation or assumes every browser and device can run the model.
---

Detect the `LanguageModel` interface and query `LanguageModel.availability()` for the intended configuration. If available, create a session when user intent is clear. If downloadable or downloading, call `create()` from a user gesture and show accessible download progress; if unavailable or creation fails, explain the limitation and provide an appropriate alternative. The source snapshot reports Chrome 148 desktop and substantial device, storage, and initial download requirements; interface support alone does not mean the model is usable. Check the actual target environment.

Destroy sessions when no longer needed, allow cancellation of generation, and handle creation, streaming and parsing errors. Treat generated text as untrusted: render it with `textContent`, or sanitize the complete output before HTML insertion. Streaming output should use an existing polite live region with `aria-busy` during updates and an appropriate language tag when the output language differs.

A remote-service fallback changes privacy, network and cost properties; do not silently send user data off-device. Offer it only when consistent with the product's disclosure and consent requirements. Model output is probabilistic and must not be trusted for authorization or other security decisions.

Source: [Language Model](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/built-in-ai/language-model.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
