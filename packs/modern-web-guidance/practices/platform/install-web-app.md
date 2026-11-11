---
id: modern-web-guidance.platform.install-web-app
title: Offer Web App Installation as an Enhancement
stage: implementation
severity: warn
applies_when: a website offers users an in-page control to install a web app
tech_stack:
  - javascript
  - web
anti_patterns:
  - id: modern-web-guidance.platform.assume-install-available
    name: Assuming in-page installation is universally available
    severity: warn
    description: A page exposes a nonfunctional install button or prevents normal website use when installation is unsupported.
---

Keep the website usable without installation. Provide a web app manifest with an explicit stable `id`, appropriate `start_url`, name and icons. For current-app installation link the manifest from the document; for another app check the upstream manifest URL, identity, HTTPS, response and same-origin requirements. Installation remains subject to browser-controlled consent and eligibility.

Choose the browser-controlled `<install>` element when its standard appearance is appropriate, or `navigator.install()` for custom UI. Feature-detect the chosen entry point; hide unavailable controls and offer browser-specific manual installation instructions only where applicable. Call `navigator.install()` directly from a user activation in a secure context. Treat cancellation as expected and report invalid manifests or unexpected errors separately. A success can also mean the user approved opening an already-installed app; do not claim a new installation unconditionally.

At the source snapshot `<install>` was not natively supported by major browsers and `navigator.install()` was limited. Browser installation UI and manifest support also vary; feature presence does not guarantee installability. Do not imitate or overlay the browser-controlled element or silently install an app.

Source: [Installing web applications](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/guides/pwa/install-web-app.md), v1.0.0, commit `4dd968349e54ca45a05dd5c818fb035c9054b022`.
