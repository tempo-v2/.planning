# Historical Games follow-up verification

The tests used synthetic fixtures and isolated workspaces on arm64 macOS 26.6.2 with Rust 1.98.1, Node 26.12.0 and npm 11.20.0. The [release ledger](STATE.md#historical-freshness-and-dataset-follow-up) identifies the combined sources. The tested contract preserves SQLite schema 11, portable format 5 and Study wire 5. The Games JSON shapes carry forward.

## Reproduction

Before the production changes, the new mounted tests ran against UI `c039f829624f7f19bc79dfad24e35cc7f20b77c9` with the following command from `tempo-ui`.

```sh
node --test --test-name-pattern='first terminal historical|foreign historical status' test/games_evidence.test.js
```

Both first-terminal cases failed on the assertion for the rendered `game-from-B` row. The foreign-status case failed because the page rendered the foreign job. The test process reported three failures after successful bundling and mounting.

| First terminal B scenario | Baseline history reads before → after | Baseline historical GETs | Baseline gaps GETs | Observed at assertion |
| --- | --- | --- | --- | --- |
| Pending Retry for A | 2 → 2 | 2 | 2 | A cleared, B visible, history empty |
| No pending command | 2 → 2 | 1 | 1 | B visible, history empty |

The same tests on the combined candidate displayed the actual fixture row on one additional history read. A stayed pending until its exact acknowledgement and B remained the authoritative view. The fixture counts above are observations from this run.

Before the production changes, `cargo test --locked --offline -p tempo --lib historical_` ran three added tests against Tempo `e6443a7372178e3e00292567d9d4f400f9a3e7d2` and Store `4027bb41cf14425bcbb5f1e8c7467999b0c40a52`. Two failed at their behavioral assertions. After supported restore, old Begin returned the completed A job and the coordinator published A instead of idle. The outstanding-provider-reply control passed. After repair, the combined candidate passed all five backfill tests, including the existing retained Retry and date-only reset checks. The new tests cover normalized equivalent Begin, immutable input rejection, stale Begin and Retry, complete/incomplete/paused reconciliation, and response draining across successive restores.

## Commands and results

Commands run from the assembled candidate. Set `CARGO_TARGET_DIR` to an isolated target for each source assembly and the `TEMPO_BINARY` for the explicit debug build. Test and build outputs belong to the disposable workspace.

```sh
cargo test --locked --offline --workspace
(cd tempo-ui && npm test)
TEMPO_BINARY="$CARGO_TARGET_DIR/debug/tempo" node --test tempo/tests/ui_boundary.mjs
python3 .planning/scripts/check_architecture.py .
python3 .planning/scripts/check_architecture.py --self-test
make build-ui
cargo build --release --locked --offline -p tempo
```

- Locked Rust workspace and doctests passed **303**. The initial sandboxed attempt hit an OS permission denial in the existing `gap_analysis` fixture's process inspection. The combined test run completed with normal process permissions.
- UI passed **53**, including **24** mounted Games and GapEditor cases. The new cases include a below-maximum retry attempt, a running-to-paused transition with durable rows, superseded noncooperative responses, timed-out replacement history, foreign status and owner changes, and successor fetch/body timeouts after accepted Save. Both successor checks recovered at the same page offset without replaying Save.
- The three Rust/UI application boundary tests passed. The dependency gate and its four self-tests passed. The separate legacy `ui_imports.mjs` regex check matches the existing Games JSX `name="from"` followed by an unrelated quote as a module import. The exact same failure reproduced on the newer main assembly. Guarded packaging consumed the installed Core 0.2.2 tarball and the mounted/packaged checks used it.
- Independent read-only review passed 22 historical Games cases, all five coordinator cases and three model tests after reconciliation. The two added successor-gap controls passed in the final 53-test run and change only test fixtures.

## Original PI-F1–PI-F3 qualification

The available original `tempo2-schema11-post-install-packet` passed all 90 entries in its SHA-256 manifest. Its runner initially exited 2 on an external probe's call to the superseded raw coordinator status method. In an isolated copy of the packet, the one-line fixture change below selects the authoritative production method and keeps the asserted current-job identity. All other assertions ran as supplied.

```diff
-    assert_eq!(job.status()["job_id"],"old");
+    assert_eq!(job.current_status(&app).unwrap()["job_id"],"old");
```

```sh
python3 "$PACKET/scripts/run_acceptance.py" "$PWD" \
  --output-dir "$RESULTS" --target-dir "$FRESH_TARGET" --include-prior
```

The combined run exited 0. All three PI finding groups, the three extra Store controls and all ten prior assertions passed.

```json
{
  "model_recovered": true,
  "historical_retry_acknowledged": true,
  "ui_read_tests_passed": true,
  "new_store_controls_passed": true,
  "prior_controls_requested": true,
  "prior_controls_passed": true,
  "reviewed_failure_groups": 0
}
```

The optimized worker probe reran transient recovery, permanent exhaustion after four attempts, and explicit Analyze priority. The original interrupted-inference check recovered one complete and one partial projection and the retained 50,000-millionths reach. The ordinary HTTP Study smoke check used an unavailable provider and missing Maia weights. It issued an eligible test, accepted and exactly replayed one answer, issued a different test, and recorded one assessment, receipt and review.

The later `tempo2-pi-corrective-review-packet.zip` was unavailable. Its manifest and its 49 adapter and two successor-gap assertions could not be rerun byte for byte. The repository suite and original packet covered the named bounded reads and the two new mounted successor-gap controls exercised fetch and body failures. Historical review logs and old asset hashes are provenance for the earlier candidate only.

## Scope of the observed behavior

A historical pause may hide already applied batches while its current window remains pending. First-observed pauses, changed window facts and observed running-to-paused transitions trigger a refresh. A resume that begins and returns to an identical paused job-and-window view between reads exposes no distinguishable revision on the existing wire. Games can reload history independently.

The restore cases use the application API on disposable SQLite and do not imply an installed HTTP restore route. The managed installation and database were outside these tests.

## Packaged browser and synthetic restart

Native headless Chrome used the previous installed checkpoint
`workspace-8467c4c7540fb7b6f55e`, whose executable matched SHA-256
`58ea1e9904ad897606ad5be9345a943caaee69a6a089ebc0e9a39c04540de095`.
It created an accepted Retry with a lost response and a second Retry that
had never reached the server, on disposable SQLite. The compiled candidate
resolved both original commands. The previously unaccepted Retry had one
durable effect. The already accepted Retry's POST body matched byte for byte
and the two retained job records matched before and after replay. A separate Chrome page held the first actual B GET
until the initial empty history rendered. It used a deterministic history
transport fixture for a visible row at settlement. Current B and Retry A
were real HTTP/SQLite operations. B's provider was intentionally unavailable,
so native Chrome first observed B incomplete. The mounted regression also
exercised first-observed complete B.

The first browser attempt entered Games before the old page was ready to
submit the initial Retry. SQLite showed zero Retry dispatches. Waiting for
initial ordinary status fixed the harness and the subsequent run passed.

```json
{
  "firstHistoricalObservation": "incomplete",
  "historyBeforeFirstSettlement": 2,
  "historyAfterFirstSettlementAndAck": 3,
  "historicalStatusReads": 2,
  "fixtureHistoryRowVisible": true,
  "lateAcceptedRetryAOnlyClearedOwnEnvelope": true,
  "oldAcceptedRequestCount": 1,
  "candidateReplayCount": 1,
  "byteIdenticalWireReplay": true,
  "previousPackagedBrowserEnvelopeCleared": true,
  "currentJob": "history-b",
  "persistedJobsUnchanged": true,
  "unacceptedRetryEffect": 1,
  "packagedHistoryTimedOutAndRecovered": true,
  "integrity": "ok\n11"
}
```

The optimized HTTP Study probe and the packaged browser ran the executable
listed below. A fresh restart and read-only Games queries on a disposable
copy of the newly created synthetic Study database preserved all 34 tables.
SQLite integrity and foreign keys passed. All 22 served files matched the
guarded build.

## Artifact SHA-256

| Artifact | Hash |
| --- | --- |
| Workspace Cargo lock | `c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0` |
| UI npm lock | `1fe3dd71e3ff0699dc38d102fbc03e8fd742b5a7742d8b42bbf626343d2d1ebb` |
| Bundled Core 0.2.2 | `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4` |
| Optimized macOS executable | `a7a61d4173eb3f583f921ffeccf0294ddd18f86f22aa8d0a0e8a6b3455f59345` |

```text
c2584eb9c9e1da000328dc635ed4a20cd31164af4c6b3bb7c572851124d2306d  assets/app.css
fc8d367edba68c99038072bcc25e74c60792a4a3404a476703a8e0685d6dfe74  assets/app.js
a5d2ee9100f3b0b74beb3c95f88e3b43a46a790a00d41aa1db8ca9a0905568f1  assets/bB-GT5SSGJP.svg
d74cd8e5e49ca921e765c6c0c3a87ce7f5f437ca95bca44948b92771f7bdd65c  assets/bK-675NAWJZ.svg
f1f4e2a1eed37dd366b61b38f857ea8fd0b890b8f02215ceb99f0e710a7950fa  assets/bN-JOUYBUTG.svg
d0e48e03ec340c39e9fde73d0ae0c8b251d42a32c13381ad0664edce77ce7eb3  assets/bP-3PVWADTM.svg
8ad433fa5876894ca03b9412e9e39b8d770e90bf1c59428ee8e06bf6bc472098  assets/bQ-PBUQEJQM.svg
32c8ae60d594e037839cb2f0815ee1739b58d1aea09b5df8b96fec62a6868884  assets/bR-CBGYAKGK.svg
7158a77f3eb9a763fe723e9c9291819de8748444a1192d10383159fd8175709b  assets/capture.mp3
da05719e6b3f0d04a2ac1a551e643ab14f4e840ae3b9410c0ea15ba4bcac5010  assets/castle.mp3
ef4764a74d19d0db1659e413e8afadc25f1e8cfba83a4a76e6e64f28f3077d52  assets/check.mp3
3224eb7a6d93e52229ddcb49c62e584764d1474c123d25c91ecb2c74aa6291f9  assets/illegal.mp3
0931855637e50e4edbc7916ec7a66cca2f0eee763e1c791ff774a9945517ea61  assets/move-opponent.mp3
3a2eb75af1334c06dafd735c23388a560285e0df9436a44d27adc95a010a8547  assets/move-self.mp3
69219212aa2dce6031d6a641f8813779809bdff33562a8418d8e003eea465815  assets/promote.mp3
b9db43162732aae75cd51b6f071185b000c514cd1b8a93a134bd8c6676351f9d  assets/wB-YLMC6FHU.svg
e1dc9b6358585210119b92c389551fc70fa6566316089b3eba017142153fd3f4  assets/wK-AUE64UFO.svg
25c6f4d7446b9f99d6b62239bf0cd0abcf2ebb902e96aa93a73b7816d8431b7d  assets/wN-CSRTRN5I.svg
0c77297b4870b95653edaf7514d3b8f36816d1a7f05c718f4c0f7f0dff016d50  assets/wP-63DUNQX4.svg
b05f4b8902f333d4e7eeb5475af4c6015a91fb7fdd3266bdd0adc84ad1f7076c  assets/wQ-6YL7MNW5.svg
494fff9b13a24122b4fa6df1fd1070b0470a7cf8d603ac14f4290d00a149bec3  assets/wR-IQNXS3HT.svg
3ebea9985d4af80e7b7dcd0fc7039b81592935057d96022ff359658413c2f9ac  index.html
```
