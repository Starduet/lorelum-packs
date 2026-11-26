---
id: code-review.navigation.ui
title: Navigate User Interface Changes During Review
stage: review
severity: info
tech_stack: [code-review]
applies_when: a review involves user interface state, interaction, events, asynchronous data, or rendering in a web, desktop, or terminal application
anti_patterns:
  - id: code-review.navigation.ui-as-checklist
    name: Treat navigation topics as defects
    description: Report an interface mechanism without establishing its actual effect and applicable contract.
    severity: warn
---

When changes affect a user interface, understand the user's action, visible feedback, and actual behavior first. Follow mechanisms affected by the change; unchanged code matters when it changes the outcome. Select relevant topics rather than checking every item.

**State and operation ownership.** Follow who creates, updates, displays, and consumes values, and whether each belongs to the current interface, an object, or an operation. Check that displayed state agrees with the state actually used. Two values may represent different things, such as a server baseline and unsaved edits.

**Callbacks and event lifecycle.** When callbacks or listeners run later, identify when they are created or updated and which values they read. Check the actual event path, dependencies, explicit arguments, and listener cleanup. An earlier value may intentionally identify the operation as started.

**Async results and cancellation.** When operations overlap or users switch objects, trace ownership at the final data, error, and loading writes. Out-of-order completion alone is not a defect if those writes are guarded; showing stale cached data can also be deliberate.

**Interaction, failures, and recovery.** Follow the real input path and check that users can complete actions, see relevant failures, and recover. Consider supported keyboard, focus, or terminal interactions when changed; preferences are not regressions.

**Rendering and resources.** For changed updates, lists, requests, or resource loading, compare work on the user's waiting path. A render or theoretical loop alone is not evidence of a material performance problem.

When a changed path raises a domain question, query using the interaction, the mechanism visible in the code, and the decision it affects. Include the framework or runtime only if its semantics matter. Read candidates that help answer the question and check their applicability against the code; a matching term alone is not enough.
