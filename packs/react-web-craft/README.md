# React Web Craft

> **Unreleased local Pack candidate.** Version `0.1.0` is a mutable working marker, not a release. No Registry entry, immutable release ref, or tag exists. The Pack is licensed CC-BY-4.0 (`pack.yaml`, determined 2026-09-15); the remaining open gate is the Registry release.

Canonical language is English. A zh-CN review companion lives under [`i18n/zh-CN/`](./i18n/zh-CN/README.md); the English files remain the runtime authority, and the companion is pinned to them via [`i18n/manifest.yaml`](./i18n/manifest.yaml).

## Intended reader

React DOM web application developers making day-to-day design and performance decisions: what component state represents and who owns it, how async work is sequenced, what code loads when, how rendering cost is controlled, and how component APIs are composed. Next.js is in scope only where the sources pin its React-facing semantics.

## Coverage

Work proceeds by category; each category groups Practices around one decision area. Selection follows the pinned-source research in `drafts/react/`, not a rule-count quota. Selection records and rejected-candidate tombstones are in `drafts/react/CANDIDATE-CARDS.md` (local authoring workspace, not part of the Pack). Provenance, exact Vercel source digests, and include/exclude rationale are in [SOURCES.md](./SOURCES.md); source attribution does not determine license permission.

| Category | Decision area | Practices |
|---|---|---|
| [state](./practices/state/) | component-state ownership, representation, initialization, and callback update semantics | 6 |
| [async](./practices/async/) | data-fetch dependency ordering, parallelization, and Suspense boundaries | 4 |
| [bundle](./practices/bundle/) | deferring non-critical code and loading on user intent | 2 |
| [server](./practices/server/) | request-scoped data boundaries, module-state isolation, and Server Action authorization | 3 |
| [rendering](./practices/rendering/) | render conditions, hydration consistency, resource priority, and update priority | 5 |
| [composition](./practices/composition/) | component API shape and composition patterns | 4 |

### state

| Decision moment | Practice |
|---|---|
| A callback uses a functional updater but still reads other reactive values | [A Functional Updater Does Not Refresh Other Captures](./practices/state/functional-updater-scope.md) |
| Multiple components must coordinate one changing UI value | [Keep Coordinated State at One Shared Owner](./practices/state/share-one-owner.md) |
| A value must persist between renders but is not rendered UI state | [Use Refs for Non-Rendered Per-Instance Bookkeeping](./practices/state/ref-for-nonrendered-values.md) |
| An editable value follows a changing default until local user intent exists | [Preserve a Reactive Default Until the User Overrides It](./practices/state/fallback-until-overridden.md) |
| Multiple flags allow impossible combinations of one exclusive workflow | [Represent Mutually Exclusive UI Modes with One State](./practices/state/model-exclusive-modes.md) |
| Expensive pure work constructs a mount-time editable snapshot | [Lazy-Initialize Expensive Mount-Time State](./practices/state/lazy-initializer.md) |

### async

| Decision moment | Practice |
|---|---|
| A function performs several independent I/O operations | [Start Independent Async Work Together](./practices/async/parallel-independent-work.md) |
| Cheap local guards could skip the branches that await | [Run Cheap Checks Before Starting Async Work](./practices/async/await-after-cheap-work.md) |
| A list fan-out needs a per-item follow-up request | [Chain Each Item's Follow-Up Fetch Inside Its Own Promise](./practices/async/chain-nested-item-fetches.md) |
| One slow data source delays the whole page shell | [Put Slow Subtrees Behind Their Own Suspense Boundaries](./practices/async/suspense-boundary-scope.md) |

### bundle

| Decision moment | Practice |
|---|---|
| A large module is needed only on a conditional or later path | [Defer Heavy Non-Critical Loads Until They Are Needed](./practices/bundle/defer-heavy-loads.md) |
| A deferred chunk sits behind a visible, predictable step | [Preload Deferred Code When User Intent Signals It](./practices/bundle/preload-on-intent.md) |

### server

| Decision moment | Practice |
|---|---|
| One server render fetches the same request-scoped value from several components | [Deduplicate Request-Scoped Lookups with React cache](./practices/server/request-dedup-cache.md) |
| Request-scoped data must reach several server components or helpers | [Keep Request Data Out of Module Scope](./practices/server/no-module-request-state.md) |
| A `"use server"` mutation's authentication and authorization need a home | [Authorize Inside Every Server Action](./practices/server/authorize-server-actions.md) |

### rendering

| Decision moment | Practice |
|---|---|
| A `&&` render guard can leak a renderable falsy value | [Make Render Conditions Actually Boolean](./practices/rendering/boolean-render-guards.md) |
| Server output and the first client render can diverge on clocks, locale, or storage | [Keep the First Client Render Equal to Server Output](./practices/rendering/hydration-consistency.md) |
| Hints and scripts each need a priority decision per resource | [Match Resource Hints and Script Loading to Real Need](./practices/rendering/resource-hints-scripts.md) |
| One interaction drives both an urgent control and expensive follow-up work | [Split Urgent Input Updates from Slow Follow-Up Renders](./practices/rendering/update-priority.md) |
| A computed value is copied into state and refreshed by an effect | [Derive Render Values; Do Not Mirror Props into State](./practices/rendering/derive-dont-mirror.md) |

### composition

| Decision moment | Practice |
|---|---|
| A component grows boolean mode flags carrying mode-specific data | [Prefer Explicit Component Variants to Boolean Mode Flags](./practices/composition/explicit-variants-over-flags.md) |
| A fillable component's slots need an API | [Compose with Children; Reserve Render Props for Data-Bound Slots](./practices/composition/children-over-render-props.md) |
| A component must expose its node to callers across React version lines | [Pass ref as a Prop on React 19; Keep forwardRef for Older Lines](./practices/composition/react19-ref-prop.md) |
| One retained public component API has mutually exclusive typed modes | [Model Mutually Exclusive React Props with a Discriminated Union](./practices/composition/model-mutually-exclusive-props.md) |

## Boundaries

This Pack targets React DOM web applications. React Native/Expo, view transitions, state-library selection, global/server data ownership, and generic JavaScript micro-optimization remain out of scope. Framework-specific server rules are admitted only where a pinned source fixes the behavior; each category's Practices state their own narrower boundaries.

## Review and release status

Results as of 2026-09-14:

| Gate | Result |
|---|---|
| Static validation | PASS — `lore validate` reports 0 diagnostics (one ID-namespace defect found and fixed during review) |
| Example compile | PASS — all 40 example blocks compile under TypeScript 5.9 strict with React 19 types (one missing-import defect found and fixed: `react.composition.react19-ref-prop`) |
| Maintainer content review | PASS — completed by the maintainer on 2026-09-14 |
| Install path | PASS — installed from a rehearsal git registry tag into an isolated store (artifact digest `48362b4b705bbcd4b2f283b10f394dabba6253dfcaef4d46f483ed002db12870`) |
| Retrieval | PASS — keyword battery 28/28 (24 positive + 4 disambiguation); semantic battery 31/31 (24 positive + 4 disambiguation + 3 paraphrase; embedding needs `LORELUM_BACKEND_REQUEST_TIMEOUT_MS=60000`); battery script kept locally in `drafts/react/retrieval-battery.py` |
| License | CLOSED (2026-09-15) — determined as CC-BY-4.0 in `pack.yaml`; the Pack's prose and examples are independently authored (no Vercel text or code reproduced), per-practice attribution is recorded in [SOURCES.md](./SOURCES.md), and the pinned sources' MIT declaration is documented there |
| Registry release | OPEN — the Pack is not committed to the official catalog; no tag exists |

**Content freeze.** The English canonical — `pack.yaml`, `practices/`, [SOURCES.md](./SOURCES.md), and this README's content sections — is frozen as of 2026-09-14. The zh-CN companion under `i18n/zh-CN/` is complete (24/24 entries current per `lore validate`) and pinned to these files by the `source_digest` entries in [`i18n/manifest.yaml`](./i18n/manifest.yaml). Digests are computed by `lore i18n sync` over CLI-canonicalized markdown (Prettier-formatted, not raw file bytes), so any later English edit requires re-running that sync and re-translating the affected entries before the companion is trusted. The `license` field added to `pack.yaml` on 2026-09-15 is release metadata required by gate 6; it does not thaw the content freeze.
