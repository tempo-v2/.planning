# Tempo V2 usable release

The consolidated packet dated 2026-11-17 governs this run. Existing local Tempo and Chess successors already supplied the real board projection. The selected workspace compiled with its original lock before implementation. Tempo UI was cloned at the packet's exact referenced head, moved out of Tempo, and qualified against packaged Core 0.2.1.

## Opening checkpoint

- The disposable Chrome journey covered file upload, preview, save, guided instruction, backend restart, rename, and complete replacement with re-teaching.
- Disposable injected-clock contract tests covered ten acknowledgements without grades or FSRS memory, the next-day seeded review order, real FSRS transitions, restart, receipt replay, and content-preview isolation from intervening review. The content receipt also replayed after a restart and subsequent rename.
- The dependency-direction gate passed. Core passed its isolated installed-artifact consumer and Chrome checks. UI owner coverage passed 19 tests.
- The opening deployment uses a fresh SQLite dataset under `.local/usable-release`. The prior tactics workspace under `.local/tactics-mvp` is outside the cutover.
- Host cutover observed at 127.0.0.1:41822 with wire 4 and the fresh opening dataset. The server served the built UI and read the empty repertoire list from the fresh database. Browser tests used disposable data.
- Checkpoint 02 binary, matching UI and lock are under `.local/usable-release/checkpoints/02`. Artifact hashes and source pins are in the single release manifest.
- Milestone 03 started after the opening service was available. Its development and tests use disposable databases until the upgrade is verified.

## Combined release qualification

| Acceptance | Observed evidence |
| --- | --- |
| A01–A02 | Locked Rust and split UI builds, dependency-direction gate, standalone installed Core consumer, Chrome board/control interactions. Core did not change after 02. |
| A03–A04 | Guided teaching, no grade or memory on acknowledgement, first blind FSRS review and sticky Again through correction. Practice preserved the learning and assessment rows. |
| A05–A07 | Mixed integration served 35 due targets in their seeded daily order with restart mid-queue. Defaults admitted 10 openings and 20 tactics independently. Chrome covered Stop, count, and resume. Store replay preserved the optional allowance without double admission. |
| A08–A11 | Chess cases cover nested routes, both colors, repeated positions, and conflicts. Chrome and app tests cover rename, complete replacement, no-op reupload, retired activity, changed-answer teaching, and accepting a content preview after unrelated grading. |
| A12–A14 | Chrome uploaded a SetUp=1 snippet, displayed an invalid separate record, and captured a complete game's selected Sicilian variation. Chess validates promotion, castling, en passant, explicit setup, final replies, duplicate identity, and authoritative collisions. |
| A15 | Study and content receipts replayed through HTTP and browser restart. A disposable SQLite receipt trigger aborted teaching and all related writes. Retrying the same command succeeded after the trigger was removed. |
| A16 | Injected day rollover accepted a previously issued lesson after the allowance fell to zero. The New York calendar test covered 23- and 25-hour study days around DST. |
| A17 | Disposable diagnostic loaded 558 valid targets and retained 60 scheduled outcomes. Issuing the next card took about 16 ms in one debug-build observation. One addressed command returned one activity, one target, and one learning row without historical outcomes. |
| A18 | Disposable 02-to-04 upgrade with a taught position and another active lesson kept every preexisting SQLite row, both durable receipts, and the active lesson. The upgraded instance accepted capture with that same dataset. |

Combined changes passed focused Tempo/Store/Queue Rust suites, 65 Chess unit tests and 3 doctests, 21 UI tests, 7 HTTP/boundary tests, and strict Clippy for the changed backend components. New tests exercised changed paths or outstanding upgrade and fault risks. Earlier Core and opening Chrome evidence was reused.

Packet archive SHA-256 `cb88fea16c9672a7d281d9909f9e2a93a2b7735a7f6ea463715593d8f1f41ba6`.

## Installed combined checkpoint

- The running Mac service serves the checkpoint 04 binary and byte-matching UI at `http://127.0.0.1:41822`. Its launchd job is `com.tempo-v2.usable-release`, loaded for the current GUI session.
- The same live SQLite path and dataset ID were retained from checkpoint 02. Schema advanced from 2 to 3. Every preexisting table's rows and the active pointer matched before and after the upgrade. Live learning and assessment tables were still empty at cutover. No synthetic lesson or grade was written to the live database. The separate disposable upgrade established preservation with actual teaching and active work.
- Host checks fetched the exact UI assets, repertoire list and Study status and previewed a tactic without saving it. The source launcher `make start` served the matched UI on a separate disposable database.
- Checkpoint 04 binary, UI and lock are under `.local/usable-release/checkpoints/04`. The opening checkpoint remains archived as 02. The combined build opens the 02 dataset in place, and subsequent use should keep the same database path.

## Installed-release follow-up

### Source and operations

| Group | Status | Evidence |
| --- | --- | --- |
| R1 Installed source and handoff | Covered/reused | All 34 archive file hashes across checkpoints 02 and 04 matched. The live listener was the foreground debug build from the pinned 04 code, with the same served HTML and JavaScript hashes as 04. The loaded checkpoint LaunchAgent was idle. The matching executable inode was observed before a locked Cargo check reused the compiled inputs and rematerialized the path with identical bytes. The manifest records that foreground binary hash separately. The source commits are reachable on the published component refs and the exact workspace Cargo lock is tracked with this handoff. |
| R7 Operations and current data | Covered/reused | The read-only Study status and SQLite readback verified the existing schema-3 dataset, the New York calendar, and the independent 10 and 20 limits. No restart or database change was needed. The documented online backup and separate recovery were tested on disposable 04 data with a taught position, active lesson, nondefault configuration, and exactly replayed teaching and content saves. |

[Workspace reconstruction](WORKSPACE.md) uses the pinned component commits. [Mac run and recovery instructions](https://github.com/tempo-v2/tempo/blob/cf94c79cc69820e1819ad32a4112a20b452ca1d6/OPENING.md) distinguish foreground and managed operation. This public handoff omits the private installation's dataset identifier. The locally retained original ledger commit has the cutover record.

### Behavior and runtime boundaries

The checks below apply to checkpoint 04. Follow-up changes in the Tempo repository are documentation and a disposable regression test.

| Group | Status | Evidence |
| --- | --- | --- |
| R2 Scheduling and grading | Covered/reused | [Live composition](https://github.com/tempo-v2/tempo/blob/8cc99ebcf1f18882dd7b0d63720e02bf73d97132/src/local_runtime.rs) selects DailyLearning and legal Chess grading. The [FSRS owner](https://github.com/tempo-v2/tempo-learning/blob/539d369e02f25f963cf16327559ef6d9272cba8e/src/daily_learning.rs) uses upstream 6.6.2, retention 0.90, zero elapsed days with no review predecessor, and elapsed study days from the prior actual review thereafter. Prior opening and HTTP tactics assertions cover ungraded Teach, memory on first review, and sticky Again. The new [disposable optional-tactics test](https://github.com/tempo-v2/tempo/blob/5cdc53816e4c6844ca2cdd1f6fe58baf41bb02b9/tests/contracts/opening_release.rs) verified that Practice failure, exact retry and correction preserved learning, scheduled outcomes, Done and the allowance. |
| R3 Replacement and preservation | Covered/reused | The pinned [opening integration](https://github.com/tempo-v2/tempo/blob/8cc99ebcf1f18882dd7b0d63720e02bf73d97132/tests/contracts/opening_release.rs) covers lifetime introduction, teaching after answer changes, removal of an active target, and ten reviews accepted after preview. The [repertoire planner](https://github.com/tempo-v2/tempo-chess/blob/304924a846627b2187f5b4c83690b4fb251a84cb/src/plan_repertoire_replacement.rs) tests surviving route references and other repertoires, while the commit binds active validity to the target and content version. The existing upgrade rehearsal and receipt-failure rollback still apply. |
| R4 Daily work and retry | Covered/reused | The pinned mixed integration asserts survivor order through 35 reviews, restart with an active exercise, independent 10 and 20 limits, and day-local admission. The skip, rollover, and local DST tests establish outstanding work and acceptance on the new study day. The new optional-tactics test advances across midnight, replays the prior allowance receipt exactly and checks that the new day receives no increment. |
| R5 PGN interpretation | Covered/reused | Pinned [Chess capture tests](https://github.com/tempo-v2/tempo-chess/blob/304924a846627b2187f5b4c83690b4fb251a84cb/src/tactic_pgn.rs) and the existing Chrome and mixed-batch evidence cover snippet setup, selected variation offsets, invalid rows and complete legal lines. The new optional-tactics test reimports learned content with different clocks and confirms unchanged identity and learning. |
| R6 Boundaries and cost | Covered/reused | The existing architecture gate, packaged-Core consumer and 558-target diagnostic remain applicable. The live-path trace confirms Queue selects, Study delegates grading, Learning schedules, and Store commits addressed facts and receipts. SQLite query plans use indexes for attempt IDs, their human assessment, receipt ID, issued definition and the addressed content/learning pair. Next reads candidate data when there is no active exercise and starts only the chosen grader. |

Only the additional disposable regression was run for the remaining behavior questions. Prior Chrome, Scheduler, Store, upgrade and performance evidence was reused with the same runtime inputs. No behavior change, service restart, or live database mutation was needed.

A clean checkout from the published branches recovered all nine component pins, the exact workspace and UI lock hashes, a successful locked optimized Rust build, and all 15 UI files byte-for-byte against checkpoint 04. Concurrent local tactics export/conversion work is outside the compiled runtime and outside the publication. No new deployment was required.

## Large PGN import follow-up

The three draft PRs remove the browser and application 256 KiB PGN checks and the Chess parser's 32-game cap. The 2 MiB HTTP content-command body limit and per-game chess validation still apply.

| Component | Tested commit | Review |
| --- | --- | --- |
| Tempo | `2d3eab57835ff463ee52d5da43964a959a18a502` | [Tempo #4](https://github.com/tempo-v2/tempo/pull/4) |
| Chess | `64872499fc486dbfc609e962eca6811520ab4562` | [Chess #2](https://github.com/tempo-v2/tempo-chess/pull/2) |
| UI | `6dd069da296d926512f2cc719f9031b32466eb45` | [UI #1](https://github.com/tempo-v2/tempo-ui/pull/1) |

Use those three commits together with the other repository revisions in checkpoint 04, the workspace lock, and the UI lock's bundled Core 0.2.1 package.

The locked Tempo and Chess tests, the UI build and 21 tests, and seven HTTP and boundary tests passed on the listed combination. Chrome uploaded and saved a valid 300-game repertoire larger than 256 KiB in a disposable database. It previewed all 277 records of a 747,227-byte game collection and saved a selected tactic from it. That collection contains conflicting learner moves for either color and remains unsuitable as one repertoire under the current import contract.

The fix awaits review and a coordinated installation of the three components. No production service or study database was used for testing.

## Coordinated main candidate, November 18, 2026

The candidate captures the current Tempo 2 sources, including tactics settings and theme selection, personal capture scheduling, and the board sounds and move feedback packaged with Core 0.2.2. It retains the large PGN import fix from the published release branches. Each component PR targets its own `main`. The [manifest](manifest.json) records the compatible component commits and input hashes.

| Component | Candidate commit | PR |
| --- | --- | --- |
| tempo-types | `8662444cfb1ed1d2710c2bd95c4939473d6c0307` | [#1](https://github.com/tempo-v2/tempo-types/pull/1) |
| tempo-study | `c0d4436987b67546f9112728893991d454e33030` | [#1](https://github.com/tempo-v2/tempo-study/pull/1) |
| tempo-chess | `db3a758350aecde33a2ec652760520f86a7e985e` | [#4](https://github.com/tempo-v2/tempo-chess/pull/4) |
| tempo-learning | `f036785bb52820d60d6c067a125987262722cf9d` | [#2](https://github.com/tempo-v2/tempo-learning/pull/2) |
| tempo-queue | `d89b95fe7a6d24dac488e17cd9f813e23335da8f` | [#2](https://github.com/tempo-v2/tempo-queue/pull/2) |
| tempo-store | `62aea494e6b5588a6c642e16e6ecec413cd74c30` | [#3](https://github.com/tempo-v2/tempo-store/pull/3) |
| tempo-core-components | `8ce37b3ff677a3145d59206d5149bc586ddf66d4` | [#5](https://github.com/tempo-v2/tempo-core-components/pull/5) |
| tempo-ui | `af08033ca98dd5115d54b878cea0aee32ea8d46e` | [#3](https://github.com/tempo-v2/tempo-ui/pull/3) |
| tempo | `04fdbf4d7d4b4cf6da898ec13e434ef4c3fbfd48` | [#6](https://github.com/tempo-v2/tempo/pull/6) |

The isolated release assembly passed 241 Rust tests, 23 UI tests, one Core package test, seven HTTP and boundary tests, and the dependency-direction gate. The rebuilt Core tarball matched the UI vendor file byte for byte. Disposable Chrome coverage saved tactic themes, verified their persistence through an app restart, and verified the board sound preference persisted across reload. The server served MP3 assets as audio.

Twenty-one of the 22 rebuilt UI files matched the running server byte for byte. The JavaScript diff consisted of the existing large-PGN fix, which removes the two upload forms' 256 KiB guards. The running instance and its dataset were left in place.

Review all ten PRs before merging as a coordinated set. Merge the component PRs and then the planning PR. Use the combined source set for the next build. Installation is a separate step.
## November 18 UX candidate

The packet pins were comparison points. At intake the workspace used those
published heads plus local source for Core 0.2.2, board reply animation and
audio, tactic theme settings, and quota-exempt personal captures. The foreground
listener on port 41822 ran the workspace debug executable and served the
workspace UI matching checkpoint 06. The checkpoint 06 LaunchAgent was idle.
The served JavaScript SHA-256 was
`392479a12f0af0bc239615de87d2c263d4660ca6c04e898e57172a0b7e645999`.
The foreground executable was distinct from checkpoint 06's archived executable.
The listener responded to a Study status read at intake and closeout. The
private dataset path, content and learning were preserved.

The candidate adopts the current runtime and bundled Core package in isolated
source trees. Existing working copies and untracked catalog recovery tools
remain in place. During publication the application, Chess, UI and Planning
integration branches advanced with the large-PGN change above. The candidate
includes those audited changes and keeps the 2 MiB content-command limit and
per-game requirements.

| Packet | Reconciliation and candidate behavior |
| --- | --- |
| 01 | **Partial at intake.** Sticky assessment and exact retries already existed. The UI now reads the terminal grade, pauses after correction, uses separate Practice and Teach wording, and continues after a confirmed lesson with independent Next recovery. Enter is scoped to the available primary action. |
| 02 | **Partial at intake.** Reused versioned Core and existing optional audio, move cues and notices. Added flip, saved theme/piece/volume preferences and shortcut help. Navigation, pausing or inspecting cancel automatic continuation. |
| 03 | **Implemented.** Separate progress read reports due work, required re-teaching, pending scheduled correction, and accepted introductions against the effective limits. It uses the same day, admission facts, and Queue projection as selection. Personal captures retain their existing quota exemption. Completed frontier positions may expose more lessons. |
| 04 | **Implemented.** Move history is derived from the disclosed prefix of the issued definition and the exact reply cursor. History input is read-only, with a return to the same live attempt. Opening context uses the known position and existing teaching context. Full route reconstruction is deferred per packet scope. |
| 05 | **Implemented.** Browse label/source and learning filters in 30-item keyset pages; detail shows stored starting position and provenance. Explicit solution reads are blocked for an active target. Theme and rating normalization are deferred per packet scope. |
| 06 | **Partial at intake.** Reused the legal parser, capture preview token, and durable exact save. The UI uses numbered SAN and selected-line replay, bulk selection of valid rows, equivalence checks after row changes, and preserves a newer draft after an older save resolves. |

### Checks and operating evidence

- The optimized locked build and isolated UI build passed, with 24 UI tests,
  66 Chess tests, eight focused application contract tests, four HTTP/boundary
  checks, strict Clippy for the changed backend owners, and the dependency
  direction check. Core's source rebuilt to the exact installed-package tarball
  consumed by the UI. Practice, rollover, exact receipt replay and learning
  preservation were verified on disposable data.
- Chrome checked terminal clean and corrected tactics, blocked active solutions,
  the played-move cursor, return to the live board, preference reload, lesson
  acknowledgement delivery loss followed by failed Next, and black-to-move
  capture with delayed delivery and a newer draft. The journeys used disposable
  data at 1280 and 390 px widths.
- Independent review led to neutral reveal wording, retention of other capture
  row drafts, and a fix for a successful Retry Next leaving Study paused. A
  stale cross-tab solution response is discarded when an activity change is
  observed. The backend checks the current active target on every detail read.
- On a disposable copy with 17,657 tactics, one optimized run measured about
  207 ms for Next when selection was required, 213 ms for full progress,
  9 ms for an unchanged progress stamp, and 42–66 ms for the first two unfiltered
  30-item collection pages. A due query took 103 ms and a no-match source search
  took 196 ms. Reads on transition share Queue policy, and periodic stamped
  checks avoid catalog reads when the dataset/day/revision match. Times are
  single local observations.
- The UX branches are open drafts against the current integration branches.
  Coordinated review is pending. The existing live service remains on its
  observed foreground binary and checkpoint 06 UI; the UX candidate was
  built and verified on disposable instances.

### Matched source and artifacts

Use the pinned sources together. The existing
[workspace build instructions](WORKSPACE.md) and `workspace-04.Cargo.lock`
apply when reconstructing the candidate with these revisions in a separate
directory. The Cargo lock SHA-256 remains
`00a275f9216923bcb093b8c1eaeec16585040fde26647ab73ab880f16e0dd042`.
Use the UI lock and the vendored Core package; the wire-4 history field is
optional and the new reads are separate from existing command receipts.

| Repository | Candidate head | Pull request |
| --- | --- | --- |
| tempo | `cbb0a3e36b39c8ebbce379de88063aaacf6c2dcb` | [#5](https://github.com/tempo-v2/tempo/pull/5) |
| tempo-ui | `d782e748b734fd2df155a39fd3025339792c5fd9` | [#2](https://github.com/tempo-v2/tempo-ui/pull/2) |
| tempo-core-components | `d30422b9bd6a972c12189200ac6eb4ca0114239c` | [#4](https://github.com/tempo-v2/tempo-core-components/pull/4) |
| tempo-chess | `b81fea2f1ed94a83ace53a094a78fb0f9a022153` | [#3](https://github.com/tempo-v2/tempo-chess/pull/3) |
| tempo-store | `d4e731c4bef33fdec560aa7f409bb3e974a69393` | [#2](https://github.com/tempo-v2/tempo-store/pull/2) |
| tempo-queue | `3009a4b6c450305abbc26f3af396f301cdffb38c` | [#1](https://github.com/tempo-v2/tempo-queue/pull/1) |
| tempo-learning | `e5bae3eb19d9aa74d9b7ca01882f2078ae1ff569` | [#1](https://github.com/tempo-v2/tempo-learning/pull/1) |
| tempo-study | `c0d4436987b67546f9112728893991d454e33030` | Reused |
| tempo-types | `8662444cfb1ed1d2710c2bd95c4939473d6c0307` | Reused |

| Candidate artifact | SHA-256 |
| --- | --- |
| Optimized Tempo executable | `f247b70cafbe12bdf3dad3c8500b1863e804c830b5001bee108cda85d9165ee8` |
| UI JavaScript | `a7399f02a638e8e2189a8a04444ad4efddba2b7612bd36faa223ec5f9002e61c` |
| UI stylesheet | `1dd1a2da646816cf0f6d3c58edb9325e8b00fa0f884b25bb98e5816d965f0eb1` |
| UI lockfile | `c15717f93ba11bd0b5e0637715d74f996f41c95c5b6f54e683fea2116e6c762c` |
| Core 0.2.2 UI tarball | `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4` |


### Release review and installation handoff

The second review found that the capture preview flipped after each replayed
ply. The UI fix anchors it to the solver's starting side. Chrome verified
black-side orientation after the first move. The full locked Rust workspace
suite and the final UI and Chrome checks passed. On a private copy of the
live schema-3 database, startup and Study, progress and collection reads
preserved every row.

The authorized cutover uses the matched checkpoint under
`.local/usable-release/checkpoints/07-ux`. Its private `verification.json`
records the observed installed artifacts and Study check. Its `source.json`
records the verified merged source trees. Startup uses the original database
path. The pre-install backup and previous artifacts are retained privately.

## Shared Study decision contracts, November 18, 2026

Checkpoint 08 installed Study wire 5 and the optional, display-only
`exercise_name`. Checkpoint 07 carried the richer Study experience on the
release branches and used wire 4. The coordinated candidate starts from the
current main branches and reconciles the accepted UX changes as one source set.

| Behavior | Basis and owner | Decision inputs | Independent of | Lifetime |
| --- | --- | --- | --- | --- |
| Continue after a clean Test or Practice. Hold a corrected completion for explicit Continue. Teach requires the learner's acknowledgement and then loads Next. | Shared Study workflow requested for the local daily runtime. UI owns navigation and cues. Study owns whole-attempt assessment, which Tempo projects. | Issued activity, completion, whole-attempt outcome, settled delivery and current view. UI also honors stop, inspection, dialogs and navigation. | Exercise name, source attribution and correctness of only the final move. | Study persists the sticky assessment and Tempo reprojects the issued attempt on replay. The UI timer belongs to the current display and is canceled when that display is left. |
| Retry an unresolved command exactly. After an accepted Answer or Acknowledge followed by failed Next, only retry Next. | Existing local Study exact-command contract. The UI controller owns delivery and the enabled recovery actions. | Controller busy state, the pending command, storage availability, authoritative stale error codes and validated replies. | Error wording and exercise metadata. | The immutable mutation envelope survives reload and releases. Next is retried in the current UI, and startup can request Next after a resolved mutation. |
| Recover a previously accepted allowance with its original summary and one durable effect. | Local Study wire upgrade and existing exact-receipt contract. Application owns response compatibility, Store owns atomic receipts and allowance writes. | Matching dataset, submission and fingerprint, receipt kind and recognized saved Empty version. | Today's clock, queue, catalog and allowances. | Historical wire-4 and current wire-5 replies can coexist in SQLite. Only the replay header is adapted. Content replies remain wire 4. |

Expected consumer outcomes were specified before changing the workflow. With a
fixed exercise, clock and command IDs, an unchanged, renamed or omitted label
produces identical commands and database effects. Changing the whole-attempt
outcome to Again holds the completion even if the last move is correct. A
reproduced Teach move alone writes nothing. Inject loss after accepting Answer
or Acknowledge and expect the same command on Retry. Separately fail Next and
expect the saved result and only Next on Retry. Replay a real wire-4 allowance
from the previous installed backend after rollover and compare the saved reply,
both days' allowances, revision and receipt count.

### Reconciliation

| Finding | Disposition |
| --- | --- |
| F1, continuation and outcome | Main already supplied the neutral name and wire 5. The reconciled UI also carries the UX branch's whole-attempt outcome, explicit acknowledgement and separate Next, played history, progress, preferences, collection and capture improvements. Exercise names are display-only. The prompt supplies move progress for any activity. |
| F2, accepted older allowance reply | Repaired in the application replay path. Existing typed attempt receipts already reprojected pinned attempts. Content saves already used wire 4 on both sides. The Study and both content pending-envelope formats are unchanged. |
| F3, prose-driven controls | Repaired in the UI controller and its consumers. Storage and refresh facts, current delivery status and the pending command determine available recovery actions. |
| F4, theme admission and transfer | Still present. The application converter `tools/tactics/convert.py` gives catalog-directory imports richer membership provenance than repository packs. `application/tactic_preferences.rs` decodes it and passes ranks to Queue for unseen admissions. Explicit theme selections can exclude items without recognized metadata. Due work and practice remain eligible under their existing policies. `apply_tactic_transfer` preserves existing items during reimport. The next contract should define validated membership at import, what reimport can enrich and how existing learning is preserved. |
| F5, repertoire replacement and identity | Still present. Application `import_pgn/apply_catalog` can reset the full Learning state on semantic changes, while browser replacement uses `DailyLearning::changed_answer` and preserves lifetime introduction evidence. The local transfer command is tactics-only. The legacy Chess `RepertoirePgnParser` uses one string as ID and label, while `compile_repertoire` separates them. Before adding a caller, define generic merge versus replacement semantics, require the appropriate Learning transition and narrow the legacy parser contract. |

### Verification

- The locked workspace passed 243 Rust tests and doctests with Rust 1.98.1.
  The UI passed 25 tests and built on Node 26.12.0 from the lock and bundled
  Core 0.2.2. Seven transport and Core boundary checks passed, along with the
  dependency-direction check.
- Real Chrome and SQLite exercised the same seeded attempt and browser submission
  IDs across original, changed and omitted names for clean and corrected Test,
  clean and corrected Practice, and Teach. Commands, receipt identities,
  grades, learning and allowance effects matched across variants. The candidate
  passed with the real clock on the same study day, comparing without elapsed
  milliseconds. A separate disposable build changed only the clock to a
  fixed instant and passed with exact row comparisons.
- A lost response after accepted Answer or Acknowledge required repeating the
  exact command. A subsequent interrupted Next displayed the saved result and
  Retry sent only Next. Chrome also checked stale recovery with empty and changed
  message text, and exercised move history, progress, preferences, collection
  and the capture draft.
- Archived checkpoint 07 (wire 4) and checkpoint 08 (wire 5) binaries created
  database fixtures using the real HTTP path. Both archived UIs produced their
  own pending allowance envelopes after loss of an accepted reply. The candidate
  loaded disposable copies and recovered those envelopes, typed Answer and
  Acknowledge receipts, and serialized repertoire and capture saves. Replays
  were compared before allowing Next to run. SQLite allowances, revision,
  receipts, assessments, attempts and learning were unchanged by the replays.
  Both archived clients also left an Answer pending before reaching the server.
  The candidate accepted each original command once and replayed it without a
  second grade or receipt.
- The cross-midnight regression inserted the historical wire-4 receipt shape
  through Store, advanced the app clock one day and recovered the original
  summary twice. The same-version cross-midnight test also passed. The archived
  binary checks and clock-controlled SQLite tests provide separate evidence.
- The independent review checked contract authority, branch reconciliation and
  the implementation. Review corrected a missing integration import, Refresh
  being hidden by empty error text, and timer rearming after failed manual Next.

The running listener still points to checkpoint 08. Candidate qualification
used disposable services and databases. This release set keeps Study wire 5,
content wire 4 and SQLite schema 3.

### Matched source and artifacts

| Repository | Candidate commit | Pull request |
| --- | --- | --- |
| tempo | `4c2b26bcaaf1dc13a300c3f6de4c265c5dce7a7a` | [#8](https://github.com/tempo-v2/tempo/pull/8) |
| tempo-ui | `d09620a123b8031fa30d183e3db41f0df478dde0` | [#5](https://github.com/tempo-v2/tempo-ui/pull/5) |
| tempo-store | `b15562b97d3db9606f6cd28a2f4d6c4b64145169` | [#5](https://github.com/tempo-v2/tempo-store/pull/5) |
| tempo-chess | `beecfd991ae2027975c1c8cc3d767671bdd80260` | [#5](https://github.com/tempo-v2/tempo-chess/pull/5) |
| tempo-queue | `1a1dfdebe97a14662b402a7a4715cb85c2c81285` | [#3](https://github.com/tempo-v2/tempo-queue/pull/3) |
| tempo-learning | `10fd7783685a70e05f3ae2a606d8d25deaddf1ef` | Reused main |
| tempo-study | `73b2482dfb2ae652220727b87451fdb4a5110807` | Reused main |
| tempo-types | `a8e46c9b9442f1180ec33b8035cef1c713414b66` | Reused main |
| tempo-core-components | `e9a1d160a729bc9fbbddaf16427625301cc9498a` | Reused main |

Use the [workspace lock](workspace-04.Cargo.lock) and the UI lock with the bundled
Core 0.2.2 tarball. The Core tarball SHA-256 is
`4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4`.

### Verified checkpoint 09 installation

The qualified source trees matched the merged main branches. The archived
executable, public UI files, workspace lock, UI lock and Core 0.2.2 tarball
matched the pinned assembly. This reused the qualification above, including
recovery from checkpoints 07 and 08. See the [checkpoint 09 manifest](manifest.json)
for merge commits, locks and artifact hashes.

Checkpoint 09 was initially installed by the session LaunchAgent on November 18.
A foreground development launch subsequently displaced it. The foreground
process and the loaded but stopped managed job were checked separately. The
managed checkpoint was then restored on the original dataset. A fresh private
SQLite backup and an isolated startup rehearsal verified integrity, foreign
keys, and unchanged content, learning, configuration, active work and receipts.
Chrome rendered Study on the rehearsal copy. After stopping the foreground
listener, a fresh pre-install backup was taken. The managed listener served
21 matching public assets, and read-only Study, progress, content and
collection checks agreed on the dataset. The live database matched the
pre-install backup row for row. No live grades or repertoire mutations were
used for verification.

## F5 repertoire mutation contract

These rules apply to the current local daily runtime and retain the separate
standard-profile import used by the durability and portable-restore fixtures.

| Operation and behavior | Basis and owner | Inputs | Independent of | Durable effect and retry |
| --- | --- | --- | --- | --- |
| Create a repertoire through Preview and Save. | Local Repertoires upload contract. Tempo allocates the destination and Chess compiles its PGN. | Dataset, exact signed upload, explicit learner color and validated label. The signed preview carries the generated ID. | Existing labels may match the new one. They are never lookup keys. | New ID and targets, default learning, one exact Save receipt. |
| Rename an existing repertoire. | Local Repertoires rename contract. Tempo applies label metadata. | Dataset, existing ID, validated new name. | Target keys, semantic versions, eligibility and learning. | Updates the catalog display label and may advance content revision. Repeating the current name is a no-op. Prior accepted Save receipts stay replayable. |
| Replace all selected routes. Retire omitted targets and restore reintroduced targets for that same repertoire. | Local Repertoires replacement contract. Chess compares against the latest retained definition. DailyLearning owns changed-answer policy and Tempo coordinates the atomic Store commit. | Dataset, selected ID, current name and learner color, exact signed input and content revision, latest catalog and learning at Save. | Other repertoires and tactics. Ordinary Study may update learning after Preview. Presentation-only changes do not alter semantic version or attempt authority. | Same definition retains version and learning, even after retirement and restart. A changed answer advances version, preserves first introduction and requires re-teaching without a new slot. Invalidated active attempts remain abandoned. An exact accepted Save returns its original receipt before freshness checks. |
| Additive catalog merge remains available in the standard profile. | Existing standard import and fixture contract. Chess plans the merge, Tempo applies its existing profile behavior, Store commits atomically. | Dataset and validated catalog or configured parser output. Explicit parser destination ID and separate label. | Display and provenance do not supply identity. | Omitted content remains present. Existing standard semantic-reset behavior stays in that profile. |
| Reject generic PGN and non-tactic catalogs in daily Study. | F5 caller audit. Daily PGN uses signed browser Preview/Save. CLI transfer and the public daily catalog method use the existing tactic-only planner. | Selected runtime profile. For a catalog, Chess accepts only active tactic items and no repertoire routes. | Label, provenance, and target spelling do not choose the mutation path. | Unsupported input, including mixed catalogs, fails before writes. These Rust methods have no persisted request envelope or browser command route. |

Changing the legal answer at the same identity must change the semantic version
and reset answer-specific learning. Changing only the name must preserve
versions, learning and valid attempts. Exact receipts remain authoritative
after later content edits. An unaccepted command for an abandoned attempt stays
invalid even when the same semantic version returns.

The independent contract review traced the browser routes, tactic-only CLI
transfer, generic Rust methods and standard durable-repertoire fixture. It
confirmed the existing daily replacement, invalidation and replay behavior on
checkpoint 09 using disposable SQLite. Browser Save and Study recovery paths
are reused without changing serialization or command interpretation.

### Implementation and focused evidence

[Tempo #9](https://github.com/tempo-v2/tempo/pull/9) is pinned at
`53fa24687013de819b6f82b66274ca59cf5d3cb6`.
[Chess #6](https://github.com/tempo-v2/tempo-chess/pull/6) is pinned at
`22f7f5934849a41cce22a4550530add921ea9a88`.
Use those trees with the other checkpoint 09 components, workspace lock, UI
lock and Core package from the manifest. No Store, Learning, wire or schema
change is required.

The locked Tempo and Chess checks passed 134 tests and doctests. The
application tests cover daily generic rejection with PGN, repertoire catalogs
and two mixed catalog forms, and verify that a valid tactic can use the same
display label. File-backed checks also cover Standard additive import,
retire/restart/restore, invalidation and exact replay. The existing quota,
ordinary review between Preview and Save, FSRS and replacement checks passed
with the candidate. Architecture and formatting checks passed.

Independent review exercised public Rust entry points, HTTP and file-backed
SQLite. It verified mixed and route-only rejection before writes and that
generic daily PGN never reaches its parser. Using the archived checkpoint 09
backend to issue original commands, it verified pending signed Save delivery
and exact accepted receipt replay after content edits, rename and restart.
It checked that restoration compares against the latest retained answer,
keeps the same identity, allows re-teaching at zero opening allowance and
cannot revive a retired or invalidated attempt. Intervening reviews retained
their learning. Older accepted Study receipts still replayed exactly, while
unaccepted commands for the invalidated attempts were rejected.

Chrome also retained a pending Save initially sent by the checkpoint 09 UI
after its committed reply was lost. On restart with the candidate, the browser
reloaded and sent the exact original request. It rendered the original success
reply while the later rename, content revision and receipt count stayed intact.

F4 theme membership remains a separate deferred task.

### Verified checkpoint 10 installation

The independent reviewer approved both exact code heads. The optimized
executable passed their HTTP, SQLite and Chrome tests with the archived
checkpoint 09 UI. The merged main trees matched the qualified heads.
[Tempo #9](https://github.com/tempo-v2/tempo/pull/9) merged as
`80d5abc63c95b003fff1da56c9dadc02a576dd54`,
[Chess #6](https://github.com/tempo-v2/tempo-chess/pull/6) as
`e454bcfe7d90c1f7cbcff02325f09b23944d31c9`, and
[Planning #8](https://github.com/tempo-v2/.planning/pull/8) as
`2fa0aef4deb34f89395489377768b8c51a1eb70d`.

The [checkpoint 10 manifest](manifest.json) records the exact component
and artifact combination. The release reuses the checkpoint 09 UI, Core 0.2.2
and both locks. Checkpoint 09 also rendered the existing live attempt in
Chrome using a read-only Resume before cutover.

A fresh private SQLite backup passed integrity and foreign-key checks. An
isolated startup rehearsal preserved all rows and rendered Study in Chrome.
After a second private backup at cutover, the macOS session LaunchAgent
started checkpoint 10 on the original dataset. The listener served
21 matching public assets. Study, progress, repertoire and collection
reads agreed on the retained dataset, and Chrome rendered the existing
attempt using read-only Resume. The live database matched the pre-install
backup row for row. Prior release artifacts and the previous LaunchAgent
configuration remain available privately for recovery.

F5 is closed. F4 remains deferred.


## Development lifecycle correction

Checkpoint 10 remains the installed runtime. The earlier foreground launch
displaced checkpoint 09. The incident evidence does not identify the exact
command that caused it.

| Operation | Basis and owner | Inputs and durable effects |
| --- | --- | --- |
| Development build/start | Packet A, assembled workspace launcher and shared preflight | Current registered plist and loaded job, resolved file and output identity, selected development database and local bind availability. An occupied port fails before build or initialization. A fresh default may be initialized. An explicit missing path requires `init-dev`. |
| Foreground shutdown | Foreground terminal | Ctrl+C reaches the process launched for this command. Development commands do not signal existing listeners. |
| Installed restart or release | Explicit Mac managed lifecycle | Registered artifact pair and retained database. Release uses qualified pins, backup and rehearsal. A stopped job retains the same resource protections. |

The canonical Mac registration is read even in an alternate worktree. A
different port, path spelling or worktree does not make a managed resource
available for development. A file or directory alias and an unreadable
registration cause refusal before the guarded operation writes. The shared
guard also runs for a direct UI build.

### Completion and editor handoff

Tooling updated; checkpoint 10 runtime retained. [Tempo #10](https://github.com/tempo-v2/tempo/pull/10)
merged as `0a2c0af9102983749b7f345aa0154b1554c008bb` and
[UI #6](https://github.com/tempo-v2/tempo-ui/pull/6) merged as
`9e47931668db1fbe6fcfe1dfab662f3584a56364`. Both published PR
diffs and merged trees matched the checked branches. The Mac workspace's
root Makefile includes the merged launcher. The matching UI guard and
operating instructions were adopted as scoped files so existing working
changes could stay in place.

Use `make start` on 41823 with the separate default development database.
Use `make init-dev TEMPO_DB=PATH` to create a disposable explicit database,
then `make start TEMPO_DB=PATH TEMPO_PORT=PORT`. Use `make build-ui` for an
output-only build. Installed use remains on 41822 through the session
LaunchAgent. Explicit managed startup and release rehearsal are described
in [Tempo's operating instructions](https://github.com/tempo-v2/tempo/blob/0a2c0af9102983749b7f345aa0154b1554c008bb/OPENING.md#installed-use-on-the-mac).

The independent report approved the code after five focused guard tests
and real Make and UI entry point checks. The checks covered occupied
ports, unloaded and uninspectable registrations, database and output
aliases, alternate worktrees, and parallel Make. A new explicit SQLite
database passed integrity checks. The development server started twice
on a single disposable database using the adopted workspace command,
with foreground shutdown between runs. The installed PID, database
identity and registration stayed unchanged. The backend and all 21
served UI assets matched the checkpoint 10 manifest before, during and
after the checks. Development used the disposable dataset throughout.
The editor can use these commands and the checkpoint 10 manifest for
the previous-release recovery rehearsal.

## Current repertoire PGN editor

Packet B applies to the local daily Repertoires authoring surface. The
independent design review confirmed the boundaries before implementation.

| Decision | Basis and owner | Semantic inputs and lifetime |
| --- | --- | --- |
| Current document | Packet B, Tempo and Store | One accepted authored PGN per dataset and stable repertoire ID. Store pins the archived source atomically with Save. Unknown legacy associations are unavailable. Names, headers and provenance order never resolve the source. |
| Edit authority | Packet B and existing F5, Tempo | The addressed read returns the content revision and authoring metadata together. Edit Preview checks that revision before signing the exact F5 input. Save verifies existing signatures unchanged and validates post-Preview freshness. Newly issued tokens authenticate a new purpose so a legacy receipt-only Save at the same revision cannot claim new Preview authority. Study revision changes alone permit the edit. Rename follows the existing content revision and keeps PGN bytes. |
| Document-only Save and replay | Packet B and F5, Store and Tempo | A changed source pointer advances the content fence even if the catalog is unchanged. Semantic versions and Learning still follow F5. The old accepted receipt replays exactly and never republishes its historical source. Migration creates an empty association table and preserves existing revisions. |
| Display and delivery | Packet B, Tempo authoring reply and UI | Explicit Edit or Download requests full PGN. Editing and downloading do not issue Study commands. The UI retains edits through failures and retries the immutable signed Save while acceptance is uncertain. After acceptance it reloads current state as a read. |

### Qualification and publication

The compatible main trees matched the independently approved PR heads and
the source used for the optimized backend and UI build.

- [Store #6](https://github.com/tempo-v2/tempo-store/pull/6) merged as
  `779c50a9fb0c63bed4e613c54d589158fc945917`.
- [Tempo #11](https://github.com/tempo-v2/tempo/pull/11) merged as
  `a41ac24f1743fbba1fddd7f9f395f2176c04e7ef`.
- [UI #7](https://github.com/tempo-v2/tempo-ui/pull/7) merged as
  `d885269c188677a38bbdb06975b3c8679a6c1805`.

Locked Tempo and Store checks passed 93 tests and doctests. The 25 UI tests
passed. File-backed acceptance included a true A→B→A document-only write,
both freshness fences, Study between Preview and Save, and injected rollback
of document, catalog, Learning and receipt. The candidate accepted exact
replay after a later edit and rename without reverting either. Reused Core
0.2.2, the component pins and locks from checkpoint 10 for unchanged
components, and existing Study wire and queue behavior.

The real Chrome editor check used guard-qualified development startup and
was repeated with the optimized pair. It covered unavailable legacy sources,
late reads, switching, invalid PGN, dirty Cancel and Study navigation,
typing after Preview, current-only download, both stale conflicts, Save
accepted with a failed document reload, and exact retry after a lost Save
reply across browser and server restart. Independent optimized checks also
covered recovery storage read and cleanup failures.

The independent reviewer used the previously installed checkpoint 10
binary and Chrome UI to capture accepted-and-lost and unaccepted signed
Save envelopes. Candidate migration preserved the full schema 3 data dump.
The accepted envelope replayed byte for byte without changing current PGN
or metadata. The unaccepted envelope committed once. A separate copy
rejected it after a real intervening content edit. A fresh Preview
established the same authored PGN after a legacy receipt-only Save at the
same revision. Altered inputs and incorrectly versioned signatures failed.

### Verified checkpoint 11 installation

On November 18, the qualified optimized backend and UI were installed on
the original dataset through its macOS session LaunchAgent. A fresh
private backup and rehearsal verified SQLite integrity, foreign keys,
and preservation of all existing rows across schema 3 → 4. A second
private backup was taken during cutover. The live dataset inode was kept
and all pre-cutover rows matched the migrated file, with only the new
empty association table and supporting index added. No synthetic edits
or grades were used on the live dataset.

The managed listener on 41822 served all 21 pinned assets and the HTML
entry point. Read-only Study status, progress, repertoire list, legacy
document read and Resume of the saved active attempt passed. The
[checkpoint 11 manifest](manifest.json) pins the installed components,
locks and artifact hashes.

Use Edit, Preview changes, Save repertoire, and Download PGN on the
Repertoires page. A repertoire that predates checkpoint 11 may have no
verified current document. An accepted complete replacement through the
existing import form establishes it. The installed schema is 4.
Checkpoint 10 cannot open that schema. Keep the private pre-cutover
backup and preserve any later accepted work if recovery is needed.

F5 remains closed. F4 theme membership, visual editing and game or
feedback integration are outside this checkpoint.

## Game evidence for daily Study

Scope is the local daily runtime and the November 18 game-evidence packet.
The candidate starts from current component mains including the PGN editor,
guarded development lifecycle, and offline tactic tooling.

| Behavior | Basis and owner | Inputs, independence and lifetime |
| --- | --- | --- |
| Import completed games | Packet, provider adapters and Tempo | Explicit source, account or PGN learner, repertoire and bounded dates. Source plus stable provider ID identifies a game. Local PGN identity derives from normalized played game facts. Preserve participants, played mainline, source time interval and separate ingestion time. Labels do not identify players or repertoires. |
| Compare covered decisions | Packet, Chess | Explicit repertoire ID and its configured color, learner identity and legal played mainline. Active canonical position identifies each target within that repertoire. Record match or deviation with target/answer version and ply. A comparison keys on game, learner, repertoire and compared semantic facts. Display changes preserve identity. A new answer version may yield new historical evidence. |
| Project relevance | Packet, Evidence and Learning | Evidence retains observations and reduces bounded current-version facts. Learning alone authorizes a coalesced Test obligation from a provably post-teaching miss whose occurrence upper bound is at or after the latest qualifying assessed Test's issuance. Unknown chronology yields record-only for learned material. Use strict comparisons for chronology and the accepted Test's configured study day for target-wide cadence across answer changes. Test issuance before the game leaves the obligation pending, while changing only import timestamp does not change coverage. |
| Accept and select work | Packet, Learning, Store and Queue | Ordinary Test alone schedules and records authoritative issued/assessed coverage atomically with any request resolution. Persist answer-version requests and coverage across restart and portable restore. Queue prioritizes actionable requested Tests, then ordinary due work and allowed opening frontiers using compiled route membership. Current attempts, quotas, cadence and answer protection remain authoritative. |

### Games usage and recovery

Open Games from Study. Choose Lichess or Chess.com, enter the learner's
public account name, choose the repertoire for the learner's color, and
select up to 31 UTC dates. Refresh is explicit. Lichess filters by game
start, and Chess.com archives by game finish. Other-color games are counted
as skips. Chess.com archives can lag the live site. A partial read lists
its errors separately and leaves the last successful refresh time intact.

For PGN, choose the learner's exact White or Black player name and one
repertoire. Upload a file or paste complete games. Legal PGN mainlines
provide comparison evidence. Authoritative UTC start and end bounds can
come from a previously verified matching provider record, or from the
PGN's UTCDate, UTCTime, UTCEndDate and UTCEndTime fields. A date alone
cannot establish a post-teaching lapse. Older repertoires without a verified
current PGN can compare exact learner positions. For their opponent moves,
unknown branches are counted as coverage gaps.

The Games views show positions matched, learner deviations, and the first
deviation's half-move, without exposing its prescribed move. A Game request
can bring a qualifying learned target into today's normal Study Tests,
subject to the next-study-day floor after Teach and one accepted Test per
target per study day. A Good or Again covers occurrences strictly before its
saved issuance. Later misses keep their request. An untaught deviation can
raise its existing route frontier within the current allowance. An active
exercise stays on the board. When a Games reply is interrupted, retry the
saved command to recover the committed result. A deliberate new import can
compare the same game with a newly edited answer version.

Study wire 5 and content wire 4 are unchanged. The new Games endpoints
have their own answer-safe report and receipt. SQLite migrates schema 4
through 5 to 6. Assessed Test issuance and target-wide acceptance day are
backfilled from existing authoritative rows. Daily portable snapshots are
format 2 and carry pending obligations and coverage even for a target
with no pending request. Format 1 remains readable and retains unknown
issuance where it has no historical evidence.

### Candidate and checks

Phase 1 used SQLite and Chrome to compare a legal uploaded game alongside
a malformed record, retry an unchanged game, and confirm that evidence-only
ingestion preserved attempts, learning, allowances and scheduling. The
serial provider adapters read both public services directly. The Lichess
bounded July 17 export returned game LhL9TRJY. The Chess.com October 4, 2009
window returned two completed Erik games, and a repeat returned the same
IDs using the cached adapter. Chrome also completed a bounded Lichess
refresh via the app.

Phase 2 exercised the real SQLite daily path. A future-due learned target
became eligible, preserving its FSRS memory until Test. The first Again
plus correction created one grade and kept a genuinely newer observation
pending until the next study day. Good resolved the newer obligation.
A deeper unseen miss prioritized the allowed frontier. Portable
export/restore suppressed reimport of already covered evidence. A completed
public Lichess PGN exercised Test selection, durable resolution, exact
receipt recovery after a repertoire edit, and deliberate reanalysis.

The reviewed runtime candidate is:

| Component | Pull request | Candidate head |
| --- | --- | --- |
| Chess | [#7](https://github.com/tempo-v2/tempo-chess/pull/7) | `427bc84f6303d35818ae4ead8a96d41fd58419a7` |
| Learning | [#3](https://github.com/tempo-v2/tempo-learning/pull/3) | `9d24ad171a4d682929a812344397eb2e05be05ba` |
| Queue | [#4](https://github.com/tempo-v2/tempo-queue/pull/4) | `aa49bdfed6bdbbea7178462f4e79748efef8e3f8` |
| Store | [#7](https://github.com/tempo-v2/tempo-store/pull/7) | `249a12a9f0ae880f6000da7de9fb94d8603b68fb` |
| UI | [#8](https://github.com/tempo-v2/tempo-ui/pull/8) | `e21ace64e49b64a6a4be336a7025861961400c65` |
| Tempo | [#13](https://github.com/tempo-v2/tempo/pull/13) | `9caf8a9ac01b71662694e4a9b778f6fcd2d30286` |

Unchanged dependencies use checkpoint 11's Study, Types and Core 0.2.2
pins. Workspace and UI locks are unchanged.

### Independent qualification

The reviewer traced the production DailySession and DailyLearning path and
tested a completed Lichess game through a future-due requested Test and
Again resolution on disposable SQLite. Games import and Study Answer
transactions both rolled back cleanly under injected receipt-write
failures and accepted the exact same command once on retry. The
implementation owner fixed the review findings affecting immutable game
receipts, interrupted refresh recovery and verified PGN source identity.

With the actual checkpoint 11 backend and Chrome UI on disposable copies,
the reviewer captured both accepted-but-lost and unaccepted Study
envelopes. The migrated candidate accepted exact retry with one durable
assessment and receipt in each case. The accepted reply replayed
byte-equivalently. Chrome retained a saved Good when automatic Next
failed and issued only Next on Retry. The guarded application completed
ordinary Next and Answer with a provider HTTP connection deliberately
stalled. Chrome also retried the original Games upload body after a lost
reply and page reload.

The 216 locked Rust tests and doctests and all 28 UI tests passed. The optimized
candidate served all 22 byte-verified UI files and the read-only
Study status/progress, repertoire document and Games reads. The
schema-4 to schema-6 rehearsal verified all prior rows and Learning values,
including 172 backfilled authoritative Test coverage records in that copy.
SQLite integrity and foreign-key checks passed.

The final independent check compared real Chrome command sequences and
durable results with the same exercise name present, changed and omitted,
using a fixed New York study clock and deterministic IDs. Clean requested
Test, corrected requested Test and Teach all matched. The optimized
candidate also recovered the checkpoint 11 editor's exact saved envelope
in both accepted/lost and unaccepted cases, preserving the authored PGN
and committing one document revision. The reviewer checked the actual
Chess.com archive payload and the provider's cache headers independently.

### Merged source and checkpoint 12 installation

The PRs above were merged in dependency order and the resulting remote
main trees matched the exact reviewed heads. The merged pins were:

- tempo-chess `d066844c83648a948ecbf47e11eaed49cdb64367`
- tempo-learning `101ec4245173f4e7afa77e074ef3a665c63e4317`
- tempo-queue `31cb46dfc7e3f513c22aaf33996d18c9498c5ab6`
- tempo-store `36a2131f1b01122b9fa8e125a824fb5d0cd41b0d`
- tempo-ui `61aff22900d1985528bd49b94aa0385c3166f2dd`
- tempo `2d171ec3f3e253d7e282701eca216c8491d11b43`

On November 18, the registered Mac LaunchAgent installed checkpoint
12-game-evidence on port 41822, using the same dataset and database inode.
A consistent checkpoint 11 backup was created before shutdown and
another was taken with the service stopped. Migration preserved all
pre-cutover rows and prior Learning values. SQLite integrity and foreign
keys passed. The release verified the listener against the registration,
all 22 served UI files, and read-only Study resume and progress, the
repertoire document read and Games history. Chrome rendered the installed
Study, Games and repertoire editor with only read-only requests.
No live grades, imports or periodic sync were used for verification.
The [checkpoint 12 manifest](manifest.json) records exact source and artifact
hashes.

Keep the paired checkpoint 11 binary, UI, registration and schema-4
backup as a pre-cutover recovery point. A release repair after new work
has been accepted must use a schema-6-compatible pair and retain the
current database. The checkpoint 11 binary cannot open schema 6.

### Checkpoint 12 Games corrections

| Behavior | Basis and owner | Inputs and lifetime |
| --- | --- | --- |
| Enrich local PGN chronology | Checkpoint 12 correction, Tempo and Store | The same game, matching played facts and precise UTC start may gain a missing valid end bound. A known end survives omission and rejects a different known end. Resolve the batch before Learning evaluates the selected repertoire. Store checks the same rule under its write lock. Accepted command replies are immutable across later imports and restarts. |
| Identify comparison rows | Checkpoint 12 correction, Store and Games UI | Use the persisted comparison ID across history reads. Game identity and display fields may be shared by several versions. Previous receipts may omit the ID. |
| Count received games | Checkpoint 12 correction, provider adapters | Count candidate records evaluated in the requested window, including records rejected individually and malformed records whose date cannot be determined. Archive, transport and limit diagnostics contribute zero. Earlier receipts retain their reported counts. |

The baseline reproduced the known-end rejection in the ordinary import
contract against SQLite. The existing JSX key produced the same value for
two comparison versions, and the existing report calculation counted one
game for a failed month that delivered no records.

The correction resolves PGN chronology across the batch, then applies
the existing Learning transition only to selected comparisons. It
preserves established timing on omission. An older comparison for
another repertoire or version needs a qualifying reanalysis to acquire
the enriched timing. Date-only PGNs and a changed normalized start keep
their existing identity and timing behavior. Older accepted reports
replay their original fields and counts.

The compatible candidate is:

| Component | Pull request | Verified head |
| --- | --- | --- |
| Store | [#8](https://github.com/tempo-v2/tempo-store/pull/8) | `09fc5933c46eb1d0a2ef02a26985f2b675d729f5` |
| Tempo | [#14](https://github.com/tempo-v2/tempo/pull/14) | `b2988778560ce35a694851eb66cea9948e3af87b` |
| UI | [#9](https://github.com/tempo-v2/tempo-ui/pull/9) | `3b55a5a9f07d9fc8737680e2840d42f5bf0e63ac` |

The other component and lock pins match checkpoint 12. Schema 6 and the
Study and content wire versions are unchanged.

The locked Tempo and Store suites passed 103 tests and doctests, with a
focused rerun for enrichment of a game already covered by an ordinary
Test. The SQLite paths covered both batch orders, omission, conflicting
known ends, rollback of earlier writes in the batch, and exact replay
across restart. The provider traversal exercised a failed Chess.com
month and a capped archive with invalid records using fixture responses.
All 29 UI tests and the guarded UI build passed.

Independent Chrome checks exercised the archived installed checkpoint 12
backend and UI on disposable SQLite copies, then used the candidate UI to
recover accepted and never-accepted PGN commands. The accepted reply
replayed byte for byte without the comparison ID. Both retries preserved
the exact command body and left one game, comparison, observation and
receipt per copy, with zero grades and clean SQLite integrity and foreign
keys. Chrome kept history rows distinct across reanalysis and displayed
zero fetched games beside a simulated failed archive. No material
review blockers remained.

Publication opens the compatible PR set. The managed checkpoint 12
installation remains the current release.

### Repertoire progress reset

| Behavior | Basis and owner | Inputs and lifetime |
| --- | --- | --- |
| Start one repertoire from the beginning | User-approved reset with Study history erased. Tempo coordinates, Store owns the atomic write, and Queue clears those targets' session deferrals. | The confirmed command addresses the current dataset and stable repertoire ID. Store scopes it to active and retired targets. The display name and PGN are independent. The reset receipt survives restart and an exact retry leaves newer progress intact. |
| Teach reset positions as new | Existing Daily Study and opening allowance rules. Learning supplies fresh state and Queue uses the existing line frontier. | Reset removes introduction dates, review state, attempts, assessments and their replayable Study outcomes. Attempts on other targets can still recover. Content identities, versions and the accepted PGN remain valid. |
| Keep played games as history | User-approved retention of games. Tempo applies the reset boundary before Learning evaluates game evidence. | A known game start strictly after the saved cutoff can affect Study. An older or unknown start remains historical. Existing import receipts replay exactly. |

The compatible candidate is:

| Component | Pull request | Commit |
| --- | --- | --- |
| Store | [#9](https://github.com/tempo-v2/tempo-store/pull/9) | `ce5b1e44226e37d5120db3fdd064fb80875d3a05` |
| Queue | [#5](https://github.com/tempo-v2/tempo-queue/pull/5) | `d10f76d6e6d2f6b564754ccd91c07c536a1449ca` |
| Tempo | [#15](https://github.com/tempo-v2/tempo/pull/15) | `507bd0b373daa1823f619b256c36e9d4e1c28707` |
| UI | [#10](https://github.com/tempo-v2/tempo-ui/pull/10) | `fb1f5de3c514b6c57e82921d719368ed45e76176` |

The unchanged component trees and workspace lock match checkpoint 12.
The UI uses the same Core 0.2.2 tarball. SQLite schema 7 adds the reset
receipts and scoped lookup indexes. Study and content wire versions continue
at 5 and 4, with a new repertoire command and reply.

All 260 locked workspace tests and doctests and 29 UI tests passed.
The optimized backend and built UI served the reset and retry journey over
HTTP with clean SQLite integrity and foreign keys. Independent Chrome
verification covered cancellation, a lost response, exact retry after new
learning, and a list failure after acceptance. A disposable backup of the
installed database migrated without rewriting existing rows. The reset erased
76 London attempts and 76 assessments on that copy. An injected receipt
failure rolled the whole transaction back. The previous installed UI produced
both accepted and unaccepted Italian lesson envelopes that recovered on the
candidate with one durable teaching effect each. Restoring a retired London
position left it new. Old or undated game imports remained historical and a
game played after the reset could influence teaching.

Installation remains a separate managed release. Take a consistent pre-upgrade
backup before installing the compatible pair. The checkpoint 12 binary cannot
open schema 7. A live repertoire reset requires its own confirmation in the UI.

### Development server restart

The user requested that rerunning `make start` replace the running local
session. The launcher can now replace a verified, same-user Tempo
development listener on the selected port. A listener from another assembled
checkout qualifies under the same rule. The managed installation and other
ports retain their existing lifecycle. Port ownership and managed resource
identity determine eligibility. Checkout paths may contain spaces.

The launcher records the process identity before building. It rechecks the
same listener before sending SIGTERM and waits for the selected port to
become available before launching. A failed build or invalid database leaves
the existing server running. Nothing about the handoff is stored in SQLite.

Real Make runs covered replacement from another checkout, a second launch
from the same checkout, an unrelated listener, managed resource protection in
both checkouts, and build and input failures. The five existing guard tests
passed. The managed listener kept its PID. The current UI guard works with
this launcher. [Tempo #16](https://github.com/tempo-v2/tempo/pull/16) contains
commit `57215e4330f5e856c2d4cf5b1861eb853634e6f8`.

### Single managed Tempo service

The user selected one ordinary Tempo service. Plain `make start` now owns
the registered Mac restart and replaces all positively identified same-user
Tempo development listeners. The archived LaunchAgent determines the retained
database and port. The assembled checkout determines the new runtime and UI.
An explicit disposable database or alternate port belongs to `make start-dev`.
A foreign listener or inconsistent registration blocks the cutover.

Build and disposable migration rehearsal run before process shutdown. A
changed build receives an immutable artifact directory and a stopped-time
database backup before bootstrap. Verification uses the registered process,
the bound port, the dataset, and exact served UI bytes. An unchanged build
restarts without a second backup. Recovery preserves the live database
and can restart the prior service while the schema remains compatible.

| Component | Pull request | Commit |
| --- | --- | --- |
| Tempo | [#17](https://github.com/tempo-v2/tempo/pull/17) | `6dbf784f446380e7c3df4097cc5b49dc9bf4cd14` |
| UI | [#11](https://github.com/tempo-v2/tempo-ui/pull/11) | `1ca0cd54d4242ad8fef5f61043b030dcef852669` |
| Store | [Merged reset #9](https://github.com/tempo-v2/tempo-store/pull/9) | `73e9b2f9eebeb275b22bf4e5b64c063d2005c202` |
| Queue | [Merged reset #5](https://github.com/tempo-v2/tempo-queue/pull/5) | `aed1e864e7a2e22f84f5fce9c616d643ca289000` |

The remaining component trees, lock and Core package match the repertoire
reset candidate. The optimized build and guarded UI build completed. All
five guard tests and the Chrome repertoire journey on `make start-dev`
passed. Independent checks exercised a pre-migration startup failure and
a post-migration startup failure on disposable retained data.

Installed and verified on the Mac on November 18. `make start` closed three
development listeners and replaced checkpoint 12 with
`workspace-5f8da4a18be2eec0cdf2` on 41822. A second run replaced the managed
PID and left one Tempo listener and one cutover backup. The database reached
schema 7 with both-direction row equality for every pre-upgrade table,
clean SQLite integrity and foreign keys, and zero repertoire resets.
Live Study status used the retained dataset and the served bundle included
Reset progress. The stopped-time backup and prior registration are retained
locally. No repository merge was performed by this task.

## Gameplay-triggered corrective Study

This milestone supersedes F4 tactic-theme cleanup. It uses the November 18
Daily Study runtime and the user's game-correction contract.

| Decision | Owner and basis | Inputs, independence, and lifetime |
| --- | --- | --- |
| Classify a game decision | Chess applies the combined repertoire contract. | Use the legal played mainline, explicitly identified learner side, and active target answers at the canonical position. Any prescribed match wins. An uncovered learner move or opponent deviation has no learning effect. Labels are display data. |
| Attribute one repair | Chess uses verified pre-miss move sequences; Tempo accepts a genuine unresolved choice. | A unique target or verified unique route can establish attribution. Save unresolved choices and check the selected option against the current comparison. Bind a choice to the raw game and canonical position across comparison revisions. |
| Apply Game Again | Daily Learning applies or initializes FSRS. Tempo and Store enforce acceptance and deduplication. | Accept at the current model assessment time with source date, compared version and played context as evidence. A date-only game suffices even after a prior Good. A precise start must follow an explicit repertoire reset, and a date-only game qualifies on or after the reset's study day. Keep one durable failure per raw game and target, including after restore. |
| Repair and recall | Daily Learning owns one sequence. Queue projects eligibility and the UI displays the result. | Guided reproduction is immediate and ungraded, including for unstudied targets at zero quota. Three clean recalls qualify on distinct subsequent configured study days. A newer miss resets progress. An already-issued card carries its failure revision. Keep model-assessment timing separate from human Test cadence. |

SQLite schema 8 preserves game receipts, stable comparison IDs, provider
counts, and verified PGN timing enrichment. Startup reconciles the evidence
behind pending legacy requests. Historical comparisons can be reprocessed
explicitly for a window of up to 31 days and 500 stored records. Portable
format 3 retains corrective progress and game deduplication provenance.
Study remains wire 5 with optional presentation fields.

| Component | Candidate commit | Pull request |
| --- | --- | --- |
| Chess | `3bfc6d53b51087901288fa0839d57a8bb49ba168` | [#8](https://github.com/tempo-v2/tempo-chess/pull/8) |
| Learning | `42689dab4f2c6393c6c5d3bb868f87cd9ff107a8` | [#4](https://github.com/tempo-v2/tempo-learning/pull/4) |
| Queue | `7d6c82aa28e38e0d7179ea6272583387528c1a52` | [#6](https://github.com/tempo-v2/tempo-queue/pull/6) |
| Store | `fa6f1a01a3a54d80dcdc7b2de6640dbfec23c8ba` | [#10](https://github.com/tempo-v2/tempo-store/pull/10) |
| Tempo | `77a1359d2e206f1e4ee82c08c5c1453984590cdb` | [#18](https://github.com/tempo-v2/tempo/pull/18) |
| UI | `6dbbbc76cd07ca828cf6e20da4623c9751ac356b` | [#12](https://github.com/tempo-v2/tempo-ui/pull/12) |

Reuse Study `73b2482dfb2ae652220727b87451fdb4a5110807`, Types
`a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core
`e9a1d160a729bc9fbbddaf16427625301cc9498a`. The workspace lock is
`00a275f9216923bcb093b8c1eaeec16585040fde26647ab73ab880f16e0dd042`.
The UI consumes the versioned Core 0.2.2 tarball with SHA-256
`4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4`.

All 263 locked Rust tests and doctests and 29 UI tests passed. Independent
Chrome runs exercised the previous actual installed schema-7 pair and
candidate on disposable copies. Accepted and unaccepted Games and Study
commands retained the original command bytes. Accepted replies matched
exactly, recovery finished, and each human command had one durable effect.
Chrome compared Italian play with London and Ruy Lopez also active. A
date-only Italian miss then offered exact-position guided repair at zero
quota and left three recalls pending after acknowledgement. Rust's
production SQLite contracts exercised separate recall days, stale open
attempts, repeated games, saved target choice, and portable restore.

The optimized backend upgraded a disposable copy of
`workspace-5f8da4a18be2eec0cdf2` from schema 7 to 8. All 20 pre-existing
tables matched in both directions. The process served the retained
dataset's Study status and exact candidate UI bytes, and SQLite integrity
and foreign keys passed.

Remote main trees matched the qualified source after the six feature PRs
merged. The [release manifest](manifest.json) records the final merge
commits and installed artifact hashes. The managed launcher installed
`workspace-1a52ad9b7cb891f341c9` on port 41822 on November 18. The service
uses the retained dataset at schema 8. Verification matched the registered
listener, byte-checked all 22 served UI files, and compared the live
database against its stopped-time schema-7 backup. All 20 pre-existing
tables matched in both directions, with clean integrity and foreign keys.

The independent browser recovery and guided-repair checks passed on the
debug candidate. An optional repeat of the Games recovery check on the
optimized build timed out waiting for a reply after replacing its test
server. The optimized build passed the disposable migration rehearsal
and installed readback. Synthetic games and grades used disposable data.

### Corrective Study portability and acceptance follow-up

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Restore Games acceptance boundaries | The installed Games contract uses each repertoire’s latest reset time and each accepted raw game/canonical-position choice. Store captures those facts and failure keys in the same read as catalog and Learning, and restores them atomically under the fresh dataset identity. Reset receipts, comparison IDs, labels and newly applied grades are independent of those boundaries. |
| Restore pending requests from older snapshots | Learning translates the saved actionable day, answer version, coverage cutoff or teaching-relevance flag into an actionable portable obligation. A qualifying Test or Teach consumes it under the original cadence and allowance rules. Current corrections take precedence. No game identity, played move, synthetic grade or FSRS update is inferred from those flags. |
| Accept a batch of game failures | Learning proposes the transitions in game order. Store validates the game/event, dataset and current target/version and requires exactly the corresponding final writes. Distinct game events for one target may contribute, in order, to one final state. Immutable command replay uses the saved receipt. |
| Validate and describe corrective recall | Learning requires recall eligibility to begin on a later study day than the last model assessment and owns the recall total. Store and Tempo retain those facts through export and restore. |

F4 and explicit Repair counts in Study progress remain follow-ups.

Portable format 4 uses SQLite schema 9. The migration adds two provenance
tables and a choice lookup view. Versions 1–3 remain readable with matching
scheduling settings. Their original fields can carry legacy obligations and
failure keys. Reset or choice facts omitted in an older export cannot be
recovered from that export. The installed-database reconciliation path still
uses actual saved game evidence.

| Changed runtime repository | Qualified commit | Pull request |
| --- | --- | --- |
| Learning | `a5cd36781a86b239da17daa9a3c26c98c54b3e8e` | [#5](https://github.com/tempo-v2/tempo-learning/pull/5) |
| Queue | `f856262183b1c40cefa8391cf060e29c08bf70af` | [#7](https://github.com/tempo-v2/tempo-queue/pull/7) |
| Store | `9330237ed983e940d18f92b353e4355cafc3806e` | [#11](https://github.com/tempo-v2/tempo-store/pull/11) |
| Tempo | `be6ca8f80c211d8df083920c06d92d0c4066a645` | [#19](https://github.com/tempo-v2/tempo/pull/19) |

Assemble these four commits with the Chess, Study, Types, UI and Core
versions in the installed milestone's [manifest](manifest.json).
Use the [candidate workspace lock](workspace-corrective-portability.Cargo.lock),
SHA-256 `c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0`.
The optimized `cargo build --release --locked --offline -p tempo` build with
Rust 1.98.1 produced backend SHA-256
`8b593c32ccef6cb2cdb709f4dea5d9bef24c5873296f02938aad95bbd7236afe`.
The test pair used all 22 byte-verified UI files from
`workspace-1a52ad9b7cb891f341c9`. The earlier UI, Chess adherence,
FSRS cadence and Study recovery qualification applies to those retained
contracts and artifacts.

All 270 Rust tests and doctests passed with the candidate lock. The focused
production SQLite round trips exercised the later of two resets, a saved
choice with a single automatic failure and no new Again, both legacy
obligations through Study, and rejection of same-day corrective recall.
Store rejected missing, stale, duplicate and mismatched writes or event
identities before publication. A real two-game import applied two distinct
transitions and saved one final state. Independent review traced the
consuming paths and reran the focused application and Store tests and the
Learning and Queue suites.

Chrome on the final optimized pair passed accepted-lost and unaccepted Games
recovery from both the actual schema-8 release and the prior schema-7 launch
pair. The schema-7 run used a disposable copy of the 20,639-target retained
checkpoint and exercised the scenario that previously timed out. Both runs
restarted the listener under the same origin and waited for the Games job
endpoint before retry. Chrome sent the original request bytes, replayed saved
reply bytes exactly, and cleared the pending commands. SQLite ended at schema 9
with one durable effect for each newly accepted game and clean integrity and
foreign keys. The original timeout's cause remains unproven.

The four runtime branches were published for review. The candidate remains
unmerged and uninstalled. Readback confirmed the managed installation still
served its recorded UI and used schema 8 on port 41822.

## Game relevance and opponent coverage

This milestone starts at the installed corrective Study schema-9 release and
uses the current Daily Study contract.

| Decision | Owner, inputs, and lifetime |
| --- | --- |
| Record positions and departures | Chess uses legal played positions, the identified learner side, current answer versions, and verified authored branches. A prescribed move accepted by any applicable book suppresses a memory miss. Record distinct-game encounters including correct play, report each book's first departure and later canonical reentry, and distinguish endpoints from unavailable context. Display names are irrelevant. Store retains game identity and learner role independently of comparison receipts. |
| Accept historical learning effects | Tempo uses the explicit backfill range, configured identities, and each repertoire's accepted reset generation at job start. A qualifying older game can receive a current-time Game Again. A later reset supersedes any remaining learning effects for that repertoire. Learning retains one ongoing correction per target. Store keeps the original game/target keys and commits bounded child imports under immutable receipts. Ordinary refresh is governed by its existing reset rule. |
| Rank eligible work | Queue compares distinct-game exposure in the latest 200 eligible games, then attributed misses against the current answer version. Known modeled reach is the fallback for targets without personal exposure. Regular eligible reviews keep corrective and capture precedence. Eligible introductions use the maximum relevance along the unintroduced route and preserve teaching precedence, rotation, quotas and tactic alternation. An answer version can change miss evidence. A display name does not change ordering. |
| Model and author responses | The fixed Maia Rapid 1500 profile caches full legal distributions. Reach sums first arrival across authored paths assuming saved learner moves. Local coverage uses only reply mass for positions with saved learner responses. Gates and starting positions come from Chess. Games revalidates each gap against the current document, and the editor proposes an explicit legal response for the existing Preview and Save workflow. Stockfish and structural-neighbor analysis provide read-only suggestions for that exact position. |

Schema 10 adds durable game facts, projected relevance, job progress, and
model caches. Study wire 5 and content wire 4 keep their existing reply
shapes. Study fetches an optional reason fixed at issuance separately.
Provider fetching, Maia inference, and optional Stockfish analysis run
outside Study. The bounded ranking snapshot is rebuilt by game ingestion or
reanalysis. Full raw game history remains in the installed database.

Production SQLite and Daily Study tests cover correctly played positions,
review order and future-due exclusion, deeper prerequisite selection,
different branches of one repertoire, evidence removal with stable counts,
versioned ambiguous choices, duplicate receipts, and a later reset at the
same clock time while a stored date-only backfill resumes. Independent
Chrome qualification covered metadata invariance, accepted answer with
interrupted Next, exact command replay, and two separate opponent gaps.
Saving the first response left the second gap available. Stalling both
provider and model workers left Next responsive and preserved the issued
attempt on a repeat Next.

The optimized final core pair recovered six previous-release scenarios from
the actual installed schema-9 binary and UI. Games import, corrective choice,
and signed repertoire Save each passed with an accepted-lost and an
unaccepted command. All six commands retained their original bytes and had
one durable effect. Accepted-lost replies matched byte for byte. The rerun
deliberately withheld Games status reads and verified that recovery could
still proceed. It qualifies [UI #14](https://github.com/tempo-v2/tempo-ui/pull/14)
alongside [UI #13](https://github.com/tempo-v2/tempo-ui/pull/13).

The first managed install tested schema 9 → 10 and preserved all 24 existing
tables in both directions, the same retained database inode, and the Study
status. All 22 served UI files matched. The existing Preview and Save workflow
attached the retained Italian and London authored sources on the live
dataset. Both documents round-tripped exactly. The target identities,
versions, ordered route memberships, decoded Learning values, attempts and
assessments matched.

The initial historical range was August 21 through November 18, 2026 UTC.
It completed 30 windows after provider splits, with 377 Lichess games and
1,930 Chess.com games processed. There were 432 durable Game Agains across
178 targets, with the existing Repair and recall rules. No provider
windows remained incomplete. Maia filled all 2,431 requested opponent
positions and projected reach for 2,980 targets.

Raw game identity follows the established provider and normalized PGN
contracts. A PGN matched to a previously verified provider record reuses that
provider record. An older standalone PGN without a verified provider link
keeps its original raw identity. Accepted obligations and receipts are
preserved independently of the derived ranking projection.

### Published and installed on November 18, 2026

The [release manifest](manifest.json) records the exact component
pins and both verified artifact sets. The merged repository trees
matched the checked candidate. Publication includes all companion PRs.

| Component | Pull requests | Installed main commit |
| --- | --- | --- |
| Chess | [#9](https://github.com/tempo-v2/tempo-chess/pull/9), [#10](https://github.com/tempo-v2/tempo-chess/pull/10) | `94b1a0fce704ef16d8065663ce38afcdc6371b11` |
| Queue | [#8](https://github.com/tempo-v2/tempo-queue/pull/8) | `b70402598c91be87687feb42932cf9d8209e3eb1` |
| Store | [#12](https://github.com/tempo-v2/tempo-store/pull/12) | `8c3a18cc3d6ffd48481ea2cd9ff1d365d4b0dc10` |
| Tempo | [#20](https://github.com/tempo-v2/tempo/pull/20), [#21](https://github.com/tempo-v2/tempo/pull/21) | `598c2d329b42c528d0924c6cd45fcad6f4260f98` |
| UI | [#13](https://github.com/tempo-v2/tempo-ui/pull/13), [#14](https://github.com/tempo-v2/tempo-ui/pull/14), [#15](https://github.com/tempo-v2/tempo-ui/pull/15) | `30a1dc13dcd71c314e57678637fc107fb16e19ba` |

The final locked workspace passed 277 Rust tests and doctests and 29 UI
tests. The optimized optional pair passed real Stockfish 19 analysis,
structural neighbors, two-page gap browsing, explicit choice and save,
and cleanup of a deliberately stalled engine. The analysis left the
draft, selection, and database state unchanged until an explicit Save.

The managed launcher installed `workspace-08812817f80797b72eaf` on port 41822.
The stopped-time backup and final database matched across all 32 existing
tables before reactivating the model summary. Dataset and database inode
were preserved. The registered listener served the verified binary and
all 22 UI files, and SQLite integrity and foreign keys passed. Live
readback showed 30 personally relevant targets in the 200-game window,
250 distinct gap groups, complete historical and Maia results, and three
legal Stockfish candidates plus three structural neighbors for a saved
gap. The live verification used a read-only analysis request and did not
save a repertoire response.
