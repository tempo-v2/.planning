# Tempo V2 usable release


## Study move review candidate

[Tempo #148](https://github.com/tempo-v2/tempo/pull/148) at
`9b7f105cee87596dde44f2a6429498211630bba8` adds post-answer review,
replacement and removal of an opening reply directly from Study.
The candidate uses schema 21 and packaged Core 0.2.2. The installed
predecessor is Tempo `5ca62757876449a59f554f0da05b853fa8537699`.
[Planning #124](https://github.com/tempo-v2/.planning/pull/124) records
that installation.

- Locked Rust workspace tests, strict Clippy and the packaged UI build passed.
- Packaged Chromium covered desktop and phone, native Stockfish evaluation
  of every legal root, similarity evidence, manual removal with both evidence
  sources unavailable, title-only invariance, Next-only retry and a two-tab
  save with a lost response. Both delivery states of a pending Answer recovered
  from disposable SQLite backups of the installed predecessor.
- Focused transaction checks verified retained Study history, a card kept by
  a transposed route, stale preview rejection and the 128-write limit. An
  independent Astra review inspected the Study consumer and save transaction.
- The qualified debug binary SHA-256 is
  `5d45f04dc86eead051f60a8c635120a2422a7faa98161dfcc7040f81c931e5d5`.
  The packaged app asset SHA-256 is
  `97a771ef21c3a482dd72287fd53b67c45613ac0c2dc78f21547a3ca19f14a9b5`.

## Study opening guide candidate

[Tempo #143](https://github.com/tempo-v2/tempo/pull/143) at
`e7274a0d735c08bfc5c4aeabfb328288d74548c2` adds a yellow arrow and move
notation to the first unanswered exposure of an opening repertoire card.
The first accepted Answer ends the guide. The candidate uses schema 20
and vendored Core 0.2.2 with the existing Answer and scheduling behavior.

- Locked Rust tests, strict Clippy and the packaged UI build passed.
- Chromium covered both colors, the opening lead-in, reload, title
  invariance, blind reviews and tactics, and Next-only retry. Disposable
  copies of installed `9ac6752731687e7089769c8754e01c70ba422847` covered
  accepted-but-unacknowledged and undelivered Answer recovery.
- Independent review verified the indexed Learning probe, issued-answer
  precedence, invalid-guide omission and one durable effect on replay.
- The qualified debug binary SHA-256 is
  `2b0f4af34a93bf46e5947d30e8c09e64aea7189cc9df0a784d2ee07757bf4f57`.
  Its packaged app asset SHA-256 is
  `230668f79e94c144efbb67b906706adc84e284d0a30e2b336f1eee0d9d2028ee`.
  The installed release is recorded below.

## Installed Lean schema 20 with the daily queue

[Tempo #142](https://github.com/tempo-v2/tempo/pull/142) merged at
`9ac6752731687e7089769c8754e01c70ba422847`. The merge tree matches fresh
Astra's cleared revision. [Planning #118](https://github.com/tempo-v2/.planning/pull/118)
merged at `94310e9512dc455e8873a9f4335736146d709b0c`.
The registered serving process, tactic worker, and independent Daily Queue
worker run the merged release. The [assembly manifest](current-assembly.json)
records their hashes, process IDs, and the stopped rollback backup.

The migration preserved all 236,314 rows from 45 predecessor tables and
retained the issued Study attempt. SQLite integrity and foreign keys passed.
On November 28, Study prepared 346 due reviews before the Daily Queue worker
started. Native Maia then published the order for all 7,893 opening targets,
with 7,465 estimates and 428 unscored. New daily allowances take effect at
the next local study day under the cutover policy.

## Lean daily Study mix candidate

[Tempo #146](https://github.com/tempo-v2/tempo/pull/146) at
`7a6477aa48cd592ec7cfe9b88f155a18ce4066d3` adds a stable proportional mix
of due reviews and ready introductions. Queue keeps the existing lane
rank, kind alternation, active attempts, committed repeats and allowances.
The candidate uses schema 21 and vendored Core 0.2.2. Its installed
schema-20 predecessor, Tempo `2163d9ef83562d2a47b3eddda5235038cf32e6b1`,
is recorded in [Planning #122](https://github.com/tempo-v2/.planning/pull/122).

- A disposable HTTP run served all 300 reviews and 40 introductions.
  The first introduction came at selection 5. The three thirds held 13,
  13 and 14 introductions, with 5–10 reviews between introductions.
  A separate server matched all 171 remaining attempts and card identities
  after restarting from the same database state.
- Locked Rust tests, strict Clippy, the packaged UI build and independent
  Astra review passed. Focused checks covered lane readiness and
  prerequisites, repeat reservation rollback, and bounded Next work as
  the due cohort grew from 100 to 10,000.
- A disposable copy of the installed schema-20 database retained all
  244,601 rows from 50 predecessor tables, the issued attempt, and 12
  committed deck entries. The schema-21 backfill, repeated migration,
  SQLite integrity and foreign keys passed. Packaged Chromium passed
  Next-only retry and both predecessor Answer delivery states.
- The qualified debug binary SHA-256 is
  `215d9163083ca5cb613eccba00e5107463cacae4518c0b93aebbe0c40aa0afdc`.
  The built app asset SHA-256 is
  `230668f79e94c144efbb67b906706adc84e284d0a30e2b336f1eee0d9d2028ee`.

The schema-21 candidate is published for review. The live release remains
on schema 20.

## Lean daily queue candidate

[Tempo #142](https://github.com/tempo-v2/tempo/pull/142) at
`87c8bc83e8f808b6a9f1de7ea0a89a0e3c87e3f4` combines the schema-20 Store,
shared Study consumers, independently supervised Maia worker, and vendored
Core 0.2.2. [Planning #118](https://github.com/tempo-v2/.planning/pull/118)
records the [daily queue operation contract](lean-daily-queue.md). The
installed baseline is still recorded in the following section.

- Optimized Chromium candidate binary SHA-256
  `3be24a8f52a4c5f7484fb76a3c316581781c1912762821c459e43c632c5a248c`.
  The UI app asset SHA-256 is
  `6b9b7970389e96a2d16d7ad3be68db24fbfbecfb7b923b737c254a9f8d6c3e31`.
  Mounted Study passed title invariance, command replay, overlapping tabs,
  and Next-only retry. The actual schema-19 predecessor passed both
  delivery-loss cases for ordinary Answer, full-line Study and Gaps on
  disposable retained copies.
- Native retained-data qualification on the same source used archive-built
  binary SHA-256 `a8e1eded6db9678012b09fe06f643e1326f57f82f42e25ee31f62126e9675e2d`.
  Migration preserved 236,314 rows across 45 predecessor table projections
  and passed integrity and foreign-key checks. It resumed the retained
  attempt and showed due work without new allocations on cutover day.
- Maia profile `maia3-5m-1500-authored-history-v2` published an exact
  7,893-card order in 7.51 seconds warm, with 7,465 estimates and 428
  unscored cards. With the worker stopped across simulated rollover,
  Study issued due work, a saved-ranked opening, and a new tactic.
  Authoring fenced a late result. Worker date divergence and child reaping
  passed with Study still available.
- Fresh Astra cleared the exact candidate. The final independent pass rebuilt
  it and passed 89 Tempo Rust tests and four daily forecast tests. It verified
  that a held opening reservation keeps Next preparing during an intake pause,
  then issues after revalidation while retaining the previously accepted result.
  Hosted CI and strict Clippy passed on the same source.

## Installed Lean schema 19 with repertoire feedback

[Tempo #141](https://github.com/tempo-v2/tempo/pull/141) serves at
`40b87f4df0881e3f57b6d6a7278ad692202b57d0` with schema 19 and Core 0.2.2.
Fresh Astra cleared `5d292fb0acfb90bc4a51d898907e2965bd5b7da8` and the
[Planning contract](https://github.com/tempo-v2/.planning/pull/117) at
`872f3993211cc4ac7dad3f0d7d1bd6bab7f8f92b`. The merged tree matches the
reviewed tree. [The operation contract](lean-operation-contract.md#schema-19-games-repertoire-feedback)
records how Games compares authored replies, publishes a complete report,
and resumes the original sealed work after a temporary file error.

The managed cutover from `087c3bf7e4e4e2ec191d8f5f882be902507502ab`
preserved all 236,311 rows across 44 predecessor tables, including
Learning records, receipts, and the active Study attempt. SQLite integrity,
foreign keys, the registered server and tactic worker, and hashes for all
three served UI assets passed. [The assembly manifest](current-assembly.json)
records the stopped backup, pins and artifacts.

Locked CI and packaged Chromium passed score and replay checks, including
Black replay from a nonstandard move number, delayed responses after
selection changed, failed refresh, sealed retry, import and archive backfill.
On disposable schema-18 data, the new release resumed a sealed Games
checkpoint and replayed both predecessor delivery states for Study Answer,
full-line commands, and Gaps Save, Replace and Apply.

In the installed Games screen, one retained imported game showed
2 of 3 repertoire decisions followed
(66.7%), 1 mismatch,
and 15 unassessed learner moves. The first mismatch
action jumped to the position before the move and showed the original
played and expected moves. The journey issued no Study commands.

## Installed Lean schema 18

[Tempo #138](https://github.com/tempo-v2/tempo/pull/138) serves at
`b2c8851ac252422c846a8bc10dda882aa73d4687`, schema 18 with Core 0.2.2.
Fresh Astra cleared `e740bbc` with [Planning #114](https://github.com/tempo-v2/.planning/pull/114)
at `ae0963d`. The merged source tree matches the reviewed tree. The
[Lean operation contract](lean-operation-contract.md#schema-18-architecture-follow-up)
records the owner and semantics of each changed operation.

The single managed cutover preserved 198,186 predecessor rows across all
44 tables, including all cards, Learning, attempts, receipts, and the active
Study attempt. The catalog now has 1,605 active authored lines and 83 retained
aliases. The original line IDs, names, routes, and semantic revisions survive.
No archived representative needed an activity transfer on the installed data.
A disposable migration verified that a required transfer preserves the
predecessor archive flag. The [manifest](current-assembly.json) records the
stopped schema-17 backup, artifact hashes, and version pins.

**Installed architecture report card · A across the nine assessed boundaries.**

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study issuance, Queue, and Store | A | Prepared-selector and committed-work checks passed in the integrated Rust suite. Read-only Current served the retained attempt with its explicit activity mode. |
| Chess, Learning, and accepted results | A | Packaged Chromium preserved ordinary Answer effects through title changes, malformed delivery, exact replay, and interrupted Next. The stopped comparison preserved Learning and receipts. |
| Study browser recovery | A | Exact packaged replay covered accepted and undelivered predecessor Move, Reveal and Tactics Start. Tab closure retained the command. Incomplete legal choices, inconsistent transitions, and invalid acknowledgements retained the original journal for Retry. |
| Games archive, detectors, and tactic publication | A | Existing bounded archive and detector tests passed. The matched tactic worker returned the retained durable status through its separate socket. |
| Games and Tactics admission | A | Opposing held HTTP bodies exercised independent receive slots. Addressed cleanup passed failed unlink and restart tests. A disposable interrupted predecessor upload resumed with its file and offset unchanged. |
| Coverage optional review and browsing | A | Packaged Chromium kept manual PGN available on malformed evidence, fetched one repertoire page by default, and restored an off-page choice by address. Native Stockfish review and optional failure paths passed. Both live projections returned for all 38 retained reports. |
| Repertoire authoring and identity | A | Canonical identity kept authored line titles and history. Both predecessor Save, Replace and Apply delivery states replayed in Chromium. A partially completed Gaps batch retained the original alias ID and resumed from its exact cursor. |
| Settings, Coverage scan, and rank Apply | A | Saved preference authorities and bounded rank staging carried forward. Native Maia preflight, mounted cancellation, and predecessor Apply replay passed. |
| Core packaging and release provenance | A | Registered server and tactic worker, schema, SQLite integrity and foreign keys, and all three served asset hashes matched the verified installation. |

Faults, synthetic commands and browser replay used disposable databases.
The serving installation was checked through read-only endpoints and the
stopped backup. The assessment covers the named paths and work bounds.

## Installed Coverage gap review

[Tempo #137](https://github.com/tempo-v2/tempo/pull/137) serves at
`b29557924301dc5a00e444ad230fe938ef380413`, schema 17 with Core 0.2.2.
Fresh Astra cleared the matching tree at `aa0fc86` after the later-page
review focus fix. Selecting a gap reviews familiar replies in Tempo.
Stockfish supplies comparable scores and winning mates. Use reply stages
PGN, and the existing Preview and Save flow publishes the continuation.

Packaged Chromium with native Stockfish passed review, focus, late-result
fencing, and extension of a staged reply at a repeated position. The
installed predecessor's lost-acknowledgement and undelivered Save commands
replayed on a retained-data copy. All-root searches can hit the five-second
deadline. Manual PGN and explicit Lichess remain available.

The managed cutover verified the stopped backup and retained all 44 tables
and 32 forecasts. Integrity, foreign keys, the active Study attempt,
registered server and worker, and all three asset hashes passed. Live reads
returned a covered gap and a ranked Stockfish result. The
[assembly manifest](current-assembly.json) records the artifacts and backup.

## Installed Gaps acknowledgement recovery

[Tempo #136](https://github.com/tempo-v2/tempo/pull/136) serves at
`f1f9c7b8b5dda8250d64629891a93a56e4b128a2`, schema 17 and Core 0.2.2.
Fresh Astra cleared Tempo `3b832d10` with Planning `8af25fc0` from
[Planning #111](https://github.com/tempo-v2/.planning/pull/111).
Both merge trees match their reviewed counterparts. The
[assembly manifest](current-assembly.json) records the running binaries,
served asset hashes and stopped schema-17 backup.

**Installed architecture report card · A across the eight assessed boundaries.**

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue, and Store | A | The prepared selector, committed-deck bounds and opening-order evidence from the Coverage release apply to the same backend sources and lockfile. The active Study attempt was retained at cutover. |
| Chess, Learning, and durable acceptance | A | Packaged replay against the installed predecessor preserved accepted and initially undelivered Study and Save command behavior. The existing grading and Learning evidence applies to the same backend sources. |
| Study UI, Core, and recovery | A | Packaged Chromium covered held Save and replacement replies during remount, cross-tab settlement, malformed acknowledgements, later-page retry, and stale feedback. Retry scan stayed available independently of obsolete transport. The same Study controller and Core package carry forward their mounted Study evidence. |
| Games, detectors, and tactic publication | A | Prior detector and Stockfish qualification applies to the same sources, and the registered tactic worker started from the installed release at the retained progress counts. |
| Browsing and optional reads | A | Both live read-only views passed for all 27 retained reports. Packaged Chromium proved an obsolete gaps page or preview could finish without clearing the current report or blocking recovery. |
| Openings, Settings, and shared writer | A | Browser Apply retained the exact command after an incomplete reply, and a late reply preserved a newer command. The same rank planning, writer and bank-switch code carry forward their prior bounded-work and atomicity evidence. |
| Coverage scan execution | A | Packaged browser cancellation passed for ordinary and post-Save scans. The same model runner carries forward its prior native Maia, cache, deadline and physical cleanup evidence. |
| Release provenance | A | The single registered listener and tactic worker use the verified release. Readiness and all three served asset hashes matched. Backup comparison preserved every row in 44 tables, including all 27 rank inputs. SQLite integrity and foreign keys passed. |

The new fault and replay checks used disposable databases. Live checks read
the installed database and served views. Native Maia and the broader backend
qualification were reused from the Coverage release below after verifying
the source and dependency pins.

## Previous schema-17 Coverage bounds

[Tempo #135](https://github.com/tempo-v2/tempo/pull/135) shipped at
`375de983463633d4dff148e2a7b0987f4570523d` with Core 0.2.2. The merged tree
matches independently reviewed `d8d95e9` and includes the opening editor from
[Tempo #134](https://github.com/tempo-v2/tempo/pull/134).
The [assembly manifest](current-assembly.json) pins the server, worker,
served artifacts for the current release. The preserved schema-16 backup
was recorded in [Planning #110](https://github.com/tempo-v2/.planning/pull/110).

The earlier report card assigned eight As. Fresh Astra later reproduced
the remount acknowledgement defect and lowered the recovery grade until
the follow-up release above.

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue, and Store | A | The candidate and predecessor issued the same due and new openings after maximum-size, overlapping, disjoint, and empty Applies. The prepared selector and committed-deck bounds passed. |
| Chess, Learning, and durable acceptance | A | An Answer, its exact replay and Next completed during a held model scan. Both delivery states of predecessor Study commands passed on disposable data. |
| Study UI, Core, and recovery | A | The packaged UI uses Core 0.2.2. The Study controller and Answer journal match the predecessor. Its mounted recovery evidence below covers lost and undelivered Answer, metadata invariance and Next-only retry. Mounted Gaps navigation cancelled uncommitted scans and retained the completed Save and its acknowledgement. |
| Games, detectors, and tactic publication | A | The unchanged detector row-budget and replay checks passed. Worker and server status remained independent during a scan. The combined editor and matched worker also passed a native Stockfish and mounted Chromium journey. |
| Browsing and optional reads | A | Live read-only requests returned both the gap page and studied summary for all 21 retained reports. Coverage paging keeps its separate bounded reader. |
| Openings, Settings, and shared writer | A | Rank preparation used 69 SQLite VM steps before and after adding 20,000 unrelated rows. The bank switch and receipt commit together. A forced interruption after 256 staged cards preserved the visible order across restart. Repeated and previously undelivered Apply commands each produced one receipt. The existing Settings policy and 128-row writer turns remain in use. |
| Coverage scan execution | A | The release ran Maia and reused the cached report with the model unavailable. A 25,800,119-byte maximum-shape fixture fit the 32 MiB limit. Blocked startup and pipes, oversized output, disconnect, deadline and shutdown exercised cleanup. Cancellation at the writer fence produced zero reports. A committed scan reused its identity. |
| Release provenance | A | The registered server and tactic worker ran the merged binaries. Health was ready, all three served asset hashes matched, SQLite integrity and foreign keys passed, and the active Study attempt was retained. |

The stopped comparison covered all 43 predecessor tables, allowed only the
inactive-bank alignment, and verified the new rank inputs for all 21 saved
forecasts. Qualification included 55 Tempo unit tests, five similarity
integration tests, the Stockfish suite, strict Clippy and packaged UI build.
The native Stockfish check timed out once under concurrent load and passed
on rerun. An initial concurrent optional read returned an unidentified
non-200 during independent qualification. The instrumented rerun passed.

Faults, synthetic answers, rank changes and browser recovery ran on disposable
databases. The release verification used read-only requests against the
installed dataset.

## Installed repertoire gap review fixes

[Tempo #132](https://github.com/tempo-v2/tempo/pull/132) shipped at
`d65f18ede624af49f2a788d8d19feaf69c7815f2` on Lean schema 16 and Core 0.2.2.
Gap preview retains verified recorded routes when it reaches the current-route
search limit. An unreachable suffix cannot cause an independent saved
continuation to be trimmed. Cyclic conflicts and work limits have explicit
preview responses that leave the PGN editable.

Fresh Astra cleared `8d16bc1`. All 53 Tempo tests and strict Clippy
passed. Chromium on the optimized release verified in-place correction,
confirmed replacement, and replay from the immediately preceding installed
release on disposable data.

The managed switch retained all 43 tables against the stopped backup.
SQLite integrity and foreign keys passed. The registered listener and tactic
worker use the published release, served asset bytes matched, and the retained
dataset and active Study attempt were verified. The
[assembly manifest](current-assembly.json) records the artifacts and backup.

## Installed schema-16 gap conflict resolution and worker replay

[Tempo #130](https://github.com/tempo-v2/tempo/pull/130) and
[Tempo #131](https://github.com/tempo-v2/tempo/pull/131) shipped at
`9be76dff41fedc7f52d5aa481fbea92ae112189b` with Core 0.2.2. Both managed processes used that release. The
[assembly manifest](current-assembly.json) retains its hashes and backup.

Openings → Gaps can repair a pasted continuation with the saved reply
or stage a separately confirmed repertoire replacement. The replacement
keeps prior lines, Study attempts, and Learning history available.
Both tactic worker modes replay the same evidence through uncertain
Submit replies. The report view and Apply use the saved forecast model
identity to make the same freshness decision.

Fresh Astra cleared the combined head `c80156e`. All 52 Tempo tests,
seven Stockfish tests, strict Clippy and the packaged UI build passed.
Mounted Chromium exercised conflict resolution, a lost replacement
reply, and predecessor command replay. Disposable native probes verified
worker replay and preserved verdicts. Seven retained coverage reports
matched through HTTP, and a deliberately incorrect display flag had
no effect on eligibility.

The stopped copy and migrated database matched across the predecessor
columns of all 42 tables. SQLite integrity and foreign keys passed.
The managed checks verified the listener, both registered processes,
served asset hashes and read-only routes. Synthetic actions ran only on
disposable data.

## Installed schema-15 tactic status and coverage bounds

[Tempo #129](https://github.com/tempo-v2/tempo/pull/129) merged and serves at
`09ff14a68030573e4bcd01e282ce8371b7705c65` with the matched tactic worker,
Core 0.2.2, and SQLite schema 15. Independent review examined `90e614a`.
The merged tree matches that head. The stopped backup preserves all 39
predecessor tables. SQLite integrity, foreign keys, registered process
identity, served asset hashes, and read-only endpoint checks passed.
The [assembly manifest](current-assembly.json) records the exact artifacts.

**Overall A across the eight assessed boundaries.**

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue, and Store | A | Prepared-order work bounds, excluded Games reads, and deferred repeats passed on the combined source. |
| Chess, Learning, and acceptance | A | Native scoring, exact Answer recovery and issued-answer preservation passed. |
| Study UI, Core, and recovery | A | Mounted Chromium passed predecessor lost and undelivered Answers, mixed tabs, display-name invariance, and Next-only retry. |
| Games, detectors, and tactic publication | A | The detector stays within 128 affected rows, including counter changes. Archived game acceptance stays independent of the tactic companion. |
| Tactic worker status and dispatch | A | The bundled SQLite singleton query stayed flat with 100,000 additional finished findings. A held status connection did not block Next or verdict replay. Native evidence committed after a lost reply and replayed across restart. An unavailable status socket left work intake available. |
| Optional reads and coverage | A | SQL authorization checks denied Learning and full-report reads during paging. All seven retained reports matched. The maximum-size disposable probe read a summary over 300,000 path references and served a cross-chunk page within the read budget. Mounted Chromium paged while summary was held, then recovered summary after a 503. |
| Openings, Settings, and shared writer | A | Predecessor Save and Apply recovered in both delivery states with one receipt each. Writer admission, fairness, and bounded detector writes passed. |
| Release provenance | A | The server and worker run the matched schema-15 release. Both hashes, served assets, the backup, and package pins are recorded here. |

All 47 Tempo tests and seven Stockfish tests passed, including native
Stockfish 19. Strict Clippy and the packaged UI build passed. Fault injection,
synthetic commands, and recovery ran on disposable databases. Live checks
used the stopped snapshot comparison and read-only requests. Four retained
findings were in retry backoff when the matched worker was activated.
A later live status read showed three unresolved and one more retired card.

## Installed shared Study and Tactics layout

[Tempo #128](https://github.com/tempo-v2/tempo/pull/128) shipped at
`21b704baab82d18a5441f063b244de76df0cab48` on Lean schema 14 and Core 0.2.2.
Ordinary Study, full-line Study and Tactics share the board layout.
The desktop board stays anchored on the left. Feedback, promotion,
replay and navigation controls sit on the right. Phone controls stack
below the board.

Fresh Astra cleared the reviewed tree after the replay focus correction
and integration with the schema-14 generated tactics release. Chromium
on the optimized release verified desktop board bounds and scroll,
mobile stacking, replay focus and Next-only retry. Predecessor recovery
passed on disposable data.

The managed switch took a verified stopped backup and served the expected
assets and existing catalog on schema 14. The tactic worker retained its
release and reconnected to the replacement server. See the
[assembly manifest](current-assembly.json) for artifact and backup details.

## Installed full-line Study recovery

[Tempo #125](https://github.com/tempo-v2/tempo/pull/125) shipped at
`7358fba69835d7b4c415a3638db49e26da8c6727` on Lean schema 13 and Core 0.2.2.
It clears a rejected predecessor Answer after a reload and resumes the issued
full-line puzzle. Chess rejects missing and malformed actions without grading
and accepts an alternate final checkmate when the prescribed move also mates.
New Starts bind their catalog revision. Historical Starts and accepted Move
receipts remain recoverable.

Fresh Astra cleared the exact source tree. Chromium against the optimized
release verified predecessor recovery on retained data, a rejected old-tab
Answer, canonical moves, alternate mate, and Retry Next after an accepted
result. Synthetic results were recorded only in disposable databases.

The stopped backup and schema migration preserved the prior fields and rows
of all 38 tables, including Learning, the active attempt, and the Lichess
catalog. SQLite integrity and foreign keys passed. The registered service
served the expected UI hashes and unchanged 74-theme catalog. See the
[assembly manifest](current-assembly.json) for the artifacts and backup.

## Installed Lichess packs and full-solution Study

[Tempo #120](https://github.com/tempo-v2/tempo/pull/120) and
[Tempo #123](https://github.com/tempo-v2/tempo/pull/123) shipped together at
`0d6e288027dee3204850676da57f0cb3b2622ce6` on Lean schema 12 and Core 0.2.2.
The verified catalog has 1,332 20-puzzle packs across 74 themes and 18,214
distinct puzzles. Tactics recommends the easiest unfinished pack, allows
direct selection of harder bands, and offers the next unfinished harder
pack at completion. Refresh replaces membership and keeps issued solutions,
accepted receipts, and per-puzzle progress.

Chess owns full-line scoring for Tactics first play and subsequent Study.
The first miss uses Again and the existing repeat placement, including
durable ordered deferral when the deck is full. A clean first solve
initializes FSRS and persists one 7–20 local study-day due date. Practice
and pack browsing leave Learning alone. Tactics leaves the issued Study
attempt in place.

All 39 Rust tests, strict Clippy, the collector fixture and the locked UI
build passed. Independent Chromium and HTTP verified a lost final reply,
exact retry, full-line restart, alternate mate and promotion, active
Study isolation, shared progress, refresh, deferred repeats, and Next-only
retry. Chromium also replayed accepted-lost and undelivered Answers from
the actually installed schema-11 predecessor on disposable retained data.
Mobile Chromium completed a pack and opened the next band directly.

The stopped backup and catalog import preserved all 29 predecessor tables.
The active LaunchAgent served the schema-12 assets and catalog index.
Readback verified 74 themes and 20 members in the first Fork pack.
The [assembly manifest](current-assembly.json) records the backup and
the binary, UI, lockfile, Core and catalog checksums.

## Installed online batch saving for large gaps

[Tempo #121](https://github.com/tempo-v2/tempo/pull/121) installed at
`f98e346ccb09271c55ebcab5671354e60e497609` with schema 11 and Core 0.2.2.
Openings → Gaps uses **Save to repertoire** for large PGNs. Openings validates
the full continuation and commits bounded writes with their durable checkpoint.
Retry uses the original command. A change to authored replies during the save
fences subsequent batches and reports the committed progress. A line name or an
additional line that uses only existing replies does not affect that fence.

Fresh Astra cleared `362a4fffe6dc5b32365c93792535ca2f9fabe158`. The reported PGN
saved 45 lines and 90 replies online on retained copies. HTTP resumed after
interruption at 9 lines, and Chromium recovered after a lost final acknowledgement
and reload. Both returned one receipt and preserved Learning. All 36 Tempo tests,
strict Clippy, the UI build, and mounted predecessor Answer recovery passed.
The stopped backup and installed database matched across all 28 predecessor
tables. The [manifest](current-assembly.json) records the artifact and backup.

## Previous offline import release

[Tempo #119](https://github.com/tempo-v2/tempo/pull/119) merged and installed at
`b048e28823cec0c09559da8989b425980e2d1f12` with Core 0.2.2 and schema 10. Large gap
previews expose an offline download with the same draft, gap selection and
command identity. The stopped-service importer uses the same revision, conflict
and atomic receipt checks as online Save. Online preview and offline import
enforce separate expanded-tree limits.

The reported PGN previewed 90 new replies and imported all 45 matching lines
on disposable retained copies. Chromium verified the exact export, repetition
returned one receipt, and learning records were preserved. The installed
browser also offered the export for the supplied PGN. Fresh Astra cleared
`38497efeb6874219f723d4f0d3eb68eca47b7554`. All 35 Tempo tests and strict
Clippy passed. A stopped backup and bidirectional comparison verified all
28 predecessor tables during installation. The reported PGN was not committed
to the live repertoire. See the [manifest](current-assembly.json).

## Installed Maia repertoire gaps and Study order

[Tempo #116](https://github.com/tempo-v2/tempo/pull/116) merged at
`6041ec9f395700518073bc9b09c783e6e455edd5` with Openings → Gaps and additive
PGN authoring. [Tempo #117](https://github.com/tempo-v2/tempo/pull/117) merged at
`fed4db1fc6186e3bd162cb90efcd69c20bfbc79a` with explicit Study rank adoption. Fresh
Astra cleared `5ebc1e780ec4ad2f4d515260e4447f3c806e0ca5`. Its tree matches the
final merge and includes the independently merged Stockfish workspace member.
Review fixes separated pending Save and Apply from browsing state, isolated
PGN previews across tabs, and preserved explicit Retry semantics.

The managed LaunchAgent serves this release on port 41823 with schema 10 and
Core 0.2.2. The stopped backup and migrated database matched across all 23
predecessor tables. SQLite integrity, foreign keys, served asset hashes and
read-only endpoints passed. The [manifest](current-assembly.json) pins the
release and backup. The exact installed artifact rehearsed the migration and
model scan on a copy before switching the service.

Maia-2 Rapid 1500/1500 predicts opponent moves after the selected starting line.
Openings supplies the learner response. Authored coverage requires an answer through
the chosen learner move, and studied coverage requires an accepted Good or Again
on every current response there. Conflicts and the scan budget leave explicit
unresolved probability. Opening names have no bearing on these decisions. The
worker uses Python 3.12, maia2 0.11.0, torch 2.8.0 and Rapid weights with SHA-256
`65aae8465eed5e65df66a24ea7370715579f9e5435098d06fe18bdb1e267e997`.
Host provisioning is documented in the Tempo README.

All 34 Tempo tests, seven Stockfish contract tests (including the native
Stockfish 19 check), two Python forecast tests, strict Clippy and the UI build
passed. Five focused mounted browser checks covered interrupted Save and Apply,
failed report reads, and two-tab preview/command isolation. Chromium followed the generated Lichess link, restored the draft,
rejected unrelated PGN, and replayed a lost Save acknowledgement with one durable
effect. A 20 KiB annotated transposition PGN added one response and excluded an
unrelated variation. Lichess returned HTTP 403 to the automated browser. The
remaining external check is to open the provided line in Lichess and export an
edited PGN there.

On disposable data the selected reply raised authored coverage from 7.01% to
36.31%. A real Again review raised studied coverage to 29.30%. An independent
3,000-card interrupted apply preserved the previous order before publication,
then recovered across restart with one receipt. With 4,095 higher-ranked future
reviews the due selector used 24 indexed probes. The mounted Study suite passed
accepted and undelivered predecessor Answer recovery on copies of the installed
database, interrupted Next, and the merged Study drop-preview journeys.

On a migrated copy of the retained Gustafsson repertoire, the scan after
1.e4 e5 2.Nf3 through White's move 10 took 7.7 seconds on the qualification
host. It returned 2,063 distinct first gaps, 2.334% confirmed authored coverage
and 0.625% unresolved probability. These are conditional model estimates.
## Standalone Stockfish analysis

[Tempo #118](https://github.com/tempo-v2/tempo/pull/118) adds
`tempo-stockfish-analysis` 0.1.0 at
`69d702f9ce8a1dd9e2111e0ce6c76e7d6627e7bd`, based on Lean main
`d895f6dfe80cd9e9d96b53a702e4540c05b0ac98`. The JSON CLI is the first
consumer. There is no installed artifact associated with this entry.

The [operation contract](lean-operation-contract.md#standalone-position-analysis)
records the supported inputs, engine budget, and ownership boundary.

All seven contract tests passed with native Stockfish 19 enabled. The CLI
returned all 20 starting moves and the exact 48-move set for Kiwipete. The
suite also checked targeted comparison, Black-to-move normalization, mate,
promotion, terminal positions, invalid and variant FEN rejection before
launch, contention, cancellation, timeout, and subprocess cleanup.
The Astra review reproduced malformed standard FEN accepted by the parser,
contradictory coverage options, and a valid engine progress message treated
as a failed score. The candidate rejects those requests before launch and
keeps progress messages separate from scored lines. A second review
reproduced admission before reaping when the caller runtime shuts down.
The worker now owns reaping independently of the caller runtime. The new
regression failed on the previous head and passed on this candidate.
Clippy passed with warnings denied. The Lean application and packaged Core
0.2.2 UI built, and the normal runtime returned HTTP 200 from a disposable
database with Stockfish absent from PATH. The serving package dependency
tree excludes the analysis crate. There is no route, settings, schema, or
managed-install change.

## Study drop preview candidate

[Tempo #115](https://github.com/tempo-v2/tempo/pull/115) publishes
`c71e810a39fa5a2c33fb8af76f4afc7f36ad7126` on the serving Lean baseline with
the same packaged Core 0.2.2. Study displays a legal drop before waiting for
the Answer journal. The chosen promotion piece appears on the destination
square using the move's promotion code. The journal commits the original
intent before network delivery.

Chromium reproduced the capture reset on the serving build using disposable
data. The candidate passed frame checks for capture, quiet moves, illegal
drops, capture promotion, and correction. A lost accepted response replayed
the same Answer and left one grade. The mounted Answer suite also passed
predecessor recovery on synthetic databases and Next-only retry.

The recorded serving release is
`1f3d2585e7b47178af990cab137b14617dd650c1`.

## Lean delivery and preparation boundaries

**Baseline grade B. Qualified and installed grade A** across the seven examined
boundaries. The baseline served schema 8 at `6c7a8d289ec9db68936ef6860d3743742ad16eed`.
Its executable and three served asset hashes matched the installed manifest.
[Tempo #114](https://github.com/tempo-v2/tempo/pull/114) was reviewed by fresh
Astra at `3f6747ed7c1110f3bd89f17c43ae5b00cfd413ed` and merged the identical
tree at `1f3d2585e7b47178af990cab137b14617dd650c1`. The qualified build uses
schema 8 and packaged Core 0.2.2. The [manifest](current-assembly.json) pins
the serving release and qualified source separately.

| Boundary | Baseline | Qualified merge | Evidence |
| --- | --- | --- | --- |
| Study, Queue and Store | A | A | Native checks kept prepared issuance bounded and excluded Games and live rank reads from Study commands. |
| Chess, Learning and acceptance | A | A | Exact Answer replay preserved one grade, schedule, receipt and repeat placement. |
| Study UI, Core and recovery | C | A | An unplayable Answer reply originally cleared the journal and crashed the board. Chromium now preserves the exact intent, recovers both predecessor delivery states and retries interrupted Next separately. |
| Games, detectors and Tactics | A | A | The HTTP suite exercised canonical archive identity, separate detector results, sealed retry, rescan and tactic publication. It also resumed an interrupted upload at its original checkpoint. |
| Optional reads and browsing | B | A | Chromium discarded stale previews and file reads. Invalid positions and move tokens preserved the draft. Only Save committed the selected route. |
| Openings and Settings | A | A | The examined reads and writes retained authoritative repertoire identities and saved preferences. A name edit left the selected preview route applicable. |
| Request limits and shared writer | B | A | The HTTP router kept Study and content commands available under saturated staging. Additional staging returned a typed unavailable reply and created no job. Reintroducing the shared semaphore made the regression fail. |

All 33 locked Rust tests, strict Clippy, optimized build, packaged UI,
mounted Chromium and HTTP qualification passed. Answer recovery and the
interrupted upload used disposable data. A retained database copy preserved
all 23 tables and 16,768 games. Health and nine read routes returned HTTP 200
on the serving release.

### Managed installation

The Mac now serves Tempo main at `1f3d2585e7b47178af990cab137b14617dd650c1`
on port 41823 through one registered LaunchAgent. The exact release build
passed the Games and Chromium suites on disposable data. The cutover kept
the existing schema-8 database and took a verified stopped backup. The
running executable, served assets, database integrity, and foreign keys
were verified. The manifest records the current executable and backup.

## Lean archive rescan bounds

[Tempo #112](https://github.com/tempo-v2/tempo/pull/112) pins candidate
`f765748b1107daee7fcbb845af522c27452ecbf3` for the schema-8
[archive rescan contract](lean-operation-contract.md#schema-8-archive-rescan-cursor).
Astra independently cleared this head and [Planning #96](https://github.com/tempo-v2/.planning/pull/96).
Tempo main merged the identical tree at `6c7a8d289ec9db68936ef6860d3743742ad16eed`.

- The bundled SQLite hit, exhausted range and 64-row page used 24, 11 and
  459 VM steps before 100,000 post-cutoff games, and 18, 14 and 459 after.
  Raising the cutoff selected the newly eligible game.
- The runner retained a partly applied schema-7 seal and both detector
  jobs' frozen membership. It restarted after committing a page of
  previously completed games and preserved the exact findings and parent count.
  Study Next and Answer completed during recovery.
- Disposable migration preserved all 23 predecessor tables and 16,768
  retained games. The schema-7 executable refused schema 8. A staged
  upload resumed its original ID, file and byte offset.
- 31 locked Rust tests, strict Clippy, packaged Core 0.2.2, the optimized
  executable and Chromium Answer recovery passed. The exact managed build
  reran the disposable Games and Chromium suites before cutover.

### Installed schema-8 report card

The stopped schema-7 backup and executable remain available together.
The locked cutover preserved all 23 predecessor tables and validated
staged-file references, integrity and foreign keys. One registered service
serves the matching executable and three assets. Health and nine read-only
endpoints responded successfully. The [manifest](current-assembly.json)
records both installations.

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue and Store | A | The locked suite retained prepared-queue isolation and bounded issuance. Real Next and Answer succeeded during scan recovery. |
| Chess, Learning and acceptance | A | Exact Answer replay preserved one grade and schedule, and the cutover preserved the Learning rows. |
| Study UI, Core and recovery | A | Packaged Core 0.2.2, schema-7 Answers, mixed tabs, display-name invariance and retry after interrupted Next passed in Chromium. |
| Games, detectors and Tactics | A | SQLite used the ordinal primary-key range for one game or one bounded compatibility page. Lookup work stayed bounded with 100,000 later games. A partly applied seal and both detector jobs recovered with exact membership, findings and parent counts. |
| Optional reads and browsing | A | Real HTTP and Chromium checks covered addressed replay, bounded pages, cancellation and read-only retry. |
| Openings and Settings | A | Cutover kept the exact catalog and preference rows. The installed routes served them successfully. |
| Request limits and shared writer | A | The writer admission and detector apply budget checks passed. A compatibility page requeues only its own job with the existing writer. |

**Overall A for the seven assessed Lean boundaries.** Scale, failure
injection and synthetic commands ran on disposable databases. The installed
checks covered cutover preservation, process and artifact identity, and
read-only service behavior.

## Lean bounded browsing

[Tempo #111](https://github.com/tempo-v2/tempo/pull/111) head `f03d7a323cadd9e207277c28e6d6b1ec9bc2c29f`
adds the read contract to the schema-7 runtime. The Mac moved directly from schema 6 to the combined build at
`2264e963674138e61b02e3ff8dda88f3379ad5c1`.

- 30 locked Rust tests, strict Clippy, packaged Core UI and optimized build passed.
- Chromium replayed the original schema-6 Answers, exercised mixed tabs and
  Next-only retry, and confirmed archive refresh coalescing and read-only retry.
- Real HTTP exercised Games identity, detector recovery, pagination and addressed
  replay. The optimized build preserved all 16,768 games and predecessor rows
  on a disposable copy, and resumed the schema-6 upload from its original checkpoint.
- Initial independent review found that a malformed current Study reply could
  trigger Next and a failed read after definitive Answer resolution could
  resend the command. Both have mounted Chromium regressions and are fixed
  in this head. Fresh independent review cleared Tempo `f03d7a3` and
  Planning `493426d`. The exact managed build passed both suites again.


### Installed evidence and architecture report card

A stopped, checked schema-6 backup was retained before the offline migration.
The migration comparison preserved all 22 predecessor tables, with archive
routes converted to the packed representation, and passed integrity and
foreign-key checks. One registered listener serves the matching executable
and assets. Health and nine read-only endpoints returned successful replies.
The [assembly manifest](current-assembly.json) pins both installations.

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue and Store | A | Prepared issuance and Again remain bounded as unrelated cards grow. Archive reads are excluded from Next and Answer. |
| Chess, Learning and acceptance | A | Answer replay preserves one durable grade, schedule and repeat disposition. |
| Study UI, Core and recovery | A | Packaged Core, original schema-6 envelopes, malformed read handling, mixed tabs and Next-only retry passed with the installed executable on disposable data. |
| Games, detectors and Tactics | A | The same occurrence with different provenance reused one game. Capture survived comparison failure, and comparison retried its sealed result. |
| Optional reads and browsing | A | Bounded read families retained their slots through cancellation. Mounted Games coalesced polling invalidation. Real HTTP served 50 maximum-length routes with stable pagination, and SQLite lock failure left health ready. |
| Openings and Settings | A | The existing ownership and saved preferences survived the migration. Installed catalog and Settings reads succeeded. |
| Request limits and shared writer | A | The writer and detector apply budgets passed. Admission and staged file ownership remain separate from optional reads. |

**Overall A for the examined Lean architecture.** Synthetic faults and
commands were exercised on disposable data with the same managed artifact.
Live evidence is confined to migration, process and artifact identity, and
read-only smoke checks.

## Lean schema 7 Game and Answer representations

[Tempo #110](https://github.com/tempo-v2/tempo/pull/110) candidate `693388c5a1453f3357afd9fefa5dd9184535d7f0`
uses the [schema-7 operation contract](lean-operation-contract.md) and packaged
Core 0.2.2. The [assembly manifest](current-assembly.json) identifies the
qualified candidate and the serving schema-6 predecessor.

- All 28 locked Rust tests, strict Clippy, the packaged UI build and the
  optimized executable build passed. Occurrence lookup stayed bounded with
  100,000 unrelated and 100,000 same-fingerprint rows. SQLite counted 128
  affected rows on the maximum final capture apply, including ready-order
  triggers and parent progress.
- A disposable copy converted all 16,768 archived games. SQLite integrity and
  foreign keys passed. All predecessor semantic rows matched in both
  directions. Packed route payloads used 3,146,978 bytes, from 8,712,290.
  The explicit offline migration refused the serving lock. A schema-6 upload
  resumed its original file, identity and byte offset on schema 7.
- Real HTTP used manual PGN and frozen local Lichess and Chess.com downloads.
  It reused one archive identity, kept independent detector progress through
  comparison failure, retried the sealed analysis after an opening edit, and
  observed the new input on an explicit rescan. Named rounds distinguished
  separate occurrences, with exact repeats and placeholder rounds reusing an
  existing game. A substituted detector
  retained its new versioned finding without changing the accepted puzzle.
  The Stats proof used the addressed Game reader.
- Chromium replayed both original schema-6 Answer cases, recovered the
  two-tab delayed response and an incomplete success reply, and retried only
  Next after acceptance. Original, renamed and blank titles yielded the same
  Good/Again commands, receipts, relative schedules, and continuation. A
  still-loaded schema-6 tab cleared its old scalar after cutover while the
  reloaded schema-7 tab retained and replayed its newer intent.
- First independent Astra pass at `33bc0a0` identified incomplete receipt
  handling, duplicated Game reconstruction and an oversized terminal capture
  transaction. These are corrected in the candidate above and covered by
  the browser and SQLite checks. The second review at `f12bff7` confirmed
  those checks and found that nonnumeric rounds collapsed. The candidate
  above now preserves named rounds and exercises them through HTTP.
- A fresh Astra review cleared Tempo `693388c5` and Planning `21ddff04`.
  It independently matched the optimized executable hash and reran all
  28 Rust tests, both qualification tools, and the retained-database
  rehearsal. Tempo #110 merged at
  `79ed7b4cc307cc8a092a2fc696975325078d5fde`. Its tree matches the reviewed
  candidate, and remote main was verified.

### Architecture report card for the merged candidate

**Overall A for the examined boundaries.** The managed installation is
still serving the schema-6 predecessor. The grades apply to the exact
qualified schema-7 source and artifacts.

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue, and Store | A | Next and Answer preserve bounded prepared selection and repeat placement as the catalog grows. The SQL probe excludes archive reads. |
| Chess, Learning, and acceptance | A | One first accepted effect persists with its repeat disposition. Exact replays and competing submissions preserve one grade. |
| Study UI, Core, and recovery | A | Packaged Core, per-intent journal, preceding receipt recovery, incomplete reply handling, mixed tabs, and Next-only retry passed in Chromium. |
| Games, detectors, and Tactics | A | All three intake paths share archive identity. Replay, Stats, and detector input share Game IR. Versioned detector retry preserves the sealed snapshot and published puzzle. |
| Optional views | A | Counts, source context, repertoire picker, and Games status retain independent bounded readers. Games status reports the parent scan and active user work without advancing jobs. |
| Openings and Settings | A | Repertoire and preference ownership stayed intact. The migration preserved those rows, and sealed detector retry exercised authored changes through Openings. |
| Request limits and shared writer | A | Bounds stayed in force. Reclamation failure and staged-file ownership were exercised while real Study Next and Answer completed. The largest capture transaction used 128 rows including triggers. |

## Lean Games admission and Study count bounds

[Tempo #109](https://github.com/tempo-v2/tempo/pull/109) merged schema 6 at
`0c9ed8b3324a40f7e88653aea4366c6e030c8c00`. The serving build has the source tree
independently reviewed at `92b434e09611e7d7e1b9ff12708c252211db240d` and uses Core 0.2.2.
The [assembly manifest](current-assembly.json) pins the candidate and managed
artifacts separately. The [Lean operation contract](lean-operation-contract.md)
records the accepted count cap and request limits.

- All 22 locked Rust tests, strict Clippy, the packaged UI build and the locked
  optimized build passed. A fresh Astra reviewer cleared the published source
  and contract and independently exercised HTTP, browser, database and
  predecessor recovery checks.
- The installed binary, running on disposable data, accepted ordinary Games
  requests at 16 KiB and rejected one byte above it with fixed and chunked
  bodies. The dedicated upload route accepted 64 MiB and rejected one byte
  above it before staging. Chrome used the correct route for provider import,
  archive scan, upload and retry of the original job.
- Capacity, duplicate hit and duplicate miss took 50, 52 and 62 SQLite VM
  steps with and without 100,000 unrelated child and finished jobs. A local
  provider feed resumed its staged window, accepted 700 games, rejected two
  records once, and rotated with a manual upload. A separate interruption test
  showed identical archive, capture and tactic rows after restart, and Study
  accepted and advanced during Games work.
- Both counts were capped on a 100,000-card fixture in 360,236 SQLite VM steps.
  The managed binary returned both capped values in a 4.9 ms disposable HTTP
  observation. Chrome rendered mixed capped and exact totals and kept Answer
  and Next usable when counts failed. It also replayed the actual schema-5
  Answer for both a lost response and an undelivered submission. Interrupted
  Next retained the accepted result and retried only Next.
- Rehearsal and the managed migration preserved all 22 predecessor tables in
  both directions. Integrity and foreign keys passed. A schema-5 upload
  resumed from its original committed file and byte checkpoint. The matching
  schema-5 executable and verified stopped backup remain available for
  recovery. After cutover, one launchd listener served the verified binary
  and matching HTML, JavaScript and CSS. Health, Study, counts, Games status,
  opening preferences and the repertoire picker returned successful reads.

### Architecture report card

**Overall grade A for the examined Lean boundaries.** The intake limits and
writer lookup bounds now hold on the real Games entry points, and the optional
Study count stays within its query and time budgets as eligible rows grow.

| Boundary | Grade | Evidence |
| --- | --- | --- |
| Study, Queue and Store | A | Next resumes or uses indexed prepared membership. The committed Next and Again tests held with 100,000 unrelated cards. |
| Chess, Learning and acceptance | A | A single committed result owns FSRS, the receipt and repeat placement. The restart and replay checks retained one grade. |
| Study UI, Core and recovery | A | The production client uses packaged Core, replays the original schema-5 Answer, and retries only Next after an accepted grade. |
| Games, scanner and Tactics | A | The worker independently resumes archive, scan and publication through persisted progress. Status stays read-only and Study advances during Games work. |
| Optional reads | A | Counts use bounded exact or capped results, and failure has no effect on grading or continuation. The existing context, Games status and picker slots retain their bounds. |
| Openings and Settings | A | The opening identity constraint, indexed picker and saved preference ownership retain schema-5 evidence. The installed routes returned successful reads. |
| Request limits and shared writer | A | Fixed and chunked ordinary commands enforce 16 KiB. The dedicated upload keeps 64 MiB. The admission index keeps work constant as unrelated work grows. |

Synthetic writes, failures and scale measurements used disposable databases.
Managed verification used the migration comparison, artifact identity and
read-only HTTP.

## Lean Games and repertoire operation bounds

[Tempo #108](https://github.com/tempo-v2/tempo/pull/108) merged schema 5 at
`0cce44a58ec8e6557bd614e2e935b0e00cf3e9da`. The managed Mac serves that exact
revision with the retained database. The source tree matches independently
reviewed head `4774aa22d652177643d166b502f981777e67bcce`. The
[assembly manifest](current-assembly.json) records the exact artifacts.

- All 20 locked Rust tests, strict Clippy and the optimized build with
  packaged Core 0.2.2 passed. The runtime fixtures covered expired writer
  admission, timeout while reading a provider body, and resuming an
  interrupted schema-4 upload whose offset pointed into a rejected game.
- A disposable local provider feed accepted 700 games and rejected two
  records exactly once, including an unsupported variant. Restart reused
  the staged file. A manual upload completed alongside provider work.
  Following writer contention, the worker recorded a failed provider turn,
  finished a different job, and accepted the original provider job on retry.
- Chrome verified that paging and a delayed refresh preserve the selected
  repertoire and practice color. Branching outside page one used the original
  repertoire and its canonical display example. The previous-release Study
  browser checks covered accepted-but-lost and never-delivered Answers and
  showed that interrupted Next retried only Next.
- The stopped schema-4 database backup passed integrity and foreign-key
  checks. The migration preserved all 21 predecessor tables in both
  directions on predecessor columns and reproduced every repertoire choice.
  Verified one launchd service, schema 5, all served artifact hashes, and
  read-only responses for health, Study, counts, Games jobs, opening
  preferences and repertoire choices. Retained the exact schema-4
  executable with its pre-upgrade backup.

## Lean architecture cleanup

[Tempo #107](https://github.com/tempo-v2/tempo/pull/107) merged schema 4 at
`1fa39971574b37c1ecfcbd45214d114d99ddbcb2`, with a source tree equal to
the qualified head. The managed service ran this merge revision before the
schema-5 cutover. [Planning #90](https://github.com/tempo-v2/.planning/pull/90)
records its installed and qualification artifact identities.

- Rebuilt with the locked inputs in the managed release directory. The served
  HTML, JavaScript and CSS matched the qualified build. The binary hash
  identifies the managed build with its release-specific asset path.
- Rehearsed with a full disposable copy. The stopped schema-3 backup
  passed integrity and foreign-key checks. The actual migration preserved
  all 20 predecessor tables in both directions on predecessor columns,
  and integrity and foreign keys passed before the worker started.
- Verified one registered Lean listener, schema 4, and successful read-only
  responses for health, current Study, Study counts, Games status and opening
  settings. The schema-3 release and matching stopped backup are retained.

- Locked Rust tests, strict Clippy, the production UI build, and the optimized
  executable build passed. Production Next and Again retained bounded SQLite
  work with 100,000 unrelated cards and selected the correct committed slot.
- A full online copy of the managed database migrated with no worker running.
  All 20 predecessor tables matched in both directions on predecessor columns.
  Integrity and foreign keys passed.
- The short PGN job completed while the long job had archived 2 of 300 games.
  Interrupted and uninterrupted runs matched all 301 archive rows, 301
  capture rows and 302 tactic rows. Study accepted Again and advanced during
  Games work. A focused retry fixture reused the saved scan findings. The
  migrated inline-PGN case resumed its original byte offset and cleaned up
  the staged file after completing the remaining record.
- Chrome captured both original Answer envelope cases from the installed
  predecessor and recovered one grade on the candidate. Interrupted Next
  retained the result and retried only Next. Chrome also checked counts,
  authored lead-in playback, Games poll coalescing and visibility, and late
  Study context rejection.
- Fresh independent review cleared `c69ea57e34da6dad4dd34b4bc127eb8a391625f5`.
  Its indexed-claim probe held at 17–18 SQLite VM steps as completed jobs
  grew by 100,000. A 120-request context burst returned bounded refusals
  and independent counts, Games status and Answer stayed usable. A local
  provider fixture resumed only the unprocessed frozen window.
- A disposable probe separated queue wait from execution. With a synthetic
  75 ms writer blocker, Next waited 77.0 ms and ran for 3.3 ms. Idle Again
  waited 0.02 ms and ran for 1.3 ms. These measurements describe the probe.

The schema-3 executable and matching pre-upgrade backup remain the recovery
pair for this cutover.

## Lean operation-boundary cleanup

[Tempo #104](https://github.com/tempo-v2/tempo/pull/104) publishes candidate `2ab49b04b96f21e7b6b293461d41971b7a6fceb5` against managed predecessor `4f97e742b0f259ba3c26109d69aa365d570439f8`. The [Lean operation contract](lean-operation-contract.md) governs this candidate. It uses schema 3 and vendored Core 0.2.2.

The candidate exercises the single write connection, indexed prepared issuance, exact Answer replay, delayed repeat placement, provider separation, bounded Games apply and offline large opening import. A full disposable schema-2 database comparison retained all rows in the 17 predecessor tables. SQLite integrity and foreign keys passed. Previous-version Chrome recovery covered accepted-but-lost and never-delivered Answer followed by a failed and retried Next. Disposable HTTP covered writer saturation, optional provider replacement, staged PGN restart, and over-budget opening and offline import. Tempo #104 merged as `48328ad4b49bbd91fadf2bcd2aa83df9cbea1ede` and the optimized build of that exact main revision is installed. The single registered Lean service at port 41823 runs schema 3 with the retained dataset. A stopped schema-2 backup passed integrity and foreign-key checks. The live comparison matched every row in all 17 predecessor tables, and HTTP served matching HTML, JavaScript and CSS. Study counts [Tempo #105](https://github.com/tempo-v2/tempo/pull/105) was subsequently merged on main.

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

#### Merged and installed on November 18, 2026

The five PR heads matched the reviewed commits. GitHub reported all five
merged into main, and each fetched merge tree matched its reviewed tree.
The [release manifest](manifest.json) records the merge commits and unchanged
Chess, Study, Types, UI and Core pins. The managed build reproduced the
qualified optimized backend and all 22 UI files using the candidate workspace
lock. The source and artifact match carries forward the locked test suite,
independent review and optimized Games recovery evidence above.

The schema 8 to 9 rehearsal ran the qualified pair on a disposable copy of
the current dataset. Existing schema objects and all rows across 22 existing
tables matched. Integrity, foreign keys and the read-only Study status passed.

The managed launcher stopped the schema-8 service, saved a consistent SQLite
backup with its previous registration, and started
`workspace-120682a40a2cf6bf6214` on port 41822. The live database kept its
dataset identity and file inode. Its 22 pre-existing tables matched the
stopped-time backup row for row, and integrity and foreign keys passed.
The registered process owned the listener, all 22 served UI file hashes
matched, and Study status and Games history responded to read-only checks.
F4 and explicit Repair progress counts remain deferred.

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
payload shapes carry forward. At review, the registered service served
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

The independent reviewer accepted the combined heads above. The optimized
binary SHA-256 is
`3ef27d814584666f77adfcccbccca40437c371a457e01412a6d752f5ccdb8945`.

### Managed cutover, November 19, 2026

All four PRs merged to main. Each fetched merge commit's complete Git tree
matched the qualified head. The six reused component main branches matched
the candidate pins.

| Repository | Verified main merge |
| --- | --- |
| Tempo | `380d178fdbdec0dcd2525735068a6292f417f38f` |
| Store | `7a7b45d39697375dcb89957a6ead8b4d3417ef0b` |
| UI | `de7f708aef837768e1b8ce9435ef4e56050fae58` |
| Planning | `cd99ebc1865550882303076f42f248565152e558` |

The managed launcher rehearsed the migration on a disposable copy before
stopping the schema-10 service. It created a private, integrity-checked
SQLite backup and saved the previous registration before changing the
LaunchAgent. The backup and detailed verification are retained locally.

At this cutover, checkpoint `workspace-68dc7fa8e5221063cbf5` was installed
and active on loopback port 41822. The registered process owns the listener and serves
the qualified binary and all 22 verified UI files. The same database and
dataset advanced from schema 10 to 11. The original columns and row counts
of all 28 authoritative tables match the stopped backup in both directions,
including content, Learning, attempts, assessments, games, settings and
receipts. SQLite integrity and foreign-key checks passed. Cache-only
projection settled with two complete books and zero pending.

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

## Stockfish tiebreak for equal nearby support

The approved Fix response rule keeps the existing repertoire priority and
support counts. When two replies have equal support in the same group,
Tempo orders them by the better comparable Stockfish evaluation. An available
comparison sorts ahead of a missing one. Structural distance and move
identity resolve remaining ties. Before engine results arrive, the nearby
list uses structural order within support ties. The completed analysis
returns the same ordering for the list and default selection. The inputs
are distinct-position support, Chess move identity, existing distance, and
the existing learner-relative score comparison. SAN and labels remain display
values. The 50/150 centipawn rules and durable Save contract carry forward.

[Tempo #28](https://github.com/tempo-v2/tempo/pull/28) qualified at
`bd01975ad0bf8bd190ec663ef23bc7db1635a9f7`, based on the installed
explicit Study input release above. Reuse that release's Chess, UI, Store,
Learning, Queue, Study, Types and versioned Core pins. The optimized backend
SHA-256 is `5c5907552ad4e03be703401cf1f60320582401a294494e058a7d33f199004995`.
The packaged UI JS and CSS hashes are
`30dff520aef7ea87564b9fa251458328c6366304bdc1d7b7320fd35b07a382e2` and
`c2584eb9c9e1da000328dc635ed4a20cd31164af4c6b3bb7c572851124d2306d`.

All four focused recommendation tests, 36 UI tests, the guarded build,
and the architecture gate passed. The real Stockfish and Chrome check
recreated the screenshot's London `5…Bg4` board and four equally supported
replies on disposable SQLite data. Chrome suggested `c4` and showed it at
the top of Similar repertoire positions. Learning, attempts, assessments,
receipts and repertoire documents stayed identical. The current live gap
list had no matching London `…Bg4` gap. At that qualification, merge and
installation were pending.

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

### Compact correction notation

Tempo UI [#23](https://github.com/tempo-v2/tempo-ui/pull/23) merged to main at
`da8e883c7bf10ec0f9c33df41d5405b7bb8be0b0`. The correction card displays
contiguous numbered SAN as `1. d4 d5 2. Bf4 Nf6`, retaining `...` when
the line starts with Black. Chess's existing SAN and replay data supply
the display. The count and save use the contracts above.

The matched Chrome journey passed for paired moves, a Black-start fixture,
replay and Next recovery. The merged UI tree matched the tested PR head.
The backend binary matched the SHA-256 above. The managed launcher rehearsed
the candidate and installed `workspace-6d37b569cfafffdcc9d1` on port 41822.
All 22 served UI files matched the qualified build. Read-only Chrome resumed
the existing correction and verified compact SAN with 96 repairs remaining.
All 34 database tables matched stopped-service backup `recovery-start-88eo2t3p`,
including 20,777 Learning records, 228 attempts, 114 assessments and 388
Study receipts. The database file, active attempt, dataset and schema 11
matched, and SQLite integrity and foreign-key checks passed.

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
format 5, and Study wire 5 carry forward.

#### Verified merge to main

| Pull request | Fenced reviewed head | Verified main merge | Verified Git tree |
| --- | --- | --- | --- |
| [Store #15](https://github.com/tempo-v2/tempo-store/pull/15) | `4027bb41cf14425bcbb5f1e8c7467999b0c40a52` | `bac6a78f3d970ea2dfd44fce834370f6cb18d042` | `61090e235be25ff8cf287d2d639bd678b815562a` |
| [Tempo #25](https://github.com/tempo-v2/tempo/pull/25) | `2f1cc242f3373ffffe333fae386d18b4cd683f79` | `d2e6382c29dc22527d27bb2a7d22192ddc58ef70` | `fb4fcc35de17a348f74173d6e21deae2efd9a3e3` |
| [UI #19](https://github.com/tempo-v2/tempo-ui/pull/19) | `046898f1f144652cb8fa0f43b6c74816e7211ba0` | `e40462e4f90bc61a8da4b256d060d9c25b9f9a15` | `80f3a6313bb67a3a672042283d709b77a7ae084a` |
| [Planning #25](https://github.com/tempo-v2/.planning/pull/25) | `06aac77cf9e9b7e55472d5db023133c67335db45` | `68ecc1b727de035a26aa331c09a05c0ede160206` | `eb0b3cbab823d5f445a11c56e5df7d4751192ca4` |

GitHub's merge previews matched the qualified trees and their expected
parents. The main branches matched the verified snapshot before merging.
Each merge used its exact reviewed head, and the remote merge commits
matched the qualified trees and the same parent pairs. A final check of
all nine runtime repositories matched the qualified assembly, including
the six companion trees.

The release-host package was rechecked on disk against the optimized
binary digest and all 22 UI hashes.

#### Managed installation and live acceptance

On November 19, the separately authorized managed install replaced
`workspace-7ed579a4d29162fc4fdc` with
`workspace-6406aa4f8658cb73dd62` on registered port 41822. The managed
rebuild matched the exact qualified package before cutover. The loaded
registration and the actual listener identified the installed Mach-O
binary at SHA-256
`b442484f85da2d3615534c7a84ec4700f80c9af8202e03a29b4827747b197798`.
All 22 files on disk and served over HTTP matched the final artifact
hashes. The first rehearsal exceeded the launcher's one-second health
probe before it stopped the previous service. A disposable startup
check passed and the standard managed retry completed the cutover.

The stopped-service database and prior registration are in
`.local/usable-release/recovery-start-l8gh2ud5`. The backup database
SHA-256 is
`6147f710c5d97ea92b03586df79e6e4dd4c0d63bee75f111e9272225e714a1d6`.
The prior registered executable and its 22 UI files still match their
pre-install hashes.

The live service reported the same SQLite file, dataset, schema 11 and
active Study attempt. Chrome used the read-only Resume command, verified
the retained position, and opened Games. History returned 100 rows and
the authoritative historical status was complete. The smoke sent zero
mutations. Study reported zero remaining guided corrections, so the
correction-context and same-tab Retry journeys remain covered by the
qualified disposable tests. After the live smoke, all 34 tables matched
the stopped-service backup row for row, including 20,783 Learning rows,
325 attempts, 115 assessments, and 485 Study receipts. Integrity and
foreign-key checks passed on both copies.

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

## Phone Study deployment, November 19, 2026

| Decision | Authority, inputs and lifetime |
| --- | --- |
| Admit a phone request | The approved phone release is online and private to the configured owner. Tempo HTTP uses Tailscale's forwarded HTTPS authority and login, the exact configured origin for POST, and the Study path and method allowlist. The managed registration retains the opt-in over restart. Public Funnel traffic and foreign origins are denied. |
| Select and save a Study attempt | The phone embeds the same Study session and calls the existing commands against the retained dataset. The shell supplies navigation and analysis availability. The application's authored Study context, receipt identity and durable grading rules apply at both origins, independent of display name and device. |

Tempo [#34](https://github.com/tempo-v2/tempo/pull/34) publishes code
built at `0167d0e210d97a1453a5709a3f980cc211e1e653`. The PR head
`eef61a152d6a6e5584fc336b441dc263fa5cae2e` adds the documented Serve off command.
UI [#28](https://github.com/tempo-v2/tempo-ui/pull/28) publishes and serves
`835d2b003295d92066b8ac57f97f6751f00f708a`. The [manifest](manifest.json)
records the compatible sources, Core package, locks and installed hashes.

The optimized locked build, 51 Tempo tests and 63 UI tests passed.
Packaged WebKit with iPhone touch input solved two tactics and confirmed
the same active attempt over the desktop API. An accepted answer with a
lost reply replayed its original bytes and had one grade and receipt. A
failed Next preserved the answer and retried only Next. Inline corrective
replay remained available. Independent packaged Chrome verification
covered desktop corrective Study, interrupted Next and standalone analysis.
The managed installer rehearsed both surfaces on a disposable copy of the
retained schema-11 database. A separate disposable copy of the stopped-time
backup returned the same active attempt on desktop and phone. The phone API
completed the first 12 exercises in order. All 12 were opening exercises.

The registered service installed `workspace-7d86fed76f7dde27c227`
on port 41822. The database kept its inode and schema, and all 34 tables
matched the stopped-time backup `recovery-start-esy5gyj0`. Integrity and
foreign-key checks passed. All 22 desktop and 24 phone assets matched the
installed files through their respective routes. Tailscale Serve on 8443
served the phone bundle privately and reported the same dataset as
desktop Study. Games, repertoire writes, and requests with a mismatched
Origin or loopback Host were rejected through the actual proxy. The
existing Tempo 1 route still responded. Three separate lab processes
were preserved. Actual iPhone Safari over cellular acceptance is pending.

### Phone continuation overlay, November 20, 2026

The phone shell places manual continuation, guided acknowledgement and
command recovery directly below the board. The board reserves the space
across moves and delivery states. Tempo UI uses the existing action selection
and handlers. When Study has no board, controls use the information panel.

UI [#28](https://github.com/tempo-v2/tempo-ui/pull/28) publishes
`ccf29c8684994d6fd48c8ae713a385b2044bc640`. Packaged WebKit at 375 × 600
confirmed that Continue, guided acknowledgement, Retry and Retry next
exercise each fit in view without moving the board or panel or changing the
scroll position. The journey verified an accepted answer and receipt, a Next
retry, a review completed after a miss and one guided acknowledgement.
All 63 UI tests and the desktop Chrome corrective Study journey passed.

The managed MacBook installation serves `workspace-f9f3e6bff02e198a60e1`.
All 24 private HTTPS phone assets and 22 local desktop assets matched the
installed build. The backend hash, Study dataset, database inode, schema 11
and Serve configuration matched the prior release. All 34 tables matched
the stopped-time backup `recovery-start-4ctmzui5`. Integrity and foreign keys
passed. The [manifest](manifest.json) records the installed bundle hashes.

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

### Retained draft and consistent repertoire evidence

Game navigation changes what is being viewed. The retained draft changes on deliberate authoring, explicit discard, or confirmed save. Its original game, range and continuation must survive browsing and return. The selected destination and its reviewed version govern preview and save. Repertoire evidence must describe the same dataset, book and version as the displayed review, including after asynchronous replies or another edit. A stale comparison offers a fresh read. Board position, column visibility and move ordering grant no permission to change content or learning.

Admission to the move table is a presentation choice over a bounded set of relevant moves. A source supplies its measurements for those rows. An exact zero remains a value. No pending or failed source can answer for another. Study determines when an answer may be shown before analysis opens. The signed authoring command and its stored delivery identity still govern an actual save.

Implemented and verified on the isolated instances. [UI #27](https://github.com/tempo-v2/tempo-ui/pull/27) is at `d16ead4f2dec84dbfffe80d2b2c572f2e8e0e75e`. [Tempo #33](https://github.com/tempo-v2/tempo/pull/33) is at `26ac49a1c1406c5d0b2c34ec285bcc3f8f8a0650`. The preceding Chess, Store and packed Core pins still apply. All three local instances served the built assets byte-for-byte.

- Reproduced losing the reply on return to the game before the fix. Afterward Chrome covered backward navigation, competing branches, explicit replace/discard, switching destinations, library return, reload and save while viewing a different board. The independent reviewer reproduced and then verified the fix for a late preview after a second tab discarded its draft. Lost-response replay used the original signed command and preserved a newer edit.
- The application rejects evidence for the wrong repertoire, document or content revision. A real document replacement during an open review removed stale Saved cells, then showed the new response after reload. The candidate browser test distinguishes measured zero, missing, pending and unavailable. The full board also exercised pinning and authoring with the explicit legal-move list.
- The 96 UI tests, shared-board drag/promotion journey, signed editor restart/replay journey and scheduled Study analysis disclosure test passed. The personal walkthrough preview listed one new position, zero changed answers and zero retired positions. Its one accepted save created one content receipt and one unintroduced target. Existing learning rows, target identities and versions, attempts, assessments, game evidence, quotas and Study receipts matched the pre-save snapshot. Only the selected book’s document changed.
- [Walkthrough](postgame-prototype/README.md#keeping-a-draft-while-looking-around). The private game, screenshots and local browser profile are on Andy’s machine. No production release was requested or installed.

### Stale review warning

A detected repertoire-version mismatch belongs to the loaded game comparison. Its owner retains the warning and reload action through board navigation, source visibility changes and failed reloads. Only a successful fresh review replaces the earlier comparison. The warning is presentation state and never writes repertoire or learning data.

UI candidate `e3392f853eb3d42f95400fb8c5afc445c20f51ab` extends [UI #27](https://github.com/tempo-v2/tempo-ui/pull/27). The Chrome regression edits the destination from e4 to c4 during review, observes the mismatch, changes source visibility, closes comparison, navigates forward and back, and forces one failed reload. The warning and its reload action survive. The successful reload shows c4 and clears the warning. All 96 UI tests passed. The preceding runtime and package pins still apply.

## Lichess analysis release

The compact **↗ Lichess** action opens the full issued tactic or the
first matching opening variation in PGN order. Replay exports use the
full loaded line. Boards with only a position open that position. Long
lines offer a complete PGN download for manual import.

| Decision | Basis, owner, inputs and lifetime |
| --- | --- |
| Authorize an analysis read | Tempo checks dataset, attempt, revision, issued content version and activity state for both position context and line export. A confirmed unfinished Test uses the existing concession and its immutable receipt. Display names and board orientation are independent of that decision. |
| Read the export line | The ordinary analysis board loads its position context. A Lichess action requests a separate read. Chess finds the first legal authored route matching the issued canonical position and prescribed move. A tactic uses its issued definition. A missing matching route yields the retained issued move. A failed document lookup or parse returns an error that the user can retry from the open board. |
| Own the external tab | Tempo UI reserves one tab for the initiating Study visit. Leaving Study or hiding the page cancels an outstanding launch, and late acceptance remains available through normal Study recovery. The initiating board supplies orientation for automatic launch. The visible Analysis board supplies orientation for its manual link. |

| Component | Verified main merge | Pull request |
| --- | --- | --- |
| Chess | `268bd292b18396880740f24ca2c471728c6651d1` | [#19](https://github.com/tempo-v2/tempo-chess/pull/19) |
| Tempo | `c8e3ac75b26f960cc33737ea1fe744c20db4ca66` | [#35](https://github.com/tempo-v2/tempo/pull/35) |
| UI | `b1f89c6d6c45ed4df935d68623bc221a04c1703c` | [#30](https://github.com/tempo-v2/tempo-ui/pull/30) |

The final independent Astra review passed on the reconciled PR heads.
The Tempo main merge incorporated concurrent Phone ingress and
repertoire recommendation work. The Lichess application projection,
contract tests and desktop route additions matched the reviewed change.
The reconciled Chess and Tempo suites passed 219 tests and doctests.
The reconciled UI passed 100 tests.

Packaged Chromium on disposable SQLite verified the final puzzle ply,
cancellation before acceptance, display-name invariance, one Again,
previous-release recovery with the original command, an interrupted Next,
and the replay cursor. It reproduced a document read failure and a PGN
parse failure and kept ordinary Analyze available. It exercised a
repurposed tab, a position read failure, reload and browser Back during
a pending concession. Phone WebKit ran the optimized release assembly
and verified touch Study, continuation and retry placement, inline
repair, and the private ingress restrictions. In earlier live HTTP
checks Lichess returned the exact inline sample PGN and orientation.
Direct headless rendering at Lichess returned HTTP 403.

### Managed installation

The installed build adds Lichess to desktop Tempo and carries forward
the active Phone Study profile through the published release refs.
The separate post-game prototype remains on its isolated origins.

| Installed source | Commit |
| --- | --- |
| [Tempo release assembly](https://github.com/tempo-v2/tempo/tree/release/lichess-with-phone) | `b93ec26b9dc86f2161c031eb0d997cefb8913b03` |
| [UI release assembly](https://github.com/tempo-v2/tempo-ui/tree/release/lichess-with-phone) | `678fe423a7cfd6056c934f3ae848435850e1e361` |
| [Chess feature head](https://github.com/tempo-v2/tempo-chess/commit/7be682bcb8d48dbd6433ccb697cec573a370db29) | `7be682bcb8d48dbd6433ccb697cec573a370db29` |

The assembly also used Store `bac6a78f3d970ea2dfd44fce834370f6cb18d042`, Learning `09c4359ab90d0cd1e5166b1f25460fd272406fd1`, Queue
`a171e70faf684dead33f04ad455012380fcb2e54`, Study `4b46e6c45a6330177b089eadcae69821e57b6657`, Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core `e9a1d160a729bc9fbbddaf16427625301cc9498a` with
the packed Core 0.2.2 tarball. It reused the corrective portability
workspace Cargo lock.

The managed launcher installed `workspace-c4afffae8dea3aea9fd1` on port 41822 after a
disposable database rehearsal. The optimized executable SHA-256 is
`37598f8b6b5c0b06c4ae5d0ff56457195aa8b075c8eb9f7f6cd37fdfc9308d50`. The registered listener served all 46 qualified desktop and
phone files byte for byte. The Phone profile still returns its Study
status and confines Lichess export to desktop. The three development
listeners kept their original processes.

The retained SQLite file kept its inode, dataset, active attempt, and
schema 11. All 34 tables matched the stopped-service backup `recovery-start-4m9w3v5q` row
for row. SQLite integrity and foreign-key checks passed on both files.


## Historical PR reconciliation, November 20, 2026

Six documentation PRs had contained historical records missing from main.
Their historical evidence is retained in the corresponding sections above.
The source observations were recorded during the original qualifications and
cutovers; this reconciliation does not revalidate or change the running service.

| Source PR | Preserved source head | Record and closure rationale |
| --- | --- | --- |
| [Planning #19](https://github.com/tempo-v2/.planning/pull/19) | `147c6361d7dd0656391ddd025861632f8103bdf2` | Schema-9 corrective Study installation and its exact manifest. |
| [Planning #22](https://github.com/tempo-v2/.planning/pull/22) | `69e5b9713a72faa6b36d4b15226cf643dc1fe401` | Schema-11 merge trees, managed cutover and data-preservation observations. |
| [Planning #28](https://github.com/tempo-v2/.planning/pull/28) | `3776e39c25792a8f62e4ee4d38655422b64b9526` | Stockfish tiebreak behavior, compatible artifacts and original qualification. |
| [Planning #30](https://github.com/tempo-v2/.planning/pull/30) | `c26c9ab4759d064683c9008ba26e3b84c021f797` | Compact correction notation installation and retained-data checks. |
| [Planning #32](https://github.com/tempo-v2/.planning/pull/32) | `b8956ba3ce09274507c7e76649274512ef12ea95` | Corrective release merges, artifact identities, backup and live acceptance. |
| [Planning #36](https://github.com/tempo-v2/.planning/pull/36) | `28c8484b0514ff40ec75f6964bd6fd153f4574fa` | Original private Phone Study deployment and November 20 continuation-overlay installation. |

The manifest's `historical_delivery_records` preserves the additional structured
records from #19 and #22 without changing any existing release or active-state
field. Their activation flags describe the recorded cutover only. The two Phone
Study manifest entries retain their original component pins and installed hashes
exactly. Those observations do not establish the current live installation.

### Repository integration observed during cleanup

GitHub readback on November 20 confirmed the nine interface PRs and five
post-game PRs below merged. The reconciliation started at Planning main
`1f1a5734ee4decbbf06f13f85fe025c0e3948c99` and incorporates concurrent main
`3be85c922684398199ce6d5e89644319ff290214`; the original qualification records,
component pins, package hashes and post-game evidence already on that main are
preserved. These are repository integrations, not new installations.

| Family | PR | Reviewed source head | Main merge |
| --- | --- | --- | --- |
| Interface | [tempo #32](https://github.com/tempo-v2/tempo/pull/32) | `89ba3123a40ec5b7cc35ea185a4817f2b2424e4f` | `8124e9399abfef54817994b96b6be766f4a264e4` |
| Interface | [tempo-ui #26](https://github.com/tempo-v2/tempo-ui/pull/26) | `2fd49d22916b997a8dd0b26d7bc1d18b8aac3a84` | `1ac53554585de7a06589592953b671f22d4fdb1b` |
| Interface | [tempo-chess #17](https://github.com/tempo-v2/tempo-chess/pull/17) | `849bcf4793ff9fc7081e91e3425713e84e153a97` | `39ffd194133df173d6aa0a295f950ab3e5eac6e7` |
| Interface | [tempo-learning #6](https://github.com/tempo-v2/tempo-learning/pull/6) | `8fe06ca10a5249b1619bba26b016f38f961a84dc` | `58197f6fa9b2ea33907f2e305ec07efda64d553d` |
| Interface | [tempo-queue #10](https://github.com/tempo-v2/tempo-queue/pull/10) | `c3b1169e3bc4990ed3e61f2d1e7a28a27328ead2` | `777345256564cefa7f25d537a5a7c51a5377e749` |
| Interface | [tempo-study #3](https://github.com/tempo-v2/tempo-study/pull/3) | `bf18a3eb827237d132763afd8fec483e06c9eb25` | `ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb` |
| Interface | [tempo-store #16](https://github.com/tempo-v2/tempo-store/pull/16) | `be8dcd2ec2039d5d3bf43acd029cbcabb0f710aa` | `8d6b4dee9788e5d1eaee2e415cdb7a8d44d93457` |
| Interface | [tempo-core-components #6](https://github.com/tempo-v2/tempo-core-components/pull/6) | `c740dac85f2f8e7124c25b31125ef0db81d9131c` | `99364f6d47a0467ed1cf0edf6a904566dc720dd6` |
| Interface | [Planning #34](https://github.com/tempo-v2/.planning/pull/34) | `3375d0ae86f2b14818f2ac1a76612dd81de60238` | `027a9f6f2b5bd18c4c656be9d7082dc46ce696c6` |
| Post-game | [tempo #33](https://github.com/tempo-v2/tempo/pull/33) | `26ac49a1c1406c5d0b2c34ec285bcc3f8f8a0650` | `9e93d008d5615731b8145c685e07026ab505a339` |
| Post-game | [tempo-ui #27](https://github.com/tempo-v2/tempo-ui/pull/27) | `e3392f853eb3d42f95400fb8c5afc445c20f51ab` | `eb9a67ee1101bc6aada10f85d457193168fdb6ea` |
| Post-game | [tempo-store #17](https://github.com/tempo-v2/tempo-store/pull/17) | `9bc90f179ca2e85ccb9a75a3aae7ffcf6bd23dc9` | `dc99718d3d3e8991be2fd9864abdceac623a4e07` |
| Post-game | [tempo-chess #18](https://github.com/tempo-v2/tempo-chess/pull/18) | `a5dcf40e3f51bfa5ff45f9c466922ca541965706` | `692e229a441fa563271db28d5073e6cbc06fc257` |
| Post-game | [Planning #35](https://github.com/tempo-v2/.planning/pull/35) | `b68a0697b814faccd19b0bbd14f79b6493246a2e` | `1f1a5734ee4decbbf06f13f85fe025c0e3948c99` |

The Stockfish tiebreak [Tempo #28](https://github.com/tempo-v2/tempo/pull/28)
subsequently merged at `ca2529b22884ace7b3ee61cc14911eb800019d89`. Its merged
tree `f27c0b70adb0ca73c2749554a320ce8e7c56d7d5` matches the inspected clean
combination with the accepted interface and post-game work.

Phone's backend [Tempo #34](https://github.com/tempo-v2/tempo/pull/34) was
reconciled and merged at `8899067d3310cd0a6e15db06174c20d399880f16`. The
published head was `971c11bf10627c571b06040587b48ae7281f4f0a`, with qualified
source tree `814cdf625bd8d9773effb851cdf9104faefb1ae9`.
A concurrent Lichess release then merged Tempo #35 at
`c8e3ac75b26f960cc33737ea1fe744c20db4ca66` and Chess #19 at
`268bd292b18396880740f24ca2c471728c6651d1`. A fresh locked build and the two
SQLite Study-analysis contracts passed against those actual mains. The phone
HTTP regression also passed, including denial of the new desktop-only
`/api/study/analysis-line` route. This records the other workstream's observed
merges without claiming ownership of them.

Phone UI [#28](https://github.com/tempo-v2/tempo-ui/pull/28) was reconciled
with the actual desktop main and merged at
`81d0802e4768a971cf8d246317cbee420e5d6633` from published reviewed head
`08bee296bb81db13cf4e00e57f740f0483702104`. Its accepted tree is
`b8e785ec3bbdd7243c15d04b64e81fc543beeb9e`. All 107 UI tests and the dual
desktop/phone build passed. The mounted real desktop Lichess flow performed
its analysis-line read exactly once; the phone surface did not expose analysis.
A fresh browser launch in the cleanup environment was blocked by `EPERM`, so
this cleanup does not claim a new browser pass. The earlier source-release
browser evidence above remains historical evidence, with its original scope.

### Verified PR closeout

This cleanup merged 17 previously open PRs: nine interface, five post-game,
one Stockfish tiebreak and two Phone Study PRs. It also merged the new
[consolidation PR #40](https://github.com/tempo-v2/.planning/pull/40) at
`027992c1dc609b67e59d492879d73f31ee3047ae`, preserving the six historical
records above. GitHub readback verified Planning #19, #22, #28, #30, #32 and
#36 closed without merge after that consolidation. Their source heads remain
the historical references; their useful evidence was preserved on main.

Other workstreams separately merged the four Lichess PRs and four Review later
PRs from the original inventory. Those eight resolutions are not counted as
merges performed by this cleanup. All 31 originally open PRs are resolved.
The later Review later installation record is preserved below without alteration.

### Verified branch cleanup

All 148 allowlisted stale refs were deleted. Independent GitHub API and Git
`ls-remote --heads` inventories completed at 2026-11-20 14:25:38 UTC confirmed
every deletion across all ten repositories. The two inventories agreed on every
remaining head. There were no expected-SHA mismatches, unexpected survivors,
missing retained refs, or missing active PR heads or bases.

Exactly 38 branches remained: ten main branches and 28 retained non-main refs.
The [branch ledger](pr-cleanup-branches-2026-11-20.json) records the 148 deleted
refs, their original expected SHAs, verification method and timestamps. It also
retains one withdrawn entry: Planning's `prototype/postgame-workbench` was
preserved as the base of active PR #39. No active branch was deleted.

| Repository | Deleted refs | Retained non-main refs |
| --- | ---: | --- |
| `tempo` | 28 | `feat/hanging-material`, `feat/lichess-analysis`, `feat/phone-study`, `feat/study-review-later`, `prototype/postgame-workbench`, `release/lichess-with-phone` |
| `tempo-ui` | 23 | `feat/hanging-material`, `feat/lichess-analysis`, `feat/phone-study`, `feat/study-review-later`, `prototype/postgame-workbench`, `release/lichess-with-phone` |
| `tempo-chess` | 17 | `feat/hanging-material`, `feat/lichess-analysis`, `prototype/postgame-workbench` |
| `tempo-store` | 15 | `feat/hanging-material`, `feat/study-review-later`, `prototype/postgame-workbench` |
| `tempo-learning` | 8 | `feat/hanging-material`, `feat/production-evidence-interfaces` |
| `tempo-queue` | 10 | `feat/hanging-material`, `feat/production-evidence-interfaces` |
| `tempo-study` | 6 | None |
| `tempo-core-components` | 6 | None |
| `tempo-types` | 3 | None |
| `.planning` | 32 | `docs/study-review-later-installed`, `feat/hanging-material`, `feat/lichess-analysis`, `feat/phone-study`, `feat/study-review-later`, `prototype/postgame-workbench` |

The manifest records the exact heads of all retained refs and the seven active
PRs. Retained source and release branches remain available to their concurrent
workstreams. This verification applies to the repository cleanup; it does not
assert a new installation or a current running application identity.

### Remaining active work

GitHub readback at 2026-11-20 14:25 UTC found seven open draft PRs, all in the
hanging-material feature. Their heads and integration bases remain outside
stale-branch disposal. Review later is already merged; it is not in this open
cohort.

| Component | Active PR | Protected base |
| --- | --- | --- |
| Planning | [#39](https://github.com/tempo-v2/.planning/pull/39) | `prototype/postgame-workbench` |
| Tempo | [#37](https://github.com/tempo-v2/tempo/pull/37) | `prototype/postgame-workbench` |
| UI | [#31](https://github.com/tempo-v2/tempo-ui/pull/31) | `prototype/postgame-workbench` |
| Chess | [#20](https://github.com/tempo-v2/tempo-chess/pull/20) | `prototype/postgame-workbench` |
| Store | [#19](https://github.com/tempo-v2/tempo-store/pull/19) | `prototype/postgame-workbench` |
| Queue | [#11](https://github.com/tempo-v2/tempo-queue/pull/11) | `feat/production-evidence-interfaces` |
| Learning | [#7](https://github.com/tempo-v2/tempo-learning/pull/7) | `feat/production-evidence-interfaces` |

The Phone and concurrent Lichess installation paragraphs above preserve the
original source handoffs' recorded deployments. This cleanup has not installed
or revalidated a running package and does not assert a current running identity.
The physical iPhone cellular acceptance remained pending in the source handoff;
no new observation here changes that status.

## Review later in Study

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Save an issued decision for later review | The approved Study request allows marking at any time on desktop and private Phone Study. Tempo addresses the reached decision by dataset, attempt, issued content version and index. Store deduplicates the versioned target and decision and records mutation receipts separately from Study. Exercise text, board orientation and subsequent answers do not determine what was saved. |
| Open a saved decision | The existing Analysis disclosure contract and the approved rule for skipped blind cards govern the desktop read. Tempo checks authoritative mode, progress and result, including a later completion of the same version, and checks for a live blind attempt on the target. The analysis position follows the issued definition across edits. The list and save reply contain no answer. |
| Retain marks and replay writes | Store ties marks to the source attempt and preserves them through a normal restart or SQLite backup. A repertoire history reset removes marks tied to erased attempts. Replaying a command acknowledges the original write, even after removal, without recreating the mark. Portable content and learning exports omit attempt-linked marks. |

A revealed reply is a Study decision fact. Tempo records the exact cursor
when an accepted answer, Show move, or concession discloses the response.
Store retains the newest such fact and the revision at which the attempt
was issued. Saved Analysis checks the source or a later closed attempt of
the same version. Complete attempts cover the full definition. An
abandoned attempt can supply evidence for an explicitly revealed
decision and the solved prefix before it. A plain skip at an unanswered
decision supplies no disclosure. A live blind attempt on the target
takes precedence. Study receipt fingerprints remain replay identities.
The Store adapter can read typed feedback from a legacy Study receipt
when a retained attempt predates the explicit fields. Older closed
attempts without retained evidence of an exact reveal stay locked.
Store supplies the later completion and reveal facts. Tempo judges
whether they cover the marked decision.

A Study change from another tab invalidates the saved board's disclosure
until the user opens it again. This also holds if the Study response is
lost. Returning to a visible page without a Study change rechecks
authorization while concealing the board, then restores its variations
and marked lines if verification succeeds. A journaled repertoire save
retains its exact retry control even while the board is concealed.

### Combined candidate

| Component | Reviewed commit | Pull request |
| --- | --- | --- |
| Tempo | `71cbade9958624719a8f5bc7725cca44e42400e6` | [#36](https://github.com/tempo-v2/tempo/pull/36) |
| UI | `e33c2fc3041ec4dc7a274e6789bb347e79a21225` | [#29](https://github.com/tempo-v2/tempo-ui/pull/29) |
| Store | `4cb4e4136d4201dbd236f993c2d2f79cfd06cfbe` | [#18](https://github.com/tempo-v2/tempo-store/pull/18) |

The [manifest](manifest.json) pins the compatible components, existing Cargo
lock, current UI lock, packaged Core 0.2.2, and qualified artifact hashes.
The candidate includes the merged StudyState interfaces, Phone Study and
Lichess analysis. SQLite advances from schema 11 to 12. Study wire v5 and
portable format 5 carry forward.

Independent Astra review traced the Study disclosure producer, Store
facts, Tempo projection, browser invalidation, and exact signed Save
recovery. The review led to typed reveal evidence, same-version
later-attempt coverage, and fail-closed invalidation of a saved view when
a second browser tab changes Study. The signed Save retry stays visible
while the board is concealed.

The optimized locked build, 31 Store tests, 55 Tempo contracts, 107 UI
tests, and architecture gate with its four self-tests passed. Desktop
Chrome covered exact positions before and after response, metadata
invariance, later completion and concession, stable deduplication,
removal and restart. It held a second tab's blind admission before
delivery, dropped its accepted response, and verified the earlier
board stayed concealed. The interrupted repertoire Save replayed
the byte-identical pending command from the concealed board. Phone
WebKit covered the shared list, lost-mark retry, and the continuation
controls. The packaged Lichess journey covered answer-safe export,
lost-concession retry, help after dismissal, and interrupted Next.

The candidate rehearsed against the stopped-time SQLite backup
`recovery-start-4m9w3v5q`. All rows in the 34 prior tables matched, and
integrity and foreign-key checks passed. Chrome used the previous
installed executable and UI at `workspace-c4afffae8dea3aea9fd1` to
leave accepted-lost and unaccepted Study commands pending. The
candidate replayed the original bytes with one grade per case.
Interrupted Next retried only Next.

The three runtime PRs merged into main. Their remote merge trees match
the qualified trees exactly. The manifest records both the reviewed heads
and the merged component revisions.

### Managed installation, November 20, 2026

The registered service activated `workspace-cc3cf48ea9fd2222131b` on port
41822. The launcher rehearsed the merged pair, then saved the stopped-time
SQLite database and prior registration as `recovery-start-_tvm060e`.

The running service matched the qualified binary and all
22 desktop and 24 private HTTPS phone assets byte for byte.
SQLite is at schema 12 on the same database file and dataset. The active
attempt and every row in the 34 previous tables matched the backup.
Integrity and foreign-key checks passed. Passive Study responded on both
surfaces. The desktop list read successfully, the phone save route
accepted validation, and the phone list route returned 404. The
observed installation in the [manifest](manifest.json) closes the release.

## Tactic capture from the board, November 20, 2026

Desktop Tactics Capture adds **Build a tactic** alongside PGN import. Set the
starting position on the board or through FEN, then play the line or append
pasted SAN. **Save tactic** runs the existing Preview and Save in one action.

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Compose one solver-first line | The capture request establishes the applied position and its side to move as the solver's start. Tempo UI projects the local draft and generates PGN with zero setup plies. Board and SAN entry produce the same PGN for the same position and moves. Whitespace, optional SAN numbering and reordered castling flags are presentation differences. |
| Validate and accept the capture | The existing tactic PGN contract gives Chess authority over position and line legality. Tempo accepts only the single valid, signed record for the same PGN and dataset. Existing capture rules determine identity, learning, and receipt effects. |
| Recover after uncertain delivery | Tempo UI retains the exact Save command in the existing recovery journal. Store replays its receipt if the command already committed. The editable drafts are page-local. |

[Tempo UI #33](https://github.com/tempo-v2/tempo-ui/pull/33) carries
`e36d214f68083a7c8ba67f22e29f6a4a5f65f792`. Qualify it with the other merged
component revisions in the `study-review-later` entry of the
[release manifest](manifest.json), including Tempo
`846fae8fa1444ddf8b00e1793e935073ac030b7c` and the packaged Core 0.2.2.
The existing UI lock and Core tarball match that entry. The candidate desktop
JavaScript SHA-256 is `9896c6b85abded82dbdeb42d969fa8fb89327eb85ecb76525c17e59a46db791e`.
The stylesheet SHA-256 is `fa152f8b2b84ee67b9b58c9f8b662f41be38445d0c660844e501d9299ed305eb`.

All 111 UI tests and four package boundary checks passed. Chrome exercised
desktop and narrow layouts against the matched Tempo binary on disposable
SQLite data. It covered board editing, FEN including reordered castling
rights, mixed board and SAN entry, atomic rejection of invalid SAN, promotion
choice, PGN import, and the saved position and solution in Tactics. The invalid
server preview issued zero Saves. After a successful reply was dropped,
reload replayed the original Save bytes and left one tactic, one source, one
receipt, and one learning row with zero assessments. Independent review traced
the validation and recovery path and ran nine focused UI checks. Chrome was
run in the implementation environment with local browser and port access.

### Independent review and managed installation

A fresh Astra review of the published heads found no interface ownership or
coupling blocker. It independently passed nine focused tests and the Chrome
capture journey, including exact Save recovery on disposable SQLite data.

Tempo UI #33 merged as `8321754ca28f2e34bd45b6d2c5102218bc33ba06`. Its merge
diff matches the reviewed diff. Repertoire suspension had also merged and
been installed, so the combined release uses its Tempo
`7f8060cabd1f03efa7faac27275f50dcd0e1a3a4`, Store
`27ffcc992d4b12424c1208676ae594d4245277e9`, and other pinned components.
The combined release passed 111 UI tests, both desktop Chrome journeys,
and Phone Study in WebKit. The backend rebuilt byte for byte against the
installed suspension baseline. The combined desktop JavaScript SHA-256 is
`6b0b7e8af45d06982e805acc2da857214e88e2c83b93387b2de61b3bd004ff60`.

The managed launcher activated `workspace-73d00fe272ee6d48eff4` on port
41822 after rehearsal, with stopped-time recovery `recovery-start-firzf3oa`.
The registered process served the built 22 desktop and 24 private phone
assets byte for byte. Both Study status reads returned the retained dataset.
SQLite retained schema 13 and the original database file. Integrity and
foreign keys passed. Thirty tables matched the backup exactly. Verified
receipts for a live repertoire suspension and a Study answer with its next
attempt accounted for the other eight tables after restart.

## Repertoire suspension candidate

**Suspend** in Repertoires pauses one book indefinitely. **Resume** restores
eligibility under the saved schedule, including reviews that became due in the
meantime. The repertoire stays visible and editable.

| Decision | Basis, owner, inputs and lifetime |
| --- | --- |
| Change repertoire activity | The requested control uses dataset identity, repertoire identity, and an explicit Active or Suspended choice. Tempo asks Study to abandon an unfinished matching attempt without grading. Store validates and saves that transition, the setting, and the receipt atomically. Display name, learner color, PGN shape, and other repertoires are independent of the command. The setting persists in SQLite and full database backups. The portable content-and-learning format keeps its existing scope. |
| Invalidate the affected reads | Store supplies a Games comparison basis with authored content and participation revisions. Participation changes also advance the Study revision. Authored editor drafts and signed PGN Save use the authored revision. The UI identifies Games evidence scope explicitly, independently of document version pinning. Historical corrective choices whose compared repertoire scope diverges carry an application-projected status asking for a new comparison. |
| Select Daily Study | Tempo supplies participating targets and routes to Queue. Suspension excludes due work, teaching, and corrective repair and recall. It retains the existing schedule, accepted results and same-day allowance usage. Exact replays keep their accepted result, and an old suspension receipt cannot undo Resume. |
| Check game coverage | New comparisons, gaps, and Maia work use participating repertoires. Raw game import and the played timeline remain available. Historical summaries, encounters, and gaps are retained, including when an old game is processed again during suspension. Resume permits subsequent checks under the usual rules. Existing corrective choices retain their authoritative attribution, including when the chosen book is suspended. |

| Component | Qualified commit | Pull request |
| --- | --- | --- |
| Store | `4d7f57593601f245d1b19a7f7a83aa5abfda6494` | [#20](https://github.com/tempo-v2/tempo-store/pull/20) |
| Tempo | `4cd489a8adeeb2ab2d304229eb809905796fe2f8` | [#38](https://github.com/tempo-v2/tempo/pull/38) |
| UI | `abd711ede99f679b7b77e3cb8580b3048c227ad1` | [#32](https://github.com/tempo-v2/tempo-ui/pull/32) |

Assemble with Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`,
Study `ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`,
Queue `777345256564cefa7f25d537a5a7c51a5377e749`,
Chess `268bd292b18396880740f24ca2c471728c6651d1`,
Learning `58197f6fa9b2ea33907f2e305ec07efda64d553d`, and
Core `99364f6d47a0467ed1cf0edf6a904566dc720dd6`
with packaged Core 0.2.2. Reuse the prior workspace Cargo lock
`c03a5547d570957d60c51510c5e1a438d5b60db59fd3aee1996378e2765943c0`.
UI lock SHA-256 is
`f713bbeded47625dd599dd75bf123ebe57d51c1a22336e94f2f6c15e05c4fe23`.
SQLite advances to schema 13. Study wire 5, content wire 4 and portable
format 5 carry forward. The repertoire list adds an optional activity field
for compatibility with earlier serialized Save replies.

The architecture checks, 174 Tempo and Store Rust tests and doctests, and
107 UI tests passed. The Study contract covered new and due work, an issued
lesson, rename and replacement while suspended, preserved grades and receipts,
restart, and unchanged activity from another repertoire. The Games contract
covered overlapping repertoires, raw game review, suppressed coverage and
Maia inputs, and existing gaps returning after Resume. A fault-injected
receipt failure rolled back the suspension and abandonment together.

Desktop Chrome exercised cancel, suspend, a lost accepted response, restart,
byte-identical replay, and Resume. Independent review ran nine mounted Study
metadata cases and six accepted-lost and unaccepted Answer, Learn more
tactics, and PGN Save cases using the actual installed predecessor. It
verified exact delivery and a single durable effect in each case, including
the previous PGN Save reply shape and Retry Next without another acceptance.
The schema-12 to schema-13 rehearsal on a disposable copy preserved all
37 previous tables and objects. Integrity, foreign keys, Study and Repertoires
readback passed.

### Astra interface review

The first review identified five issues. The candidate now uses separate
participation and authoring revisions, moves the abandonment decision to
Tempo and Study, carries Games evidence scope explicitly, projects stale
historical choice availability in Tempo, and preserves existing choice
attribution when a book leaves the comparison. Focused tests on disposable
data cover an unaffected signed edit, unpinned Games evidence, the projected
choice status, and both reprocessing and startup reconciliation after suspending
a previously chosen repertoire.

The second review caught an unnecessary Store prompt comparison and a UI
handler that discarded a valid PGN preview. Store now relies on its existing
snapshot invariant for prompt lifetime. The editor retains its signed preview
while the activity command refreshes the catalog. The mounted Chrome journey
completed the preserved replacement alongside suspension recovery, the Games
scope, and the historical choice readback.

A fresh final Astra review found no interface, ownership, or correctness
issues in the revised runtime. The reviewer independently passed six
focused Rust tests and nine mounted Study metadata journeys. The prior
PGN Save fixture waits for the old response to fail and for the independent
old model projection to settle before comparing every prior table.

### Managed installation, November 20, 2026

The coordinated PRs merged into main. Each fetched merge tree matched
the reviewed tree. The managed launcher activated
`workspace-361ad459f99b60436bd2` on port 41822 and created the
stopped-time backup `recovery-start-4v3afd5a`. The first rehearsal
timed out before stop. The launcher's exact desktop and phone readiness
checks passed in a separate trial, followed by the standard managed retry.

The registered process owns the listener and serves the qualified optimized
binary and all 22 desktop and
24 private HTTPS phone assets
byte for byte. The database kept its file identity, dataset, active Study
attempt, and all 36 previous application tables and SQLite sequence rows.
Schema 13 passed integrity and foreign-key checks. Live Study and the
Repertoires list responded on their supported surfaces. Suspension,
resumption, and grade-generating checks used disposable databases.

On the optimized candidate, Chrome completed the mounted signed PGN
replacement across suspension, suspend and resume, lost-reply recovery,
stale corrective-choice presentation, and scoped game-gap analysis.
The installed predecessor replay passed all six accepted-lost and unaccepted
Answer, Learn more tactics, and PGN Save cases. The existing durable replies
replayed exactly and Retry Next sent only Next. The [manifest](manifest.json)
records the compatible merge commits, artifact hashes, and backup.

## Tempo notifications candidate

The user requested a short lower-right confirmation for Review Later and
selected a first rollout that includes repertoire changes. Desktop and
Phone Study share the same notification host. It holds one message for
four seconds, fades over 200 ms, and keeps keyboard focus in place. With
reduced motion it disappears after the hold without a fade.

| Decision | Basis, owner, inputs and lifetime |
| --- | --- |
| Show a confirmation | Tempo UI uses the existing validated acceptance for Review Later, Save Previous Response, removing a saved review, Tactics settings, and repertoire saves and renames. Suspend and Resume use the refreshed list for the addressed repertoire. Display text can change without changing the command, acceptance, recovery, or decision to notify. |
| Display and dismiss | Core takes a caller-supplied event ID and message. Each new event replaces the current confirmation and gets the full display time. An old timer can dismiss only its own event. IDs live in the app session and are independent of durable commands and receipts. |
| Retain information for recovery | The owning page displays validation failures, pending writes, retry actions, cleanup warnings, and detailed results inline. A confirmed save and the subsequent document reload continue to have independent outcomes. |

| Component | Qualified commit | Pull request |
| --- | --- | --- |
| Core | `82cc41db0a146ff0db77bc2b9a308f12eee077fb` | [Core #7](https://github.com/tempo-v2/tempo-core-components/pull/7) |
| UI | `8140d64e545d6b571ef808de0686da8b1b43d86c` | [UI #35](https://github.com/tempo-v2/tempo-ui/pull/35) |

UI bundles Core 0.2.3 with tarball SHA-256
`4e74b8f2f4c643bdb6e576ca12dbdf58faa3a407d4906b18ba060be7c6ab40bf`.
Use the backend and workspace lock from the installed tactic-board capture
release above, including Tempo `7f8060cabd1f03efa7faac27275f50dcd0e1a3a4`.
The candidate is presentation-only and requires no wire or database
migration.

The packaged Core test passed in standalone Chrome with accessible status
markup, preserved focus, repeated text and replacement during a fade, the
hold and fade intervals, and reduced motion. Both UI builds and all 111 UI
tests passed. Chrome on disposable databases verified bottom-right placement
without layout shifts, marks retained after dismissal, removal, settings
confirmation across navigation, repertoire save and rename, suspend and
resume, marked-line saves, and Games workbench saves and replay. After a
repertoire document reload failed, Retry reload remained available beyond
dismissal and sent only the read. Phone Study in WebKit verified viewport fit
and dismissal, with no success toast on a lost acknowledgement and a
confirmation after exact replay of the original mark.

Both component pull requests target main. Installation is separate.

### Independent review and installation, November 20, 2026

A fresh Astra review found no interface, ownership, or coupling issues. The
reviewer independently ran the desktop Saved for Review journey in Chrome
and Phone Study in WebKit on disposable databases. The checks covered
accepted replies, dismissal, settings across navigation, removal, and
replay of the exact command after a lost phone acknowledgement.

[Core #7](https://github.com/tempo-v2/tempo-core-components/pull/7) merged as
`56fbc3e0acfa89a2a4798a8e854f147bbb1f8498`,
[UI #35](https://github.com/tempo-v2/tempo-ui/pull/35) as
`8d0632e54fe12dc73005ce714d530af424c7b0f9`, and
[Planning #46](https://github.com/tempo-v2/.planning/pull/46) as
`30ced5fcae583168f6bbde732828c255c9d07fca`. All three merge trees matched
the reviewed heads.

The managed launcher rehearsed on a disposable copy, took stopped-time
backup `recovery-start-xiot478i`, and activated
`workspace-d109531bfb95cf3cf2f6` on port 41822. It used the launcher's
option to retain the separate post-game prototype. The backend matched the
preceding release byte for byte.

The registered service served all 22 desktop and 24 private HTTPS phone
files byte for byte. Both Study status reads and the desktop repertoire
list reported the retained dataset. The database kept its file identity,
schema 13, and the active Study attempt. All 39 SQLite tables matched the
backup, and integrity and foreign-key checks passed.

| Installed artifact | SHA-256 |
| --- | --- |
| Tempo executable | `156eaa0bb833831881360eea160b56ce2932be2290ceba5cc26fba7fbf4fcbb6` |
| Desktop JavaScript | `ebe33969e3ec4aa3139433e0a3c636d5de034859e57cb6a4c2440248a3118fde` |
| Phone JavaScript | `5c1ba6d33aa02753b4f70c1737fd6b2c9802ad3df923a90c034a0e28f6e08455` |

## Opponent moves in Study

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Find the opening move | Study should begin one ply before the learner's response when the exact move is available. Chess accepts the legal predecessor from an authored route, selected tactic range, or explicit source setup. Game repairs use the preceding move in the verified played game. The move must reach the canonical issued position. Chess combines matching source evidence independently of order. Conflicting candidates remain ambiguous across reimports. Labels, activity display text, and clock counters are independent. |
| Present the exercise | Tempo pins the verified pair when issuing the attempt and exposes playback context for an unplayed first decision to opted-in Study wire 5 clients. The current board also carries its exact opponent arrow on resume, based on the issued definition and played cursor. Desktop and phone UI hold the pre-move board for 250 ms and keep one presentation per active attempt in the browser tab. Later replies use the grader's accepted autoplay moves and replace the red arrow in place. Playback has no command or scheduling effect. |
| Recover saved context | The user selected existing-card coverage. An explicit metadata backfill uses the retained authored PGN, referenced capture archives, and verified original tactic transfers. Missing or conflicting evidence leaves the solver position available. Additional source evidence can mark an already-verified context conflicting through the same Chess reconciliation. Store updates only current presentation metadata against the observed dataset and write revision. Issued attempts, content versions, authored revisions, receipts, and learning stay as they were. |

Qualify together on the installed notifications baseline
`workspace-d109531bfb95cf3cf2f6`, SQLite schema 13. The candidate keeps
Study wire 5 with opt-in move context and portable format 5.

| Component | Qualified commit | Draft PR |
| --- | --- | --- |
| Chess | `013c9d3497bdc6d7287371b2201073aeff3bcdc5` | [#21](https://github.com/tempo-v2/tempo-chess/pull/21) |
| Store | `ee3cae09a496a3eec60fde76ec561e85a8146d36` | [#22](https://github.com/tempo-v2/tempo-store/pull/22) |
| Tempo | `33117a0ff09101f9e7516693515b9e9d42914499` | [#41](https://github.com/tempo-v2/tempo/pull/41) |
| UI | `326b54e1d96cc14e986e2d20183ff9196ac19bac` | [#37](https://github.com/tempo-v2/tempo-ui/pull/37) |

Reuse Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`,
Study `ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`,
Queue `777345256564cefa7f25d537a5a7c51a5377e749`,
Learning `58197f6fa9b2ea33907f2e305ec07efda64d553d`, and
Core `56fbc3e0acfa89a2a4798a8e854f147bbb1f8498`.
Use the installed notifications release's workspace and UI locks and
packaged Core 0.2.3.

The locked Chess, Tempo and Store suites passed 269 tests and doctests.
The packaged UI passed 112 tests. Chrome covered the exact pre-move board,
the hold and board lock, legacy client compatibility, refresh, navigation,
reduced motion, wrong-move recovery, restoring the latest arrow after a
refresh, and successive replies on a stable board.
WebKit covered touch Study, the red arrow, the actual game's repair lead-in,
and Retry Next. Nine Chrome journeys reproduced the same Study commands and
durable outcomes with the exercise name present, renamed or omitted. Six
accepted-lost and unaccepted journeys started with the actual installed
predecessor and replayed the exact Answer, Learn more tactics, and PGN Save.

A disposable backup of the installed dataset recovered 3,310 repertoire
positions and 17,267 tactics. Verified disagreement for 106 positions was
retained as ambiguous presentation metadata. The
preview left the file byte-identical, and repeating Apply produced zero
updates. Thirty-seven tables matched exactly. Only current card metadata and
the store write revision changed. SQLite integrity and foreign keys passed.

Prepare the private transfer from the retained Tempo 1 bundle. Preview on the
disposable database before adding `--apply` to the backfill command.

```sh
python3 -B tempo/tools/tactics/recover_setup_moves.py RETAINED_BUNDLE > PRIVATE_TRANSFER.json
target/release/tempo backfill-study-lead-ins DISPOSABLE_DATABASE PRIVATE_TRANSFER.json
```

### Independent review, merge, and installation

The first review found that a refreshed card lost the last reply arrow and
that conflicting predecessors could depend on source order. The second
review verified both fixes and found that backfill could overlook new
evidence on cards with an existing move. The third fresh Astra review
found no actionable interface, ownership, or coupling issues. It ran the
SQLite backfill conflict regression independently and confirmed the active
attempt and learning remained pinned. The reviewed combined build retained
the installed notifications release and its Core 0.2.3 package.

| Repository | Verified merge commit |
| --- | --- |
| Chess | `07b13a0d04c616db1db46943dc45a512470ddcaf` |
| Store | `262a379823c71dee455fad24dd46a866a13b2525` |
| Tempo | `4013a6d1c8d3ca32cb8b8ab756541f2ab4474605` |
| UI | `5a9f35878212ae9d9caaf9816591e524725d39a8` |
| Planning | `78d4e1ce6722aadbdb313fe91600c7dc4a591c2b` |

All five merge trees matched the reviewed source. On November 20, 2026
the managed launcher installed `workspace-641aab206895726c7169` on port
41822 and saved backup `recovery-start-gyo8ui35`. The launcher retained
the separate development prototype. Disposable rehearsal checked the
same managed readiness before and after annotating the saved dataset.

The live backfill took a separate stopped-time backup,
`recovery-opponent-moves-91tuby6j`. It added 3,093 repertoire contexts and
17,267 tactic contexts and marked 84 additional disagreements. The final
catalog had 20,599 verified contexts and 106 conflicting contexts. A second
application made zero changes. Thirty-seven tables matched the stopped-time
backup exactly. The two other tables changed only in current presentation
metadata and the store write revision. The active attempt, all previously
saved learning, and the original schema-13 database file were preserved.
Two accepted repertoire document saves between the artifact switch and the
backfill account for the independently observed content changes in that
interval.

The registered listener served all 22 desktop and 24 private HTTPS phone
assets byte for byte. Both read-only Study status calls and the desktop
repertoire list used the retained dataset. SQLite integrity and foreign
keys passed.

| Installed artifact | SHA-256 |
| --- | --- |
| Tempo executable | `02d3769ef42b0589ba9d2f3704c0cf68972e301bf1cb42ddf9ca3d77511def2a` |
| Desktop JavaScript | `ee96cfa2fc753b5eeb12ad9bbdb6ef1cbaf3d7c5bf5ff55749f24975e80eb4db` |
| Phone JavaScript | `6d0ea3363110bec7991e801c219b69e22d748342057919c28b8bfa8b93f573a8` |

## Position analysis integration

| Decision | Basis, owner, inputs and lifetime |
| --- | --- |
| Enqueue actual learner positions | The accepted position-analysis plan authorizes new accepted imports and explicit archive selections. Tempo resolves participation and Chess provides the played turns. Store keys by dataset, source revision, ply and requested detector versions. Labels and repertoire matches are independent. Pause and restart preserve completed work. |
| Share and settle analysis | Chess uses legal moves and exact comparable engine evidence. A winning mate supersedes other findings. Incomplete results never authorize a puzzle. Tempo coordinates the engine slot and Store atomically accepts a position and its training effects. |
| Deliver missed capture practice | Learning owns activity and cadence. Queue alternates accepted game requests and regular due work at durable issuance. The exact game predecessor is display context only. Replays preserve the issued attempt and result. |
| Yield to the foreground | Tempo runs background engine work only on wall power after 30 seconds of inactivity and yields to input or foreground engine requests. Cancellation retains ownership until acknowledged. |

The integrated candidate uses schema 14 and the existing Study wire 5 opt-in
for opponent context. The compatible application, Chess, Store, Learning, Queue,
UI and inherited release pins are in the manifest under
`queued-position-analysis`. The PRs target main and remain drafts.

The combined locked Rust run passed 354 tests and doctests. A separate
engine-gated real Stockfish 19 check passed cancellation, engine restart and
exact all-root result recovery. The shared-host test ran two registered
detectors through one position and counted one engine evaluation. The
application test exercised two saved positions, the exact opponent setup move,
a due review between game puzzles, and alternation across restart. The UI
passed all 125 tests and built both output surfaces.

The managed predecessor's stopped-time backup was cloned for a schema 13 to 14
startup rehearsal. The candidate preserved all 39 prior tables row for row.
SQLite integrity and foreign-key checks passed. Managed installation and live
game enrollment remain separate.

With a controlled idle signal on one disposable game, real Stockfish confirmed
the missed pawn capture of the queen and issued a Study puzzle with the exact
opponent move. The run took 10.4 seconds, with a slowest queue tick of 3.6 ms
and a slowest in-process Study progress read of 0.7 ms. Headless Chrome loaded
that saved result through the compiled Games UI, exercised Pause and Resume,
and observed the predecessor board transition to the solver board in Study.

The separate unassisted real-engine HTTP/browser run remained waiting for Mac
idle and could not qualify automatic start or a multi-game soak. The timings
above describe the single-game disposable run. Large-archive throughput and
latency on a populated result write remain release checks.

### Hardware qualification and independent review

On wall power the first unassisted candidate started 31.36 seconds after the
last Study activity, with the real Mac hardware idle timer at 41.68 seconds.
It completed 383 positions in 12 retained games on a disposable copy in
14 minutes 9 seconds, with no failed games or pending positions, nine
inconclusive positions, five confirmed missed captures, and clean database
integrity and foreign keys. The tester deliberately made uncached Study
progress reads at every probe. Those reads had a median of 1.23 seconds and a
95th percentile of 5.02 seconds under that workload. The installed predecessor
on a disposable copy had a median uncached read of 0.94 seconds and a 0.34 ms
median for the stamped reads the UI uses between changes.

Four fresh Astra reviews found and drove corrections for selected learner
identity, versioned membership and per-finding attribution, shared validated
board and move history, typed retry disposition, actual multi-detector durable
settlement, independent mate validation, exact skipped members, stable report
identity across changing detector membership, and truthful progress and retry
controls. The fifth fresh Astra reviewed the runtime pins now recorded in the
manifest and found no material interface or coupling blocker. It independently
passed 29 application, Store and mounted History checks, including real
Stockfish and the exact fulfilled-miss replay. The full Rust run passed 359
checks and the UI passed 125 tests.

The revised candidate independently passed the production 30-second gate
at 30.45 seconds after Study activity, with AC and the real hardware idle
sensor. The already completed 12-game run is the batch coverage evidence.
Additional follow-up probes were closed once renewed physical activity held
the idle gate and installation and health checks passed.

### Merged and installed on November 20, 2026

The six runtime pull requests and [Planning #51](https://github.com/tempo-v2/.planning/pull/51)
are merged. All seven remote main trees matched their reviewed candidate trees.
The managed launcher rehearsed on a disposable backup, kept the registered
development prototype, and installed `workspace-0fe92773f4f7b84ecd62` on port
41822. The rollback backup and previous registration are in
`recovery-start-6sczmyp4`.

The installed process owns the managed listener. The installed detector
discovery endpoint reported the hanging-material Stockfish detector available.
The installed desktop served all 22 files byte for byte. Schema 14 retained
the same dataset and the active Study attempt. All 39 preexisting tables
matched the stopped-time backup, integrity and foreign keys passed, and no
retained games were enrolled as part of installation.

### Background analysis follows Study focus

| Behavior | Basis and owner | Inputs and independence | Lifetime |
| --- | --- | --- | --- |
| Analysis can start after 30 seconds away from Study on wall power. | User-selected Study-only focus policy. The presentation shell reports presence, and Tempo's local runtime owns the admission and cancellation decision. | Visible and focused desktop Study, visible phone Study, actual Study commands, power, manual pause and foreground engine demand. Mouse, keyboard and unrelated browser activity are irrelevant. | Presence is an expiring in-memory signal per tab. A service restart gives clients 30 seconds to reconnect. Queued positions and accepted results retain their existing Store identity. |
| Games explains what holds the queue. | The existing Analysis panel reflects the local runtime's decision. | A typed wait reason from the runtime. No policy depends on display text or a user setting. | The optional reason is negotiated by the client to preserve compatibility with older open tabs. |

The service tracks each Study tab by an ephemeral identity and monotonic message
sequence. A delivered release starts the quiet period even when it overtakes
activation. A lost browser becomes inactive when its last heartbeat is 30
seconds old. Study status reads, Games, Settings and backgrounded Study tabs
leave analysis eligible. Active Study and genuine Study commands interrupt
background work through the existing detector host.

Candidate branches are [Tempo #43](https://github.com/tempo-v2/tempo/pull/43)
and [Tempo UI #39](https://github.com/tempo-v2/tempo-ui/pull/39), based on
the installed position-analysis source pair. Their code heads are
`0ae0f0b1ca27d5bd83abf126dc01c4b6815eb1c8` and
`6ec60270aa50daf26f4ebc75c60f642eb55142ee`. All other component pins
and the dataset schema are shared with the position-analysis release.

Independent review traced desktop and phone presence through the real UI entry
points, the HTTP authorization boundary, and the existing cancellation path.
The final heads passed 402 Rust tests and doctests, 128 JS tests, and four
production HTTP tests, including phone ingress and Study receipt replay.
The Mac Chrome rehearsal kept a focused Study page active for over 30
seconds without a move. After switching to Games, real analysis started in
30.26 seconds while the machine's HID idle time was 0.23 seconds. Returning
to Study yielded the engine and kept completed positions.

Both qualified source trees merged to main. The managed installer installed
`workspace-d29667030ac522f8838b` on November 20. Readback verified the
schema-14 dataset and active attempt, all 46 pre-existing tables, all 22
served desktop files, working Stockfish discovery, 12 queued games and
24 previously completed positions. The service used the existing
registration and kept `recovery-start-niswgz8t` as the stopped-time backup.

### Desktop board resizing

| Behavior | Basis and owner | Inputs and independence | Lifetime |
| --- | --- | --- | --- |
| Drag the corner to resize a square board that stays near the vertical center. A click leaves its size alone. | The user's desktop board request covers Study, Analysis, Games review, repertoire response, tactic building and setup, and tactic detail. Core owns the gesture, handle clearance and sizing within the host. Tempo UI owns desktop eligibility, which main boards opt in and their page or dialog layout. | Desktop pointer and viewport, available board space, and drag displacement determine the size. Chess position, orientation, lock state, and display text are independent. The handle sits outside chess input, so resizing leaves Study commands and the repertoire response recommendation alone. | Size belongs to the mounted board. Reopening uses automatic fit. The phone shell and embedded previews use their existing presentation. |

This candidate uses the Study-focus checkpoint backend and all of its
non-UI pins. [Core #8](https://github.com/tempo-v2/tempo-core-components/pull/8)
has verified head `dad0ea4797b5c137cf804b082037b092a6e67992`.
[Tempo UI #40](https://github.com/tempo-v2/tempo-ui/pull/40) has verified head
`2a0c0286a49aa12a7a241f6c4f5fea73fa84f562`. Both PRs target `main`.
Tempo UI vendors the byte-identical Core 0.2.4 package with SHA-256
`9971c41100e96082a55ef96dd925a7d443dc641c7961d96cffd798e3eb82c9ee`.

The packaged Core Chrome consumer and all 128 UI tests passed. Both UI
bundles built. Chrome verified initial and resized vertical centering on all
seven main boards, size and square targeting, short Games and all three
tactics views,
and handle absence on a narrow viewport, a wide touch-first viewport and
an import preview. Study kept its size through a move and sent no command
during resizing. The repertoire response accepted a pending recommendation
after the drag. The Phone Study WebKit journey passed with the handle absent.
Browser journeys used disposable databases.

The independent Astra reviews found a blocked corner square, a surface signal
leaking React pointer data, and short-window layout problems in the tactic
builder, setup and detail. Core now reserves space outside the chess surface
for the handle and invokes the surface consumer with zero arguments. Tempo UI
owns a single viewport and device rule, sizes its own tracks and puts desktop
tactic controls beside their boards. The packed browser check verified a
legal move from h1 at the 240 px floor and a zero-argument surface signal.
The tactic detail journey verified a real resize at 1000 × 500.

A third fresh Astra reviewer found no material interface or coupling issues
in the verified heads. The reviewer independently ran the packaged Core
consumer, the h1 move and zero-argument signal probe, and all six Tempo
browser journeys on disposable data.

Core and Tempo UI merged to main at
`a5f8f320313d6650700617eb24ca83ec2f3cb827` and
`0f141717ceab7e6b51447bc21de78f3d82ae3b5a`. Both remote main trees
matched the independently reviewed heads.

On November 20, 2026, the managed launcher rehearsed on a disposable copy
and installed `workspace-f9b26eccfcf93e4da47f` on port 41822. The backend
binary matched the previous checkpoint byte for byte. The installed service
served all 22 desktop and 24 phone files byte for byte and reported Study
status and Stockfish availability. The database kept its identity, file
inode, schema 14 and active study state. All 46 tables matched the
stopped-time backup, and SQLite integrity and foreign keys passed. The
previous registration and database backup are in
`recovery-start-iwd4c9vb`.

## Personal tactics and playing patterns

| Behavior | Basis, owner and inputs | Independence and lifetime |
| --- | --- | --- |
| Record all eight motifs across actual learner turns. | Andy's approved plan. Chess uses the verified legal occurrence, move history and the explicit King > Queen > Rook > Bishop > Knight > Pawn hierarchy. Tempo verifies participation. | Presentation names and game outcome do not determine motifs. Retain every candidate and share comparable engine evidence at each game occurrence. |
| Classify misses and admit only-move puzzles. | Chess compares all legal roots. The reporting band is 30 cp inclusive. Study admission requires a 75 cp lead, or a unique root preserving forced mate at any distance and a verified mate in one or two. Verify again for standalone content. | Game result and display metadata do not affect grading. Keep ambiguous misses in Games, once per turn overall. Store binds a request to the game occurrence and an issued attempt to exact content. |
| Compare game outcomes and playing load. | Tempo joins verified game result and canonical game metadata. Load counts use completed games before the current start and the approved Eastern time calendar. | Filters do not change past load or game identity. Partial analysis and unavailable metadata remain visible. |
| Resume through existing Study and analysis interfaces. | Queue and Learning own delivery and cadence; Chess owns mate grading; Store owns atomic acceptance and replay. | Earlier receipts and issued content retain their original meaning. Results on a new detector revision can reconcile unissued work only. |

The implementation is [Chess #23](https://github.com/tempo-v2/tempo-chess/pull/23), [Store #24](https://github.com/tempo-v2/tempo-store/pull/24), [Tempo #44](https://github.com/tempo-v2/tempo/pull/44), and [UI #41](https://github.com/tempo-v2/tempo-ui/pull/41). The `personal-tactics` manifest entry pins the compatible component sources. SQLite stays at schema 14 and Study wire 5 continues to project the pinned issued content. The Games tactical report uses its own version 2 read, while unrecognized clients receive a typed request to reload.

Focused independent review traced the actual Games and Study consumers. It found reissue and duplicate-introduction risks when rescans changed a result, a missing participant boundary in Games, and loss of rating and clock facts in PGN upload. The candidate retains issued requests and current attempts, reconciles only their future issuance, scopes findings to the verified game participant, and preserves validated PGN metadata. A revised-solution test verifies catalog and learning equivalence with the live issued attempt and ensures Skip cannot reissue the superseded request.

The earlier draft’s locked Rust unit suites passed 226 tests. Both engine-gated legacy recovery and source-position checks passed on their isolated real Stockfish run. The UI passed 128 tests and built desktop and phone output against the existing packaged Core. A normal-runtime Stockfish and Chromium journey qualified six disposable games, opening a stored finding in the source game, playing the Study move, and recovering from both a lost Answer reply and an interrupted Next. The previous installed executable issued the compatibility exercise. The candidate replayed its accepted and undelivered commands with one durable assessment.

The paused desktop report on a disposable copy of the installed archive returned 2,317 games, including 523 at the canonical 1+0 control. The report took 310.6 ms with a concurrent stamped Study read of 1.2 ms. All 45 application tables matched the pre-rehearsal snapshot and SQLite integrity and foreign keys passed. Archive aggregation runs outside the foreground Study path. These timings describe the disposable rehearsal and the pinned development artifact.

The full live archive scan and missed-tactic and playing-load estimates are pending. Analysis uses the existing AC and Study-focus gate.

A separate real Stockfish run on the populated archive copy settled 12 learner turns in 106.7 seconds including the startup quiet period, with no inconclusive results and clean integrity and foreign keys. The exploratory probe reused a stale progress stamp after analysis wrote changes and saw a peak 4.82-second Study progress read. That workload differs from the on-screen client, which advances the stamp after a response. A fresh, stamped read during the concurrent archive report and during the six-game browser test remained responsive.

Final review verified that the detail read uses the addressed position and that the archive report has a bounded background worker. The finding and game reads carry the exact verified learner and the application checks them again at the join, so a concurrent import changing the requested perspective cannot mix two players' evidence.

The repeated debug run also saw one 4.91-second current-stamp read. The final optimized candidate resumed the paused archive copy, committed five additional turns in 58.0 seconds including the Study quiet period, and kept 55 stamped Study reads at a median 0.6 ms and a maximum 9.9 ms. One turn was inconclusive and retained its retry state. The copy passed integrity and foreign keys. This verifies a bounded resume, while the full installed archive scan and its correlation readout remain pending.

### Interface review corrections

- Chess declares whether a detector produces complete decision evidence. The host selects the archive producer by that declaration. Descriptor IDs, labels, ordering and other detector registrations are independent of whether the personal archive is enrolled and reported. Legacy winning-mate evidence and complete decision evidence are mutually exclusive. Store selects the report rows by the accepted assessment kind.
- A clear opportunity contributes to its playing-load band even when a different turn in the same game has an unclear motif. Game-level loss attribution still withholds an uncertain no-miss claim. The approved ambiguity rule applies to competing non-mating options.
- Store's request state distinguishes queued, issued, superseded while issued, and reviewed. Games renders that typed state. Supersession preserves the original active attempt and forbids future issuance of the obsolete request.
- The combined candidate includes the installed desktop board-resize release and its packaged Core 0.2.4. Prior runtime behavior and evidence unrelated to the changed consumers remain in scope.
- Engine scores that preserve a forced mate remain mate comparisons, including distances beyond the two detected mate motifs. A slower winning mate is a sound alternative. The 30 cp ambiguity rule applies to centipawn scores.
- When a shared detector set settles partially, only a complete decision finding from the requested report can establish otherwise inconclusive personal-archive coverage. A complete finding from another detector cannot mask an uncertain complete-decision result.
- A discovered attack or check requires a moved blocker on the stationary slider's ray. The owning Chess detector still verifies that the resulting attack is legal. Simply freeing a previously pinned slider does not change whether its ray was opened.
- Pin and skewer evidence uses a legal threat on the front target. King-safety pin geometry remains separate from that evidence. A slider restricted to its own pin line cannot report an off-line attack on two opposing pieces.
- Registration allows one complete-decision producer. A second claimant is rejected by the host regardless of either descriptor's identifier, so the active archive never selects an owner by ordering. Legacy producers may still be registered independently.


### Merged and installed

The sixth fresh Astra reviewer found no remaining interface or coupling
blocker. The reviewer independently verified 21 focused Tempo, Chess and
Store checks. These covered renamed and reordered detector registration,
rejection of a second complete-decision producer, the existing Games-to-Study
request, and replay of its saved answer after restart.

| Component | Reviewed head | Verified main merge |
| --- | --- | --- |
| Chess | `f2c156c5ab31086149d0b939afa027b142eeef68` | `e1b23ee430e3a1dea8895db673d2ca0769986b67` |
| Store | `7dba1bc669b0b78f6c409b0c9924195824af67c3` | `c81ff1e227bb08cf15176f0295eb91ff6a35ce9a` |
| Tempo | `0f6f727121337a2584b622fae59bd00421749040` | `58feb9ad66d000edc95fa2bc100f8e4c804e0043` |
| UI | `a9285e3e70fb8ddff2e8f81285775fd646118ed0` | `81bbd3d4c20b1e24bebdf33e93610f773649aee2` |

Each remote main tree matched its reviewed head. The combined candidate
passed 231 Rust tests before the final registration constraint. Its focused
analysis-to-Study test passed again at the final head. All 128 UI tests and
both builds passed with packaged Core 0.2.4. The combined Chrome and real
Stockfish journey qualified six games and verified source and candidate
boards, Study capture, original Answer replay and retry of Next alone. The
journey took 107.8 seconds with a concurrent stamped Study read of 1.3 ms.
Previous-release recovery used the same backend bytes as the board-resize
checkpoint and verified both accepted and undelivered pending commands.

On November 20, 2026, the first managed start ran out of disk space while
copying the stopped database. The previous registration restarted after
clearing the regenerable debug cache. The retry rehearsed the combined
candidate and installed `workspace-587a3ebb0de530457b3e` on port 41822.
Readback verified the listener, personal tactics detector and version 2 report.
The live report found 2,317 games, including 523 at 1+0. All 46 database tables
matched the stopped-time backup. Dataset, active attempt, database inode and
schema 14 were preserved. SQLite integrity and foreign keys passed. All 22
desktop and 24 phone files matched the installed artifacts, and both clients
reported Study status for the same dataset. The rollback registration and
verified database copy are in `recovery-start-qoee13ij`.

## Bounded hardening, November 20, 2026

The run started at 23:42 UTC on November 20 with a hard stop at 01:42 UTC
on November 21. **Partial candidate. Core is not ready.**

| Compatible component | Published draft | Exact candidate head |
| --- | --- | --- |
| Tempo | [#45](https://github.com/tempo-v2/tempo/pull/45) | `2410513e56a2d915bc3c6931cb97146a73aeef6e` |
| Store | [#25](https://github.com/tempo-v2/tempo-store/pull/25) | `6992170493d15cfca02e5c2dea69716e8a5f413a` |
| Queue | [#13](https://github.com/tempo-v2/tempo-queue/pull/13) | `5aad5035c05e6b4d85a6574a02151e06c079f550` |

The locked assembly used these heads together with unchanged Chess
`e1b23ee`, Learning `4fb3053`, Study `ddf6839`, and Types `a8e46c9`.
It passed 238 unit and integration tests and the dependency-direction gate.
Independent review on the same heads reran the tactical and Queue checks
and confirmed exact issue and receipt replay across restart.

Both supplied M1 cases failed on current main. The candidate preserves the
original issued or fulfilled binding and prevents the revised answer from
showing up in ordinary Next. The unissued replacement still fails at Next
after solving the replacement. A restore-and-scan regression proves that
an existing ungraded introduction and one newly made by the scan can yield
the same saved request and Learning. Safe withdrawal needs a durable link
to the introducing request and a rule for already-retained unknown ownership.

For M3, Queue proposes the ordering effect at selection. Store records it
with the exact issuance and request binding. Request → regular due → request,
restart, and failed-binding rollback are verified.

D2 is a separate reviewed report-snapshot candidate in [UI #42](https://github.com/tempo-v2/tempo-ui/pull/42)
at `7a156014f9fee2cba9cfa2d8e19cdbb358f187cc`. M2 and D1 remain deferred.
No merge, installation, live data changes or historical cleanup were performed.

### Narrow M1 continuation, November 21, 2026

The continuation started at 00:46 UTC. Normal implementation freezes at
01:26 UTC, and the hard stop is 01:46 UTC.

The revised acceptance policy supersedes the earlier unissued-replacement
expectation. A rescan retains the occurrence's stored target and version
even before issuance and after cancellation or abandonment. The report
can show a different preferred answer. Invalidation may cancel priority,
while catalog and ordinary Learning remain intact. Distinct occurrences
can still acquire their own requests. Active content, current version and
eligibility checks still govern issuance.

This applies to the binding currently stored. Older retargeting may have
overwritten a first binding, and earlier scans may already have introduced
extra targets. This continuation leaves that history as stored.

| Compatible component | Published draft | Reviewed head |
| --- | --- | --- |
| Tempo | [#45](https://github.com/tempo-v2/tempo/pull/45) | `e39a797f83eaf398b21b43df37372f13d308f12c` |
| Store | [#25](https://github.com/tempo-v2/tempo-store/pull/25) | `28446c2f6028bf97d20d5ac4fe5479c0a99c1a14` |
| Queue | [#13](https://github.com/tempo-v2/tempo-queue/pull/13) | `5aad5035c05e6b4d85a6574a02151e06c079f550` |

The integrated locked suites passed 244 tests with two existing engine
tests ignored. Independent review reran the tactical and Queue suites,
including the Queue doctest, and the dependency-direction gate passed.
The new normal regression checks B in the report, A in actual Next, and
an empty queue after completing A. Other checks cover retained issued and
fulfilled bindings, cancellation and Skip, exact replay, unchanged
Learning, stale-content eligibility, and M3 restart and rollback.

D2 remains separate. M2 and D1 remain deferred. No merge, installation,
live data changes, schema migration or historical cleanup.

## Remaining audit release, November 20, 2026

The release assignment supersedes the prior timeboxes and publication
endpoint. The M1 retained-binding rule and M3 Queue-proposed ordering effect
still govern. The target is one independently qualified release on the
registered Mac.

The baseline is Tempo [#45](https://github.com/tempo-v2/tempo/pull/45),
Store [#25](https://github.com/tempo-v2/tempo-store/pull/25),
Queue [#13](https://github.com/tempo-v2/tempo-queue/pull/13), Planning
[#56](https://github.com/tempo-v2/.planning/pull/56), and the reviewed D2
change in UI [#42](https://github.com/tempo-v2/tempo-ui/pull/42). The
manifest identifies their starting heads and the diagnostic candidates.
The prior 244-test integrated result and D2 evidence apply to their recorded
revisions. The combined release requires fresh evidence.

**LEGACY RETAINED BY POLICY.** Migration must preserve stored occurrence
bindings, existing targets, Learning, attempts, assessments and receipts.
Prior retargeting or separate introductions cannot be reconstructed reliably
from the retained data. Historical cleanup was outside this release's scope.

### Integrated candidate

- **M1 and M3.** The assembled consumers preserve the retained Finding and
  Decision bindings, including unissued, issued, cancelled and abandoned
  requests. Next still applies the active/version/eligibility fences and
  records Queue's proposed ordering with the issued attempt. Replay, Skip,
  distinct occurrences and rollback are covered by the independent exact-build
  rerun.
- **M2.** Chess prepares the exact identity, source ownership and proposed
  content. Learning supplies the introduction transition. Store's addressed
  commit includes the authorized effects, receipt and report invalidation.
  Two disposable sizes varied current content, old versions, attempts,
  assessments, receipts and game evidence independently. SQLite used the
  target, identity and source indexes. Missing/exact lookups measured 49/69
  VM steps at both sizes and zero full-scan steps. A new target wrote one row
  each to current content, history and Learning. Pinned rescans wrote zero
  rows to those tables. Exact replay and a stale revision wrote zero rows.
- **D1 and D2.** Store fences capture with persisted archive and evidence
  generations. The worker keeps one compact generation, four filter
  snapshots and up to four top-30 anchors per filter. A cold generation
  builds facts once. Warm pages reuse aggregate/bootstrap and ranking
  results. Status reads can check freshness without rebuilding the report.
  Same-count rescans advance evidence without reloading archive PGNs.
  The UI owns the manual snapshot and handles stale, failed and late reads.
  Position details read the exact finding and live training link.
- **Diagnostics.** The integrated observational changes supersede Tempo
  [#40](https://github.com/tempo-v2/tempo/pull/40), Store
  [#21](https://github.com/tempo-v2/tempo-store/pull/21), UI
  [#36](https://github.com/tempo-v2/tempo-ui/pull/36) and Planning
  [#47](https://github.com/tempo-v2/.planning/pull/47). A delivery ID
  correlates HTTP, Store and worker phases and is independent of a durable
  command. The offline export keeps bounded allowlisted fields and
  canonical process labels.

The locked workspace passed 437 Rust tests and doctests with two existing
engine tests ignored by the ordinary suite. The independent reviewer reran
39 focused application, Store and analytics checks. The dependency-direction
gate and four self-tests passed. All 143 UI tests and the desktop/phone build
passed with the locked Core 0.2.4 package, and an independent focused UI
suite passed 35 checks. The optimized candidate used the exact source trees
and artifact set in the manifest.

The retained-copy rehearsal migrated the schema-14 database from the
registered artifact pair. All 45 preexisting application tables matched by
row counts and hashes, including the active attempt, Learning and receipts.
SQLite integrity and foreign keys passed. For the 2,317-game archive, seven
full report replies matched the prior installed behavior, including filters,
cohorts, keyset pages, exact similarity and addressed training detail.
One Mac measurement put the cold report at 220 ms, a warm older page at
1.26 ms and an addressed detail at 0.75 ms. The concurrent stamped Study
read took 0.52 ms. These timings describe this archive and host.

With the previous installed browser and binary on separate retained copies,
both a committed Answer with its reply lost and a pending unsent Answer
recovered from the original browser envelope against the upgraded candidate.
Each scenario produced one durable assessment and receipt. An independent
six-game Chrome and Stockfish journey with the prior UI and candidate backend
also passed, including report/detail, Study, exact replay and Next.

The independent optimized diagnostics checks passed four controlled
HTTP/SQLite scenarios and one real transport restart/replay case. The
collector passed 16 tests, including offline export and process label
redaction. The controlled fault establishes diagnostic capability.

On the populated disposable database, a burst of seven cold report
requests admitted two and returned typed `report_busy` for five. Normal
Stockfish admission then produced two committed tactical acceptances.
Recorded cold aggregate work overlapped acceptance, and a generation
change produced the explicit stale response. Across 243 concurrent Study
progress reads, the median was 0.64 ms and the maximum was 54.42 ms.
The 186 report requests took at most 235.99 ms. Foreign keys, SQLite
integrity and active-attempt identity remained intact.

Chrome on the paired candidate verified query pending state, late response
fencing, an addressed detail read, stale pagination and manual refresh after
accepting a backdated game. Refreshed results included the new game.

The Mac evidence is in the isolated workspace's
`.local/remaining-audit-20261120/evidence` directory. It includes the locked
workspace and optimized build logs, baseline/candidate report comparison,
retained-copy Answer replay and the concurrent and mounted browser rehearsals.
The data copy and registration files are kept local.

### Qualified release merged and installed

The managed launcher reproduced the qualified artifact hash and rehearsed on
a disposable database using the registered desktop and phone surfaces and
engine dependencies. The reviewed source landed in dependency order. Each
remote main tree matched the exact reviewed tree in the candidate manifest.

| Component | Release PR | Verified main merge |
| --- | --- | --- |
| Chess | [#24](https://github.com/tempo-v2/tempo-chess/pull/24) | `376db59658a2f1354248279a4cddc2eeadd8196b` |
| Queue | [#13](https://github.com/tempo-v2/tempo-queue/pull/13) | `7a79e413f519d2b3396f4fd8a90e0b946bb904d9` |
| Store | [#25](https://github.com/tempo-v2/tempo-store/pull/25) | `b4f04ef140820e224682fec0b9fa827511affc60` |
| Tempo | [#45](https://github.com/tempo-v2/tempo/pull/45) | `265362618fb9486623ee24f44cd8f5413272020c` |
| UI | [#42](https://github.com/tempo-v2/tempo-ui/pull/42) | `5e6a9742c0063ea7b84d6ee2fa0857bdf6cf82d0` |

`make start` replaced the owned listener on port 41822 and left the
unrelated development listeners running. The registered process served
`workspace-692fdc88f2fadf494a7b`, including the exact optimized binary and
all 22 desktop and 24 phone files. The previous binary/UI registration
and verified stopped-time database copy are in `recovery-start-x08vvc90`.
Installed readback matched the stopped-time backup on all 45 preexisting
application tables. The database inode, dataset and active attempt
were preserved. SQLite quick check and foreign keys passed at schema 15.

Read-only Study resumed the retained attempt. Personal Tactics returned a
matching report generation and 32 fully analyzed games out of 2,317.
The personal-tactics detector was available. Analysis was enabled and
reported waiting for Study to leave the foreground. The registered browser
exported its diagnostic ring with the Chrome context offline. The native
collector recorded the registered PID and the correlated report response.
The controlled and installed evidence establishes diagnostic capability.
The cause of the historical timeout remains undetermined.

**LEGACY RETAINED BY POLICY.** The migration and installed readback
preserved authoritative data. A later historical correction would require
its own evidence and decision.

## Repertoire coverage scan

| Behavior | Basis and owner | Inputs, independence and lifetime |
| --- | --- | --- |
| Estimate coverage through the chosen learner move | User-approved Games scan. Chess supplies legal transitions and the saved response at each canonical position. Tempo blends Explorer and Maia and stops each path at its first missing response. | The active verified repertoire, its color, opening depth and opponent move evidence determine coverage. Display names and PGN comments are irrelevant. A terminal line needs no further response. |
| Publish suggested first gaps up to the target shortfall | User-approved target prioritization. Tempo ranks first gaps by their probability from the start. Store atomically replaces one report per repertoire. | The selected target governs the number of suggestions. The dataset and verified repertoire input fence publication. Reports survive restart. After an edit the last estimate is stale and suggestions are checked against current chess content. |
| Fix a missing response | Games uses the existing signed additive Preview and Save operation. Chess verifies the legal anchor and need for a response. | The current document and the addressed legal position determine the draft. An accepted Save retains its existing receipt and replay rules. The scan publishes forecast records. |

The desktop Games entry accepts one active verified standard-start repertoire
per manual scan. The inputs default to 90% through the learner's eighth move.
Tempo uses Lichess Rapid's 1400–1599 bucket and the existing Maia Rapid 1500
model with a prior weight of 100. Both the first-gap estimate and the unresolved
mass are measured from the standard initial position. The existing signed
Save can make a previously missing branch reachable. Another explicit scan
evaluates that branch.

Schema 16 stores the latest report and gap identities per dataset and
repertoire. The write checks the current verified input and the prior report
identity in one transaction. The existing Games list merges estimates with
recorded counts. Current chess content determines whether a stale suggestion
can still be opened. Forecasts are derived local data and can be regenerated
after restoring a portable export.

| Component | Draft PR | Verified head |
| --- | --- | --- |
| Chess | [#26](https://github.com/tempo-v2/tempo-chess/pull/26) | `ea97595462078e1be94fcd31566b87aff2603906` |
| Store | [#27](https://github.com/tempo-v2/tempo-store/pull/27) | `d9895877ae7032edfb78c7b3e77ac208d71cbd77` |
| Tempo | [#47](https://github.com/tempo-v2/tempo/pull/47) | `d4e428f1f688e13e9264ef15e59252cf463c0e31` |
| UI | [#44](https://github.com/tempo-v2/tempo-ui/pull/44) | `70acf73cecb370f850daf566211262f3fc8944f5` |

The assembled candidate uses Core `a5f8f320313d6650700617eb24ca83ec2f3cb827`
and its vendored 0.2.4 tarball, Learning `4fb305325acd4a533d2617b871651f6ffc11a9a3`,
Queue `7a79e413f519d2b3396f4fd8a90e0b946bb904d9`,
Study `ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`, and
Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`.
It uses the retained remaining-audit Cargo lockfile and the UI's locked
dependencies.

The locked workspace passed 442 Rust tests and doctests, with two existing
engine tests ignored. All 143 UI tests, the desktop and phone build, and the
dependency-direction gate passed. Chrome exercised the new scan and the
existing Fix Response flow. The scan wrote forecasts while the fixture's
learning, attempts, assessments, saved content receipts and observed gaps
matched their pre-scan rows. The browser found both a forecast-only row and a
row with observed games, saved a response through the signed editor, and
rescanned from 60% to 85% coverage. Rename kept the report current, restart
retained it, and a delayed start carrying a prior report ID was rejected.

A disposable two-move scan used live Lichess Explorer and the pinned Maia
runtime at its one opponent position. It reported 57.1% coverage and zero
unresolved probability.

The optimized binary from the same source set passed the browser scan journey.
Its SHA-256 is
`17c15ab934ef9eb028410404698662e875c34ebee318b3dd0f98a3687dcde64c`.
Independent review checked the four published heads, including the actual
backlog, authoring, and migration paths.

Independent recovery qualification used an online backup of the registered
schema-15 database and the previously installed binary and browser assets.
The optimized candidate reached schema 16 with SQLite quick check and
foreign-key checks passing and 11 preexisting table hashes matching before
replay. Two old-browser sessions replayed their original signed Gap Save
bytes after restart, one after a lost accepted response and one after a
request that never reached the old server. The accepted replay added zero
content receipts and the unaccepted replay added one. Both browser sessions
settled, with Study attempts, assessments, receipts and game evidence
preserved.

The four component PRs form a single candidate. This entry records source
publication and disposable qualification. Merge and managed installation
remain pending.

### Strict interface review follow-up

Chess owns whether a legal successor has a saved response, is terminal, or
needs a response. The scan and Fix Response consume this classification.
During delivery recovery the browser retains the immutable submitted scan.
Only a status or report for that scan confirms acceptance. An older report
remains displayable, and retry resends the same scan identity and parameters.
Tempo owns the merged Games backlog. Every caller uses the same application
operation, which obtains the observed and forecast facts through Store.
The local scan worker owns background execution.

| Component | Revised review head |
| --- | --- |
| Chess | `13fb1b162b6c02911c67ad7c8dfb4b25b7d4fe09` |
| Store | `5bf98f65aa8ba7d05ef426f55d146553cdcc36d1` |
| Tempo | `34844fe85dfa5132213f47432b648b7d38a46d58` |
| UI | `e0d681f1cb975c6a84816232d772593b8b2b9794` |

A missing gap kind in a legacy Games reply uses the historical editor.
A present kind must be recognized before Games offers Fix Response.
The client preserves a recognized explicit kind in the draft command.

The revised heads passed 443 Rust tests and doctests with two existing
engine checks ignored. Both lost-start cases passed in Chrome. A request
that never reached Tempo was retried with identical bytes. A lost response
after acceptance reconciled without another POST. The Store-backed public
application list exposed a forecast-only row and opened the signed editor.
The same optimized binary passed both legacy signed Save replay cases on a
fresh backup of the registered database. Live Explorer and pinned Maia
each supplied evidence for a disposable one-position scan. All 25 concurrent
Study Status reads completed within 1.16 ms and identified the expected
dataset. The revised UI passed 144 tests, including the unknown-kind case.

### Merged and installed

Three fresh Astra reviews traced component decisions and the actual Games
consumer. The last review approved the exact revised heads after independent
Chrome checks of both scan delivery cases, typed gap drafts and signed
preview. The published runtime PRs merged into main with trees identical
to their reviewed heads.

| Component | Verified main merge |
| --- | --- |
| Chess | `53e08bc72e74044ec5fb227e7458ae1a40571d14` |
| Store | `646912c8333cb4382172e1828aed70d993954c32` |
| Tempo | `c4f0b678b24d209f00ad33c4aa77944971de9a61` |
| UI | `b62ae6da3243df0cc99e627c8d0228bc9557d9ad` |

`make start` installed `workspace-d0a77637b0613aadb029` at port 41822.
The running binary matched the qualified SHA-256
`55b1c9d5e7f5b1b2314cc87b8a6fdb5c4080be740c5ae263bf040be19fdae791`.
The registered process served all 22 desktop and 24 phone files byte
for byte. The prior registration and stopped-time database backup are in
`recovery-start-6jvss7wm`. All 48 preexisting table counts and hashes
matched the backup. The dataset identity, active attempt, and database inode
matched across the schema-15 to schema-16 upgrade. SQLite quick check and
foreign-key checks passed.

Read-only Study resumed the retained attempt. Games returned coverage
status for both active repertoires, and Chrome opened the installed scan
form and verified the 90% and move-8 defaults. Provider and authoring
checks ran on disposable data.

## Connected repertoire reviews

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Reconnect repertoire decisions | The accepted Study plan keeps Queue's first ordinary due pick. Chess supplies consecutive occurrences from the current saved PGN with both answers verified. Multiple predecessors leave the first review without a warm-up. A fork with multiple eligible replies, a repeated target, or a gap ends the run. Names, comments, and variation order have no effect. |
| Choose practice or review | Learning interprets the latest applied human Test on the current answer version and current due and corrective facts. One familiar predecessor may be practiced without scheduling or deferring it. Queue can link up to three independently due ordinary reviews. Existing priority work takes its usual turn. A Test miss ends the run and isolates that target until a later applied clean result. |
| Resume an issued run | Tempo issues ordinary Practice or Test attempts, pins each authorized opponent reply, and exposes a warm-up presentation to opted-in clients. Store fences the bounded cursor with dataset, version, attempt and revision checks. Each answer and its receipt commit with its own result. Next resumes an active attempt or advances the persisted run. |

The first release covers automatic warm-up and short scheduled runs through the
desktop and phone Study entry points. Full-variation Practice is a follow-up.
Once selected, the exact path remains pinned while its moves, versions and
eligibility still match. A newly available alternative does not replace it.

### Published candidate and acceptance

The compatible candidate uses Study wire 5 with an opt-in run presentation and
SQLite schema 17. Assemble these heads on the installed repertoire coverage
release with its workspace lock and packaged Core 0.2.4.

| Component | Verified source | Draft PR |
| --- | --- | --- |
| tempo-chess | `3d599189d75cd1d99e672ec0d81cb5c8f4a04fea` | [#25](https://github.com/tempo-v2/tempo-chess/pull/25) |
| tempo-learning | `ca9a3baa531b12c63903a149372e2c25952eda14` | [#9](https://github.com/tempo-v2/tempo-learning/pull/9) |
| tempo-queue | `4b485f4d1c1feb99758213b7642161e3385a0536` | [#14](https://github.com/tempo-v2/tempo-queue/pull/14) |
| tempo-store | `4e7b8075ecd0b1404ce310ab7716389ed5ae1870` | [#26](https://github.com/tempo-v2/tempo-store/pull/26) |
| tempo-ui | `1537bc0e9ad3911214b32024f0815fd0f75e6d5f` | [#43](https://github.com/tempo-v2/tempo-ui/pull/43) |
| tempo | `1934d7793e30c382b63a40449b409e7ca66edb8d` | [#46](https://github.com/tempo-v2/tempo/pull/46) |

Reused Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`, Study
`ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`, and Core
`a5f8f320313d6650700617eb24ca83ec2f3cb827`.

- The locked Rust workspace passed 453 tests and doctests with two existing
  ignored tests. The packaged UI passed 145 tests. The dependency-direction
  gate and optimized build passed.
- Native SQLite Study verified the warm-up, three separate assessments, a miss
  followed by isolated recall, forks and transpositions, comment-only and
  semantic edits, suspension, priority interruptions, and identical commands,
  receipts and learning for present, renamed and omitted exercise names.
- Chromium desktop and WebKit phone played an ungraded warm-up and three
  reviews on the same board. Chrome also covered Skip warm-up, correction,
  retry of only Next after an accepted result and immutable Answer replay when
  its response was lost. The mounted clean, missed and Teach journeys matched
  across all three display-name variants.
- Six accepted-lost and unaccepted journeys with the exact previous registered
  binary and UI covered Answer, additional tactics allowance and repertoire
  save. Two further Answer journeys used copies of the registered schema-16
  database and its old browser recovery envelope. Each accepted one grade and
  one receipt. Direct migrations preserved all 50 tables from schema 16 and
  all 48 tables from schema 15. SQLite quick check and foreign keys passed.
- The first fresh Astra review traced the published diffs through the SQLite
  and mounted clients. It required Queue to own the warm-up proposal and
  issuance effects and reproduced a run crossing a repeated position.
  The fixes below passed the native, mounted browser, and previous-release
  checks on the updated pair. SQLite confirmed the bounded latest-Test query
  uses the new index.

| Qualified artifact | SHA-256 |
| --- | --- |
| Optimized Tempo executable | `02ad730616d53e9c67ef801ef711dc77390f23c937111778baf1dc25892135c7` |
| Desktop JavaScript | `7779357c4289464b58bfa295c22d0d018ad61aca6281461f4d7a1cdc0c0048d4` |
| Phone JavaScript | `d75483e9e5a42a894c9a59b63386916e016deed2aadc0f54cfdfe68313302777` |


### Strict interface review follow-up

Queue owns the warm-up choice and its effects on the regular review turn,
deferral, and tactics practice rotation. Tempo supplies the familiar,
verified predecessor of Queue's ordinary due pick and maps the returned
warm-up to an ungraded Study Practice attempt. The wire presentation derives
from that declared activity. A repeated target on a surviving authored route
ends expansion at that step even when another variation can continue. The
ordering of the two variations has no effect.

The Queue regression exercises warm-up deferral, the regular review turn,
priority requests, and tactics practice rotation. The native Study regression
plays the same repeated-position boundary with both PGN variation orders.

### Combined with the installed repertoire coverage release

The second fresh Astra approved the Queue ownership and repeated-target
fixes. Coverage merged and became the registered schema-16 release before
this feature's merge. The updated branches build with those published
components. SQLite applies the coverage migration at 15 to 16 and adds
Study run storage at 16 to 17. The current branch preserves both receipts
and versioned forecast rows. The mounted Games test exercised scanning,
merged backlog, signed response, rescan, restart and scan recovery on the
same optimized binary used for the connected Study journeys. The schema-16
installation is the prior artifact in the replay checks above.

### Merged and installed on November 21, 2026

The third fresh Astra approved the exact combined source set after checking
Queue ownership, the repeated-position boundary, the two schema transitions,
and the mounted Study and Games consumers. Independent verification passed
the seven native Study scenarios and Queue regression, desktop and phone
journeys, display-name invariance and all eight prior-release recovery cases.
The six code PRs and the qualification ledger merged into main. Each remote
merge tree matched its reviewed head.

| Component | PR | Verified main merge |
| --- | --- | --- |
| tempo-chess | [#25](https://github.com/tempo-v2/tempo-chess/pull/25) | `54f64a7a002b28a28f787653bc6d792c423d2e7d` |
| tempo-learning | [#9](https://github.com/tempo-v2/tempo-learning/pull/9) | `ee542cc1971f40de2de7a80edad9f51f2f6eecdc` |
| tempo-queue | [#14](https://github.com/tempo-v2/tempo-queue/pull/14) | `74e09a1ea1cc2ca9bdf308b8fb7cc75963378214` |
| tempo-store | [#26](https://github.com/tempo-v2/tempo-store/pull/26) | `10f16634600553bbe3c186d51369c31ad3ebdd05` |
| tempo | [#46](https://github.com/tempo-v2/tempo/pull/46) | `ed2a5417423c4543bd20f85d4c87ce020b44a010` |
| tempo-ui | [#43](https://github.com/tempo-v2/tempo-ui/pull/43) | `fe7b81260092c67a87ba184aa905ff088d2b121c` |
| .planning | [#57](https://github.com/tempo-v2/.planning/pull/57) | `3005a742c7e10125e5b3674136cac7354afd5d35` |

The managed launcher rebuilt from those merge trees and reproduced the full
qualified artifact set. A disposable rehearsal checked the registered
schema-16 database, desktop and phone startup. The launcher installed
`workspace-4a7550d7f5cf89ba434d` on port 41822 and saved the previous
registration and stopped-time backup in `recovery-start-419498cj`.

The registered listener uses schema 17 and the retained database
inode, dataset and active Study attempt. All 50
existing application tables matched the stopped-time backup. SQLite quick
check and foreign-key checks passed. Read-only Study status on desktop and
phone reported the retained dataset. The listener served all
22 desktop and 24 phone assets
byte for byte. Chrome and WebKit exercised the installed artifact pair on
disposable data, including the three-review run, warm-up Skip, correction
and exact recovery. The separate post-game lab listeners kept their ports.

### Study completion checkmark, November 21, 2026

The desktop checkmark added height to its centered board container and made
the board jump 9.5 pixels after a clean review. Study UI now uses the existing
positioned checkmark overlay on desktop and phone. The render path takes the
same completion cue from Study, and the phone layout still reserves space for
its controls. A fresh Astra review of `f02f4caa360d5fa7f7243d3e9519ad4eae940a71`
found no interface or coupling issues. The reviewed tree merged as
`e704c731874013e22d59cccc24561b6267d84efa`. [Tempo UI #45](https://github.com/tempo-v2/tempo-ui/pull/45)

The installation pairs that UI with Core Components 0.2.4 and the byte-identical
Tempo backend from `ed2a5417423c4543bd20f85d4c87ce020b44a010`. The managed
launcher completed its disposable rehearsal using five-second readiness
deadlines for this invocation after the default deadline timed out. It
installed `workspace-e61e13268f69e36fdf37` on port 41822 and saved the stopped-time
backup and prior registration in `recovery-start-53vchggh`.

All 22 desktop and 24 phone assets matched the reviewed build byte for byte.
Read-only desktop and phone Study status returned the retained dataset. The
database inode, schema 17, active attempt and all 51 table contents matched
the stopped-time backup. SQLite quick and foreign-key checks passed. Chrome
on the installed artifact pair, using disposable data, verified that the board
held its exact bounds and Study sent one Answer and one Next. WebKit on the
qualified candidate verified that Phone Study's Continue and Retry controls
stayed below the board. That run used direct HTTP access checks in place of
the older assertions about route names in the diagnostics bundle.

## Games tabs candidate

Games opens on Library and keeps Library, Import, Analysis, and Coverage within
reach while scrolling. Tempo UI owns the selected view. The browser history
entry restores it on reload and returns game reviews to their source tab.
An explicit tab destination uses the Games-owned ID. Valid review links still
address the original game and board cursor. The saved gap editor resumes in
Coverage. Tab changes preserve drafts and do not rerun game commands.

- [Tempo UI #48](https://github.com/tempo-v2/tempo-ui/pull/48) uses
  `868be21322e1697fbe4204100e35f70e72ac8d9c` on the installed UI baseline
  `e704c731874013e22d59cccc24561b6267d84efa`.
- The guarded build used the vendored Core Components 0.2.4 package.
  Chrome tested against the registered release's Tempo backend
  `ed2a5417423c4543bd20f85d4c87ce020b44a010` on disposable schema-17 data.
- All 145 UI tests passed. Chrome verified the narrow-screen sticky strip,
  keyboard navigation, retained PGN file and paste drafts, source-tab return
  and refresh results. Coverage and suspension journeys passed, including an
  exact scan retry and recovered gap Save. Dynamic analysis used a fixture.
- The four prior-client Refresh cases preserved the original bytes and
  committed once each. Independent review ran 60 focused tests and verified
  direct navigation, hidden panels and draft retention in 320 px Chrome.

Candidate status is reviewed and published for integration. The managed
installation is a separate release step.

### Games tabs installed on November 21, 2026

A fresh Astra reviewer traced routing, tab ownership, job lifetimes and
pending-request recovery through the mounted Games page. All 43 focused
Games evidence tests passed independently. The reviewer found no blockers
in the reviewed source.

[Tempo UI #48](https://github.com/tempo-v2/tempo-ui/pull/48) merged as
`9db62f94c35ce9a54764b17aeef7d5b65196fa57`.
[Planning #63](https://github.com/tempo-v2/.planning/pull/63) merged as
`c7f46a4aa62b89b8f1052aff6fab296eaa943b83`.
Both merge trees matched their reviewed heads.

The managed launcher installed `workspace-582dafaf513210a4ad34` on
port 41822. The build reused the registered backend and the packaged
Core 0.2.4. The launcher completed its disposable rehearsal and readiness
checks with five-second HTTP deadlines after the default rehearsal timed
out. The stopped-time backup and previous registration are retained in
`recovery-start-m2mvgxn4`.

The running service served all 22 desktop and 24 phone files byte for byte
against the merged-source build. The two desktop text bundles differed from
the review build only in generated dependency paths. Desktop and phone
Study status returned the retained dataset. The database inode, schema 17,
active Study attempt and all 51 table contents matched the stopped-time
backup. SQLite quick check and foreign-key checks passed. The release build
also passed the Chrome Games journey on disposable data.

### Study card origins and removal, November 21, 2026

Study now offers Card details after a miss or completion on desktop and phone.
Saved for review can exclude a tactic from future Study and still open its
saved position. Removing a saved mark remains a separate action.

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Disclose an issued card's origin | The requested post-answer context is a read owned by Tempo. The dataset, attempt, revision and issued version address the disclosure. A stored miss allows source categories during correction. New attempts snapshot current source facts and an exact issuing game request or explicitly related game. Older attempts use retained issued content and a historical attempt binding when available. Saved mark checks and fresh details reads share the same authorization. An explicitly excluded tactic may be reviewed after its active attempt ends. Visible rich details and Saved Analysis recheck the addressed disclosure every 1.5 seconds and hide on lost authorization or read failure. Opening details requests current authority. Capture attribution, titles and themes are presentation data. |
| Exclude a saved tactic from Study | The user's removal choice applies to the dataset and canonical tactic target. Tempo requests Study's no-grade abandonment for a matching active attempt. Store validates the addressed mark, prepared transition and revision, then saves the exclusion, active transition and exact command receipt atomically. Queue sees only eligible candidates across introductions, reviews, Practice and game-linked requests. Existing learning and spent allowances are retained. Reimport and rescan of the same target preserve the exclusion. Games and Capture report only work eligible to appear in Study. |

| Component | Tested commit | Review |
| --- | --- | --- |
| Tempo | `6f6ad4806f2f350aee670c5f0cd2e68fa4184549` | [Tempo #48](https://github.com/tempo-v2/tempo/pull/48) |
| Store | `bf8772bd7013e8bfba09deb64a3383e9bceb402a` | [Store #28](https://github.com/tempo-v2/tempo-store/pull/28) |
| UI | `10de21d6ede706f06953ff3d16993a2e327355ce` | [UI #46](https://github.com/tempo-v2/tempo-ui/pull/46) |

Use the Chess, Learning, Queue, Study and Types pins from the connected
repertoire release and the packaged Core 0.2.4 dependency from the Study
completion checkmark release. That checkmark change is in the qualified
UI base. The workspace Cargo lock SHA-256 is
`ba4ccbbdd3b9e4fa6fd9c40ff8ac2b851f580273eaa00e7f76ab38ce507e765c`.
The UI package lock SHA-256 is
`31cfd692d2271cd7b82d26342ed403a60ae34724edc1ca5215402b6cbd22ae1a`.

The implementation passed 114 Tempo tests and 52 Store tests. The final
disclosure candidate passed 145 UI tests and its mounted browser checks.
Two pre-existing tests requiring a tactical engine setup were skipped. The
focused tactical test checked source evidence, version changes, preserved
learning and suppression after a rescan. Other focused checks exercised exact per-game attribution, capture metadata before and after issue, and rejected Store writes without a valid revision or abandonment. Independent review checked the
mounted Study and Saved for review consumers, the disclosure boundary and
the addressed exclusion transaction.

Chrome and WebKit exercised Card details and blind-card protection. Chrome
also exercised cancellation, an accepted removal with a lost reply,
inspection after removal, stale answers, restart and reimport, and denial of old disclosures and new detail reads when another client starts a blind attempt. The mounted Study consumer also passed display-name invariance for clean reviews, misses and Teach. The
installed `workspace-582dafaf513210a4ad34` artifact pair supplied six
accepted-lost and unaccepted command cases, which replayed on the candidate.
Four fresh Astra reviews traced the Study card feature through its interfaces.
The final feature review cleared the addressed disclosure and transaction
boundaries. An additional fresh integration review cleared the merged UI
combination after Games tabs joined main. The optimized combined build
passed desktop Chrome and Phone Study WebKit, the Games workbench, and
six pending-command replays from the installed Games tabs baseline.

#### Merged and installed on November 21, 2026

| Runtime component | Verified main merge | Pull request |
| --- | --- | --- |
| Tempo | `4e37421ab72651e89a5dad57ec5cd795c8e127ec` | [#48](https://github.com/tempo-v2/tempo/pull/48) |
| Store | `b3ea523fe038753ce4b6dfa1aaddcd683f27f330` | [#28](https://github.com/tempo-v2/tempo-store/pull/28) |
| UI | `07fd57feb40df5530ca936f920a992e68d99f02b` | [#46](https://github.com/tempo-v2/tempo-ui/pull/46) |

The Tempo and Store merge trees matched the cleared versions. The UI merge
kept the cleared Study paths and included the installed Games tabs change
from [Tempo UI #48](https://github.com/tempo-v2/tempo-ui/pull/48).

After the disposable upgrade rehearsal, the managed launcher installed
`workspace-b917da6ebc3f10036d30` on port 41822. It saved the
stopped-time database backup and previous registration in
`recovery-start-681t6dxm`. The live file kept its dataset and inode
and advanced to schema 18. All 52
pre-existing SQLite tables, including attempts, learning and receipts,
matched the backup row for row. SQLite quick check and foreign-key checks
passed. The registered listener served all 22 desktop
and 24 Phone Study assets byte for byte. Both surfaces
reported the retained dataset. The installed binary and UI matched the
combined build. Binary SHA-256
`a9d54c9c34a0a09e6e320a747ee977c22725847db7c8f533e1e7d143ff6ac0e0`.

## One-line repertoire coverage fixes

| Decision | Authority, inputs and lifetime |
| --- | --- |
| Rank the backlog | Tempo orders current fixable scan gaps by the saved chance of reaching the first missing reply from the opening position. A retained observed count annotates the same stable gap independently of eligibility. A scan-backed fix uses the forecast authoring contract. Observed-only rows follow in count order. The exact gap identity breaks ties. Existing scan estimates survive an edit and carry the earlier-scan label until a rescan. |
| Draft a likely continuation | The accepted Games plan puts one line under review from the selected first reply through the scan's learner move. The selected report fixes the depth. Chess validates the anchor and owns move legality and saved replies. Tempo uses the coverage blend for the opponent and the existing learner recommendation with a Stockfish fallback. The background preview is transient and carries the content revision. Chess provides the exact lead-in used for the draft, and the UI replays it when exporting the viewed line. |
| Save and continue | The existing signed additive Save appends one PGN route and commits a receipt with it. Store checks content revision and preserves existing learner identities and state. The UI replays the identical command if acceptance is uncertain. After acceptance it only reloads the highest-ranked remaining gap in the same list. |

Assemble these heads on schema 18, including the installed Games tabs and Study card origins release.

| Component | Published candidate | Verified head |
| --- | --- | --- |
| Chess | [#27](https://github.com/tempo-v2/tempo-chess/pull/27) | `f790ab5965c48735cb3ee3c0cb6de74cea7f2fa1` |
| Store | [#29](https://github.com/tempo-v2/tempo-store/pull/29) | `5facc3b147ffdeb9d91fdcd301edc39c0e163358` |
| Tempo | [#49](https://github.com/tempo-v2/tempo/pull/49) | `9c06215ab302594d4e19656077e8f6a7871a7060` |
| Desktop and phone UI | [#47](https://github.com/tempo-v2/tempo-ui/pull/47) | `c2ec67bdf9b2ac5706e533bd5ca16ca67c9b20dc` |

Reuse Core `a5f8f320313d6650700617eb24ca83ec2f3cb827` and its packaged
0.2.4 tarball, Learning `ee542cc1971f40de2de7a80edad9f51f2f6eecdc`,
Queue `74e09a1ea1cc2ca9bdf308b8fb7cc75963378214`,
Study `ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`, and
Types `a8e46c9b9442f1180ec33b8035cef1c713414b66`. The locked Rust assembly
used `workspace-remaining-audit.Cargo.lock` and the UI's published lock.

- All 145 UI tests, the packaged desktop and phone build, and the dependency
  direction gate passed. Native continuation tests covered both colors at
  move eight and a custom depth, plus a transposed answer and a shorter line
  when evidence ran out.
- Chrome used saved Maia distributions and local Stockfish on a disposable
  database. It verified the mixed list's probability order, the connected
  board preview, one durable content receipt, preserved Learning and attempts,
  exact replay after lost acceptance, and retry of only the next-gap load
  after the save was accepted. The coverage scan, rescan and restart journey
  also passed against the original optimized candidate and packaged UI.
- Independent review followed the ranking, signed preview and recovery
  through the mounted Games UI. It found a suspension fence and a preview
  board/export mismatch. The candidate checks participation when signing
  and exports the position being viewed. The prior registered binary and UI
  replayed two saved single-response Games commands across the upgrade on
  disposable schema-17 data. The independent reviewer repeated the pair on
  clones of the recorded installation's archived database using the optimized
  candidate. Both preserved the exact command and Learning and advanced the
  browser after one durable receipt. Six other previous-release command
  journeys also passed.
- The locked Rust workspace passed 453 tests and doctests, with two existing
  engine checks ignored. The tactics archive timing check hit its settle
  deadline in debug and passed on an optimized build.
- The Chrome fixture exposed simultaneous starting-position and line searches.
  The continuation now allows the starting search to release the shared
  Stockfish slot, bounded by the preview deadline.
- Archived retained-catalog saves took more than ten seconds, so the Gap
  Editor now allows 30 seconds for the existing signed Save to settle before
  presenting exact-command recovery.

| Candidate artifact | SHA-256 |
| --- | --- |
| Optimized Tempo | `562317298bdd145009e06ad91515c3edbffbd052e5a22a65227d6aa3665313db` |
| Desktop JavaScript | `0602e457b5066feb01571a4d411546dac2bafccd4dace8f2cbdd4ac70074a80c` |
| Phone JavaScript | `40b108fea34c67af63247b25de5d73084ca279c07987b024311f011a8426d3c4` |


### Strict interface review revisions

The first fresh Astra review reproduced two issues in the original candidate.
A matching game's count disappeared when its opponent move became an authored
endpoint that still needed a reply. Tempo now projects retained counts by
stable gap identity and derives eligibility and the authoring operation from
the current repertoire and scan. The preview's Lichess export also dropped
the opening history. Chess now supplies the exact anchor route for the
preview, which the UI validates and replays for export. The draft identity
and signed Save envelope retain their existing formats.


The second fresh Astra verified both fixes and found a scan could reach a gap
ahead of its authored move number via a prepared transposition. Chess now
applies the same saved-reply decision in the lead-in and the scan. The route
can follow a legal opponent move into a position with a verified learner
reply. The mounted Coverage regression reaches the move-three reply and
exports the same route that the player reviewed. The locked combined build
and all 145 UI tests passed on the installed schema-18 baseline.


The third fresh Astra reproduced a mismatch between the forecast preview and
the PGN appended by Save response only. Both signed save paths now use the
Chess-owned coverage anchor. The FEN, opening route, heading and export
describe the same preview. Marked Analysis accepts the exact Chess-verified
forecast route as an anchor alongside its existing authored-route contract.
The continuation worker receives the saved response catalog, and the
single-position editor retains its separate presentation context. The
transposition journey now verifies the heading, authorized marked preview,
export and persisted PGN with one receipt.


### Approved, merged and installed on November 21, 2026

The fourth fresh Astra approved the exact four code heads after independently
running the packaged Chrome journey. It verified that the transposed
heading, export, marked preview and saved PGN followed the same Chess route.
The mounted feature also retained the game count after an opponent endpoint
edit, replayed a lost Save with one receipt, and retried only the next load
after acceptance. The dependency gate and all 145 UI tests passed. The
combined Games workbench and Saved for review browser journeys passed.

Both accepted-lost and unaccepted single-response commands from the
previously registered `workspace-b917da6ebc3f10036d30` browser replayed
against the exact optimized candidate from disposable clones of its live
schema-18 database. They reused the original Save bytes, left exactly one
receipt, preserved existing learning and Study records, and opened the next
gap. The accepted case returned the original receipt reply.

| Component | Pull request | Verified main merge |
| --- | --- | --- |
| tempo-chess | [#27](https://github.com/tempo-v2/tempo-chess/pull/27) | `b23b37fb6d256c65c40596266121b4a33fb47114` |
| tempo-store | [#29](https://github.com/tempo-v2/tempo-store/pull/29) | `443122e2946725571a3c142eec710b910aa21e99` |
| tempo | [#49](https://github.com/tempo-v2/tempo/pull/49) | `0ad7607d66716297414f74f86d27fc81e6671986` |
| tempo-ui | [#47](https://github.com/tempo-v2/tempo-ui/pull/47) | `ec3f8c5d441abbd4c0f490fe558c7e00ee1edcb4` |

The remote merge trees matched the independently reviewed heads. The managed
launcher rebuilt those sources and matched the reviewed binary and every
UI asset before rehearsing on a disposable copy. It installed
`workspace-eb9e0c464f15fde74483` on port 41822 and saved the
stopped-time database and previous registration in `recovery-start-g3nqoqmp`.
The readiness probes allowed five seconds for this invocation, and the
launcher released its disposable copy before retaining the recovery backup.

The running listener matched all 22
desktop and 24 phone assets. Both Study
surfaces reported the retained dataset. The database inode, schema
18, active attempt and all 52
application tables matched the stopped-time backup. SQLite quick check and
foreign-key checks passed. The live Games read returned its first
100 gaps in the expected ranked order.

## Fixed desktop navigation candidate

Tempo UI now has a fixed 40 px bar, with a 44 px menu on narrow and touch
layouts. Pages use the viewport below it. The Games shortcuts use the Games
tab IDs, and the shared page transition respects locks and draft confirmations
from the current view. A direct Games visit can open Saved for review through
the catalog read before entering Study.

Commit `b552ce74da03d6858ccc42522d92f062ff8fb27f` is published for review. The
candidate uses the Coverage Lines release backend from
`0ad7607d66716297414f74f86d27fc81e6671986`, schema 18 and the packaged Core
Components 0.2.4. [Tempo UI #49](https://github.com/tempo-v2/tempo-ui/pull/49)

The guarded build and all 146 UI tests passed. Chrome on disposable data
verified wide, short and touch layouts, Games tab and review history, dirty
repertoire cancellation, Coverage Analysis exit, and Saved for review. Study
kept the board stable and retried only Next after a saved answer. Phone Study
passed its WebKit touch, continuation and access checks.
Independent Chrome review verified that a lost accepted Teach acknowledgement
replayed the original request with exactly one durable receipt.

Fresh review reproduced a history exit bypass and a stale Analysis board after
Games Back. Browser traversal now checks the current page's existing exit
guards before committing the destination. Chrome verified that declining
Forward restores the entry and the unsaved repertoire text, and that accepting
Forward opens the original Games tab. Accepted Games Back closes Analysis
and restores the prior tab. Existing Study history and exact recovery passed
on disposable data.

### Merged and installed on November 21, 2026

Fresh Astra approved the final head after independently running the Games
workbench and Coverage browser journeys. The reviewed source tree merged as
`64c486cd327521ea14fc03dbaf3bec32a243ee8a`. [Tempo UI #49](https://github.com/tempo-v2/tempo-ui/pull/49)

The managed launcher rehearsed the release with the byte-identical Coverage
Lines backend, then installed `workspace-642a00df5faa79064842` on port 41822.
It retained the stopped-time backup and prior registration in
`recovery-start-tr3t1wqk`. The live schema 18 database kept its inode, dataset,
and active Study attempt. All 52 application tables matched the backup.
SQLite quick check and foreign-key checks passed.

The managed service served all 22 desktop and 24 Phone Study assets byte
for byte against the reviewed build. Both surfaces returned the retained
dataset through Study status. Chrome on the live desktop confirmed the
fixed bar and direct Games tab navigation without starting Study.

## Study explanations for missed game tactics

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Explain an accepted missed move | The approved Study plan covers game tactics in Practice and scheduled Test. Tempo uses the accepted Answer's cursor and issued definition. A retained game finding or independently verified capture record establishes origin. Display names, theme labels, and subsequent reports have no role. |
| Retain proof across import and issuance | The Tempo 1 converter reads the kind, identity, board, and moves from one recorded capture request. Tempo's import adapter compiles the complete legal line and matches the canonical definition before attaching evidence. Chess preserves the typed fact across equivalent definitions. A replacement requires proof for its own definition. Store snapshots the fact when it issues the card. |
| Show the relationship on the playable position | Chess applies the one disclosed correction and verifies the resulting relationship. The shared Study UI maps the typed roles and squares to text and board shapes. History inspection hides this live correction's clue and the next accepted move clears it. |
| Recover the original Answer | The optional Study v5 reply field is negotiated by `X-Tempo-Study-Tactic-Explanation`. On replay, the immutable definition, issued attribution, and stored Answer supply the evidence. The client recovery envelope retains the original command and exact submission identity. |

### Review and verification

The first fresh Astra reproduced a clue assembled from unrelated import
aliases and a king-fork clue over two defended targets. In the revised
candidate, flat tags are display metadata. Per-capture evidence must match the
retained source and complete legal definition. Study omits king forks, whose
legal threats the reused geometry cannot establish.

The next fresh Astra cleared the four exact code heads and found no
additional blockers. Independent Chrome verified the later pin, split aliases
and a mismatched capture line, flipped-board correction, history, exact
Answer retry, and Retry Next. The mounted present, renamed, and omitted-name
cases sent matching commands and produced matching durable outcomes for clean
completion, a miss, and Teach. WebKit covered review and Practice on Phone
Study. The native king-counterexample regression passed.

The locked optimized build, dependency gate, 374 native tests and doctests,
148 UI tests, and five converter tests passed. Two existing engine tests were
ignored. All six previous-client recovery cases passed, including the saved
allowance response. Both Answer cases also replayed on disposable copies of the
registered schema-18 database from `workspace-642a00df5faa79064842`.

### Merged and installed on November 21, 2026

| Component | Reviewed source | Verified main merge | PR |
| --- | --- | --- | --- |
| Chess | `ad022f42b4474d2a8371f2b56589f296133f82a8` | `5fd994ccb295af6dc0ca45a6b9239cf667d778ea` | [#28](https://github.com/tempo-v2/tempo-chess/pull/28) |
| Store | `59990838e5a9b9af933d8ef4cd6e1f619bcc1fa3` | `87653ad882135db5ebc7c35a5f71d18b45031c05` | [#30](https://github.com/tempo-v2/tempo-store/pull/30) |
| Tempo | `2d1d83e98ee390688a1ff041857da0ef7e0c7cd9` | `4d7a155e45e2c07afb8e81f6a7a9d7fe87efa11e` | [#50](https://github.com/tempo-v2/tempo/pull/50) |
| Tempo UI | `1cdea04e34c1e7841e461000658a52f6c8770bdb` | `3e1573c0c5056f58c78fccc3391155f68bdcf43c` | [#50](https://github.com/tempo-v2/tempo-ui/pull/50) |

The main merge trees matched the reviewed sources. This build reuses the
Learning, Queue, Study, Types, and packaged Core Components 0.2.4 pins from
the Coverage Lines and Fixed Desktop Navigation releases. The workspace lock
SHA-256 is `ba4ccbbdd3b9e4fa6fd9c40ff8ac2b851f580273eaa00e7f76ab38ce507e765c`
and the UI lock SHA-256 is
`31cfd692d2271cd7b82d26342ed403a60ae34724edc1ca5215402b6cbd22ae1a`.

| Installed artifact | SHA-256 |
| --- | --- |
| Optimized Tempo | `e95885cc9b11675768718bc06ab4b035a8f17326ab8b76231e4a3547879a4ce8` |
| Desktop JavaScript | `cb19019f0d50bcab6c65201d1a4575d1ad0a00bc99ac36f85c7a068c538ae58e` |
| Phone JavaScript | `c6d8fcac5b1b2db37fb114e76ee735e18887f43cc29500d3cded68cda6eaa972` |

The managed launcher installed `workspace-c15e29a396023a240b45` on port
41822 and retained the previous registration and stopped-time SQLite backup
in `recovery-start-d6zld0qt`. Readback matched schema 18, the dataset,
database inode, active attempt, and all 52 tables at startup. SQLite quick
and foreign-key checks passed. The listener served all 22 desktop and
24 Phone Study assets byte for byte, and both Study status reads passed.

The private archive supplied 25 retained captures with exact matched source
identities and definitions. A disposable rehearsal of
`backfill-game-capture-origins` added their proof and preserved all 50
other tables, with zero additions on a repeat. The managed installation
then recorded the same 25 facts and a subsequent preview found zero
remaining. Catalog definitions, versions, active attempt, receipts,
assessments, and learning matched the backup after recording the proof.
The registered background analyzer completed pending work during this
comparison, advancing five tactical-analysis tables through its normal
writer. The remaining 45 tables matched the backup, and SQLite integrity
and foreign-key checks passed again.

## Study tactic feedback across sources

An accepted wrong submitted move in an active tactic Test or Practice may
explain the prescribed move from the issued definition. The Study application
owns when that move can be disclosed and Chess owns the proof. Changing the
issued move or board can change the result. Card names, source tags, and
capture attribution are independent of this decision. A verified immediate
capture with no legal recapture is the fallback after the existing motifs.

This display-only projection uses the existing negotiated reply extension.
Pending commands and saved receipts keep their existing identities and effects,
and a client that does not understand a motif can still use the correction.
Phone and desktop render the same semantic evidence alongside the board.

### Reviewed and qualified candidate

| Component | Candidate source | Pull request |
| --- | --- | --- |
| Chess | `5142e76235343b38263a1acb2f5137b9c9095ebf` | [#29](https://github.com/tempo-v2/tempo-chess/pull/29) |
| Tempo | `d79bd469ac7485a547bfc9d1b66e75fe01daf61c` | [#51](https://github.com/tempo-v2/tempo/pull/51) |
| Tempo UI | `5598a8d96a747bd2d268d87b9aef6e1cc69c633d` | [#51](https://github.com/tempo-v2/tempo-ui/pull/51) |

Build these three heads together with the retained Store at `87653ad`,
Learning at `ee542cc`, Queue at `74e09a1`, Study at `ddf6839`, Types at
`a8e46c9`, and packaged Core Components 0.2.4. Both lockfiles match the
previous installation. The tested optimized executable begins SHA-256
`7e93ebb17d38d909`; desktop and Phone JavaScript begin `7a10a565737b48f0`
and `e0ec2cdf8244f5e2`, respectively.

Fresh independent Astra reviews cleared the consuming path and the final
heads. Native Chess and Tempo, the dependency gate, and 148 UI tests passed.
Chrome exercised the later pin with present, changed and omitted names and
with split source tags. It verified the hanging-piece label, blue correction
arrow and green ring on an imported tactic, history suppression, exact
Answer replay, and retrying only Next after accepted completion. Clean and
Teach name invariance reuse the preceding release evidence. Their paths
cannot enter the changed miss projection. Phone WebKit verified the
imported mate-in-one clue directly below the board after a miss in both
Test and Practice, and Practice preserved the schedule.

All six pending-command cases from the installed release recovered. The
old desktop bundle also accepted a reply containing the new motif and
completed the review. The accepted-but-lost and never-delivered Answer
cases replayed against disposable copies of the registered schema-18
database, with one receipt and one assessment each. No catalog refresh,
migration, or live data changes were needed.

### Merged and installed on November 21, 2026

A fresh Astra review cleared the exact published diffs for the strict
component interfaces and independently ran the mounted Chrome journey.
GitHub main readback matched each reviewed tree after merging.

| Component | Verified main merge | Pull request |
| --- | --- | --- |
| Chess | `9fef1cda9b044d1929a3ab5a4bedbfb36a74f47f` | [#29](https://github.com/tempo-v2/tempo-chess/pull/29) |
| Tempo | `fe39e8883f55f6f7938d42b89d4f5a4dc5bd73d5` | [#51](https://github.com/tempo-v2/tempo/pull/51) |
| Tempo UI | `4cc5a8f92f1ebf88774b2226c4156e16b114ca2b` | [#51](https://github.com/tempo-v2/tempo-ui/pull/51) |
| Candidate ledger | `982c88bd28c1ec759046570bf31aed4a4f9896f4` | [#67](https://github.com/tempo-v2/.planning/pull/67) |

The rebuild from the verified merge trees passed the desktop Chrome and
Phone WebKit journeys and all six previous-client pending-command cases.
The managed installer rehearsed and installed `workspace-4fc560562ed4443ee7a1`
on port 41822. The first desktop read during rehearsal needed a longer
timeout, so the release invocation gave that read up to eight seconds
while retaining the managed checks and backup steps.

The installed optimized binary SHA-256 is
`ee886e303f70807a149863e827ba24999f24f0ff0607f4426e511e45c5a71c57`.
Desktop and Phone JavaScript matched the candidate hashes above. The
registered listener served all 22 desktop assets and 24 Phone Study assets
byte for byte. Both Study status reads and both SQLite integrity checks
passed. The stopped-time backup and prior registration are in
`recovery-start-8ibh9sbt`. Schema 18, dataset, database inode, active attempt,
and the fingerprints of all 52 tables matched that backup.

## Compact Tempo controls candidate

| Behavior | Owner, inputs and lifetime |
| --- | --- |
| Show a button hint | Core handles 500 ms mouse hover and immediate keyboard focus on an enabled button. The caller supplies the action description and any binding it handles. Escape, loss of the anchor, and unmount dismiss the hint. Hint state lives in the mounted browser control. |
| Make common controls compact | Tempo UI groups replay, details, bookmarking, and board tools on desktop and Phone Study. Icons use the existing action handlers, availability, and addresses. The Games replay arrows also step the board from a focused replay control. |

| Component | Verified candidate head | Pull request |
| --- | --- | --- |
| Tempo Core 0.2.5 | `b66af6e6e69a3516d97dd0e9b912cef8feed4f01` | [Core #9](https://github.com/tempo-v2/tempo-core-components/pull/9) |
| Tempo UI | `56f0cd1748ede24fb694e30628d048797f1d5ebb` | [UI #52](https://github.com/tempo-v2/tempo-ui/pull/52) |

The UI lock installs the bundled Core tarball with SHA-256
`d6677336130b4e478ff497dee4b7ae0d85c840cca20d1317de1578591c0f7dfc`.
The disposable browser journeys use the optimized source-independent tactic feedback
backend from `fe39e8883f55f6f7938d42b89d4f5a4dc5bd73d5`, SHA-256
`ee886e303f70807a149863e827ba24999f24f0ff0607f4426e511e45c5a71c57`.

- The packed Core consumer passed Chrome and WebKit checks for hint timing,
  focus, Escape, clipping, offscreen dismissal, and single-tap activation.
- The locked desktop and phone build and all 148 UI tests passed. Phone
  Study in WebKit kept each utility row on one line at 320 and 375 px with
  44 px targets. Continue stayed below the board. Mark recovery kept one
  receipt, and recovery after an accepted answer sent only Next.
- Chrome exercised focused Games replay shortcuts, Study flip and saved
  reviews, tactic capture and pagination, Analysis, Coverage dialog
  dismissal, and Games draft and move-evidence behavior.

The initial independent review found a hint could linger after its anchor
scrolled offscreen and a focused Games replay control ignored its advertised
arrow key. A fresh independent review confirmed the fixes on the published
heads and reran the packed Core, Games Workbench, and Phone Study checks.

### Merged and installed on November 21, 2026

A fresh Astra review cleared the strict interfaces and coupling on the
combined published candidate, including the newer source-independent tactic
feedback. Its packed Core, Phone Study, Games Workbench, and Saved Reviews
checks passed. The locked build and all 148 UI tests also passed.

| Component | Verified main merge | Pull request |
| --- | --- | --- |
| Tempo Core | `71cbd2b1e4a3514f42a1f0293506ad71e0343d93` | [Core #9](https://github.com/tempo-v2/tempo-core-components/pull/9) |
| Tempo UI | `35562186d8c32f1947db7f384faa31ea0de26ecc` | [UI #52](https://github.com/tempo-v2/tempo-ui/pull/52) |

Both main trees matched the reviewed heads. The managed launcher rehearsed
and installed `workspace-12d119da2c68d03793a3` on port 41822, with the same
optimized backend bytes as the previous checkpoint. The invocation reused
the eight-second desktop readiness window. Recovery backup
`recovery-start-wvmq39ny` contains the previous registration and stopped-time
database snapshot.

The registered listener served all 22 desktop and 24 Phone Study assets
byte for byte against the qualified build. Both Study status reads passed,
and the private phone endpoint served the installed bundle. The live schema
18 database kept its inode, dataset, and active attempt. All 52 application
tables matched the stopped-time backup. SQLite quick and foreign-key checks
passed.

### Generated tactical continuations and Study explanations, November 21, 2026

The two reported positions establish the product rule. A generated puzzle should let the learner play the material-winning capture or deliver mate. After a miss, the correction should explain what the issued sequence accomplishes while leaving later answers playable.

- In the first position, White plays Qh5+, Black replies ...g6, and White takes the bishop with Qxc5. The first correction identifies the fork of the e8 king and c5 bishop. In the second position, ...Qxh3 takes the h3 pawn. The defended bishop on e3 and pawn on d3 do not support a skewer explanation.
- Game analysis keeps its existing admission rules and report identity. Tempo obtains a separate best-defense variation for an accepted root during background analysis. The search is limited to depth 18 or 500,000 nodes, requires depth 12, and supplies at most 16 plies. Chess checks legality, net material from the starting position, recaptures and actual mate. An inconclusive search retains the short definition.
- Chess uses the issued solution and current decision to produce a display clue. Relative pins and skewers need a material payoff supported by the continuation. A mating line can be identified without disclosing later moves. Imported solutions keep their supplied length. Labels and source display text do not select the clue.
- Store publishes a verified retained extension as one new version under the same target. Pending requests, an active attempt and a version-bound correction defer publication. Historical definitions, accepted requests and Learning stay attached to their original identities. A related game finding can be carried forward through the verified version relationship. The original report and issuance attribution remain independently addressable.

| Component | Candidate head | Pull request |
| --- | --- | --- |
| Chess | `d8007b93ef69fd3871832f4d1ac46ba901b95daf` | [Chess #30](https://github.com/tempo-v2/tempo-chess/pull/30) |
| Store | `c82cb1a623ce8e98e5153cb2eeb990dce780bc7f` | [Store #31](https://github.com/tempo-v2/tempo-store/pull/31) |
| Tempo | `0bf0daf1a5bc5fa29486fc42c1437974d040768a` | [Tempo #52](https://github.com/tempo-v2/tempo/pull/52) |
| UI | `23b8d9cd704bbeb9c564c4515939ccfb88f615cb` | [UI #53](https://github.com/tempo-v2/tempo-ui/pull/53) |

The assembly used Types `a8e46c9b9442`, Study `ddf6839af0fa`, Queue `74e09a1ea1cc`, Learning `ee542cc1971f` and UI's packaged Core 0.2.5. The optimized executable SHA-256 was `ec394b1b52feac69652699d45f1e882f508e8f6787773488c600e25e823be9b8`. The desktop bundle was `442586bf640d4ed0dfaaae75bd29046700c268bf474898676b748f5c4576c2c2` and the Phone bundle was `944f7ad1dc56705bc76dd4858d3e62441c110a0f9f6797007352b715b180c279`.

**Qualification**

- 109 Chess tests, the focused SQLite version/rollback test, all 25 Tempo tactical-analysis tests including both native Stockfish cases, and 148 UI tests passed. A newly imported game produced the extended fork before its first request issued.
- Mounted Chrome exercised both reported positions, a mating setup, a clean fork and a fork after a miss, one assessment, clue arrows, hidden later answers, display-name invariance, exact Answer replay and interrupted Next. Phone WebKit exercised touch Study and tactic feedback in both Test and Practice. Independent review verified the four published heads and reran the Chrome journey on the candidate executable.
- On a disposable copy of the registered schema-18 database, the idle worker upgraded the pictured fork from v1 to v2. It preserved the previous history row, request, assessments, receipts and schedule. A restart produced no duplicate version. On an isolated copy with the card made due for verification, an ordinary v2 Test played through Qxc5 and still linked to the original game at half-move 13. Its fulfilled request retained v1.
- The previous registered release was `workspace-12d119da2c68d03793a3`. All six pending-command cases for Answer, allowance and repertoire save passed with its binary and assets. Accepted-but-lost and never-delivered Answers also replayed on separate copies of its retained database. Its browser bundle accepted a response carrying the new optional mating clue and completed the attempt.

The component changes are published on feature branches. Merge and installation are separate release steps.

#### Independent interface review corrections

- A continuation search starts only after the authoritative detector completion. Its own deadline or cancellation leaves the completed position available for normal acceptance and the original puzzle can still issue. The zero-budget engine test exercises that fallback through the durable job and Study issuance.
- Store checks pending requests, active work and version-bound corrections before the worker spends engine time, and rechecks the same facts in the write transaction. Publication distinguishes a temporary hold, a superseded basis, a conflicting definition and a committed extension.
- The job dispatcher waits for a retained payoff worker before starting a durable detection deadline. Each retained search yields a dispatch turn to the detector. Only a direct game-analysis request that actually queues work cancels optional payoff work. The dispatch fact is internal to the runtime and a replay of a running request retains its existing HTTP response.

#### Merged and installed on November 21, 2026

A fresh Astra review cleared the published Chess, Store, Tempo, UI and Planning heads after the dispatch fixes. It independently reran the detector replay contract and the Chrome Study journey. All 25 native tactical-analysis tests passed in a serial run against the reviewed source. The installed component trees match the reviewed trees.

| Component | Verified main merge | Pull request |
| --- | --- | --- |
| Chess | `e1542ac67f7e0c69735f5c9abe3871fcc62fa1eb` | [#30](https://github.com/tempo-v2/tempo-chess/pull/30) |
| Store | `606456dda59c06f54c37749e1358f1de8ab0d538` | [#31](https://github.com/tempo-v2/tempo-store/pull/31) |
| Tempo | `d952d215cbedb66810ea6b1493f11183c4865705` | [#52](https://github.com/tempo-v2/tempo/pull/52) |
| UI | `052817d781e9c0b0ba7c19cdffcc1acc7ac7516d` | [#53](https://github.com/tempo-v2/tempo-ui/pull/53) |
| Candidate ledger | `2d4277d11ac566f193570f253e770e2b8b47f03e` | [#70](https://github.com/tempo-v2/.planning/pull/70) |

The managed service installed checkpoint `workspace-cc9e4ebef2187a942646` on port 41822. The registered listener served the qualified binary and all 22 desktop and 24 Phone assets. Both Study status reads passed. The database kept its inode, dataset, schema 18 and active attempt. All 52 table fingerprints matched the stopped-time backup in `recovery-start-73j30u4x`, and integrity and foreign-key checks passed.

The first cutover attempt ran out of disk space while copying the recovery database. The previous registration was restarted and responded before the retry. The successful run released the completed disposable rehearsal copy before creating its verified stopped-time backup. The installer preserved the three separate postgame lab listeners.

The installed idle worker published version 2 of the pictured fork. It stores Qh5+, autoplays ...g6 and requires Qxc5. The original fulfilled request, Learning state, assessment, receipts and version 1 history match the stopped-time backup. Live foreign-key validation passed after the upgrade.

## Phone repertoire Build

| Behavior | Basis and owner | Inputs, independence and lifetime |
| --- | --- | --- |
| Scan and rank likely missing replies | The approved phone Build scope reuses the Games coverage scan. Tempo estimates and orders first-gap reach. Chess decides legal transitions and missing replies. | The chosen repertoire, target, learner move depth and opponent evidence determine the result. Display names and phone layout are independent. Store retains the latest forecast, and rescan is explicit. |
| Preview and append a reply or line | Build reuses the signed gap editor. Tempo admits only a verified forecast gap on the configured private phone surface and signs the exact additive change. Store accepts it through the existing content transaction. | The dataset, repertoire, current document revision, forecast gap and legal selected reply determine the draft. Preview leaves Study and Learning untouched. The signed command and receipt survive reload and restart. |
| Continue after Save | The shared UI editor owns delivery recovery and the Build view loads the next ranked gap after acceptance. Study uses its existing controller on return. | Retry an uncertain Save with its original command. Once accepted, retry the gap read. An earlier coverage estimate stays visible until the next explicit scan. |

| Component | Published candidate | Commit |
| --- | --- | --- |
| Tempo | [#53](https://github.com/tempo-v2/tempo/pull/53) | `108c17b73102f908a19941147ba5ade5447dd07b` |
| Tempo UI | [#54](https://github.com/tempo-v2/tempo-ui/pull/54) | `c65d6c082b93a943c884b171acc4761f50905857` |

Assemble those two heads with the preceding tactical payoff Chess and Store
merges. The other component commits are Learning
`ee542cc1971f40de2de7a80edad9f51f2f6eecdc`, Queue
`74e09a1ea1cc2ca9bdf308b8fb7cc75963378214`, Study
`ddf6839af0fa027aa8e2a67ca6baa3831dfb9deb`, Types
`a8e46c9b9442f1180ec33b8035cef1c713414b66`, and Core
`71cbd2b1e4a3514f42a1f0293506ad71e0343d93` with vendored Core 0.2.5. The
workspace lock is `workspace-remaining-audit.Cargo.lock` with SHA-256
`ba4ccbbdd3b9e4fa6fd9c40ff8ac2b851f580273eaa00e7f76ab38ce507e765c`.
The UI uses its published lock. The schema remains 18.

The optimized Tempo suite, 148 UI tests, architecture gate, phone HTTP
ingress, packaged phone Study WebKit, and full desktop coverage Chrome
passed. At 320 and 375 px, packaged phone Build verified ranked gaps, board
input, Save line, Save response only, both loss cases for scans and saves,
stale-preview refresh, gap-read-only retry after Save, and return to the
original Study attempt. A direct Build launch initializes Study on first entry.
During an existing Study visit a trip through Build retains the completed
result and its Continue action without sending Next or issuing a new attempt.
Existing learning and Study rows were preserved.
The independent review reproduced the stale-preview problem before the fix
and verified the typed refresh path. Serial browser runs passed after one
concurrent run timed out during engine startup.

On disposable copies of the retained schema-18 database, the previously
registered desktop bundle and binary from
`workspace-cc9e4ebef2187a942646` produced signed gap commands for
accepted-with-response-lost and never-delivered Saves. The candidate replayed
the original bytes and opened the next gap with exactly one receipt in each
case. The accepted case returned the original receipt reply. A separate
disposable scan received live evidence from both Maia and Lichess Explorer.

### Reviewed, merged and installed

The first fresh Astra review found that returning from Build with a completed
Study result issued Next. The follow-up preserves the mounted visit in the
shared shell. A second fresh Astra approved the exact published heads after
running packaged phone Study, the shell cases, phone ingress, and nine
mounted metadata-invariance journeys for clean, corrected, and Teach
outcomes.

| Component | Pull request | Verified main merge |
| --- | --- | --- |
| Tempo | [#53](https://github.com/tempo-v2/tempo/pull/53) | `7c5531031c5d9a6397fc6e1b2208c0e22407f5d2` |
| Tempo UI | [#54](https://github.com/tempo-v2/tempo-ui/pull/54) | `bc1d92fc9723c25e05cb79f2317e1308cc53c4bc` |
| Planning | [#72](https://github.com/tempo-v2/.planning/pull/72) | `b0560239de63379ffcd63655b9b67d3d3810a0d1` |

The three merge trees match the approved heads. The managed launcher installed
`workspace-ee43c26e1197cc490ed1` on port 41822 and saved the stopped-time
backup in `recovery-start-9gmt_hqk`. The first rehearsal timed out before
cutover. The retry used up to eight seconds for readiness reads and released
the disposable rehearsal copy before creating the retained backup.

The listener matched all 22 desktop and 24 phone assets. The private HTTPS
route returned the new phone bundle and catalogue for the retained dataset.
The phone ingress also returned the addressed coverage status and gap list.
The dataset, database inode, schema 18 and active attempt were preserved.
All 52 tables matched the stopped-time backup. SQLite quick check and
foreign-key checks passed.

The installed binary matched the managed rebuild. Its bytes differed from
the pre-install workspace executable, so phone HTTP and both packaged
WebKit journeys were rerun successfully with the installed binary and UI
on disposable data. Physical iPhone acceptance remains pending.

## Winning exchange in Study feedback

In the reported puzzle Black plays `...Qxd4 Qxd4 ...Nxd4` and wins the
knight. The earlier explanation pointed out the pin on f2. The clue now
explains that Black has at least two attackers on d4 and only White's queen
can recapture. Study marks d4 and d1 on the existing board.

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Explain the material gain from the revealed capture | The reported puzzle establishes the teaching rule. Chess proves that the issued capture has one legal immediate defender, a legal second attacker in the original position, and a legal retake by that attacker leaving a settled material gain. The proof is limited to the exchange square and ordinary captures. The verified exchange outranks incidental patterns. |
| Show the clue after a miss | Tempo uses the existing authorized correction for Test and Practice. The optional payload carries the target and defender from the issued position. The UI renders those facts on desktop and phone. Display names and source labels are independent of the proof. |
| Recover an interrupted Answer | The typed receipt retains the grading result. On replay, Tempo projects the clue from the immutable issued definition. The prior UI accepts the reply and omits the unfamiliar optional clue. Clients without clue negotiation receive the original correction shape. |

| Component | Verified candidate head | Pull request |
| --- | --- | --- |
| Chess | `f30b74fa5462271ac10d5dac39cfb9b63e811b94` | [Chess #31](https://github.com/tempo-v2/tempo-chess/pull/31) |
| Tempo UI | `a906a8ac7d347eff3b2aad68c24894b9ec10c3ca` | [UI #55](https://github.com/tempo-v2/tempo-ui/pull/55) |

The assembly used Tempo `7c5531031c5d`, Store `606456dda59c`, Types
`a8e46c9b9442`, Study `ddf6839af0fa`, Queue `74e09a1ea1cc`, Learning
`ee542cc1971f` and the packaged Core 0.2.5 from `71cbd2b1e4a3`.
The debug executable SHA-256 was
`f43f14942723af0a552bb04fc34927c235daf6571c6dd1e1518d7ef95d238989`.
The packaged desktop and phone JS hashes were
`6f86c868d916a8844b748ae38af4daa5bf34690f98135fd6273811badfef640c`
and `5f11979fe25eb26ae365228fe36c453336f88d7797ed355fba5c9b17e8916b61`.

- The full Chess suite passed 131 checks including doctests. The UI build,
  148 UI tests and the architecture gate passed.
- Chrome exercised the exact reported puzzle, with its display name present,
  renamed and omitted. It checked identical ordered commands, receipts and
  assessment and Learning effects, with wall-clock milliseconds normalized.
  The second decision remained playable. Interrupted Next retried only Next.
- Packaged Phone WebKit exercised the exact exchange in Daily Study and
  Practice. Both decisions remained playable and only Test produced an
  assessment.
- Disposable copies of the registered schema-18 database reproduced the
  exact puzzle under the prior installed binary and assets from
  `workspace-ee43c26e1197cc490ed1`. Accepted-but-lost and never-delivered
  Answers replayed with their original bytes and one durable assessment.
  The accepted receipt stayed byte-for-byte identical. The previous UI
  also accepted the candidate's response and finished the two decisions.
  No live learning data was changed.
- Independent Guardian review checked the published Chess and UI heads,
  the actual disclosure and consumer path, and reran the focused Chess,
  Chrome, WebKit, metadata and previous-release recovery checks.

The first fresh Astra interface review found that the clue implied an exact
attacker count and a broader material outcome than the proof establishes.
The revised copy states the lower bound and limits the gain to the exchange
square. The Chess API documentation and regression cases now describe the
same scope. The revised component PRs are open.

### Reviewed, merged and installed

A second fresh Astra review cleared the exact revised Chess, UI and
Planning heads for interface ownership and coupling. The reviewer reran
the scoped Chess and UI tests, the mounted Chrome and phone WebKit
journeys, and all three previous-release Answer replay cases on disposable
database copies. The verified merge trees match those reviewed heads.

| Component | Pull request | Verified main merge |
| --- | --- | --- |
| Chess | [#31](https://github.com/tempo-v2/tempo-chess/pull/31) | `a6afe4f78ab844e69bc40be42c8cac5e63fdd2b9` |
| Tempo UI | [#55](https://github.com/tempo-v2/tempo-ui/pull/55) | `dc19b05177e89af8e880da14f3fe0c2d8363976d` |
| Candidate ledger | [#74](https://github.com/tempo-v2/.planning/pull/74) | `45b4de414a7ce27bc4ffb1c2b5575f28ae9466cd` |

The managed launcher installed `workspace-676c127ccf257f4139ab` on port
41822. The release reused the eight-second readiness probes and preserved
the three separate lab listeners. The stopped-time database and prior
registration are in `recovery-start-7jcroi2l`.

The installed executable matched the reviewed assembly's optimized build
at SHA-256 `ba37bc335eb3f93c613bf0f3e4f4b5487c60373c3de201432be984a9315a353e`.
The listener served all 22 desktop and 24 phone assets byte-for-byte.
Desktop and phone Study reported the retained dataset. The private phone
route also served the installed bundle. Schema 18, dataset, active
attempt and database inode survived the restart. All 52 application
tables matched the stopped-time snapshot. SQLite quick and foreign-key
checks passed. The installed binary and assets independently reproduced
the exact exchange in Chrome and packaged Phone WebKit on disposable data.

## Recognizable tactics through the payoff

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Issue a connected lesson through its material gain or verified short mate | The approved recognizable-tactics plan. Chess uses the legal board, concrete motif participants and credible defensive replies. A link needs an observable tactical effect. Labels, aggregate engine scores beyond the first-move quality check, and raw line length do not establish a link. Study grades the resulting issued definition. |
| Requalify retained generated training | Tempo requests Chess's decision using the retained game binding. Store applies it to future delivery with the current version checked in the transaction. Historical definitions, attempts, receipts, game links, manual exclusions and Learning retain their identities. |
| Count simple opportunities at actual game decisions | The verified learner turn and played move determine found, missed, alternative or unclear. A continuation explored for Study does not create a game decision. |

### Candidate source assembly

- [tempo-chess](https://github.com/tempo-v2/tempo-chess/pull/32) `9cb3f8d1e48ebbbb4354bcfe4da4b5a9678ff1aa`
- [tempo-store](https://github.com/tempo-v2/tempo-store/pull/32) `9747044ef8e16d475edd4861218f9013596912cb`
- [tempo](https://github.com/tempo-v2/tempo/pull/54) `8cb1e5cf1055335868be3ade318b067de32e4eec`
- [tempo-ui](https://github.com/tempo-v2/tempo-ui/pull/56) `89eb02fb5e518d2003d4a1778ef6c3b324e4e348`

The assembly uses Learning `ee542cc1971f`, Queue `74e09a1ea1cc`, Study `ddf6839af0fa`, Types `a8e46c9b9442` and the packaged Core 0.2.5 from `71cbd2b1e4a3`. Store upgrades schema 18 to 19. Study commands and replies continue to use the existing wire version. The Personal tactics report adds optional counts while existing readers can continue to use the previous report fields.

The full continuation can be used as engine evidence. Study receives only the verified prefix. Chess checks all immediate defenses to the proposed capture or threat, and follows local exchanges and immediate checking replies as needed. The retained archive advances on the existing background analysis window. Game positions with unfinished recognition evidence are reported as awaiting verification.

### Qualification on November 22, 2026

| Retained game-generated cards | Count | Representative behavior |
| --- | ---: | --- |
| Kept | 387 | Bxf2 takes a loose pawn in one move. |
| Shortened | 60 | The reported card now ends with Bxe8. The following rook move, pawn capture and queen trade do not belong to the fork. |
| Extended | 52 | A checking pawn capture sets up a pin that wins the queen, then a checking fork wins another pawn in a five-decision lesson. |
| Withheld | 547 | The candidate line could not prove a connected material gain or short mate, or the replacement would collide with a retained target. |
| Deferred | 0 | All 1,046 generated targets in this snapshot received a verdict. Eight other game-linked targets were outside the game-owned repair set. |

The first pass needed 75 continuation searches retried. The final search
retains the deepest exact iteration available when it stops at a bound,
using the existing minimum depth and node limits. All 75 settled on retry.
SQLite quick and foreign-key checks passed. The full snapshot comparison
matched the 14 examined preserved tables, including Learning, attempts,
assessments, receipts and manual exclusions. Every existing definition,
the issued request bindings and the active pointer survived.

The new-card integration ended the pictured lesson at Bxe8 after restarting
mid-attempt and recorded one Good. The retained repair independently issued
the same three learner moves through HTTP, recorded one Good and returned
the original game link. Games counted the actual initial learner turn once.
The five-decision chain passed through the normal grader.

With the previous installed schema-18 executable and assets, Chrome
recovered accepted-but-lost and never-delivered Answers after the schema-19
upgrade. The request bytes and accepted reply stayed exact. The previous and
candidate clients advanced the already-issued six-decision card with one
durable assessment. Packaged Chrome and Phone WebKit also passed the
existing disclosure and correction journeys, including the display-name
variants and interrupted Next on Chrome.

The assembled Rust workspace passed 487 tests and doctests. The final
Stockfish search adjustment was exercised separately by the tactics
integration suite. The UI build and all 148 UI tests passed. An independent
review traced the committed qualification and report paths and ran the
focused Chess regression tests.

#### Fresh interface reviews

- After a checking payoff, a later setup must realize a motif the earlier
  tactic enabled. Chess compares against the legal winning motif already
  available before the payoff. A discovered check also needs to enable the
  actual capture rather than leave an already-winning capture available.
- A completed search with zero demonstrated opportunities adds neither an
  unclear result nor pending work to the simple tactics totals. The Games
  projection uses the verified motif set.
- A material lesson ends at its last complete payoff if the mating tail
  would allow an earlier mate that the final-board replay cannot address.
- The tightened proof reproduced 498 of the 499 previously admitted archive
  lines, including the pictured fork and the five-decision chain. One
  previously kept discovered-check card is now withheld. A fresh engine
  search for that card confirmed the decision. The revised tally for the
  same snapshot is 386 kept, 60 shortened, 52 extended and 548 withheld.

### Reviewed, merged and installed on November 22, 2026

The third fresh Astra review cleared the final runtime heads after the
two review rounds. It passed 13 Chess payoff tests, three Tempo report
tests and 18 Store tactical analysis tests. The Game-to-Study suite
passed 26 cases after the first review fixes. The final discovered-check
fix passed its focused Chess checks and the archive replay above.

| Component | Pull request | Verified main merge |
| --- | --- | --- |
| tempo-chess | [PR](https://github.com/tempo-v2/tempo-chess/pull/32) | `b37fa00f37560b846dbab5eebb0fd2581a53c998` |
| tempo-store | [PR](https://github.com/tempo-v2/tempo-store/pull/32) | `0f6eaca7492bbf296bcf9cab9d6708453b529e10` |
| tempo | [PR](https://github.com/tempo-v2/tempo/pull/54) | `64027dd96fcee6e1ac944bdf56353add7017aaba` |
| tempo-ui | [PR](https://github.com/tempo-v2/tempo-ui/pull/56) | `58221fc1fb7e1586456c5fcce68fb4f1fb31bcac` |
| .planning | [PR](https://github.com/tempo-v2/.planning/pull/76) | `9f272d2a0ca0c603a16242d32beec24282cb7315` |

Each merge tree matches its reviewed head. The managed launcher installed
`workspace-12d72e3bad5274125c09` on port 41822, using schema 19.
The binary SHA-256 is `639215a0862ffb45070218a652227aa0112da3b96565dc4be9dbaab1405418d6`.
The service returned Study status for the retained dataset and served all
22 desktop and 24 phone assets byte-for-byte. Private phone ingress
returned the installed bundle. The dataset identity and registered database
inode were preserved. All 52 pre-existing tables matched the stopped-time
backup, and SQLite quick and foreign-key checks passed.

The backup and prior registration are in
`recovery-start-ylxupfcd`. The exact installed artifacts
issued the three-decision fork on a disposable copy, returned the original
game link and saved one Good at Bxe8. The live background requalification
started after installation. The pictured live card was still pending at
readback.


### Black repertoire split and conditional coverage

| Behavior | Basis, owner, inputs, independence and lifetime |
| --- | --- |
| Split the selected Black book | The user chose first-move groups e4, d4, and other. Chess determines legal routes, independent of labels and transpositions. Tempo maps the same canonical position and reply to its new target and copies its saved Learning state. Store validates revisions and commits documents, catalog, Learning and the mapping together. Historical attempts and assessments retain their issued identities. |
| Scan from a saved opening line | The user chose one saved route per repertoire and the absolute learner move deadline. Chess resolves the legal route and move number. Tempo assigns all probability at that position, independent of its frequency in whole games. Store binds published forecasts to the selected route. Old reports and pending requests preserve their initial-position semantics. |

The partition preview found 241 Caro-Kann, 9 Slav, and 14 other routes.
All retained Caro-Kann routes begin e4 c6. The schema-19 disposable rehearsal
preserved 23 destination Learning states, the 270 corresponding game failure
keys and the original attempt, assessment and receipt rows. The replay used
the original preview token and left the same three books. SQLite integrity
and foreign keys passed. The installed artifact must carry Store's guided
repair lineage lookup before the split is applied to managed data.

### Conditional repertoire coverage

One exact saved starting line belongs to each repertoire in the active
dataset. The setting uses the authored move sequence and scope revision.
Chess validates that sequence and supplies the absolute learner move number.
Tempo starts all probability at the resulting opponent position after any
required prepared learner move. Store invalidates a forecast when the scope
revision changes, even if later edits restore the same moves. A prior report
or pending command without the scope carries revision zero and the initial
position. A displayed repertoire label cannot change these decisions.

| Component | Split change | Coverage change |
| --- | --- | --- |
| Chess | [#33](https://github.com/tempo-v2/tempo-chess/pull/33) `aa6639a` | [#34](https://github.com/tempo-v2/tempo-chess/pull/34) `46d4f23` |
| Store | [#33](https://github.com/tempo-v2/tempo-store/pull/33) `91fc17e` | [#34](https://github.com/tempo-v2/tempo-store/pull/34) `ebd7992` |
| Tempo | [#55](https://github.com/tempo-v2/tempo/pull/55) `eaa66bd` | [#56](https://github.com/tempo-v2/tempo/pull/56) `e91ad88` |
| UI | | [#57](https://github.com/tempo-v2/tempo-ui/pull/57) `941afe7` |

The managed workspace combines both changes over the recognizable-tactics
release, with Tempo `6fd6e8d`, Store `e203102`, Chess `bde3e96`,
and UI `941afe7`. The other component pins and workspace lock are from
that same installed release. The GitHub feature pull requests are open.

The independent optimized split rehearsal preserved all 23 moved Learning
states, 270 accepted failure keys, and the original attempt, assessment,
receipt and game observations. All 22 moved corrective targets still resolve
to their original raw game and played move subject to the reset boundary.
The live split preflight found an open attempt on a moved target and deferred
the edit. Finish that attempt and repeat the live preflight before applying.

The conditional estimate, forecast retirement and signed editor contracts
passed. The Store suite passed 53 tests. The UI suite passed 148 tests.
Packaged Chrome and Phone WebKit covered the starting line picker, gap
editing and exact command recovery. Both an accepted and an undelivered legacy
coverage request recovered with original whole-game scope when moving from the
previous installed binary to schema 20 on disposable copies.

The managed launcher installed `workspace-b0d3ec28b5c64b6f6757` on 41822.
The registered database migrated from schema 19 to 20 and retained its
dataset and active attempt. SQLite quick check and foreign keys passed.
A rollback backup and prior registration are in
`recovery-start-sfwzumu9`. Running readback confirmed Italian starts after
`1.e4`, Caro-Kann after `1.e4 c6`, and e4e5 after `1.e4 e5`.

The final installed executable passed the packaged Chrome and Phone WebKit
checks on disposable data. After the live Study attempt cleared the edit
fence, a new preflight passed and the split was applied. The live catalog
kept 241 Caro-Kann routes and gained 9 Slav / vs. 1.d4 routes and 14 Black
vs. Other First Moves routes. The original apply token replayed without an
additional write. All earlier attempts, assessments and receipts were
present and unchanged. All three coverage starts survived, and SQLite
quick check and foreign keys passed. The immediate pre-split backup is in
`recovery-repertoire-split-7rrzhg5o`.

#### Fresh interface review and corrections

| Behavior | Basis, owner, inputs, independence and lifetime |
| --- | --- |
| Resolve a moved correction | The committed split maps an exact destination answer version to its source answer version and cutover time. Store owns this relation and resolves it alongside reset and miss boundaries. Receipt text and repertoire labels cannot affect it. Migrate the already installed split once, using the historical receipt format only for that migration. |
| Commit a forecast edit | The forecast editor authorizes its addressed report for the selected starting line. A newly authorized but unaccepted Save requires that report and scope to remain current when Store commits. An accepted Save replays its immutable receipt. Keep the previous installed token protocol readable for commands already issued. |

A signed forecast edit also depends on the repertoire remaining active and
verified at the time of commit. The same Store guard applies to desktop and
phone. A normal authored-content edit retains its existing scope.

The first Astra review identified receipt-format coupling, stale forecast
Save authorization, and the need to check verified source authority. The
second review reproduced the remaining desktop suspension gap and checked
the public editor contract. A third fresh Astra reviewer cleared the combined
runtime after the suspension and removed-prefix fixes.

| Component | Merged pull requests | Verified main |
| --- | --- | --- |
| Chess | [#33](https://github.com/tempo-v2/tempo-chess/pull/33), [#34](https://github.com/tempo-v2/tempo-chess/pull/34) | `f62d2bba248862862f1fe72c65d5df69a361dda4` |
| Store | [#33](https://github.com/tempo-v2/tempo-store/pull/33), [#34](https://github.com/tempo-v2/tempo-store/pull/34) | `4cac8713da331115fdf53e6bcdd32d27c5d4af32` |
| Tempo | [#55](https://github.com/tempo-v2/tempo/pull/55), [#56](https://github.com/tempo-v2/tempo/pull/56) | `c24ca5a65cfc409d7138cb1e1a919773619ba1bf` |
| UI | [#57](https://github.com/tempo-v2/tempo-ui/pull/57) | `801daf2793c86b64f1e2381ffb2d9db18cdc1386` |

Each remote main tree matched its reviewed version. The schema-20 copy
retained all 23 partition links on upgrade to schema 21 and recovered both
an accepted and an undelivered prior-version signed Save. The public editor
contract rejected unaccepted saves for a changed scope or suspended book,
and replayed an accepted save. The Store suite passed 53 tests and the UI
suite passed 148. The merged optimized executable passed packaged Chrome
and both phone WebKit recovery journeys on disposable data.

Managed Tempo is running `workspace-e94d03d7261d1a57a771` on port 41822.
The executable SHA-256 is
`e59bb3ca3b677ade6ed70644082fc7f783c4ce4ec761452dcc6eb196bddb885a`.
After the launcher's readiness timeout during migration, direct readback
confirmed the registered listener and private phone ingress. The executable
and all 46 served assets matched the qualified build. The schema-20 rollback
backup and prior registration are in `recovery-start-_52qr0g0`. The live
schema-21 database kept its dataset, active attempt, Study records, new
repertoires and three coverage starts. All 23 partition links matched the
pre-upgrade receipt mapping. SQLite quick and foreign-key checks passed.

## Clarity for simple capture drills

| Behavior | Basis, owner, inputs, and lifetime |
| --- | --- |
| Withhold a game-generated, one-move hanging-material lesson when another legal capture independently keeps at least the same material gain | The approved capture-drill plan. Chess uses the issued board, proposed move, verified motif and existing checks for forcing replies and material retention. Engine ordering, card labels and game attribution do not decide ambiguity. A second defensible capture changes admission. A rename does not. Store persists the verdict for the current version through the existing qualification gate while retaining prior definitions, attempts, receipts and learning. |
| Explain a revealed tactic on both correction paths | The approved capture-drill plan. Tempo projects the existing optional Chess explanation after a submitted miss or Show move in active Test or Practice, using the pinned version. Blind delivery still omits it. The desktop and phone render the same feedback. Replays preserve the command identity and accepted assessment. |

### Candidate and verification

| Component | Draft PR | Candidate commit |
| --- | --- | --- |
| tempo-chess | [PR](https://github.com/tempo-v2/tempo-chess/pull/35) | `e9272e26063a17d8382522a2b9bc5897c5d4eb1d` |
| tempo-store | [PR](https://github.com/tempo-v2/tempo-store/pull/35) | `0d6593733790aec0e244124b7fe745e47d8cf4bd` |
| tempo | [PR](https://github.com/tempo-v2/tempo/pull/57) | `204e7f0398ec12e5b7a9a0f22f4d4684526db624` |
| tempo-ui | [PR](https://github.com/tempo-v2/tempo-ui/pull/58) | `cdc8c43d1ed5d3c9844e91e85ad8c8adba86aa31` |

Assemble these heads with Types `a8e46c9b9442`, Study `ddf6839af0fa`,
Queue `74e09a1ea1cc`, Learning `ee542cc1971f`, and the packaged Core 0.2.5
from `71cbd2b1e4a3`. The workspace lock matches the conditional-repertoire
coverage assembly (SHA-256 `ba4ccbbdd3b9e4fa6fd9c40ff8ac2b851f580273eaa00e7f76ab38ce507e765c`).

The installed schema-21 baseline was `workspace-e94d03d7261d1a57a771`.
Its disposable copy migrated to schema 22 and withheld 20 cards, including
the reported …Nxd4 / …Nxh4 position. The clear …Bxf2 example stayed
eligible. The reported card issued before migration. After migration the
same issued attempt could resume, and future Study and Practice issuance
excluded the card. That scenario also exercised a retained request
whose card needed a new qualification row. Bidirectional comparisons
matched content and version history, game records, attempts, assessments,
learning, receipts, saved reviews, pending request bindings and the active
pointer. SQLite quick and foreign-key checks passed.

Independent review traced new qualification, retained ownership and the
consumer paths. The assembled locked Rust workspace passed 491 tests and
doctests, with five engine or integration cases ignored by default. The
rebased desktop and phone bundles built successfully, and all 148 UI
tests passed. The Chess regression exercised the reported card, a unique
capture, and an immediately defended alternative. The existing Chrome
journey on the assembled candidate compared ordered commands and durable
results with the original, renamed, and omitted display name. It also
passed previous-release concession recovery and interrupted Next.

On the installed baseline and disposable retained data, Chrome recovered a
schema-21 Show move command both when it was accepted but its reply was
lost and when the request never arrived. The candidate sent the original
command bytes, completed with one Again, and displayed the optional clue.
The accepted typed receipt was byte-identical in SQLite. The reprojected
reply added only the optional clue. Packaged Phone WebKit displayed
Hanging pawn after both Show move and a submitted miss in Practice,
with identical saved learning and no scheduled assessment.

Portable snapshot restore remains outside this upgrade. Its format does
not carry game tactic request or qualification records. The candidate
has been built and tested separately from the running installation.

### Astra review correction

The first fresh review found a position where either knight capture takes a
rook, then the opponent can take a pawn. Each move retains four points.
The initial check compared the competing capture's proved four points with
the prescribed capture's immediate five. Chess now uses the existing
forcing-reply and exchange proof on both moves. It finds the greatest
material balance the prescribed capture can retain, then checks whether a
different legal capture can retain at least that balance. The regression
also checks a position where the competing capture retains less.

The corrected Chess candidate is `746d484093ea0d8b129c7d6d5f34b653212754ba`.
The application, Store and UI candidate heads above are unchanged.

The initial review also reproduced two boundary failures. A verified
longer line could resolve to an older quarantined one-move game card,
then reactivate that card. A same-day Study progress stamp could remain
valid after the migration changed eligibility. Chess now exposes the
qualified game proposal as a distinct value. Its planner checks the
resolved definition and can return no training plan. Tempo still records
the finding and preserves any existing request binding. Independent
authored content and allowable longer lessons retain their existing
resolution. Chess re-proves older standalone moves whose stored motif is
absent, and a mating capture can satisfy the same material-retention floor.

Store uses the same revision and evidence invalidation for migration and
normal qualification publication. A migration that withholds cards bumps
the Study revision once in the same transaction. It preserves the active
attempt, per-attempt revisions, content versions and existing receipts.

The revised runtime heads are Chess `e17b0f2697702c4d1a45c6da0069164c1857d9c1`,
Store `b5102b7612787dcc9e2362c73f90a85bb2c9223f`, Tempo
`9656c2137f53dc81f3030a17e3b5d89fbec916bd`, and UI
`cdc8c43d1ed5d3c9844e91e85ad8c8adba86aa31`.

The next review checked the reverse resolution. Chess now limits the
early proposal step to proving the candidate payoff. It checks ambiguity
after resolution establishes the actual lesson and its ownership. A new
ambiguous one-move game lesson has no training plan. An exact authored
match or retained longer lesson can still serve as before. The final
Chess review head is `a43c2bb15698d8c3ad30dd7ddca76e51434ebc65`.

### Reviewed, merged and installed on November 22, 2026

The fourth fresh Astra review cleared the final interfaces and behavior.
It reran all 17 Chess payoff tests, the retained-content and Store upgrade
regressions, both correction projections and the issued-version contract.
The locked workspace passed 495 tests and doctests across two runs. The
archive report test reached its assertions and passed after an isolated
rerun following fixture setup timeouts under build load. Five cases stayed
ignored by default. The unchanged packaged UI had passed all 148 tests.
The final optimized pair passed the schema-21 rehearsal, including
refreshing the previous same-day due count, both Chrome Show move
recovery cases, and both Phone WebKit Practice reveal paths.

| Component | Merged PR | Verified main commit |
| --- | --- | --- |
| tempo-chess | [PR](https://github.com/tempo-v2/tempo-chess/pull/35) | `becee471325ece0a382d4e482263e2b87670a23d` |
| tempo-store | [PR](https://github.com/tempo-v2/tempo-store/pull/35) | `6190660a67504dccea9617154f86fd5c7e3bd671` |
| tempo | [PR](https://github.com/tempo-v2/tempo/pull/57) | `33f8d119ab31d7bea4f84310bfd62a3a02494376` |
| tempo-ui | [PR](https://github.com/tempo-v2/tempo-ui/pull/58) | `82c6f6eb3e58104e0f81df0767195aa4353bc909` |
| .planning | [PR](https://github.com/tempo-v2/.planning/pull/80) | `7966d9bc8192e008fbef3e49f1f6c1be2301e701` |

All five merge trees matched the reviewed source. The managed launcher
installed `workspace-14d369622d72f12c66af` on port 41822, with SQLite
schema 22. The installed executable SHA-256 was
`2536f1b466f53dccf3e87292db2f47330302c4cf56bf6d6e33650aaa86af8f1d`. The registered listener served
all 46 desktop and phone assets byte-for-byte. Desktop
and private phone Study reported the retained dataset.

The live readback found 42 newly withheld verdicts,
including the reported …Nxd4 / …Nxh4 card. The dataset, database inode,
active attempt, content versions, attempts, assessments, learning, games,
receipts, saved reviews, requests, manual exclusions, repertoire lineage
and coverage starts matched the stopped-time snapshot. The Study revision
advanced and SQLite quick and foreign-key checks passed. The snapshot
and prior launch registration are in `recovery-start-9wz2d2qg`.

## Indexed Study relevance read

The Store read continues to return saved personal relevance and verified
modeled reach for the current dataset and answer version. Queue retains
ownership of ranking. SQLite materializes verified modeled rows once, so
the join can use a temporary covering index on target ID. The change uses
the existing public interface and has no schema or wire migration.

A fresh Astra review cleared the Store boundary and checked producer-side
target uniqueness and the verified-input join. The review independently
compared both query forms on 3,516 distinct targets. The retained schema-22
read also returned 3,516 identical rows, with a five-run median of 712 ms
before the change and 23 ms after it. The earlier candidate passed 53
Store tests, 29 Queue tests, four doctests, 42 Study contract tests and
the focused model-projection test.

[Store PR #36](https://github.com/tempo-v2/tempo-store/pull/36) merged to
main at `065b626f315a7145a7d64119a59c6c93e817df6e`. The fetched merge
tree `5f60bff31f92643508b700d1d336dd0949ea8c6a` matched the assembled
candidate. This release uses the same schema-22 Tempo, Chess, UI, Core,
Learning, Queue, Study and Types pins as the preceding installation, with
this replacement Store pin and the same workspace lock.

On matched disposable copies of the schema-22 dataset, the combined
optimized build returned the same Study card and Progress values. Fresh
Next took 1,344 ms on the previous build and 291 ms on the candidate.
Progress took 1,426 ms and 604 ms, respectively. These are local samples.
The full catalog read still contributes to fresh Next.

On November 22, 2026, the managed launcher installed
`workspace-e1c18810c03bd3ad05db` on port 41822. The installed backend
SHA-256 is `c5c7e27765ee4cfee61010c03012a10297f87e5ae92eb8b5fe5687004eea2edf`.
All 46 desktop and phone assets matched the preceding installation and
the built artifact. Live desktop and private phone Study endpoints
reported the retained dataset, and the desktop Progress endpoint replied.
The database kept schema 22, its file inode and active attempt. The 13
checked tables matched the stopped-time backup in both directions,
including content, Learning, assessments, receipts, games, and saved
reviews. SQLite quick check and foreign-key checks passed. The backup
and previous registration are in `recovery-start-o8ik55sn`.

## Structural cleanup execution

The cleanup starts from the currently installed Store #36 assembly and
current published integration revisions in [current assembly](current-assembly.json).
Unrelated implementation is paused for this run. No existing checkout was reset.
The [operation contract](structural-cleanup/operation-contract.md) records the
simplified supported product before dependent implementation.

- T01 checked the registered listener binary and SHA-256, the served desktop index
  against the installed artifact, and all ten live GitHub main refs. The historical
  audit probe inspected earlier local checkouts and skipped unverified query
  extraction. Its result does not repeat or invalidate Store #36.
- A fresh read-only SQLite online backup from the running schema-22 dataset passed
  integrity and foreign-key checks. The full backup is held locally with restricted
  permissions. Portable export is outside recovery.
- T02 owns the current operation/consumer census. T06 owns test-only SQLite probes.
  Coordinator retains schema sequence, public interfaces, application composition,
  locks and manifests. One heavy test run may execute at a time.

- T02 census covers 45 routes, 10 CLI modes, 39 command variants, 16 startup and
  worker paths, and four receipt families. Current product dispositions accompany
  the census. T13, T34 and T37 own external-consumer and previous-release lifetime
  investigations before removal.
- T03 review covered managed phone, allowance authority, authored-frontier and
  correction semantics, replay identity and operation ceilings. The contract
  records all decisions before T04/T05 and downstream implementation.
- T06 test capability released for review in [Store #37](https://github.com/tempo-v2/tempo-store/pull/37)
  at `cca526807e9f32353cf562fd8e710723003924c3`. The author and coordinator each ran
  all 20 focused tactical tests. The work regression recorded identical index
  steps and zero full-scan steps across its two unrelated-state sizes.
- T04 adopts canonical cleanup guidance and a current/missing/stale identity
  check. The current workspace guidance is preserved pending assembly adoption.
- T05 released its dataset identity slice in [Store #38](https://github.com/tempo-v2/tempo-store/pull/38)
  at `9abd554a06e72beb229f0acd2b1e5ef9fa2c5139`, stacked on Store #37.
  Study, authoring, Games acceptance, administration and writer admission
  capabilities remain open.
- T07 adopted the identity read in the real Games caller in [Tempo #58](https://github.com/tempo-v2/tempo/pull/58)
  at `366a2e0fed5f922c7d06a163c1bc0eb2da15efdb`. The compatible test assembly
  uses those two commits and every other baseline pin and lock. The SQLite
  authorizer allowed only the dataset identity read. Disposable Games Review
  passed with poisoned Study attempt, Learning, run and policy records and
  rejected a stale dataset. The new assertion failed on the prior installed
  binary. The relevant repertoire suspension Rust contract also passed.
- The runtime still uses the existing Study selector and status-driven Games
  apply. No feature retirement has been verified. Continue with remaining T05
  capability contracts and the T08 health/context consumer. Subsequent tasks
  retain their packet prerequisites. No cleanup candidate was merged or installed.

### Context and retained Learning

- T08 adopted context on desktop and authenticated phone and through managed
  readiness in [Tempo #60](https://github.com/tempo-v2/tempo/pull/60)
  `726ef278095a0c43f00f285c1101c8d9b55a45ae` and
  [Store #40](https://github.com/tempo-v2/tempo-store/pull/40)
  `0cbcd4b3b486149fe87cfa05f61c2b0cbfb2d565`. The HTTP route passed while Study
  policy was unreadable, rejected the wrong phone owner, and reported the actual
  schema. The Store identity check and two disposable installer cases passed.
  T46 still owns independent cold startup and T09 owns UI consumption.
- T11 retained Test uses the configured lifecycle in Tempo #60 and
  [Learning #10](https://github.com/tempo-v2/tempo-learning/pull/10)
  `1d75747031ff35959d3adf31719f8429e9d46270`. All 61 application contracts,
  25 Learning unit tests and one doctest passed on the combined assembly.
  The completed personal-tactics backfill command was removed. The existing
  fixture bridge remains until T13 eliminates its callers and the legacy Games
  bridge is retired with its consumer. Persisted shapes are unchanged.
- T13 removed live stdio registration and its demo in
  [Tempo #61](https://github.com/tempo-v2/tempo/pull/61)
  `9185321f4cf29b006086ba8c29ee16c8e4578b41`. The existing boundary test now
  exercises real HTTP and SQLite. Four checks passed, including rejection of
  stdio and recovery of an exact answer with one durable grade. Library and
  Queue/Study fixture removal remain open.
- T10 published offline ingress, current-row migration and Chess vocabulary in
  [Tempo #63](https://github.com/tempo-v2/tempo/pull/63)
  `df6f5edfec6d3eea227a4cba9fd4774b8c41e3af`,
  [Store #41](https://github.com/tempo-v2/tempo-store/pull/41)
  `ff5e159d7e8d9eff6d3a3b20cd0225475a037fd5` and
  [Chess #36](https://github.com/tempo-v2/tempo-chess/pull/36)
  `df5304f75c5f1d92b1c1538c616d53fb2f9e5505`. Rebuilt all Rust dependencies
  in a fresh target with Learning `1d757470`. All 69 scoped Rust checks and
  five converter tests passed. The disposable schema upgrade preserves issued
  attempts, historical content, Learning and receipts byte for byte and rolls
  back malformed required rows. Actual Study admission now uses only typed
  membership for new tactics and stable target order in
  [Tempo #64](https://github.com/tempo-v2/tempo/pull/64) `c419f90593a89aef017d7ec9f223fc0d4ef9bc53`.
  The former pack parsing now runs only for the schema-1 offline import report.
  Due-capture priority remains for T17/T21 to remove.
- T09 published shell, Capture and Games context in
  [UI #60](https://github.com/tempo-v2/tempo-ui/pull/60)
  `4d87636c24f6b5daf72d48562f4386cd667da977`. All 157 UI tests passed.
  Mounted evidence protects exact pending payloads and confirms retained plain
  replay, manual import and library browsing without Study or Repertoire
  identity calls. Remaining shell/controller scoping and optional polling
  retirement are open.
- T50 moved the installation guard to the one Tempo tooling owner with
  [Tempo #62](https://github.com/tempo-v2/tempo/pull/62)
  `4f58634de40f066967896df4929ed11fca889447` and
  [UI #61](https://github.com/tempo-v2/tempo-ui/pull/61)
  `b9123489c8472fde03d4f2dad21a0884f4b3f27b`. All five protection tests
  passed and a disposable desktop/phone build used the shared guard.
- T51 current setup and verification use [one manifest](current-assembly.json).
  A fresh temporary workspace fetched all nine published component pins,
  verified both locks, packaged Core and canonical guidance, and resolved all
  seven Rust workspace packages with the locked manifest. The same verifier
  rejected an intentionally stale guidance copy and passed after restoring it.
  Its reviewed assembly is distinct from the installed baseline and does not
  qualify installation. T54 still owns the normal release gate.
- The same Tempo #64 candidate removed the standalone fixture application,
  with [Queue #15](https://github.com/tempo-v2/tempo-queue/pull/15) `f53fbbb730e8a510223e59303f3f7a69796e774a`,
  [Study #4](https://github.com/tempo-v2/tempo-study/pull/4) `9756fce36b373af24b15cb6bf3ad171052ac5f5d`
  and [Chess #37](https://github.com/tempo-v2/tempo-chess/pull/37) `33958d575d6949fdd5fef77065f02db0165f94d7`.
  The exact compatible assembly used Store `ff5e159`, Learning `1d75747`,
  Types `a8e46c9` and the existing lock. It passed 54 Tempo contracts,
  356 library tests and the disposable desktop/private-phone context journey.
  Five existing real-engine tests remained ignored and no engine or live
  installation claim follows from those checks.
- T42 has an unpublished
  cap draft `916d080`. The current HTTP dependency may finish reading a
  body during request cleanup, so a declared byte limit alone cannot protect
  the command owner. T42 remains open for deadline-safe ingress and evidence.
  Heavy tests remain serial.

### Connected-run retirement

- T14 removed connected-run issuance and opt-in handling across
  [Tempo #59](https://github.com/tempo-v2/tempo/pull/59) `4338b3718fae736749a4ffc927d14c7b543b69d6`,
  [Store #39](https://github.com/tempo-v2/tempo-store/pull/39) `b792843aaf8dd22b3b4efee44bfd83fc41501eac`
  and [UI #59](https://github.com/tempo-v2/tempo-ui/pull/59) `279a22c0fac78af77bec0616a0b26df6405f9f91`.
  Two Tempo cases, a real SQLite malformed-row isolation case and 149 UI tests
  passed. Disposable HTTP verified equivalent issuance with both old-header
  variants (excluding generated IDs), an unchanged retained active Test and
  previous installed warm-up receipt replay with zero added effects.
  Archive rows/encodings remain inert. T34 still owns full prior-release replay,
  T38 legacy reset cleanup, and T27/T57 final unreachability of retired helpers.
  The reviewed drafts are published and the managed installation is unchanged.

### Addressed Study and plan preparation

- Explicit Resume uses the addressed compatibility capability in
  [Tempo #65](https://github.com/tempo-v2/tempo/pull/65) `ca0da162d153e156efd58df57c7cda822066ef20`
  and [Store #42](https://github.com/tempo-v2/tempo-store/pull/42)
  `6a130fa8f9149915835712b430d8b15574048dc6`. A real SQLite authorizer
  verified the addressed read without Learning or assessment access. All
  54 application contracts passed. The disposable HTTP consumer resumed the
  same issued attempt while Learning was unreadable.
- T15 owns the pure work-token, basis and update types. T16 is designing
  schema 24 for those exact types and the captured epoch fence. T42 is
  replacing the request dispatcher ingress so the app write owner will receive
  prepared bodies, independent of socket cleanup. These slices are active and
  have no installation result.
- T12 compact Study content and exact issued definition provider are published
  in [Store #43](https://github.com/tempo-v2/tempo-store/pull/43)
  `c9efc50ad72065388e6a5ed4c77d50c9920c8433` and adopted for explicit Resume
  in [Tempo #66](https://github.com/tempo-v2/tempo/pull/66)
  `5cd0269d0635637de97d9c2680ada9690e87817e`. Three SQLite projection tests,
  all 54 application contracts and the disposable desktop/private-phone
  journey passed. The latter resumed the same guided activity with unreadable
  Learning and optional history bytes. Batch and Next adoption remain T17/T18/T21.

### Exact combined review assembly

- [Tempo #67](https://github.com/tempo-v2/tempo/pull/67) `4538e22560ae9b320c1dcb7aeebeb7483c6b883e`
  and [UI #62](https://github.com/tempo-v2/tempo-ui/pull/62)
  `42336036c59595b72f4f89e2ba0c438357c8171f` are the current review heads in
  [the single assembly manifest](current-assembly.json). The backend contains
  typed admission, fixture retirement, the later context checks, addressed
  Resume and issued content, bounded ingress, and the shared guard. The UI
  contains Games/Capture context, the shared guard and the saved-import fix.
- The exact backend composition passed 54 application contracts, three
  loopback HTTP cases, and four diagnostics cases. The exact UI passed all
  159 tests and built desktop and phone assets. A disposable paired instance
  served schema-23 context and byte-identical JavaScript from that build.
  The saved import can retry the exact envelope while context is unavailable.
  A known mismatch stays explicit, a failed delivery retains the original
  envelope, and new imports require context.
- The bounded ingress handles body and socket lifetimes ahead of the
  application. PGN preparation, fair apply scheduling, legacy oversized
  receipt recovery, prepared Next, independent Progress and projection-free
  acceptance remain open. These checks qualify the listed review slices.
  The installed baseline has not changed.
- [Types #2](https://github.com/tempo-v2/tempo-types/pull/2) and
  [Queue #16](https://github.com/tempo-v2/tempo-queue/pull/16) release the
  work-token and plan records used in this review assembly. Their 23 unit tests
  and one doctest passed. [Queue #17](https://github.com/tempo-v2/tempo-queue/pull/17)
  and [Store #44](https://github.com/tempo-v2/tempo-store/pull/44) subsequently
  released the pure stable builder and schema-24 staging capability. They
  passed their own suites and remain outside the schema-23 combined pins
  pending coherent-capture and runtime adoption.
- T13 deletion audit found the old `init-practice` alias still registered.
  Its bounded removal is assigned. T39 read-only report and worker retirement
  is assigned as a deletion slice, with shared tactical paths and persisted
  receipt compatibility kept in their owning packets.

### Schema-24 review successor

- [Tempo #68](https://github.com/tempo-v2/tempo/pull/68) and
  [UI #63](https://github.com/tempo-v2/tempo-ui/pull/63) removed the personal
  tactics report worker and UI. Both old endpoints return explicit retirement
  without dispatching Store work. Those revisions also removed the old
  initializer alias; the current fixture proves it creates no database.
  Retained Study, context, Games and private-phone checks passed. Report-only
  maintenance and other retired tactical workers remain separate.
- [Queue #18](https://github.com/tempo-v2/tempo-queue/pull/18) `0363fcb` and
  [Tempo #69](https://github.com/tempo-v2/tempo/pull/69) `16c56ed` remove the
  rotating tactic ranker. Only the offline import report retains legacy pack
  fields. Exact combined schema-24 testing passed 14 Queue tests, four
  offline importer tests, 55 Tempo contracts and one phone HTTP case.
- [Store #45](https://github.com/tempo-v2/tempo-store/pull/45) `c35a242`
  writes versioned Study receipts and reads the exact legacy form. All 72
  Store tests and three doctests passed. [Tempo #70](https://github.com/tempo-v2/tempo/pull/70)
  `12611b9` exercised accepted and never-delivered Teach against the actual
  previous installed backend and a disposable database. Valid retries worked
  without a plan or summary. The original accepted receipt stayed byte-identical;
  the previously unsent command accepted once in the new form. The full
  previous-release browser matrix and T20 acceptance are open.
- [Tempo #71](https://github.com/tempo-v2/tempo/pull/71) `0dfaf8b` and
  [UI #64](https://github.com/tempo-v2/tempo-ui/pull/64) `8c2fc5b`
  are the current combined review successors. They remove the interactive
  position-evidence worker, panels and requests. Five runtime diagnostics and
  all 155 UI tests passed. The disposable Chrome flow exercised actual game
  import, replay, repertoire authoring and mobile resume with zero retired
  endpoint calls. An unused private Stockfish helper remains for its retirement
  owner. None of the cleanup has been installed.
- [Store #46](https://github.com/tempo-v2/tempo-store/pull/46) `2861ec4`
  passed three coherent-capture tests, 72 Store unit tests and three doctests,
  including a second-connection WAL race. This capability remains separately
  staged. It explicitly reports incomplete until durable day authority is
  supplied by T19/T20. Prepared Next, independent Progress and production
  acceptance adoption remain open.
- [Tempo #72](https://github.com/tempo-v2/tempo/pull/72)
  `2ddd462be66b1feec7237b28c7536a718697e686` adopts addressed replay from
  [Store #47](https://github.com/tempo-v2/tempo-store/pull/47)
  `8864597a11070bfb7842818eb39cddc97b01b030` for Answer, Give Up, Concede,
  Acknowledge, Skip and Abandon. The active dataset fences replay, and new
  work rechecks receipts against concurrent acceptance. All 55 Tempo
  contracts and two actual prior-binary Teach HTTP cases passed on these
  exact heads. Accepted replay succeeded with unreadable Learning. Dataset
  mismatch stayed explicit, and never-delivered Teach accepted once with an
  absent plan and summary. The current paired UI manifest remains pinned
  to the last verified composition. Full prior-release recovery,
  projection-independent new acceptance and installation remain open.

### Addressed replay and standalone gap retirement assembly

- [Tempo #74](https://github.com/tempo-v2/tempo/pull/74) `b71d9150` includes
  addressed Study receipt replay and retires the standalone gap-analysis job.
  [UI #65](https://github.com/tempo-v2/tempo-ui/pull/65) `d1d6541` removes its
  real Games consumers. Both former HTTP routes return typed retirement.
  Six runtime diagnostics, the phone route/owner check, all 154 UI tests and
  a real Chrome flow passed. Chrome verified manual reply, navigation and
  exact Save recovery after a lost accepted response with no gap-job call.
  Coverage continuation and tactical workers remain separate.
- [Tempo #75](https://github.com/tempo-v2/tempo/pull/75) `447c91a`, UI #65 and
  Store #47 are current in the single manifest. Tempo #75 removes the
  one-off game-capture origins and Study lead-in backfills and black
  repertoire split. The former commands return retirement before touching a
  database. This exact successor passed 56 Tempo contracts, six diagnostics,
  two previous-binary Teach HTTP recovery cases, one private-phone HTTP case,
  and the same actual Chrome Save journey with unchanged UI artifacts.
  Repertoire Reset remains open.
- Separately staged schema-25 authority and retained tactics Settings CAS
  are published in [Store #48](https://github.com/tempo-v2/tempo-store/pull/48)
  `971ec4d` and [Tempo #73](https://github.com/tempo-v2/tempo/pull/73)
  `8f7bafa`. Tests are scoped to the equivalent pre-rebase patches
  Store `f73d4da` and Tempo `89d4e58`: 77 Store tests, three doctests and
  the actual Settings handler passed. The broader Tempo library run passed
  108 tests, ignored five and hit three process-permission failures in
  engine cleanup. The rebased heads await exact combined checks. Durable day
  state is present, but capture remains incomplete until the effective
  profile and current acceptance and issuance producers adopt it. No
  cleanup artifact has been installed.

### Manual detector retirement and atomic first Teach

- [Tempo #76](https://github.com/tempo-v2/tempo/pull/76) `b97df13` and
  [UI #66](https://github.com/tempo-v2/tempo-ui/pull/66) `3ab86a4` are the
  schema-24 review successor in the single manifest. The manual Games detector
  and panel are gone. Three former routes return typed retirement without
  dispatching detector, application or SQLite work. Both builds, 151 UI tests,
  four shared detector tests, seven runtime diagnostics, private-phone HTTP
  and Chrome Games replay and authoring passed. A normal manual tactic
  Preview and exact Save retry also passed. Two older broad suites still
  expect the retired position-evidence route or an input above the existing
  2 MiB cap. Neither suite qualifies its old expectation. Automatic tactical
  jobs, Study presence, coverage continuation and engines remain open.
- [Store #49](https://github.com/tempo-v2/tempo-store/pull/49) `7bb210c`
  adopts first-Teach authority in the normal acceptance transaction. It
  records an applied introduction on the acceptance day, atomically with
  the attempt, Learning and receipt. It writes a dirty projection state
  even without a plan or summary. [Tempo #77](https://github.com/tempo-v2/tempo/pull/77)
  `86cca91` exercises that exact backend pair using commands originally
  issued by the actual previous binary. An accepted command replays
  unchanged. A database trigger failure on spend rolls back receipt,
  Learning and attempt, and the original previously unsent command
  then accepts once. Both HTTP cases, 77 Store tests and three doctests
  passed. The schema-25 pair remains separate from the current UI pins;
  Skip, assessment/correction and further acceptance effects remain open.
- The current schema-24 pins supersede the detector-only heads above.
  [Tempo #76](https://github.com/tempo-v2/tempo/pull/76) `bd2fca6` and
  [UI #66](https://github.com/tempo-v2/tempo-ui/pull/66) `ec44e83` retire fresh
  Practice and Learn More admission while keeping exact accepted
  allowance replay. The retained recovery owner kept the saved command
  and resolved the original effect. An unaccepted previous request was
  rejected without a new durable effect. The exact composition passed
  56 Tempo contracts, 151 UI tests and the UI build, three loopback HTTP
  checks and six Chromium journeys using the prior installed app and
  backend on disposable data. Legacy issued Practice and its old
  immediate-recall source still require retirement. No managed install.
- The separate schema-25 Settings candidate is published as
  [Tempo #78](https://github.com/tempo-v2/tempo/pull/78) `3d58b63` and
  [UI #67](https://github.com/tempo-v2/tempo-ui/pull/67) `80e481e`, tested
  against Store `7bb210c` and Queue `0363fcb`. The real Settings handler
  passed both focused tests. The locked build, real Chrome Settings journey
  and both previous-binary Teach HTTP cases passed. Desktop Settings is
  the shared owner of opening and tactic caps. The browser observed a cap
  change in live Next without restart, preserved unrelated profile data,
  and showed the retired CLI directing the user to Settings. The older
  Phone Study and Saved Reviews Playwright fixtures still carry retired
  Practice expectations. Only the exact Settings and prior-binary checks
  above qualify this candidate so far; the paired review manifest remains
  at the broader schema-24 composition until the next admission.

### Tactical retirement and durable issued Skip

- [Tempo #79](https://github.com/tempo-v2/tempo/pull/79) `8d6e0a0` and
  [UI #68](https://github.com/tempo-v2/tempo-ui/pull/68) `8b2b331` remove the
  automatic tactical worker, tactical controls and Study presence heartbeat.
  [Store #50](https://github.com/tempo-v2/tempo-store/pull/50) `c78a94f`
  removes tactical enrollment from manual Games import. The schema-25
  candidate passed eight diagnostics, private-phone HTTP, Games replay and
  Chrome, both prior-binary Teach cases and six previous-release Chromium
  recovery cases. A disposable copy of the full schema-22 archive kept its
  authoritative tactical and Study rows through migration, startup, active
  Resume, retired controls and manual import. The import still advanced an
  obsolete report counter through SQL triggers. The candidate remains outside
  the paired review manifest until schema 26 removes those triggers and the
  explicit counter bump, with a fresh archive comparison. Authored-source
  pairing previously reserved schema 26 and now owns schema 27.
- [Store #51](https://github.com/tempo-v2/tempo-store/pull/51) `0c06729` and
  [Tempo #80](https://github.com/tempo-v2/tempo/pull/80) `7bdf660` persist
  an optional exact issued-work token and commit matching Skip deferrals with
  the original receipt, without a plan or summary. 78 Store tests, three
  doctests, 56 Tempo contracts and three real HTTP cases passed. The Skip
  test seeds the future issuer's stored token, interrupts the deferral write
  and proves rollback before a successful exact retry and replay. The other
  two cases use the actual previous binary's Teach commands. Production
  prepared issuance, replacement of legacy tokenless Skip and durable
  Resume Skipped remain open. No managed install.
- Schema 26 closes the tactical report write residue. [Store #52](https://github.com/tempo-v2/tempo-store/pull/52)
  `62ffb46` removes all 18 obsolete triggers and the last explicit counter
  bump; their historical tables and rows remain. [Tempo #81](https://github.com/tempo-v2/tempo/pull/81)
  `f28d955`, Store #52, UI #68 and unchanged Queue #18 are now in the single
  review manifest. The exact binary passed 79 Store tests, eight diagnostics
  including manual Capture, real Games replay and three acceptance/recovery
  HTTP cases. The disposable schema-22 archive reached schema 26, passed SQLite
  quick and foreign-key checks and preserved all 11 tactical tables through
  startup, active Resume, retired controls and a valid new manual import.
  The import retried its identical body once after a typed busy response and
  accepted once. Study authority rows stayed unchanged through startup and
  Resume. Gap-line, coverage and provider retirement remain separate.

### Portable retirement and exact human correction

- [Tempo #82](https://github.com/tempo-v2/tempo/pull/82) `841fc17` removes
  the public portable JSON export/restore API and codec. Recovery uses full
  SQLite archives. The exact predecessor build passed 134 Tempo tests,
  three HTTP checks and six prior-installation browser recovery journeys.
  The executable rejected four legacy portable command spellings without
  creating files. Unused private Store/Learning helpers and historical
  compatibility remain separately scoped.
- The current schema-26 manifest moves to [Tempo #83](https://github.com/tempo-v2/tempo/pull/83)
  `43bb449`, [Store #53](https://github.com/tempo-v2/tempo-store/pull/53)
  `274a486`, and [Learning #11](https://github.com/tempo-v2/tempo-learning/pull/11)
  `b198c96`; UI #68 is unchanged. The exact candidate passed 27 Learning,
  79 Store and 52 Tempo contract tests, four doctests, five real HTTP cases
  and six actual prior-installation Chromium journeys. The two correction
  cases seed an exact prepared Test token and exercise a real legal wrong
  move or Give Up. After restart the original attempt completes the
  persisted correction with one assessment and no change to the already
  accepted schedule. The current UI #68 passed 133 units and built both
  artifacts on the previous matching UI revision. Its exact assets were
  reused in the six current browser journeys.
- Prepared issuance has yet to create those tokens in normal runtime.
  Durable Resume Skipped, summary publication/read adoption and the old
  fresh-selector deletion remain open. These changes are uninstalled.

### Stockfish gap-line retirement and coherent capture

- [Tempo #84](https://github.com/tempo-v2/tempo/pull/84) `7ab7368` and
  [UI #69](https://github.com/tempo-v2/tempo-ui/pull/69) `1e96728` are
  the current schema-26 paired review pins. The gap-line start/status
  routes and desktop/phone callers are removed. There is no remaining
  Stockfish production route, implementation or selector. Nine runtime
  diagnostics, private-phone HTTP, 133 UI tests and both built artifacts
  passed. The same current UI sources were used for a Chrome manual-reply
  journey. Disposable previous-installation Chrome and private iPhone WebKit
  verified exact original signed whole-line Save after upgrade. The phone
  exercise includes accepted-lost and never-delivered cases; the desktop
  exercise includes the accepted-lost case. No preview request was needed
  for the saved command. General coverage, its providers, single reply and
  Phone Build remain within their own retirement scopes.
- [Store #54](https://github.com/tempo-v2/tempo-store/pull/54) `50c612b`
  captures only the saved calendar, opening and tactic caps, and effective
  themes, plus exact day deferrals above the accepted cutoff, in the same
  deferred read as the plan basis. The capture distinguishes missing and
  malformed policy from a valid empty work set. All 82 Store tests and
  three doctests passed. Calendar fencing and active issued identity remain
  necessary for a complete capture. This Store-only capability is separately
  tested until the paired consumer successor admits it. No installation.
- [Tempo #85](https://github.com/tempo-v2/tempo/pull/85) `1642eb7` and
  [Store #55](https://github.com/tempo-v2/tempo-store/pull/55) `7f6e39e`
  advance the current paired manifest with unchanged UI #69. Normal
  HTTP Next and the internal issuer check active retained attempts first
  through the addressed Resume path. Real HTTP returns the same issued
  work with unreadable Learning and policy. Missing and incompatible
  identities produce explicit errors without writes. The scoped legacy
  Practice closure adds no grade and still replays an accepted original
  answer. The exact pair passed 55 Tempo contracts, four HTTP cases and
  the real SQLite Store read probe. Fresh Next still uses the transitional
  selector pending the ready-plan consumer. No installation.
- [Store #56](https://github.com/tempo-v2/tempo-store/pull/56) `30b65a0`
  releases durable Resume Skipped on the separate capability branch.
  It addresses dataset, Study day and submission identity. Acceptance
  records that day's cutoff and versioned receipt in one transaction.
  Exact replay after restart and rollover leaves a later deferral intact.
  The real SQLite test injects a late receipt failure and checks rollback,
  then exercises stale day, wrong dataset, changed payload and an
  unsupported stored receipt version. All 83 Store tests and three
  doctests passed. The actual UI has yet to adopt the addressed command
  and separate acceptance from Next. The paired manifest remains on
  Store #55 until that capability is admitted. No installation.
- [Store #57](https://github.com/tempo-v2/tempo-store/pull/57) `bb3eb2a`
  adds the active attempt and its exact issued-work token to coherent
  capture. A prepared human miss binds its correction from that attempt's
  immutable assessment. A newer Learning revision, rollover and restart
  leave the captured binding unchanged. Legacy tokenless active work
  remains explicit. All 85 Store tests and three doctests passed. The
  production capture still reports incomplete and the current paired
  manifest remains on Store #55. The calendar fence, retained eligibility
  and producer invalidations are still needed before issuing prepared work.
- [Tempo #86](https://github.com/tempo-v2/tempo/pull/86) `715a1d8` and
  [UI #70](https://github.com/tempo-v2/tempo-ui/pull/70) `fc2d657` are
  current paired pins. They remove coverage scan jobs, refresh polling
  for those jobs and the last Lichess gap Explorer caller. Former routes
  return typed retirement without worker, application or Store work.
  Saved gaps and starting-line saves remain. Both starting-line URLs
  returned the same saved revision on an exact retry. Builds, 132 UI
  tests, ten diagnostics and private-phone HTTP passed. Desktop Chrome
  and private-phone WebKit recovered original signed saves from the
  previous installation. Saved coverage readers, Maia and Phone Build
  remain within later retirement scopes.
- [Store #58](https://github.com/tempo-v2/tempo-store/pull/58) `843d022`
  fences civil-day observation to the current dataset and its persisted
  timezone. Observation attempted with a superseded timezone leaves the
  basis unchanged. [Learning #12](https://github.com/tempo-v2/tempo-learning/pull/12)
  `9658880` supplies ordinary saved FSRS eligibility independently of
  obsolete Games-only obligations. The actual Store capture uses this
  projection and preserves priority for exact current human correction.
  The exact capability pair passed 28 Learning tests, 87 Store tests and
  four doctests. Calendar observation has yet to be wired into the live
  prepared-plan host, and capture still reports incomplete until the
  actual invalidation producers are ready.
- [Queue #19](https://github.com/tempo-v2/tempo-queue/pull/19) `cf18f19` and
  [Tempo #87](https://github.com/tempo-v2/tempo/pull/87) `505b1ec` release
  the stable input adapter and explicit introduction/relearning distinction.
  Queue suppresses only exact active work, including when its due priority
  cannot be established. The adapter respects authored prerequisites and
  separate caps, and its fixture consumes the actual retained Learning
  producer rather than a copied eligibility predicate. All 16 Queue tests,
  four Tempo adapter tests and two Settings calendar tests passed on the
  exact Store #58 and Learning #12 pair. The adapter is built for tests
  only while production capture remains incomplete.
- [Store #59](https://github.com/tempo-v2/tempo-store/pull/59) `c6e0f6f`
  fences prepared membership and summary on retained content and
  participation changes in the existing acceptance transactions. Display
  edits preserve both epochs. Relevant version, availability, authored
  occurrence order, effective qualification and suspension changes fence
  stale projections, and late receipt failure rolls everything back.
  The exact Store passed 89 tests and three doctests. The matching
  [Tempo #87](https://github.com/tempo-v2/tempo/pull/87) suspension and
  manual Capture contracts passed. Calendar/worker adoption, exact fresh
  issuance and removal of remaining legacy writers still gate ready plans.
- [Store #60](https://github.com/tempo-v2/tempo-store/pull/60) `82be4fa`
  fences accepted Study changes once per transaction. Active-slot changes,
  first-Teach spend and changes in captured Learning eligibility can
  invalidate both projections, including acceptance of an older tokenless
  attempt. Intermediate moves and exact replay leave compatible work alone.
  The exact backend passed 90 Store tests, three doctests and five real HTTP
  cases, including previous-binary Teach, exact Skip and both correction
  journeys. This Store successor is staged for the next paired manifest.
  Prepared issuance, fair publication and independent Progress remain open.

### Remote refresh retirement and bounded prepared issuance

- [Tempo #88](https://github.com/tempo-v2/tempo/pull/88) `12bda8d` and
  [UI #71](https://github.com/tempo-v2/tempo-ui/pull/71) `90753b3` replace
  the current schema-26 review pins with Store #60, Learning #12 and Queue
  #19. They remove the remote refresh worker and job polling. An exact
  accepted refresh returns its original receipt result. An exact
  never-accepted request returns retirement without a provider or status
  poll. Both builds, 133 UI tests, 11 diagnostics, private-phone HTTP,
  real Games replay and current Chrome Game Workbench passed. Four
  previous-installation Chrome cases exercised accepted-lost and
  never-delivered commands from inline storage and IndexedDB. The same
  candidate performed retained manual PGN import and replay. Historical
  backfill and its shared provider still have their own retirement gate.
- [Store #61](https://github.com/tempo-v2/tempo-store/pull/61) `5dbea2f`
  stages the bounded ready-read and exact issuance transaction separately.
  At most 32 entries are checked and only the selected definition is
  hydrated. Issue saves the original attempt identity, active pointer and
  Ready-to-Issued transition together. Rank-only drift leaves admitted
  membership valid. The exact Store passed 93 tests, three doctests and
  four matching Tempo adapter tests. Production has yet to adopt this
  capability. No managed install.
- Separately qualified [Tempo #89](https://github.com/tempo-v2/tempo/pull/89)
  `95e165f` and [Store #62](https://github.com/tempo-v2/tempo-store/pull/62)
  `0dc9b4c` release schema 27 authored-source pairing. The real editor
  read no longer needs model authority, and startup no longer reconstructs
  missing legacy pairings. The exact pair passed 94 Store tests, three
  doctests, 58 Tempo tests and five HTTP acceptance/recovery cases. On the
  already rehearsed schema-26 copy of the previous archive, all six original
  authored PGNs served unchanged after migration even with model inputs
  unavailable. SQLite quick and foreign-key checks passed. A legacy
  unverified source remains unavailable until replaced by verified
  authoring. Full model worker and caller retirement remains open.
- [Queue #20](https://github.com/tempo-v2/tempo-queue/pull/20) `d4e591e` adds
  independent summary classification from the same pre-order eligibility.
  It passed 18 Queue and four matching existing Tempo adapter tests. The
  summary does not read, construct or order plan entries. Bounded Store
  publication and real Progress screen adoption remain open. No installation.

### Historical backfill retirement and schema-27 review

- [Tempo #90](https://github.com/tempo-v2/tempo/pull/90) `2fd9643` and
  [UI #72](https://github.com/tempo-v2/tempo-ui/pull/72) `bba81c5` are the
  current paired pins with Store #62, Learning #12 and Queue #19. They remove
  historical backfill workers, controls and provider execution. The retained
  readback resolves exact accepted prior Start and Retry and reports unfinished
  work as stopped. Never-accepted commands return retirement. Both builds,
  the focused Rust checks, three HTTP cases, private-phone admission and all
  120 UI tests passed. Actual previous-installation Chrome recovered the
  accepted-lost and never-delivered Start and Retry envelopes through both
  recovery stores, and the same candidate supported current manual PGN
  import and replay.
- A fresh disposable copy of the rehearsed schema-26 archive migrated to 27.
  It replayed all four original accepted Starts and two accepted Retries,
  preserving 104 completed and 15 stopped windows. Stored jobs, recognized
  accounts, Games records and receipts, comparisons, Learning and Study
  receipts remained byte-identical. SQLite quick and foreign-key checks
  passed. The direct full schema-22 archive upgrade hit disk I/O while
  local space was constrained. Direct schema-22 to 27 upgrade passed on
  the actual previous-installed browser fixtures. No managed install.
- [Tempo #91](https://github.com/tempo-v2/tempo/pull/91) `4f3b347` is
  current with the same schema-27 Store and UI. Existing authorization
  applies before serving static assets or the bounded read-only context
  lane. A real disposable SQLite write lock held a foreground Settings
  save. Context and static assets still returned before release, and the
  original Save subsequently committed. Five Node and 12 Python
  diagnostics passed, including private-phone access and correlated
  asset diagnostics. Fair prepared apply remains separate. No installation.
- A direct full schema-22 archive copy subsequently upgraded to schema 27
  after unused build output was reclaimed. The exact #91 runtime served
  all six original authored PGNs with model authority unavailable.
  SQLite quick and foreign-key checks passed. This direct run qualifies
  the full authored-read upgrade. The earlier detailed historical
  backfill invariance result remains scoped to its staged archive copy.
- [Store #63](https://github.com/tempo-v2/tempo-store/pull/63) `a227644`
  publishes schema-28 independent summary storage. It bounds the payload
  to one row per dataset and publishes against the captured dataset,
  civil day and summary epoch. The SQLite probe denied rank, plan and
  Learning reads on summary lookup. Exact retry, stale fencing and
  rollback after an injected late failure passed among 95 Store tests
  and three doctests. The production publisher and Progress/Study Status
  users remain open. This capability is outside the current schema-27
  paired pins. No installation.

### Repertoire Reset retirement and schema-28 review

- [Store #64](https://github.com/tempo-v2/tempo-store/pull/64) `a8abe6c`,
  [Tempo #92](https://github.com/tempo-v2/tempo/pull/92) `c419ccb` and
  [UI #73](https://github.com/tempo-v2/tempo-ui/pull/73) `a11cad2` are
  the paired schema-28 review pins with Queue #20. The Reset writer and
  current control are gone. Exact prior accepted reset returns its old
  result by dataset, repertoire and command identity. Unaccepted Reset
  returns terminal retirement. Historical boundaries remain readable
  by their retained consumers.
- The exact composition passed 95 Store tests, three doctests, focused
  prior-choice and issued-definition Tempo contracts, and the previous
  actually installed schema-22 binary plus candidate HTTP and desktop
  Chrome recovery. Current UI had no Reset control, the original pending
  replay left newer Learning and receipts unchanged, and wrong dataset,
  changed identity and unaccepted requests remained explicit. Schema-28
  summary persistence is present. Its actual publisher and screen
  adoption remain open. No managed installation.
- [Tempo #93](https://github.com/tempo-v2/tempo/pull/93) `5b54167` and
  [Store #65](https://github.com/tempo-v2/tempo-store/pull/65) `ba53882`
  are current with unchanged UI #73 and Queue #20. The actual Settings
  writer uses the same Store connection as Study. The former Settings
  connection now reads only remaining model metadata. Existing Settings
  validation, compare-and-set and exact no-op behavior remain. The exact
  candidate passed two Settings tests, three real loopback admission
  checks and Chrome Settings. In the SQLite-lock check, context/assets
  responded independently and the original Settings write then committed.
  Reset recovery evidence is scoped to the tested predecessor. The
  prepared-plan publisher is still separate. No managed installation.

## Historical schema-13 Settings candidate

| Behavior | Basis, owner, inputs and lifetime |
| --- | --- |
| Apply board appearance and audio within one browser | The approved Settings plan preserves browser scope. Tempo UI owns theme, pieces, volume and sound enabled. Settings and quick mute use the same browser record. Study, Game Review and preview boards consume it. The prior browser keys are upgrade inputs. |
| Save daily opening and tactic limits, extra tactics, and themes | The desktop Settings section is the edit surface. Tempo validates the requested settings, dataset and profile revision. Store commits the existing profile atomically. Tempo applies the confirmed values to future selection and allowance grants. Names, board preferences and navigation do not affect a grant or admission. Settings carry forward through restart and database backup. |
| Preserve the current exercise and accepted grants | Opening Settings is a read. Returning to an empty or paused Study uses a read-only status refresh. Due reviews, issued attempts, introductions already consumed, accepted allowances and command receipts keep their existing identities. An accepted allowance still replays its original result after a settings change. An unaccepted command uses the applicable settings when accepted. |
| Keep the Phone Study route boundary | Tempo's desktop endpoint owns shared settings. Phone changes browser-local board preferences and reads the latest limits through its existing Study routes. Progress revalidation includes a settings revision independently of attempt and learning revisions. |

The canonical agent guidance requires every user preference to be editable
in Settings with one authoritative value and save path. The workspace copy
carries the same rule. Desktop Settings replaces the older tactics editor and
the configure writer. Browser-local choices also apply to the new tactics
builder, including its setup board. Host provisioning remains in its managed
scope.

| Component | Qualified head | Pull request |
| --- | --- | --- |
| Tempo | `54d8fb450d07d88c6236b291adb76f10af160d54` | [#39](https://github.com/tempo-v2/tempo/pull/39) |
| UI | `8da234145dfd87be0f589ed7f9f7a533cff1bf37` | [#34](https://github.com/tempo-v2/tempo-ui/pull/34) |

Build the pair with Store `27ffcc992d4b12424c1208676ae594d4245277e9` and the
other pinned components from the installed repertoire-suspension release.
Use its Cargo lock and UI lock with packaged Core 0.2.2. The candidate
includes the merged tactics builder. SQLite schema 13 and Study wire 5
carry forward. An older progress stamp triggers one fresh read.

| Artifact | SHA-256 |
| --- | --- |
| Optimized Tempo binary | `90703cf6bf9f1b7169d404c58257bd5ee4f223c223e5008f71a91807be735f7a` |
| Desktop JavaScript | `7d9aa7bf586256fcd90ddcf0012041ee2fd635e8a976d94609713fee9bb2552c` |
| Phone JavaScript | `f2643fcd193e9ac8781304f310f1c70e52673639d495a9f3ad72f7b00c68a8ae` |

The combined architecture gate, 174 Rust tests and doctests, 111 UI tests,
and four focused HTTP checks passed. Packaged Chrome and phone-sized WebKit
covered browser preference carryover, separate desktop and phone preferences,
lost Settings acknowledgements, concurrent tabs, and changes in shared limits
and theme admission through Study. Chrome verified the existing repertoire
suspension and tactics builder workflows using the same candidate.

Independent review reproduced two edge cases. A Settings status read now
offers ordinary Next when new work is eligible. Large allowances are projected
within the existing browser integer range, while previously accepted grants
retain their exact receipts. Focused consumer checks verified both fixes.

The exact Review later, repertoire-suspension, and board-capture
installations each passed six recovery cases covering accepted-lost and
unaccepted Answer, Learn more tactics, and repertoire Save. Retry Next sent
only Next. Study metadata
invariance passed for clean Test, a miss, and Teach. A settings save on a
disposable copy of the installed schema-13 profile preserved all 39 tables
apart from the intended profile preference, with integrity and foreign keys
verified. The prior omitted extra-tactics value retained its effective
default on the first save.

This evidence covers the predecessor multi-repository candidate. Integration of its component PRs is tracked separately.

## Installed unique-solution qualification for generated tactics

[Tempo #127](https://github.com/tempo-v2/tempo/pull/127) installed
`493918320d1ceec19cedb9b11e0c1ab6a66d2459` on schema 14 with Core 0.2.2
and the Maia-3 UI from its immediately preceding release. A separately
registered `com.tempo-v2.lean.tactics` worker uses Stockfish 19. The
serving package dependency graph excludes Stockfish. Both registered
processes and the served asset hashes were verified.

The shared Chess qualifier requires a unique best proposed move from all
legal roots at depth 10. A gap of 30 centipawns or less is equivalent,
including quiet alternatives. Moves preserving the same forced mate also
count as equivalent. Games remains the source of capture findings. The
catalog applies one verified verdict at a time before publishing new
cards, narrows existing answer sets under their original identity, and
removes failed cards from the active catalog and Study queue while
retaining their receipts and learning records.

Fresh Astra cleared source `7da8b5e62b611afbd2f7feb6bf87f2fb62c8160a`.
The 45 Tempo Rust tests, seven Stockfish contract tests including the native
test, strict Clippy and the packaged UI build passed. A disposable HTTP
journey imported a game with the worker absent, held publication while the
engine was unavailable, published with Stockfish 19, and graded and replayed
one Study Answer after restart. A disposable catalog preview evaluated
442 findings and removed 120 cards, narrowed 15 and kept 307. Matching
preview evidence was reapplied through the production writer.

The stopped backup was
`20261125T164924.809386Z-before-unique-tactics/tempo.sqlite3`. The migration
preserved the dataset, current attempt, and the counts of cards, learning,
attempts, games, tactics, and Lichess versions. SQLite integrity and foreign
keys passed. The reported `Qf6` position is five centipawns ahead of
`bxc6` at depth 10. All 34 matching occurrences were retired, and their
three saved reviews were retained.

The worker was observed advancing through the remaining historical catalog.
Incomplete positions stay unresolved for automatic retry under the same
bound. Worker status reports the live kept, narrowed, removed and unresolved
counts. This release scans retained findings without an archive rescan.
