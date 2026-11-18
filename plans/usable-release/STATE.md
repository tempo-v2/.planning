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
| R1 Installed source and handoff | Covered | All 34 archive file hashes across checkpoints 02 and 04 matched. The live listener was the foreground debug build from the pinned 04 code, with the same served HTML and JavaScript hashes as 04. The loaded checkpoint LaunchAgent was idle. The matching executable inode was observed before a locked Cargo check reused the compiled inputs and rematerialized the path with identical bytes. The manifest records that foreground binary hash separately. The source commits are reachable on the published component refs and the exact workspace Cargo lock is tracked with this handoff. |
| R7 Operations and current data | Covered | The read-only Study status and SQLite readback verified the existing schema-3 dataset, the New York calendar, and the independent 10 and 20 limits. No restart or database change was needed. The documented online backup and separate recovery were tested on disposable 04 data with a taught position, active lesson, nondefault configuration, and exactly replayed teaching and content saves. |

[Workspace reconstruction](WORKSPACE.md) uses the pinned component commits. [Mac run and recovery instructions](https://github.com/tempo-v2/tempo/blob/cf94c79cc69820e1819ad32a4112a20b452ca1d6/OPENING.md) distinguish foreground and managed operation. This public handoff omits the private installation's dataset identifier. The locally retained original ledger commit has the cutover record.
