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
| tempo-ui | `f4c39cf40e4f1b74feb117dbad0806f084ad5857` | [#2](https://github.com/tempo-v2/tempo-ui/pull/2) |
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
| UI JavaScript | `10053c20ab59bbbea6bb2f5eb341dd354207c4f3baa75517313a517f07774283` |
| UI stylesheet | `1dd1a2da646816cf0f6d3c58edb9325e8b00fa0f884b25bb98e5816d965f0eb1` |
| UI lockfile | `c15717f93ba11bd0b5e0637715d74f996f41c95c5b6f54e683fea2116e6c762c` |
| Core 0.2.2 UI tarball | `4413023594936e57196bdd3864e83968fcfb7d753017bff46ee98cd1cf510ca4` |
