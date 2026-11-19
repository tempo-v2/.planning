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

## Schema-10 corrective candidate

The corrective packet applies to R10-F1 through R10-F5. The earlier
deferred tactic-theme finding is separate. The ten remote main heads
matched the reviewed checkpoint at dispatch. Existing worktrees and the
older open ledger PR #19 are preserved. One backend owner sequences
terminal reach, choice provenance and repair, account recognition, then
model currentness. One UI owner works in parallel. This candidate reserves
SQLite 11 and portable format 5, with a single forward 10 → 11 migration
and matching fresh creation. Preserve the literal intermediate schema 10
in the 9 → 10 predecessor step.

| Finding | Behavior and owner | Semantic inputs and independence | Lifetime and disposition |
| --- | --- | --- | --- |
| R10-F1 | Tempo verifies each book's model input. Store serves the current projection to Daily Study; Queue owns ordering. | Canonical finite authored routes including endpoints, learner side, final active target/version/answer facts, and explicit projection identity. Names, comments, duplicate route representations, tactics and grades do not determine validity. | Keep document edit freshness and inference cache identity separate. Persist bootstrap, verified and revoked authority distinctly. Fence publication by current dataset and book input and preserve complete results against old partial work. Implemented and exercised through the owning consumer. |
| R10-F2 | Tempo projects complete encounters from Chess and accepted choices. Store atomically persists a choice with its selected target/version, independently of Learning. | Dataset/source/game/position closes a choice. Current Chess miss and matching target/version determine attributed relevance. Automatic failures and current candidate ordering cannot select an old choice. | Keep closure through restart, reset, version changes and restore. Recover only proved historical attribution and repair derived encounters under content and exact-choice fences without grading. Implemented and exercised through the owning consumer. |
| R10-F3 | Tempo's existing finite projector includes terminal first arrivals from Chess's canonical endpoint map. | Authored path edges, exact after-position and reply probabilities determine reach. Labels and duplicate path order are irrelevant. | Reproject from raw distributions under the corrected projection identity. Implemented and exercised through the owning consumer. |
| R10-F4 | Tempo scopes each job to the accounts supplied for it. Store recognizes explicitly accepted identities additively. | Supplied valid accounts define fetch windows. Retained recognized identities filter relevance and gaps, with the existing unconfigured fallback. Omission does not remove an identity. | Recognition survives later jobs, failure, retry, restart and Study reset. Implemented. Retained-copy inspection found no missing recognized identity. |
| R10-F5 | Games UI publishes and retries each evidence read independently. | Resource replies, bounded timeouts and request generation determine read feedback. Background reads cannot clear action errors or replay mutations. | Abort stale requests and timers. Preserve successful data and immutable pending command identity. Implemented and exercised through the owning consumer. |

### Qualification and review

The [candidate manifest](manifest.json) records the exact compatible
revisions, Cargo and npm locks, release binary, and every packaged UI file.
Study wire 5 and content wire 4 retain their accepted payload shapes.
Disposable Chrome verified that the candidate served all 22 packaged files.

The assembled `cargo test --workspace --locked` run passed 285 tests and
doctests. The final test-only additions passed focused metadata and portable
contracts (five tests), Store (28 tests and three doctests), and the historical
account scenario. The opening-release selector passed 27 tests. The
architecture gate, debug and optimized builds, 36 locked UI tests on Node
24.22.3, the guarded UI build, and three Rust/UI boundary tests passed. The
final optimized rebuild reproduced the binary hash after the test-only
commits. The independent reviewer accepted all three exact runtime heads.

R10-F1 preserved actual Next ordering under rename and an unrelated tactic
edit. An issued reason survived a projection update and a subsequent eligible
selection used the new evidence. Signed equivalent PGN preserved reach. A
real route edit invalidated only its book, and old publication and bootstrap
were rejected across newer authority and dataset replacement. A deterministic
SQLite test queued explicit Analyze behind cache-only work. R10-F3 contributed
0.38 at the terminal transposition through native projection publication.
Missing raw distributions left the affected target unknown and the book
partial.

R10-F2 Chrome recovery used the archived schema-10 binary and UI. Both
accepted-lost and unaccepted Choose recovered with and without a new Game
Again. Each made one closure and one receipt with the accepted target/version.
All request bytes and accepted-lost reply bytes matched. Signed document-only
Save passed both loss modes with stable target versions. A native schema-9
fixture replayed an earlier saved Teach and Choose after upgrading. A startup
fixture damaged by the old import path repaired its miss with unchanged
Learning, assessments, failure keys, resets, and receipts. A matched Study
control verified that the recovered miss decided the tie between two equally
exposed eligible reviews. Late receipt failure rolled back the complete
choice and encounter transaction. An exact choice-set change without a
normal revision change fenced both ordinary replacement and evidence repair.

In five independent schema-10 fixtures, provenance recovery found three
provable selections, one closed unattributed selection and one conflict.
The repair examined five encounter maps, corrected three, and reported two
unresolved. The repaired cases covered a no-grade native child, an exact
legacy parent alias and a legacy failure-only closure. A second startup
repaired zero additional maps in each case. A separate schema-9 fixture
recovered one direct attribution.

R10-F4 preserved both exposure and gap counts at two after a narrower request.
Fetch windows stayed scoped to its explicit provider and learner. Real
coordinator tests covered initial filtering, additive recognition, exact
replay, conflicting command, provider failure/retry and restart. R10-F5
mounted tests covered independent publication, bounded timeout and retry,
stale response cleanup, retained action errors and exact pending bytes.
Packaged Chrome covered read-error recovery, complete and partial projection
status, opening a legal gap response, signed Preview/Save, actual modeled
selection after rename, and a lost accepted Answer followed by an interrupted
Next. Recovery replayed the original Answer bytes once, and Next Retry sent only
Next. Cache-only work caused no Maia process spawn. Explicit Analyze also
completed with a fixture worker that returned legal distributions.

### Retained-copy rehearsal

Fresh creation and retained-copy upgrades from schema 10 and schema 9 passed.
An injected migration collision rolled back both predecessor paths. Removing
the collision allowed migration to complete. Subsequent startup and restart
matched all original base columns and row counts in both directions across
28 authoritative schema-10 tables and 24 schema-9 tables. SQLite integrity
and foreign keys passed. The schema-10 copy retained 432 failure keys,
103 Games receipts and all 2,431 cached distributions. Cache-only work rebuilt
2,980 reach rows for two complete current books. The schema-9 retained copy had
no verified source associations and reported two unavailable books.

The schema-10 retained copy contained no choice closures or chosen-position
failure keys. Provenance recovered, unattributed and conflicting counts were
all zero. Encounter maps examined, repaired and unresolved were all zero.
Both identities from the sole accepted historical request were already
recognized. No identity-data repair was required.

### Publication and delivery

| Repository | Verified review head | Pull request |
| --- | --- | --- |
| Tempo | `5f622e3748ab1830af0894e02a0bae408c1c7440` | [#22](https://github.com/tempo-v2/tempo/pull/22) |
| Store | `0d3a7cc13b91013764fbf466e35a0cc5caed2d9f` | [#13](https://github.com/tempo-v2/tempo-store/pull/13) |
| UI | `90ed0057214f78fbe4eff59de67f266435eed142` | [#16](https://github.com/tempo-v2/tempo-ui/pull/16) |

The corrective candidate is implemented, tested, independently accepted and
published for coordinated review. It remains unmerged, uninstalled and
inactive. The active service still serves schema-10 checkpoint
`workspace-08812817f80797b72eaf` on port 41822. Qualification used retained and
synthetic copies. Live provider fetching and real-weight Maia inference were
outside this qualification.

The next delivery stage is coordinated merge of the compatible heads and
comparison of the merged trees with the qualified candidate. Installation
requires the managed launcher and authorized cutover, including a stopped
database backup and post-start database, listener and artifact readback.

## Schema-11 review repairs

The adversarial review held the candidate above for three reproduced
findings. The revised [candidate manifest](manifest.json) supersedes its
Tempo and Store pins and optimized binary hash. All other runtime pins,
the UI package, SQLite schema 11, portable format 5, and the public
payload shapes carry forward. The registered service still serves
schema-10 checkpoint `workspace-08812817f80797b72eaf`.

| Finding | Behavior and owner | Inputs, independence and lifetime |
| --- | --- | --- |
| R11-F1 | Store restores attribution of an accepted native choice only when retained evidence establishes one historical target/version. Tempo's existing startup reconciliation repairs the derived encounter. | The saved closure, parent position and ply, candidate target/version, exact child identity and recorded miss establish provenance across restart and upgrade. The selected-child hash may use the direct schema-9 parent, wrapped schema-10 parent, or the exact wrapper reconstructed from a schema-9 alias. Candidate order and an existing automatic grade do not select a target. Missing or conflicting proof leaves the choice closed. Learning, grades and accepted receipts carry forward. |
| R11-F2 | Tempo's single model coordinator retries a failed automatic projection up to three times, waiting 1, 2 and 4 seconds after failures. A newer cache request replaces the pending retry and explicit Analyze takes priority. | Each attempt reads current inputs and uses the existing dataset and per-book Store publication checks. A successfully published partial result settles cache-only work. Exhaustion is logged and the durable projection stays pending. Analyze can recover it when the underlying fault clears. Retries are in memory and startup schedules from current retained content. |
| R11-F3 | Tempo's projector carries exact zero through multiplication with a missing reply probability in either order. | A known zero determines the product. Missing evidence on an otherwise positive path still leaves the contribution unknown. First arrival, per-book completeness and the raw cache retain their existing meanings. The reserved schema-11 projection was qualified from fresh predecessor copies. |

### Qualification

- The review packet reproduced all three findings on the original heads,
  with all seven hostile Store controls passing. Independent rerun on the
  repaired candidate passed all ten assertions.
- The three historical writer combinations passed independently via actual
  schema-11 startup and HTTP replay: direct old/old, old/new alias, and
  direct new/new. Each synthetic schema-10 reimport removed the attributed
  miss before upgrade. Startup recovered target and answer version 1 and
  repaired exposure 1 / misses 0 to exposure 1 / misses 1. Learning,
  assessments, failure keys, retained receipt bytes and the replayed Choose
  reply matched. Repeated startup repaired zero additional maps and another
  reimport preserved the miss. Integrity and foreign keys passed.
- The optimized HTTP listener with one retained raw distribution reproduced
  a failed cache publication under SQLite contention. After unlock, GET
  observed complete 1 / pending 0 with unchanged content and no other
  trigger. A separate permanent failure stopped after four attempts, with
  the final failure logged. Repeated reads left it pending and explicit
  Analyze recovered both targets after the fault was removed. In a separate
  run, Analyze preempted the first automatic retry delay and published once.
  An SQLite audit trigger confirmed the subsequent cache wake did not
  publish again.
- The transposition published 200,000 millionths while its book stayed
  partial. The projector also passed unknown followed by zero, positive
  followed by unknown, and the existing 380,000 millionths complete case.
- The locked assembled suite passed 289 Rust tests and doctests. The
  architecture gate, three Rust/UI boundary tests and 36 UI tests passed.
  All 22 packaged UI hashes match the previously qualified artifact. The
  earlier browser and saved-command evidence remains applicable to the
  unchanged UI and wire shapes, supplemented by the historical HTTP replay.

The checks used disposable databases. Live provider fetching and inference
with real Maia weights remain outside this qualification.

### Publication and handoff

| Repository | Qualified head | Pull request |
| --- | --- | --- |
| Tempo | `061b718e11903ecba2bee4f401eed1b21931c56e` | [#22](https://github.com/tempo-v2/tempo/pull/22) |
| Store | `529efb31c2b302af7e2571a48626aeca12414e70` | [#13](https://github.com/tempo-v2/tempo-store/pull/13) |
| UI | `90ed0057214f78fbe4eff59de67f266435eed142` | [#16](https://github.com/tempo-v2/tempo-ui/pull/16) |
| Planning | This ledger and the revised candidate manifest | [#21](https://github.com/tempo-v2/.planning/pull/21) |

The independent reviewer accepted the combined heads above. The optimized binary SHA-256 is
`3ef27d814584666f77adfcccbccca40437c371a457e01412a6d752f5ccdb8945`.
The open PRs contain the qualified set. Coordinated merge and managed
installation are separate stages. At merge, compare the resulting trees
to this set. At authorized cutover, verify the running artifacts,
database and registered listener against the managed release.

## Board-first repertoire fixes

Games opens confirmed opponent gaps in a modal. The learner can play a legal
reply on the board or stage a Stockfish or Explorer suggestion, then select
**Save response**. The normal Repertoires page still provides PGN editing.

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Stage and compare replies | The approved board-first workflow gives UI ownership of hover, focus and the staged reply. Chess supplies the exact position and legal UCI identities. SAN and analysis labels affect display. The selected move changes the drafted line only when explicitly saved. |
| Append a response | Tempo revalidates dataset, repertoire and document revision. Chess builds the PGN addition. Tempo signs the existing Save payload only if Chess’s plan preserves existing answers and learning. UI delivers the signed command and manages recovery. The signed command and its receipt retain the same identity across reload and replay. Client continuation stores the gap context alongside that command. After confirmation, a failure to load the next gap allows a read-only retry. |
| Show position evidence | Maia describes the position before the opponent move. Stockfish, structural similarity and Explorer describe the position where the learner responds. Tempo queries the rated Rapid Explorer independently using the validated position and chosen rating band. No result changes legality, save eligibility or Study policy. |

### Qualified source and artifacts

| Component | Qualified commit | Pull request |
| --- | --- | --- |
| Chess | `996971b48e1ff763f2a638f75ad981488e80155c` | [#11](https://github.com/tempo-v2/tempo-chess/pull/11) |
| Tempo | `827a83067e02ce1e8c94ddf1f49072af5ccb73e7` | [#23](https://github.com/tempo-v2/tempo/pull/23) |
| UI | `8be2381cb3f256d8f00b4cf07a3abb6c1b5d3d49` | [#17](https://github.com/tempo-v2/tempo-ui/pull/17) |

Use Store `7a7b45d39697375dcb89957a6ead8b4d3417ef0b`, Queue
`b70402598c91be87687feb42932cf9d8209e3eb1`, Learning
`09c4359ab90d0cd1e5166b1f25460fd272406fd1`, Study
`73b2482dfb2ae652220727b87451fdb4a5110807`, Types
`a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core
`e9a1d160a729bc9fbbddaf16427625301cc9498a`. Use the workspace lock with
SHA-256 `c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0`
and the versioned Core 0.2.2 tarball
`4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4`.

The optimized backend SHA-256 is
`9e76796d5993d78ee4c53bb122034b7d716dfeaff7a480adc6aa868b8549a1ea`.
The packaged JS and CSS hashes after a fresh locked install are
`c15a30cef7afa5a2e5b1ef776339c2be72e76e7cab63ccf4a6e4e381d80d679e` and
`1b98748452a1f75e6ea42f51cfb1fd20ee670b806b0e1862e38b45379ae88d9b`.
This candidate inherits schema 11 and the existing Study and content wire
versions from the integration baseline.

### Verification and handoff

- All 292 locked Rust tests and doctests, all 36 UI tests, three Rust/UI
  boundary tests, the architecture gate, and the guarded UI build passed.
- On a disposable retained copy, the archived installed schema-10 pair
  served its gaps. The optimized candidate opened the same copy under
  schema 11, displayed the Scandinavian gap in SAN, and passed SQLite
  integrity and foreign-key checks.
- Packaged Chrome exercised White drag and tap, Black orientation, explicit
  underpromotion on a narrow screen, keyboard and hover arrows, automatic
  Stockfish analysis, and two consecutive saves in one repertoire. An actual
  revision change and an injected unsafe preview stopped Save. Existing
  answers and learning matched after the additions. Accepted-lost saves
  replayed byte for byte, including after reload, with one receipt per
  response. A typed stale successor error allowed a next-only retry.
- Independent review exercised the board and recovery with fixture
  transport. The real local endpoint returned the setup state without a
  token. Explorer timeout, rate limit, count rendering and stale-result
  handling passed with simulated provider replies. A live authenticated
  Explorer lookup remains unverified until a token is configured.

### Interface audit

The dependency and source-confinement gate passed for all seven Rust
packages. The packaged UI consumes Core 0.2.2 from its versioned tarball.
Core handles board input and rendering. UI handles staging, arrows, and
exact-command continuation. Chess supplies legality, canonical position, SAN,
the authored PGN addition, and the typed change plan. Tempo now enforces the
append-only rule against that plan before signing. Store commits the existing
Save and its receipt atomically. The approved gap path can restore a retired
answer when its version and learning are preserved. A different answer at
that same retired target is rejected, with no Save token issued.

The audit also traced application → Study/Chess grading and attempt
progression, Learning transitions, Queue eligibility and ordering, and Store
receipt replay through their public interfaces. Study continuation consumes
the declared activity, status and assessment. Repertoire names and SAN
remain display values. The missing-SAN case now preserves selection of an
otherwise legal suggestion. Explorer and local analysis contribute display
evidence independently of save and Study decisions.

An inherited ownership cleanup remains. The application’s repertoire-side
helper extracts side-to-move from Chess’s validated canonical FEN. Moving that
projection behind a typed Chess interface would remove the application’s
dependency on the FEN field layout. The current release reuses the same
validated inputs. This audit covered the package graph and the changed
runtime and Study handoffs.

### Merged, installed and verified on November 19, 2026

The runtime PR heads matched the qualified commits. The verified main merge
trees matched each tested source tree.

| Component | Verified main merge |
| --- | --- |
| Chess | `06fc9717b4d8abe5d0eff3b55c7a45cebfd350b2` |
| Tempo | `61f590a013eb868446a7b10f8edad42508bd5532` |
| UI | `1e8d668ac2dd15aaca4fb793fd1e731f86b35c5b` |

The supported Mac lifecycle installed `workspace-3876ee307c2769bbcf01` on
port 41822 after proving all 34 tables matched on a disposable rehearsal.
The stopped-time backup and prior registration are in
`.local/usable-release/recovery-start-etqol4ik`. The registered process
served the tested optimized binary and all 22 UI files. SQLite stayed at
schema 11 with the same dataset and file inode. Integrity and foreign-key
checks passed.

On a separate disposable copy of the existing dataset, Chrome opened the
real Italian `1…d5` gap, staged `exd5`, and accepted the signed Save exactly
once. The original 20,639 learning rows, 148 attempts, 114 assessments,
308 Study receipts and two reset records matched afterward. On the live
service Chrome opened the same modal, observed Stockfish and the hover
arrow, staged and cleared `exd5`, then closed the modal. The verifier
intercepted Study startup and blocked live mutation requests. After the
browser check all rows across all 34 live tables matched the stopped-time
backup in both directions.

## Exercise-first Study and source game replay

Study leads with the exercise and places Today below the card. A guided
repertoire correction can show the move played in the source game and replay
its legal mainline through that deviation. It remains outside the new opening
allowance.

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Authorize correction context | Tempo serves the read only for the active guided repair in the requested dataset. Store matches the issued target, answer version, miss revision and acceptance time against the reset boundary. The saved failure and exact choice or unambiguous retained observation determine the source across restart. Chess verifies the issued canonical position and the actual move before projecting SAN and FEN. Missing or ambiguous evidence leaves the guided lesson available. |
| Display and browse the game | The UI uses the ready Repair flag and verified context for presentation. Exercise names are display text. The replay index and guided board preview are local to the issued view, and browsing emits no Study command. Returning restores the current exercise and a reproduced unsaved move. |
| Show daily progress | The card explains the existing Learning and Queue rule. Today displays the server's existing daily projection. Study wire 5, SQLite 11 and portable format 5 carry forward. |

### Compatible source and evidence

| Component | Source commit | Pull request |
| --- | --- | --- |
| tempo | `94f1028fbc82ba6accfbecd9d621758e8a6b6d72` | [#24](https://github.com/tempo-v2/tempo/pull/24) |
| tempo-chess | `77f7c7b88f9925b7f418d4c79e08a582f5bd9734` | [#12](https://github.com/tempo-v2/tempo-chess/pull/12) |
| tempo-store | `04e215b7a6bbd95ac06a4ecd606d291d290e528f` | [#14](https://github.com/tempo-v2/tempo-store/pull/14) |
| tempo-ui | `b6f42e41808246626c6e37cedec379f61060945b` | [#18](https://github.com/tempo-v2/tempo-ui/pull/18) |
| tempo-core-components | `e9a1d160a729bc9fbbddaf16427625301cc9498a` | Integration baseline |
| tempo-learning | `09c4359ab90d0cd1e5166b1f25460fd272406fd1` | Integration baseline |
| tempo-queue | `b70402598c91be87687feb42932cf9d8209e3eb1` | Integration baseline |
| tempo-study | `73b2482dfb2ae652220727b87451fdb4a5110807` | Integration baseline |
| tempo-types | `a8e46c9b9442f1180ec33b8035cef1c713414b66` | Integration baseline |

The locked assembled build used the existing split workspace layout and the
bundled Core 0.2.2 npm package. Candidate artifacts and locks have these
SHA-256 values.

| Artifact | SHA-256 |
| --- | --- |
| Workspace Cargo lock | `c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0` |
| UI npm lock | `1fe3dd71e3ff0699dc38d102fbc03e8fd742b5a7742d8b42bbf626343d2d1ebb` |
| Bundled Core package | `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4` |
| Development Tempo executable | `225de0fa30a56de04b31888234100069c372737a917e3837579838abbe119b1f` |
| Packaged UI JavaScript | `9bcc998174ae0d86dc7c76d009814ef9df96a9779eeefeef84641a174f9b7db8` |
| Packaged UI CSS | `f40d6d8e9d06d5057d463ea0d3de4435e1cf60a9c6dccb0aec7715ab5aad6b3b` |

The locked workspace suite passed 292 Rust tests and doctests. The locked UI
install, build and 36 tests passed, along with three Rust/UI boundary checks.
The SQLite contracts cover a newer miss while the old repair is open, restart,
an explicit choice, an ambiguous repeated position, missing source after
portable restore, a reset, and a blind recall. A disposable copy of the
installed dataset verified an active correction's exact prefix and original
provider link.

Independent review accepted the combined feature. Packaged Chrome exercised
desktop and narrow layouts, exact replay and the keyboard controls, returning
with a reproduced unsaved move, and navigation without Study commands or
durable writes. It recovered a lost accepted acknowledgement with identical
bytes, followed by a failed Next and a Next-only retry. Present, renamed and
omitted exercise names across cloned baselines produced identical commands,
accepted replies and durable Learning, assessment, receipt and failure rows.

The initial candidate was published for coordinated review.

### Combined Study replay installation and interface audit

The Study replay PRs were merged on November 19 after the board-first changes
landed. GitHub main trees matched the qualified assembly in each repository.
The UI merge keeps the exercise-first layout and the earlier move labels.

| Component | Verified main commit | Pull request |
| --- | --- | --- |
| tempo-chess | `a8c24fad8aec9645fa006d68fa6dcdf4ddac16ad` | [#12](https://github.com/tempo-v2/tempo-chess/pull/12) |
| tempo-store | `461c7c10370386e119a9d4dbb7734a4449ecad0b` | [#14](https://github.com/tempo-v2/tempo-store/pull/14) |
| tempo | `41ea8dcf4324b547e719f130bea343b21c1674b0` | [#24](https://github.com/tempo-v2/tempo/pull/24) |
| tempo-ui | `ce146692e1479937c2f57e8a9a4535d47dfdb367` | [#18](https://github.com/tempo-v2/tempo-ui/pull/18) |

The combined release passed 295 locked Rust tests and doctests, 36 UI tests,
three Rust/UI boundary checks, the dependency gate and its four self-tests.
The managed build reproduced the qualified executable and all
22 packaged UI files. Packaged Chrome exercised the
correction and its recovery at desktop and narrow widths. Three cloned
baselines with present, renamed and omitted exercise labels produced the
same requests, receipts, assessments and Learning.

The managed service serves `workspace-307fc8e77c3135e6e5e4` on port
41822. Chrome resumed the active correction **by read** on a
retained copy and on the installed service. It confirmed the nine-ply replay,
original-game link, start/deviation navigation and return to the exercise.
After the cutover and live check all 34 SQLite tables matched the
stopped-time backup row for row, including 20,639 learning
records, 148 attempts, 114 assessments and
308 Study receipts. The dataset, database inode and schema 11
matched. SQLite integrity and foreign-key checks passed. Recovery is in
`recovery-start-t4oe1vao` beside the installation. The optimized
binary SHA-256 is `b80d2b39e6845279da223a9aa9a8fb5ad7dfee7b2faec59528b93786eaadd5ee`.

The dependency audit covered all seven Rust packages and the packaged Core
consumer. Study owns attempt progression, Learning owns schedule and credit,
Queue owns selection, and Store owns SQLite transactions and receipts. The
release audit traced the actual replay consumer across the HTTP boundary.
Tempo gates the read on the active issued repair, Store resolves its durable
provenance, Chess verifies and projects the legal mainline, and UI/Core hold
the replay index and display the supplied positions. Replay emits no Study
write. The signed repertoire preview remains an application decision and
recovery resends the original command.

The audit identified inherited ownership debt. Tempo derives learner color
by reading the side-to-move field of a validated FEN, and Study UI can format
fallback SAN for a server-disclosed move. A Chess-owned projection would keep
those chess representations authoritative in one component. A second issue
is the tactical metadata boundary. Daily Study derives personal capture
priority from a reserved provenance string and tactic selection decodes
legacy pack metadata from the same generic provenance field. Those inputs
should enter selection as explicit domain facts. No selection, grading or
persistence policy was changed to address these findings in this cutover.

## Repertoire-aware default in Fix response

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Reuse nearby replies | The approved authoring preference tries the current repertoire before other active same-side repertoires. In each, distinct supporting positions determine frequency and closest support breaks ties. Chess owns canonical structure, saved moves and whether the same piece can play the same legal move at the gap. Labels and SAN are display values. |
| Compare against Stockfish | Tempo tries the ranked replies until it finds a comparable move within 50 centipawns. A best comparable repertoire reply 51–150 centipawns behind leaves the selection blank. Stockfish needs all eligible comparisons to exceed 150. Missing or mate scores cannot justify that fallback. The identical top move is a zero difference for any score type. |
| Stage a default | A matching analysis request and content revision can fill an untouched modal. UI owns manual input, clearing, arrows, focus and exact-command recovery. An automatic selection changes no durable state. Explicit Save uses the existing signed preview and Store receipt. |

The similarity panel shows support counts and expandable board examples next
to Stockfish. Explorer shows its game counts and outcomes on a full-width
row below the pair. Narrow screens stack the panels beneath the board.
Tempo looks at eight distinct positions per group and compares up to sixteen
distinct repertoire responses in a bounded same-depth Stockfish search.
If that budget leaves responses unscored, the selection can stay blank.
The existing top-three neighbor projection remains available to older pages.

| Component | Qualified commit | Pull request |
| --- | --- | --- |
| Chess | `c6da613f37e0ae11e7abf25167b01f9a45ba3065` | [#13](https://github.com/tempo-v2/tempo-chess/pull/13) |
| Tempo | `966f0982b53f59de2bd8c604014809e1e77d1d9a` | [#26](https://github.com/tempo-v2/tempo/pull/26) |
| UI | `47fa621e7cb04b7cb14cef38a44ac7e76707bdaf` | [#20](https://github.com/tempo-v2/tempo-ui/pull/20) |

The combined candidate starts at the installed Study replay source. Reuse
Store `461c7c10370386e119a9d4dbb7734a4449ecad0b`, Queue
`b70402598c91be87687feb42932cf9d8209e3eb1`, Learning
`09c4359ab90d0cd1e5166b1f25460fd272406fd1`, Study
`73b2482dfb2ae652220727b87451fdb4a5110807`, Types
`a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core
`e9a1d160a729bc9fbbddaf16427625301cc9498a`. Use workspace lock SHA-256
`c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0`
and the packaged Core 0.2.2 tarball
`4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4`.
SQLite schema 11 and the existing Study and repertoire Save contracts carry
forward.

The optimized backend SHA-256 is
`3b1e5b564cf391ef0327ba3aa38057031a708bee147428d25824b63696454ed6`.
The packaged JS and CSS hashes are
`dae72ededfcda99f758a31729c36b46f0c20cb865179910958f4914d49c73a77` and
`c2584eb9c9e1da000328dc635ed4a20cd31164af4c6b3bb7c572851124d2306d`.

The combined build passed 298 locked Rust tests and doctests, 36 UI tests,
three Rust/UI boundary tests, and the architecture gate. Independent review
verified the owner boundaries, same-depth Stockfish comparison including
replies outside the unrestricted top three, and the actual packaged board
consumer. In Chrome the synthetic transport exercised both layouts, arrows,
manual override during a held drag, clearing, stale analysis, and exact
Save replay after reload. The underlying disposable database preserved
existing learning and accepted one save.

The production endpoint on a disposable copy of the retained dataset
recommended `exd5` against the Italian `1…d5` gap. The move appeared once
among the current repertoire neighbors and tied Stockfish. Analysis left
all checked durable rows identical. An explicit signed save added one
receipt and preserved all 20,639 existing learning rows, 148 attempts,
114 assessments, and existing Study receipts in that copy.

The runtime PR heads were verified against main. Merge and managed
installation are separate delivery stages.

### Merged, installed and verified on November 19, 2026

The merged runtime trees matched the independently reviewed and qualified
candidate.

| Component | Verified main merge |
| --- | --- |
| Chess | `52ae0ee6d8ad0fd367ec1e6f84202f024981d054` |
| Tempo | `a1117eb23c9a417e36d80a4cfd00f1840fc05bfd` |
| UI | `92350d27d0317cfa78057034b4bb51a28fa46438` |

A read-only Chrome check on a disposable copy of the earlier retained dataset
opened the Italian `1…d5` gap and displayed **Suggested exd5** with its green
arrow. One nearby position in the current repertoire supported the move,
which tied Stockfish. Similar positions appeared to the left of Stockfish,
with Explorer across the row below. All three stacked under the board at
the narrow viewport. The copy matched its baseline across all 34 tables.

The current live repertoire already had `1.e4 d5 2.exd5` saved. Its
Scandinavian position was therefore absent from the gap list. On the
current-data rehearsal and live service, Chrome checked both layouts on
the remaining Italian `7…Qd7` gap. It displayed **Suggested Bxb5** with two
nearby positions supporting it and a zero-centipawn difference. The live
document still contained the saved Scandinavian move. Both browser checks
used a read-only Study startup and issued zero saves.

The managed launch agent installed `workspace-ba11fdade1d61e762d39` on
port 41822. The registered listener served the qualified binary and all 22
UI files. The database kept its inode, dataset identity and schema 11.
After the live check, all 34 tables matched the stopped-time backup row for
row, including 20,720 learning records, 174 attempts, 114 assessments and
334 Study receipts. Integrity and foreign keys passed. The stopped-time
backup and prior registration are in
`.local/usable-release/recovery-start-37czkteg`.

## Chess projections, explicit tactic inputs, and the deviation arrow

| Behavior | Authority, inputs, independence, and lifetime |
| --- | --- |
| Display learner color and SAN | Chess projects learner color from the solver start. It formats only the move that the issued lesson or already-disclosed correction permits. The pinned definition determines the result across restart and receipt replay. Labels are independent of identity, grading, and scheduling. |
| Select tactics | Queue receives the existing capture-priority timestamp. Tempo derives it from the typed personal-capture origin and its unreviewed introduction. Pack ordering takes typed theme, difficulty, ordinal, position, and admission facts. The compatibility adapter alone interprets the reserved catalog encoding. It decodes packs only when the policy needs them. Ordinary attribution and display names are independent. Existing catalog records, learning and ordering rules carry forward. |
| Display the game deviation | UI draws the exact verified game move in red and the issued repertoire move in blue at the live correction. The replay cursor and pending guided move have their own board state. Browsing never submits a grade. Supplemental fields use an HTTP display opt-in. The prior strict v5 HTTP and stdio shapes and immutable commands remain readable. |

### Verification and managed installation

| Component | Verified main commit | Pull request |
| --- | --- | --- |
| tempo-chess | `10701e28ae259de46b04a1a62ba914a46bc012d2` | [#14](https://github.com/tempo-v2/tempo-chess/pull/14) |
| tempo | `c6d47cb463b83dedff0f96cd087def8b42f2fdf9` | [#27](https://github.com/tempo-v2/tempo/pull/27) |
| tempo-ui | `377b09c9b48213d326c99a0aeb8398b85246aa37` | [#21](https://github.com/tempo-v2/tempo-ui/pull/21) |
| tempo-store | `461c7c10370386e119a9d4dbb7734a4449ecad0b` | Integration baseline |
| tempo-learning | `09c4359ab90d0cd1e5166b1f25460fd272406fd1` | Integration baseline |
| tempo-queue | `b70402598c91be87687feb42932cf9d8209e3eb1` | Integration baseline |
| tempo-study | `73b2482dfb2ae652220727b87451fdb4a5110807` | Integration baseline |
| tempo-types | `a8e46c9b9442f1180ec33b8035cef1c713414b66` | Integration baseline |
| tempo-core-components | `e9a1d160a729bc9fbbddaf16427625301cc9498a` | Integration baseline |

The merged runtime trees matched the qualified build, including the repertoire
recommendation release that landed during verification. The locked suite passed
299 Rust tests and doctests, 36 UI tests, three Rust/UI boundary checks, and the
dependency gate. Core 0.2.2 was consumed through its locked npm tarball.
The recommendation browser check passed its layout, override, and signed Save
recovery scenarios. Independent packaged Chrome exercised both arrows, replay and guided-state
restoration on desktop and narrow layouts. It recovered accepted-lost and
unaccepted wrong-answer commands from the previous installed recommendation release with both
the previous and current UI. Original command bytes and identities matched and
each accepted command had one assessment and receipt. No Study wire version,
SQLite schema, portable format, or learning rows required a migration.

The installed checkpoint is `workspace-8467c4c7540fb7b6f55e` on port
41822. Chrome resumed the existing active repair by read, verified
both arrows and the original-game link, replayed the game and returned to the
exercise. After the live check all 34 SQLite tables matched the
stopped-time backup row for row, including 20,724 learning
records. The database inode, dataset and schema 11 matched. Integrity and
foreign-key checks passed. The registered listener served all
22 verified UI files. The backup is
`recovery-start-opl3ya1b`. The optimized binary SHA-256 is
`58ea1e9904ad897606ad5be9345a943caaee69a6a089ebc0e9a39c04540de095`.

## Repertoire correction context and pending count

| Behavior | Basis, owner, and inputs | Independence and lifetime |
| --- | --- | --- |
| Show the numbered SAN before the correction decision. | Study request for the daily release. Chess already projects the verified mainline through the issued deviation. UI shows the prefix during the live correction and uses the full line during replay. | The prefix ends before the played deviation. A first-move decision or unavailable source omits it. Replay and the displayed SAN do not submit commands or change Learning. |
| Count all pending guided repairs, including the current card and skipped repairs. | Study request and explicit choice to count all pending corrections. Queue projects the size of its Repair set before applying session deferrals. Tempo reads active current-version Learning facts and publishes the count via `/api/study-progress`. | Labels and the availability of replay evidence do not determine membership. An accepted repair moves the obligation into recall. The UI refreshes after confirmed Study transitions and uses the progress stamp for periodic reads. Study wire 5, SQLite schema 11 and the saved receipt formats carry forward. |

### Qualified source set

| Component | Verified PR head |
| --- | --- |
| Queue | `36c712ab15c36ac6e609d6497952c75b3aeddd55` [#9](https://github.com/tempo-v2/tempo-queue/pull/9) |
| Tempo | `75834a5ef5f144d001ee60c074072d6ca49114a6` [#29](https://github.com/tempo-v2/tempo/pull/29) |
| UI | `2f035ce0660add5af09274cdd8cd71b22d9717e2` [#22](https://github.com/tempo-v2/tempo-ui/pull/22) |

The combined candidate uses the other six component pins from the installed
`workspace-8467c4c7540fb7b6f55e` table above. Its workspace Cargo lock is
`c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0`
and UI npm lock is
`1fe3dd71e3ff0699dc38d102fbc03e8fd742b5a7742d8b42bbf626343d2d1ebb`.
The UI consumed the locked Core 0.2.2 tarball.

The locked workspace passed 300 Rust tests and doctests, 36 UI tests,
five Rust/UI application integration checks, and the architecture gate
with its four self-tests. The new SQLite regression checks skip, save,
exact receipt replay, recall eligibility and content replacement. The
packaged Chrome check uses a disposable server and database. It verifies
the SAN prefix on desktop and at 390px, replay and return, the count
before Save and after a saved repair with interrupted Next, one receipt
and zero additional assessments, and fallback rendering with a first-move
decision, unavailable game context and a progress response without the count.

The standalone UI import scanner reports the same JSX false positive in
`GamesPage.jsx` on untouched main and the candidate. Changed Rust files
pass formatting. Workspace-wide formatting reports existing differences
in Tempo and Chess module declarations.

### Managed installation

| Component | Verified main merge | PR |
| --- | --- | --- |
| tempo-queue | `a171e70faf684dead33f04ad455012380fcb2e54` | [#9](https://github.com/tempo-v2/tempo-queue/pull/9) |
| tempo | `df06acb9aab5d16b7f642089101e5e0c277ef8fd` | [#29](https://github.com/tempo-v2/tempo/pull/29) |
| tempo-ui | `ea729f5d0f2499ce36fc3ab49aca256b400d7fd7` | [#22](https://github.com/tempo-v2/tempo-ui/pull/22) |

Each merged runtime tree matched its reviewed PR head. The six companion
pins still matched their remote main branches. The optimized binary and
locked UI passed the packaged Chrome correction check on disposable data.
The five focused Rust correction contracts and five application integration
checks passed again. The broader suite evidence above applies to the same
runtime trees.

The managed launcher rehearsed the candidate on a disposable copy, created
a stopped-service backup in `recovery-start-wctlsa51`, and installed
`workspace-63a0f28a9bbb29b9ae89` on port 41822.
The registered service ran the qualified binary and served all
22 matching UI files. The binary SHA-256 is
`c7e798e1d4a6489c46fe3777fad06f0330867f1f32f71d290088e6c1c576bad8`.

The live read-only Chrome check resumed the retained active correction,
matched the displayed SAN prefix to its source, and verified the heading
with 98 repairs remaining. The same database file, dataset,
active attempt and schema 11 were observed after restart.
All 34 tables matched the stopped-service backup
row for row, including 20,777 Learning records,
226 attempts, 114 assessments and
386 Study receipts. SQLite integrity and foreign-key
checks passed.

## Shared analysis board and marked-line authoring, November 19

The candidate starts from the compact-correction installation `workspace-6d37b569cfafffdcc9d1`. The table records the initial coordinated review heads. The final merge commits and installation checks follow below.

| Component | Head | Pull request |
| --- | --- | --- |
| Tempo | `e2322515433f7256f5306f76c031a8fa993b29c3` | [#30](https://github.com/tempo-v2/tempo/pull/30) |
| UI | `5d535f58eeeb59ca3a46cfcb7fd590e35732a472` | [#24](https://github.com/tempo-v2/tempo-ui/pull/24) |
| Chess | `98c557ab85bdc4edf130f829530889f1bc0e02b4` | [#15](https://github.com/tempo-v2/tempo-chess/pull/15) |
| Study | `addc9a1fcba2460858e525865fb554e4003891d0` | [#2](https://github.com/tempo-v2/tempo-study/pull/2) |

Use Store `461c7c10370386e119a9d4dbb7734a4449ecad0b`, Queue `a171e70faf684dead33f04ad455012380fcb2e54`, Learning `09c4359ab90d0cd1e5166b1f25460fd272406fd1`, Types `a8e46c9b9442f1180ec33b8035cef1c713414b66` and packaged Core 0.2.2 from `e9a1d160a729bc9fbbddaf16427625301cc9498a`. The candidate reuses the installed workspace lock and schema 11.

| Decision | Owner, input and effect |
| --- | --- |
| Open the issued decision | Tempo resolves dataset, attempt, revision and issued content version. Confirmation on an unfinished scheduled Test applies Study's terminal concession with at most one human Again. Learning and Store handle the normal transition and atomic receipt. Guided visits retain the issued attempt. Practice assistance preserves scheduling. The UI recovers the immutable command separately from reading the analysis position or requesting Next. |
| Compare a position | Each source receives a Chess-validated position. Stockfish uses a bounded common-depth search for the pinned moves. Each Explorer population has its own counts. Maia supplies the side-to-move distribution. Selected repertoire, learner side and content revision scope the saved-move comparison. Source results, labels and arrow preferences have no grading or authoring authority. |
| Author marked lines | The UI submits the explicitly marked paths. Chess verifies the anchor and legal moves against the current source, checks one learner answer per position and previews replacements across transpositions. The application signs the reviewed document. Store applies the existing receipt-bound Save. Unmarked branches are exploratory. |

The combined candidate passed 305 Rust tests and doctests, 39 UI tests and the dependency-direction check. Chrome verified creating a repertoire with two marked branches, excluding an unmarked move, returning to a pin, comparing a fourth engine candidate, source failure isolation, and rejecting a late result. The Fix Response journey covered its recommendation, manual override, stale results and signed Save recovery.

Chrome on disposable retained copies verified guided return, cancel before disclosure, one accepted Again, reload, and Next for original, changed and omitted display names. Previous installed clients produced accepted-lost and unaccepted Answer, Show Move and signed repertoire Save commands. The candidate replayed the original identities with one durable effect. A separate database check covered an attempt with an earlier miss and an edit that changed the issued answer.

All five real evidence sources returned results for the London position on a disposable retained copy. In one optimized run the repertoire comparison took about two seconds cold and 19 ms on the next ply. Strict workspace Clippy still flags existing Store warnings. Those checks used disposable data. Whole-repertoire first-gap probability remains a later feature.

### Coordinated review and merge

The UI now binds confirmation to the displayed dataset, attempt, content version and revision. Returning from analysis resumes the addressed open activity or requests Next when it has ended. Fix Response retains the selected move across an exploratory visit. The analysis table opens the supporting boards for a particular move and shows the size of each Explorer population.

Chess verifies a supplied starting move order against a contiguous authored route, including the observed opponent departure permitted by Fix Response. Tempo checks that the signed Save fits the HTTP transport before returning a successful preview. A rejected replacement preview clears its previous Save button.

The final candidate passed 307 Rust tests and doctests, 41 UI tests, and the architecture gate. Packaged Chrome covered staged response retention, a stale preview followed by refresh and Save, cancel and confirmed Again, cross-window return, and independently delayed evidence. The five real providers returned evidence for the London decision on disposable data. Strict workspace Clippy has the existing Store findings described above.

| Repository | Qualified head | Verified main merge |
| --- | --- | --- |
| [tempo-study #2](https://github.com/tempo-v2/tempo-study/pull/2) | `addc9a1fcba2460858e525865fb554e4003891d0` | `4b46e6c45a6330177b089eadcae69821e57b6657` |
| [tempo-chess #15](https://github.com/tempo-v2/tempo-chess/pull/15) | `78c51850495ac9ef587d240e17c26cd13f4761d2` | `531cadaea8c89de230d3516d31d95582dc7263dd` |
| [tempo #30](https://github.com/tempo-v2/tempo/pull/30) | `9a43767c4ed47851f2d263ae3b679c37548bc4c8` | `70850707200c856b089820b32e0baabdff3a21a7` |
| [tempo-ui #24](https://github.com/tempo-v2/tempo-ui/pull/24) | `1e293784106ac219959acfd590e42cc2a30fcc34` | `3bf2278469d846007243761dc96be9e17cde2117` |

### Managed installation and live acceptance

The merged trees matched the reviewed runtime heads. The managed launcher rehearsed the release on a disposable backup, stopped the prior service, backed up its database and registration, and installed checkpoint `workspace-7ed579a4d29162fc4fdc` on port 41822. The binary SHA-256 was `79176f94d5df5d728c57df8127e0eabab654a1c27187bb0ba0f31df5a40b8dc3`. All 22 served UI files matched the qualified build.

Chrome resumed the existing London System guided correction, opened **Analyze** using the live Study button, matched the analysis board to the exact issued position, and returned to the same active correction. The live check used the read-only Resume operation on entry and return. The card displayed 89 repairs remaining. The installed repertoire list reported London System with 1,201 positions and Italian with 1,923.

After the browser journey all 34 database tables matched the stopped-service backup `recovery-start-b8d4qxqe` row for row. The same database file, dataset, active attempt and schema 11 were retained. Counts included two repertoire documents, 20,783 learning records, 235 attempts, 114 assessments and 395 Study receipts. SQLite integrity and foreign-key checks passed on both copies.

## Post-install Games recovery repairs

PI-F1–PI-F3 use the schema-11 review packet as historical reproduction
evidence. The follow-up starts from the combined Study replay main trees
above. Store selection excludes partial headers, historical Retry gates
durable replay on current-job state, and selected Games callers own read
deadlines. Independent source review also found that publishing a retained
job acknowledgement as current status would displace a newer job in Games.
Import, Reprocess and Choose already check stored command identity before
repeating effects. Ordinary Refresh retains its separate single-status-slot
delivery contract.

| Flow | Authority, identity and lifetime | Recovery boundary and proof |
| --- | --- | --- |
| Model | Tempo originates cache-refresh or explicit Analyze intent. Store retains raw distributions by raw model and position. Reach is derived under dataset, verified book input, projection algorithm and target versions. Raw evidence survives restart for matching positions. | Raw distributions commit individually before guarded projection publication. A partial header can survive alongside newer durable evidence. The worker restores progress on the existing startup/content trigger. Incomplete cache can settle successfully, while operational errors consume the bounded retry budget. Zero, unknown and known positive reach keep their existing meanings. |
| Historical commands | Tempo validates active dataset and immutable command identity. The saved job retains accepted Retry IDs under dataset and job across replacement and restart. The current-job pointer governs new work admission. | The retry ID and incremented window attempts commit together before execution. A validated acknowledgement for the original job clears the UI envelope. The saved view may evolve. The status read owns publication of the current job. |
| Games reads | The six named UI adapters own deadlines through response-body consumption. The page, dataset and gap offset govern publication. Catalog and paginated gaps are reads even when transported as POST. | Deadline expiry exposes a recoverable resource error. Owner cancellation suppresses obsolete publication. The page owns polling and reload. The separate exact-command path resolves uncertain mutation acceptance. |

The browser can retain a partial model snapshot until its next read.
Automatic cache work has no separate public activity signal. Recovery is
verified through the normal status endpoint without changing the meaning of
projection completeness.

### Compatible candidate

| Component | Exact commit | Follow-up |
| --- | --- | --- |
| Tempo | `e6443a7372178e3e00292567d9d4f400f9a3e7d2` | [#25](https://github.com/tempo-v2/tempo/pull/25) |
| Store | `4027bb41cf14425bcbb5f1e8c7467999b0c40a52` | [#15](https://github.com/tempo-v2/tempo-store/pull/15) |
| UI | `c039f829624f7f19bc79dfad24e35cc7f20b77c9` | [#19](https://github.com/tempo-v2/tempo-ui/pull/19) |

The other build inputs are Chess `a8c24fad8aec9645fa006d68fa6dcdf4ddac16ad`,
Queue `b70402598c91be87687feb42932cf9d8209e3eb1`, Learning
`09c4359ab90d0cd1e5166b1f25460fd272406fd1`, Study
`73b2482dfb2ae652220727b87451fdb4a5110807`, Types
`a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core
`e9a1d160a729bc9fbbddaf16427625301cc9498a`. The assembled set uses
SQLite schema 11, portable format 5, Study wire 5, and unchanged Games
and content reply shapes. Qualification used Rust 1.98.1 and Node 26.12.0.

| Artifact | SHA-256 |
| --- | --- |
| Workspace Cargo lock | `c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0` |
| UI npm lock | `1fe3dd71e3ff0699dc38d102fbc03e8fd742b5a7742d8b42bbf626343d2d1ebb` |
| Bundled Core 0.2.2 package | `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4` |
| Optimized executable | `0ae630f423245caf314823ffa59676a0e4e0b71620ce80876a0b291c82416adc` |

<details>
<summary>SHA-256 values of all 22 packaged UI files</summary>

```text
bcd62afaf82ff483a5bd4f065ccbbea0a1f3619cbbce18efc7d0e9886af4e2de  assets/app.css
a1db424c8ff70be144862ea018980c347b30127a595b22304e20537f44251c5e  assets/app.js
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

</details>

### Before and after

The acceptance packet was checked against its supplied SHA-256 list.
On untouched integration heads it returned exit 1 with all four expected
assertions across three finding groups. The ten prior assertions and three
additional Store controls passed. The same packet with `--include-prior`
returned exit 0 on the combined candidate, with all findings and controls
passing.

| Finding | Integration baseline | Qualified candidate |
| --- | --- | --- |
| PI-F1 | Interrupted Analyze left two partial projections and no known reach for A on startup without inference. | Cache-only startup reached one complete and one partial projection with A's retained 50,000-millionths reach before any manual trigger. Content and raw inputs matched. An optimized worker test recovered a transient failure, exhausted a permanent failure after four attempts, and gave Analyze priority during backoff. Tests also passed the stale and downgrade fences, transposition, and zero/unknown controls. |
| PI-F2 | Retry A had one durable acceptance and failed replay while B was current, including after SQLite reopen. | Real SQLite checks acknowledged A while current, while B was processing, after B settled, and after reopen. The suite rejected unseen old-job retries and scope mismatches. Packaged Chrome delivered a byte-identical lost-response Retry from the previous installed UI and cleared the envelope with B still visible and the stored jobs unchanged. A separate previous-browser envelope that had failed before delivery was accepted on a disposable database copy exactly once. |
| PI-F3 | Both mounted history and catalog reads remained loading after the transport recovered. | Mounted tests recovered all six scoped reads, including a stalled body, a nonzero gap offset, and a deliberately late transport. Read recovery preserved pending bytes and unrelated action errors. Packaged Chrome displayed a history timeout and recovered the history without a mutation before the explicit Retry. |

The locked workspace passed 296 Rust tests and doctests, 43 UI tests
including 14 mounted Games cases, and three Rust/UI application boundary
tests. The architecture gate and its four self-tests passed. The independent
reviewer exercised both affected backend paths, the mounted Games cases,
and worker failure and priority on the optimized binary. With both the
provider and Maia unavailable, the disposable HTTP Study check issued a
normal activity, accepted and replayed one answer, then issued a different
activity. It saved one human assessment, one receipt, and one review.

On a disposable copy of the previous schema-11 backup, optimized startup
and read-only Games requests preserved every row in all 34 tables,
including 20,639 Learning rows, 148 attempts, 114 assessments, and 308
Study receipts. SQLite integrity and foreign keys passed. All 22 assets
served by the candidate matched the guarded UI build. Provider failures and
inference interruption used deterministic fixtures. Live providers and
real Maia weights were outside these checks.

The compatible source set is qualified and published for coordinated review.
The deployed Study replay release remains the installed version. Candidate
merge and managed cutover are separate authorized operations.

### Historical freshness and dataset follow-up

| Behavior | Basis and owner | Inputs and independence | Lifetime |
| --- | --- | --- | --- |
| Refresh Games history when authoritative historical status first reveals settled work or reveals new progress since the previous settlement. | CR-F1. Tempo publishes persisted job and window progress. The Games page owns history invalidation and bounded reads. Complete and incomplete jobs can have applied batches. A paused job can also have committed earlier batches. | Active dataset, current job, settlement state, ordered window identities, attempts and outcomes, and an observed transition out of running. Notes and error text are presentation data. | Page-local observation. Invalidation supersedes older history reads immediately. Only an owned, successful history response replaces displayed rows. Errors retain the read retry. |
| Refresh Games history once after a validated local Retry and a matching authoritative settlement, including an identical paused view. | CR-F3. The Games page owns freshness. Tempo owns current job status and validates command acceptance. | Dataset and job from the accepted Retry, plus an owned status GET for the same dataset and job in complete, incomplete or paused state. Acknowledgement A cannot establish status or execution for B. | Page-local until matching settlement, dataset replacement, a newer eligible local Retry acknowledgement, or unmount. Failed, timed-out, cancelled and foreign status reads leave the fact available. |
| Scope historical command acceptance and current status to the active dataset. | CR-F2 and the historical commands contract above. Tempo owns active dataset, retained command checks and current-job reconciliation. Games owns read publication for the dataset established by its catalog. | Active dataset, immutable command identity and normalized input, retained job, and outstanding provider reply ownership. Retained acknowledgement and current status may name different jobs. Identity-free idle remains valid. | Retained acceptance survives within its dataset. Coordinator work from a prior dataset is discarded in memory, with outstanding provider replies drained before starting another window. |

#### Reconciled corrective candidate

The original corrective PRs remain the integration path. Their heads now
include the newer Study interface and repertoire recommendation releases on
main. The merge bases for the new runtime assembly include Tempo
`c6d47cb463b83dedff0f96cd087def8b42f2fdf9` and UI
`377b09c9b48213d326c99a0aeb8398b85246aa37`. Planning includes main
`6d4d0366c100f3dee12d26cbddd525ad3d1a3617`.

| Component | Qualified commit | Review |
| --- | --- | --- |
| Tempo | `dd2a5e5e2dec81cda666775abc77cb77425ce1e4` | [#25](https://github.com/tempo-v2/tempo/pull/25) |
| UI | `2fd11a8860ee0a5664aae85f85adea861005c3d3` | [#19](https://github.com/tempo-v2/tempo-ui/pull/19) |
| Store | `4027bb41cf14425bcbb5f1e8c7467999b0c40a52` | [#15](https://github.com/tempo-v2/tempo-store/pull/15) |
| Chess | `10701e28ae259de46b04a1a62ba914a46bc012d2` | [Integrated #14](https://github.com/tempo-v2/tempo-chess/pull/14) |
| Learning | `09c4359ab90d0cd1e5166b1f25460fd272406fd1` | Existing dependency |
| Queue | `b70402598c91be87687feb42932cf9d8209e3eb1` | Existing dependency |
| Study | `73b2482dfb2ae652220727b87451fdb4a5110807` | Existing dependency |
| Types | `a8e46c9b9442f1180ec33b8035cef1c713414b66` | Existing dependency |
| Core | `e9a1d160a729bc9fbbddaf16427625301cc9498a` | Existing Core 0.2.2 package |

CR-F1 refreshes history after a first or newer historical settlement and
cancels any earlier in-flight history read. The exact acknowledgement
resolves A independently of current job B. A newer window attempt can
trigger a refresh under the same job ID. CR-F2 fences commands and status
to the active dataset and preserves outstanding-provider reply isolation.
CR-F3 also refreshes after a same-tab Retry whose job resumes and pauses
between GETs with the same status bytes. The acknowledgement supplies
freshness once for its own dataset and job.

The [verification record](historical-follow-up-evidence.md) contains
before/after observations, commands, artifact digests, and the qualification
limits. The CR-F3 run passed 58 UI tests, 56 supplied consumer probes,
three Rust/UI boundary tests, and the architecture gate with four self-tests.
Packaged Chrome verified same-tab freshness, prior-release Retry recovery,
and all 22 HTTP-served UI files.
The unchanged backend assembly retains the prior evidence from 303 Rust
tests and doctests, the original backend acceptance groups, optimized model
controls, optional-service Study, and synthetic restart.

The next release step is coordinated review of the linked PR heads. The
corrective set is awaiting merge and installation authorization.

### Corrective integration at the reviewed snapshot

This candidate was qualified before shared analysis landed on main.
The earlier corrective checks and the installed correction-context
release remain recorded in their respective sections. This integration
snapshot used Tempo `df06acb9aab5d16b7f642089101e5e0c277ef8fd`, UI
`da8e883c7bf10ec0f9c33df41d5405b7bb8be0b0`, Queue
`a171e70faf684dead33f04ad455012380fcb2e54`, and Planning
`53da95502431dbc091afb45c7678eccce0dd5b8c`. Planning merge
`cc515dd1adec985eb6ee63421ff5826104e7786d` retains both appended ledger
histories. Review and publication use the current corrective PR heads.

| Runtime component | Final source commit | Git tree |
| --- | --- | --- |
| Tempo [#25](https://github.com/tempo-v2/tempo/pull/25) | `e9771becbf26b1e8c76d1a5bc68da4dce10eb54b` | `dee7ba84f6b36418255c5cb5e97eb505618520f8` |
| UI [#19](https://github.com/tempo-v2/tempo-ui/pull/19) | `bf0c05f608cd5fcb4e017b45ff1202de1cd66d48` | `f8c4ef79cbe45ea53c14d2fe97733b49d5251ea5` |
| Store [#15](https://github.com/tempo-v2/tempo-store/pull/15) | `4027bb41cf14425bcbb5f1e8c7467999b0c40a52` | `61090e235be25ff8cf287d2d639bd678b815562a` |
| Queue | `a171e70faf684dead33f04ad455012380fcb2e54` | `a1ebab77ddf5473c9d98b27ab0f26f12aca63c14` |
| Chess | `10701e28ae259de46b04a1a62ba914a46bc012d2` | `39772c7fc7b4739c1033b650c9208725d23cba67` |
| Learning | `09c4359ab90d0cd1e5166b1f25460fd272406fd1` | `2f7312f3dba27d2e3477e7b821a292b71913fe67` |
| Study | `73b2482dfb2ae652220727b87451fdb4a5110807` | `f2efa867550bca6ce3a96ed77359f6f02eea492d` |
| Types | `a8e46c9b9442f1180ec33b8035cef1c713414b66` | `88926c441ed45c8fc983efe097ac9226b3fb51d4` |
| Core 0.2.2 | `e9a1d160a729bc9fbbddaf16427625301cc9498a` | `ad591c239ba10befbfb77bf8cd573e31323821d3` |

All nine runtime trees match the independently reviewed merge preview.
The final Tempo consumes the newer Queue's pending-repair count. The final
UI retains the correction context, count and compact SAN from main.
Its Games implementation and mounted acknowledgement regressions match
the accepted CR-F3 commit byte for byte.

The [reviewed-snapshot qualification and artifact record](historical-follow-up-evidence.md#combined-release-qualification-at-the-reviewed-snapshot)
identifies the locks, Core tarball, macOS executable and all packaged UI
files. SQLite schema 11, portable format 5 and Study wire 5 carry forward.

The shared analysis merge below supersedes this package for the release decision.

### Final corrective candidate with shared analysis main

Main advanced during qualification. The final snapshot includes Tempo
`70850707200c856b089820b32e0baabdff3a21a7`, UI
`3bf2278469d846007243761dc96be9e17cde2117`, Chess
`531cadaea8c89de230d3516d31d95582dc7263dd`, Study
`4b46e6c45a6330177b089eadcae69821e57b6657`, Queue
`a171e70faf684dead33f04ad455012380fcb2e54`, and Planning
`4589d3ecdf6988fdb26c50ab8a8bcb775d3981f1`. Planning merge
`a7316225ad4ab087ae49c3e84ceaa2156dd801ef` preserves the shared analysis
installation and both previously reconciled histories.

| Runtime component | Final source commit | Git tree |
| --- | --- | --- |
| Tempo [#25](https://github.com/tempo-v2/tempo/pull/25) | `2f1cc242f3373ffffe333fae386d18b4cd683f79` | `fb4fcc35de17a348f74173d6e21deae2efd9a3e3` |
| UI [#19](https://github.com/tempo-v2/tempo-ui/pull/19) | `046898f1f144652cb8fa0f43b6c74816e7211ba0` | `80f3a6313bb67a3a672042283d709b77a7ae084a` |
| Chess | `531cadaea8c89de230d3516d31d95582dc7263dd` | `9007327f271afdabdc18cc6de25f137bd64abc36` |
| Study | `4b46e6c45a6330177b089eadcae69821e57b6657` | `f435026c89fb88db58faebc2d05b091e20ac1e96` |

The Store, Queue, Learning, Types and Core pins and trees match the
reviewed-snapshot table above. Tempo and UI match the clean merge trees
of the new snapshot and the original corrective heads. These two trees,
plus the new Chess and Study trees, differ from the attached merge
preview. The refreshed assembly keeps the CR-F3 acknowledgement path
and mounted regressions alongside the newer Study and Games analysis
entry points.

The [final qualification and artifact record](historical-follow-up-evidence.md#final-combined-release-qualification)
identifies the actual release-host package. SQLite schema 11, portable
format 5, and Study wire 5 carry forward. The next unfinished step is
the decision on merging the coordinated PRs. Managed installation
requires separate authorization and verification of the retained live
data and registered artifact set.

## PGN upload caps removed, November 19, 2026

The earlier PGN change removed the 256 KiB and 32-game checks. A 5,075-byte
Caro-Kann export still failed Repertoires Preview because its single game
contained more than 512 plies across variations.

| Decision | Authority, inputs and lifetime |
| --- | --- |
| Accept uploaded PGN | The requested rule applies to Repertoires, Tactics and manual Games import. Chess owns legal moves, valid PGN and the repertoire response for each canonical learner position. Byte count, game count, total plies, nesting and route expansion are independent of acceptance. Provider refresh and historical window policies have their own inputs. |
| Save an accepted preview or import | Tempo validates the same dataset and command identity. Repertoire and tactic saves use their existing signed previews. Store continues to own atomic writes and receipt replay. The UI can hold a large immutable command in IndexedDB under the same per-tab recovery scope. Earlier session envelopes remain readable. |

| Changed component | Qualified head | Pull request |
| --- | --- | --- |
| Chess | `6695bfb5a932d28ac2ec00521879d3814ecd7764` | [#16](https://github.com/tempo-v2/tempo-chess/pull/16) |
| Tempo | `143cbdb12d9d2c8b90c1c56661e444ac4fb33c18` | [#31](https://github.com/tempo-v2/tempo/pull/31) |
| UI | `9b02b0fc82aa2b826cf395b5bd1fe44bd14e90be` | [#25](https://github.com/tempo-v2/tempo-ui/pull/25) |

The companion pins are Store `bac6a78f3d970ea2dfd44fce834370f6cb18d042`,
Learning `09c4359ab90d0cd1e5166b1f25460fd272406fd1`,
Queue `a171e70faf684dead33f04ad455012380fcb2e54`,
Study `4b46e6c45a6330177b089eadcae69821e57b6657`,
Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`, and
Core `e9a1d160a729bc9fbbddaf16427625301cc9498a` with packaged Core 0.2.2.
The workspace reuses the corrective portability Cargo lock. SQLite schema
11 and the existing wire shapes carry forward.

The optimized build, 63 UI tests, six HTTP/consumer tests, architecture
check, and focused Tempo and Chess Rust suites passed. The standalone
Stockfish process cleanup test passed when rerun with host process access.
Disposable HTTP covered signed repertoire and tactic saves above 2 MiB, 501
manual game records, and refusal of an incomplete declared HTTP body. Chess
crossed the previous move, depth and expanded route counts and still
rejected an illegal move. Independent review accepted the combined change.
Packaged Chrome uploaded and saved the original Caro-Kann file. For 6 MiB
repertoire and tactic saves, it lost the accepted reply, reloaded, sent
the exact original command and observed one durable receipt per command.
Chrome also submitted 501 games from a 6 MiB file, reloaded after an
accepted reply was lost, and replayed the exact original request once
without adding a receipt.

The managed installer rehearsed and activated
`workspace-c21029b32dd79bcfc7e2` on port 41822 from the reviewed PR heads.
The optimized backend SHA-256 is
`d214b0c5055389592b8f8e03cb70bd9fe714ab1a551cdf9b2c59a3957f04c0d8`.
The listener served all 22 expected UI files. The live database kept its
inode, dataset and schema. All 34 tables matched the stopped-time backup
`recovery-start-848yw9po`; integrity and foreign keys passed. Live
Repertoires Preview accepted the original PGN. The corresponding Save
was verified on disposable data.

GitHub merged the three runtime PRs into main. Each fetched main tree
matched the qualified head listed above. The merged workspace uses
Chess `25fe9e01482ddc04d323207c18fdcfb5e97be4db`,
Tempo `5130af42f78e5aa25ad42056c8f0b2c6544dd5f3`, and
UI `a16b7ca4ca3149b5789f8e6f935fcdf9b3f8f75c` with the same companion pins.

## Interface execution packet, November 19, 2026

The remote mains match all ten SOURCE_BASELINE pins. The isolated assembly
starts from those mains and preserves the existing workspace branches.
Tempo #28 and Planning #19/#22/#28/#30/#32 remain outside the implementation
leases. The running executable is workspace-c21029b32dd79bcfc7e2 and its
SHA-256 matches the PGN upload release above.

| Packet and acceptance | Owner | Evidence and disposition | Published review |
| --- | --- | --- | --- |
| E01 · A01–A02 | Chess | Passed public consumer tests for N+1 occurrences, custom Black starts, special moves, repeated positions, uncapped PGN and rejected claims. | [Chess #17](https://github.com/tempo-v2/tempo-chess/pull/17) |
| E02 · A03–A07, A29 | Tempo | Passed real-host HTTP and SQLite checks for exact accepted inputs, typed outcomes, replay during a newer run, Busy, timeout and dataset replacement. The supplemental coordinator checks below establish worker acknowledgement, late-success fencing and slot reuse. Ordinary discovery is unconfigured. The default daily ports and explicit fixture capabilities are exercised through real daily and fixture consumers. | [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| E03 · A04–A08 | UI | Passed Chrome against the separate external executable using the production host. The journey covers repeated anchors, relabeling, perspective, detector revision/configuration, unavailable/empty/invalid/timeout, late selection ownership and Study while analysis is active. Analysis-only requests preserve disposable SQLite rows. | [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| E04 · A09–A11 | Evidence owners and UI | Passed fresh and retained source checks and Chrome Analysis/Gap consumers. Invalid unit mass and aggregate counts are rejected. Verified local reach, engine POV, known zero and optional source failures stay distinguishable. Engine/provider inference in the deterministic tests uses controlled replies. | [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) · [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| R01 · A12, A14 | GameJobs | Passed five SQLite/channel Refresh cases and replay through real HTTP. A retains its exact durable acknowledgement while B owns current status, including replay after reopen. | [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| U01 · A13–A15 | Games UI | Passed mounted persist-before-send, unreadable recovery, mismatched address and accepted cleanup tests. Actual prior-release Chrome created both inline and IndexedDB forms for both accepted-lost and unaccepted Refresh. Candidate reload replayed exact bytes, preserved B's slot and kept one receipt per accepted command. | [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| U02 · A15–A16 | UI transport | Passed ignored-abort fetch and body checks, bounded acknowledgement/read delivery, typed errors, mounted Study progress recovery and Games model start reconciliation. Real large PGN and exact prior envelopes were exercised by the combined consumer checks. | [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| S01 · A17–A18 | Store and Tempo adapters | Passed scoped/complete read, capability, rollback, import and receipt checks. SQLite accesses for single Study commands remain addressed/scoped. | [Store #16](https://github.com/tempo-v2/tempo-store/pull/16) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| L01 · A19 | Learning | Passed future/matched/stale correction and cadence tests plus daily FSRS, repair recall and restored obligation journeys. | [Learning #6](https://github.com/tempo-v2/tempo-learning/pull/6) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| Q01 · A20–A21 | Queue | Passed named admissions, canonical rotation, unrestricted versus restrictive-empty, duplicate-ID regression and actual daily ordering. Relevance preserves eligibility and admission. | [Queue #10](https://github.com/tempo-v2/tempo-queue/pull/10) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| ST01 · A22 | Study, Chess and Tempo | Passed shared initialization, legal shown move and ungraded completion. Guided errors, atomic rollback, sticky Test outcome and Practice preservation exercised through daily consumers. | [Study #3](https://github.com/tempo-v2/tempo-study/pull/3) · [Chess #17](https://github.com/tempo-v2/tempo-chess/pull/17) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| I01 · A23 | Tactic ingress | Passed converter parity and real daily transfer/admission with a retained-item reread. Read-only retained diagnostic completed. Enrichment remains deferred. | [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) |
| C01 · A24 | Core and import guard | Passed packed consumer Chrome and actual JS/TypeScript syntax guard with negative fixtures. Packed Core 0.2.2 matches the vendored runtime bytes. The UI npm lock adds a pinned development parser. | [Core #6](https://github.com/tempo-v2/tempo-core-components/pull/6) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) · [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| S02 · A25 | Store read measurement | Measured and retained the current live-offset query at observed scale. See timings below. | This ledger |
| V01 · A26–A29 | Independent reviewers and manager | Passed real HTTP/SQLite/controller, mounted metadata cases, accepted Answer interrupted Next, exact uncertain replay and actual previous-release representations. Review caught a Queue duplicate-theme panic and rechecked its correction. | [Queue #10](https://github.com/tempo-v2/tempo-queue/pull/10) · [Tempo #32](https://github.com/tempo-v2/tempo/pull/32) · [UI #26](https://github.com/tempo-v2/tempo-ui/pull/26) |
| D01 · A30 | Manager | This ledger, current interfaces and manifest record the reviewed source combination, built artifacts and remaining release steps. | This ledger |

The E02 analysis is an explicit read over an accepted dataset/source/game
and resolved learner color under the packet V1 contract. Tempo owns request
identity, deadlines and result delivery. Chess owns the legal timeline and
finding validation. A changed source or semantic detector descriptor fences
delivery. Labels and unrelated Learning revisions are irrelevant. Exact
queries own ephemeral retained replies, which expire on eviction or restart.
Detector absence is a capability state. Analysis has no durable mutation.

### Retained source and gap checks

The open Planning records preserve earlier work. #19 records corrective
portability, #22 schema-11 cutover, #30 compact notation and #32 corrective
release merges before the current PGN-cap checkpoint. The current checkpoint
supersedes those installations. Planning #28 and Tempo #28 track the separate
repertoire tiebreak work. Their dispositions remain open.

S02 used the exact SQLite gap query on disposable in-memory copies of the
stopped backup. Dataset and account predicates used covering indexes. SQLite
used temporary B-trees for distinct, grouping and order. The 50-row copy
materialized 50 groups (5,695 JSON bytes) in 0.212 ms first and 0.116 ms
median warm. The retained-scale copy materialized 201 groups from 214 rows
(22,869 JSON bytes) in 0.658 ms first and 0.497 ms median warm. A disposable
host copy served 100 verified groups with more available in 27,374 bytes.
The first read took 50.5 ms and the warm median was 16.8 ms over 30 repeats.
Keep the current query at this observed scale. Store still materializes all
groups. The endpoint uses live offsets, so page order is guaranteed across
reads only while the evidence, recognized accounts and content basis stay
stable. Revisit if growth makes grouping or materialization material.

I01 ran the read-only diagnostic on the stopped backup and verified local
Tempo 1 source assets. It found 17,267 active tactics with known membership,
388 missing membership, no malformed membership, and four conflicts.
Known source facts include focused and advanced packs outside the current
daily ranking policy. The private diagnostic contains target references and
source membership evidence for deliberate follow-up. Ordinary transfer still
preserves retained items byte for byte and reports incoming membership gaps.

### Compatible candidate and verification

The [manifest](manifest.json) records full component commits, Git trees, lock
hashes, Core package and the exact backend, external example and UI artifacts
used for verification. Rust qualification kept the existing locked Cargo
inputs. The candidate keeps SQLite schema 11, portable format 5, Study wire 5
and content wire 4. Detection adds a separate V1 read-only wire. Ordinary
Refresh adds its addressed acknowledgement to HTTP 202 and dataset identity
to non-idle current status. Existing receipt bytes and browser storage formats
carry forward.

Executed evidence includes 236 locked Tempo/Store/Chess tests and
the focused Learning, Queue and Study suites, architecture self-tests and
the actual dependency gate, the UI build and 91 tests, four import guard
tests, four converter tests and the independent packed Core consumer. The
final HTTP run executed four production cases and three fixture/stdin cases.
Chrome exercised detection, nine Study metadata journeys, four old Study
recovery journeys and four old Games recovery journeys. The metadata
comparison fixed issued and submission identities and study day, and
normalized wall-clock milliseconds. The same locked compatibility set
exercised the larger-than-old-limit PGN path. Previous PGN-release evidence
for the 6 MiB repertoire and tactic IndexedDB replay is reused from the
unchanged envelope and unchanged signed command/receipt format.

Independent reviewers traced detector ownership, Daily Study decisions,
Games recovery and the packed Core consumer. The manager separately reviewed
the Store, source-evidence and Games detector consumer changes. The Queue
duplicate-theme finding was repaired and rechecked. The previous-release
browser cases use the actual installed PGN-cap artifact pair on disposable
data. Study cases exercise typed Answer receipts and serialized allowance
replies. Games cases exercise inline and external envelopes.

### A06 detector lifecycle closure

Tempo commit `89ba3123a40ec5b7cc35ea185a4817f2b2424e4f` adds test-only
coverage for the gap identified on `2cc1a53`. From the pinned candidate
workspace, `cargo test --locked --offline -p tempo --lib game_detection::tests::`
executed three cases with zero failures and zero ignored. A timed-out scan
kept the worker occupied through repeated Busy replies, and the same worker
completed a fresh scan after acknowledgement. A controlled late Complete
message exercised the coordinator fence directly. The dataset-replacement
case verified the stale response after acknowledgement and completed a scan
against the replacement dataset. Independent review inspected the test-only
diff and reran all three cases at the same commit with zero failures and
zero ignored. A06 is closed.

Prior HTTP Study responsiveness, Chrome timeout presentation and read-only
SQLite evidence carry forward from the original qualification artifacts
because the runtime source and inputs are identical. The manifest retains
those artifact hashes and identifies their original Tempo source revision.

N1 remains a diagnostic follow-up. Align the classification of repeated
proved pack occurrences with the converter and Queue before using conflict
counts to scope retained-data repair. N2 remains a converter follow-up.
Report non-string difficulty values through the normal invalid-metadata
path and cover the list-valued case. Retained enrichment is deferred.

The next release steps are coordinated merge of the compatible component
PRs followed by Tempo/UI and the Planning record, remote tree verification
and a separately authorized managed installation. The current live release
is still the PGN-cap checkpoint described above. All mutation and failure
fixtures used disposable data. No install or retained-data enrichment
was performed in this run. Tactical detector algorithms and flashcard
generation belong to the subsequent project.

### Disposable post-game repertoire prototype

Andy asked to compare a completed game with a chosen repertoire and save a useful
continuation through a chosen board. The baseline is the reviewed interface
candidate above. This experiment uses synthetic games, separate local origins
and SQLite files. Implementation and browser observations belong to the prototype.

| Decision | Basis, owner, inputs and lifetime |
| --- | --- |
| Open the game and select a position | Store identifies the accepted raw game by dataset, source and game ID. Tempo validates the learner's side and selected repertoire. Chess supplies its played timeline, position identity, authored replies, departure and reentry. UI holds the selected occurrence, destination and navigation. Display names, game results and detector availability do not determine preparation. |
| Explain existing preparation | Compare the current verified document with this game's positions. A different played move at a prepared learner position is a review opportunity. An unfamiliar opponent move can need a reply. An authored endpoint can be left as it is. Only Learning's introduced fact establishes whether a saved decision has been introduced. A missing document or learning row remains unknown. The historical import result keeps its original meaning. |
| Save a selected line | Exploring and reviewing are reads. The selected endpoint and destination determine the exact line submitted to Chess's existing signed preview. An add-only save accepts the preview only when it preserves prior responses and retires no routes. Store owns acceptance, revision checks and immutable replay. A successful save refreshes the current comparison. An explicit study answer remains a separate operation. |
| Describe completion | Report the specific completed comparison or accepted edit and the currently unresolved positions. Opening the board cannot establish completion of a human review or detector run. Current comparisons are specific to this game and destination and imply no population-level coverage. |

One relevant change is a different prescribed response for the same canonical
board. Renaming the repertoire and changing move order on the way to that board
must preserve its exact prescription. A different destination can legitimately
change that answer.

The [walkthrough, screenshots and disposable setup](postgame-prototype/README.md)
record the two fresh browser visits and a return-screen follow-up. The first visit
could save a marked line but could not find an arbitrary game board or a
transposition, or determine completed work on returning. The independent repeat
completed all eight tasks. Its first pass still required reopening River to
identify the remaining move. In the subsequent repeat, the library displayed
the saved stop at 5.cxd4 and the outstanding 4…Nxf3+ for the same destination.

| Prototype component | Verified source | Draft PR |
| --- | --- | --- |
| Store | `8f3bb25ff7c0713ebda8b433571701bba4bbc547` | [#17](https://github.com/tempo-v2/tempo-store/pull/17) |
| Tempo | `0e89791476a95372a36090b3abd11b955c03bd6c` | [#33](https://github.com/tempo-v2/tempo/pull/33) |
| UI | `fc1a1cfd25dd5a2b242140ac174a532678b47c42` | [#27](https://github.com/tempo-v2/tempo-ui/pull/27) |

Each PR targets the reviewed interface execution candidate. Retain its
[other component pins](manifest.json) and workspace lock. The Core 0.2.2
package SHA-256 is `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4`.
Schema 11 and the existing immutable command and receipt formats carry forward.
The new addressed game review is a read. Player headers were added to the
history read. No released or managed installation was selected or changed.

The application and Store passed 96 library tests. The UI passed 93 tests.
Chrome exercised exact rendered piece squares, an explicitly selected range
through reentry, a switch between two same-color books mid-variation, a
protected conflict, a bounded save, reload and mobile layout. Existing
detector, gap recommendation and Games recovery journeys passed. Independent
old-release recovery used a clone of the static installed-schema backup and the
real previous binary for both lost and unaccepted Games imports and signed
repertoire saves. Chrome recovered each immutable command with one effect.
The [walkthrough](postgame-prototype/README.md) records the proof limits.

The reviewer's only content save added one authored line through 5.cxd4 and
two unintroduced targets. All 18 prior learning rows and target versions
matched. SQLite integrity and foreign keys passed. The populated and empty
copies reserved for Andy use separate local origins and databases; every
database row matched its own starting fixture at handoff. All 22 served UI
files matched the qualified directory on both ports. Ports 42684 and 42686
are reserved only for these local demo instances.

The optimized executable SHA-256 is
`dbfe98b22b2b0bd077e73f8eeec4bbefe9af4612a5850c215a8e2ddd2a841615`.
The UI JavaScript SHA-256 is
`033895265be34eb7294b52111b30285225f4d1142c25410221d3b5bea5647dae`.
The CSS SHA-256 is
`5ed443269e98902e379a1a597a9f4600308368716b283bbe036f06ff31fd0094`.

### Andy's board and game-finding walkthrough

Andy could tell that he chose Bb5 over Bc4, but the board replayed his drag and the candidate controls competed with a simple review. He could not find an Italian game with an unexpected reply in the library.

- A drop follows the legal move accepted by the existing board and Chess. A played departure and a saved response are cues at that exact position. Changing their labels, source visibility or table order has no effect on selection or saving. An off-game branch is an unsaved candidate until Andy previews and confirms its selected range through the existing command.
- A game is discoverable by its retained player names, opening tags and first main-line moves. For the action filter, only a saved comparison for the selected repertoire can describe how that game first left preparation. Its recorded departure kind is authoritative for that comparison. Opening names and names of books are display facts. Opening a result compares against the current document again. Reading or filtering makes no learning or content changes.
- Engine line count controls only the bounded position search. Omission preserves three lines for older callers. Changing engine count or ranking never selects a repertoire response.
- The personal instance is a point-in-time copy in its own local directory, port and browser origin. Restart reopens the same copy. Real games, account settings and credentials stay outside repository artifacts.

The independent walkthrough used a new private browser context. The final return visit explained how a previously recorded opponent gap became a different played response in the current document and retained that explanation on reload. Frame sampling covered actual board drags. The candidate comparison, opening search and signed add-only save were exercised in Chrome on disposable games. The empty library loaded separately.

| Prototype component | Reviewed source | Draft review |
| --- | --- | --- |
| Chess | `a5dcf40e3f51bfa5ff45f9c466922ca541965706` | [#18](https://github.com/tempo-v2/tempo-chess/pull/18) |
| Store | `9bc90f179ca2e85ccb9a75a3aae7ffcf6bd23dc9` | [#17](https://github.com/tempo-v2/tempo-store/pull/17) |
| Tempo | `29623cf1951a06b73ffe57db364d0ecf6c507106` | [#33](https://github.com/tempo-v2/tempo/pull/33) |
| UI | `59e05d22d2b02d39e0040b4282036f82ff794d1e` | [#27](https://github.com/tempo-v2/tempo-ui/pull/27) |

Use the remaining pins and packed Core package from the preceding prototype entry. The application added a read-only archive page and an optional engine search count. New manual imports retain optional opening labels independently of game identity. Existing comparison, learning and save command formats still apply. The Store regression covers two learners, historic summaries, more than one page and a new comparison arriving between reads. All 93 UI tests passed. Live requests returned one, three and five Stockfish candidates and actual Lichess and Maia values. A row-by-row digest of thirteen content, game, receipt and learning tables still matched the source snapshot after the independent walkthrough. The database copy also passed integrity and foreign-key checks.

The [updated walkthrough](postgame-prototype/README.md) includes the synthetic board screenshot and both disposable launch options. Personal examples and data remain local. No merge or production installation was performed.
