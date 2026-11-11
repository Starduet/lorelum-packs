# Pack Creator 0.3.0 release verification

- Date: 2026-11-11.
- Registry: `lorelum/lorelum-packs`; release ref `pack-creator-v0.3.0`, commit `554a4e6d042b72cdfa932015b5dcc5bd56d4c40c`.
- CLI: `0.1.0-alpha.7`, compiled clean build, revision `1f1efff94c915f6d336b2b38a3d98918cbd3054c`, build identity `64378a5867c5d56adacbeef82e2200ebfde722de64fdeb6b38f1b7fb7042be78`.
- The candidate passed `lore validate`: no Pack diagnostics and 28 current Chinese companions.
- In an isolated Store, `lore pack install pack-creator@0.2.1` installed the official `pack-creator-v0.2.1` release. `lore pack update pack-creator` resolved the official Registry's `0.3.0` release and the commit above, with no diagnostics. The update added `pack-creator.design.derive-pack-content-from-task-needs`; `lore pack list pack-creator` returned 28 Practices, and `lore get` returned that new Practice and its resource link.
- The installed `references/task-shaped-pack-design.md` had SHA-256 `1f7a61ee268d7224b967b3784d2108a2df5894fcd1f0e8c8cd498de778bd8740`. Its contents matched the release worktree after CRLF normalization; the installed copy uses LF.

This verifies the official Registry upgrade path and one resource in the installed artifact. It does not establish semantic retrieval quality or improved downstream model behavior; see `fixtures/pack-creator/task-shaped-evaluation.md` for the exploratory authoring comparison and its limits.
