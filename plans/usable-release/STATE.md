# Tempo structural cleanup

Use the [current assembly](current-assembly.json) for exact revisions and artifact hashes. Use the [workspace setup](WORKSPACE.md) and the selected restart task. The [operation contract](structural-cleanup/operation-contract.md) governs retained commands and their work limits.

| State | Evidence |
| --- | --- |
| Merged source | Schema 25 source prefix. Exact main revisions are in `merged_sources`. |
| Continuation | Schema 28 source. Use `review.components`, including Tempo #94's test-only apply helper, Store #65, UI #73 and Learning #12. |
| Recorded installation | Schema 22, `workspace-e1c18810c03bd3ad05db`. Artifact identity is in `installed`; this record has no new live observation. |

Keep the consolidated drafts as the continuation. Settings drafts Tempo #39, UI #34 and Planning #45 supply only the listed retained deltas; use the selected Settings task for scope.

Planning #84 provides the compact guidance and manifest. Run `learning_good` and `exact_skip` with disjoint reservations, then `prompt_invariant`. Component work can use verified source-equivalent Git trees at their actual local revisions. Exact combined qualification and installation still require the manifest revisions. Capture may become Complete only after every relevant writer retires or atomically fences the captured basis. Move actual runtime publication, Next and summary consumers to the existing capabilities and remove their replaced paths. Qualify the exact combined release before managed installation.

Use the immutable [prior ledger](https://github.com/tempo-v2/.planning/blob/f71f80fa7c168993a8d5979be10102bc70fd64ae/plans/usable-release/STATE.md) and [prior workspace instructions](https://github.com/tempo-v2/.planning/blob/f71f80fa7c168993a8d5979be10102bc70fd64ae/plans/usable-release/WORKSPACE.md) for archive verification, previous-release command recovery, and historical builds. The [release manifest](manifest.json) retains earlier installation and recovery identities.
