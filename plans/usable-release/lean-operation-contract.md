# Lean operation contract

Tempo #104 used `4f97e742b0f259ba3c26109d69aa365d570439f8` on Lean schema 2 as its baseline. Keep live data, first-answer Good/Again, FSRS, the repeat deck, opening preferences, provider imports, and scanner-driven tactic publication. This contract governs Lean. The older structural-cleanup contract remains evidence for the predecessor.

The [daily Study queue contract](lean-daily-queue.md) supersedes the prior selection and prepared-membership rules for the daily queue increment.

| Operation | Owner and permitted facts | Effect and lifetime |
| --- | --- | --- |
| Study resume and Next | Study identifies the active attempt. Queue uses the committed deck, prepared availability, due times, previous card kind and saved new-opening policy. | Resume first. Check at most 32 prepared entries and hydrate at most one definition. Missing or stale membership means preparing. Done requires a complete exhausted order. No catalog fallback. |
| Answer | Study validates dataset, attempt and immutable submission. Chess grades the issued moves. Learning computes FSRS. Queue draws and places Again. | Store atomically accepts one grade, schedule, receipt and repeat obligation. If fresh membership is unavailable, the obligation retains its original draw and blocks only subsequent issuance until placed once. Saved answers replay before current-attempt checks. Prior accepted response encodings remain readable. |
| Prepared membership | Store captures the revision and owns publication. Queue owns ordering. Use card identity, kind, active status, due or unseen state, saved rank and reservations. | Apply addressed deltas in the original mutation. Initial seeding and its cursor commit together in turns of at most 128 affected rows. While seeding, every authoritative mutation updates its addressed entry in the same transaction, including inserts behind the cursor. Only an exhausted cursor may mark the queue ready. Any future builder that computes from an independent snapshot must fence publication against that snapshot’s original revision. Never use stale membership to issue new work. Use exact Lean due times, with no new calendar or review policy. |
| Games | Provider adapters supply normalized games. Runner owns checkpoints and retries. Scanner returns versioned observations, and Tactics publishes puzzles through its existing intake. | Archive acceptance, scanning and publication have separate durable progress and retry. Status reads never advance jobs. No provider, scan or optional enrichment gates Study acceptance or issuance. |
| Content and settings | Chess validates submitted content. Openings owns the repertoire destination, position and one-active-reply rule. Settings saves one authoritative value per preference. | Online content saves that would change more than 128 rows reject atomically with an offline import path. Settings and catalog mutations update only their addressed facts and affected projection. Large Games uploads retain the 64 MiB limit and run in bounded, resumable batches. |

The runtime has one write connection, at most eight waiting proposals, two seconds to enter execution, and at most four foreground turns ahead of a waiting background apply. A claimed proposal can finish after a disconnect. Parse, network, ranking, and scanning run outside write transactions. Offline writers acquire the same exclusive database lock as the service. Ordinary JSON uses the 16 KiB budget. Deliberate PGN inputs have a separate bounded path. Online applies count all affected rows, including projection changes.

Display titles, provenance, optional game metadata and equivalent representation do not change acceptance or queue policy. A changed authoritative due time, card availability, saved rank or committed repeat position may change selection. Qualification uses the real HTTP and browser consumers, read-only SQL access checks and row budgets, writer contention, restarted imports, and original pending Answer envelopes from the preceding installed build on disposable data.

## Standalone position analysis

The Stockfish library owns position analysis and the CLI is its first
consumer. The Lean runtime does not depend on the library. Scope is standard
chess FEN and per-request analysis evidence. Callers own any blunder
threshold and product action. Repeating a request starts a fresh search and
does not create a saved result.

| Operation and owner | Inputs and effect | Independence, limits and lifetime |
| --- | --- | --- |
| Evaluate a position, Stockfish analysis | Accept one complete standard FEN and typed depth and coverage. All legal moves are the default. The caller may ask for the top 1–10 or a distinct legal candidate set. A successful reply carries the engine version, engine-ranked lines at one completed depth, and White-relative centipawns or mate winner and distance. Zero legal roots yield a terminal result without a process. | One physical slot per shared instance, immediate admission, five-second startup and search deadline, one Stockfish thread and 16 MiB hash. CLI input is capped at 16 KiB and engine output at 4 MiB. Cancellation and failures retain the slot until the child is reaped, including when the caller runtime shuts down. Results are transient. Callers own thresholds and product effects. |

## Schema-3 handoff for Tempo #104

[Tempo #104](https://github.com/tempo-v2/tempo/pull/104) shipped schema 3 with
Core 0.2.2 and migrated from schema 2.

## Schema-4 follow-up operation rules

[Tempo #107](https://github.com/tempo-v2/tempo/pull/107) advances the managed
schema-3 predecessor `48328ad4b49bbd91fadf2bcd2aa83df9cbea1ede` to schema 4.
The [assembly manifest](current-assembly.json) records the qualified and
installed artifacts. The schema-4 merge is the managed predecessor to schema 5.

| Operation | Owner and permitted facts | Independence, limits and lifetime |
| --- | --- | --- |
| Committed repeat lookup | Queue reads the saved repeat slots and active card identities. | Slot and active state determine the result. Catalog growth outside the deck adds no work. Next still hydrates one issued card. |
| Study context and Games status | Each reader serves only its own read operation. Context is addressed by attempt, and status reports durable jobs. | Each family has one physical slot, immediate admission, zero SQLite lock wait, a 250 ms deadline and a two-million-step budget. Failure or browser cancellation has no durable effect. The browser drops obsolete reads by identity or visibility. |
| Games job turns | The runner owns rotation at one provider window, PGN record, scanned game, or publication batch. Store owns the indexed ready order and commits progress and requeue together. | Only ready order selects the next job. Restart retains jobs, checkpoints, and ordering. Archive acceptance, scanning and tactic publication remain separate. Provider inventory is frozen for the job after discovery, and the account checkpoint advances on job completion. |

A full archive rescan captures the archive high-water mark on its first turn.
Newly archived games receive their own scans. An interrupted claim retains its
previous place until a completed turn returns it to the tail. A provider
inventory is discovered in its own turn. A schema-3 Chess.com job that had
already advanced its ordinal revisits all applicable windows because the old
inventory is unavailable. Canonical game acceptance deduplicates replay, and
the final rejected total keeps the greater of the previously recorded total
and the replay count. Staged and predecessor inline PGN retain their byte
boundary across restart. The worker stages surviving inline data before the
next record and commits the representation change with requeue.

## Schema-5 operation bounds

[Tempo #108](https://github.com/tempo-v2/tempo/pull/108) preserves the schema-4
Learning and Study operation rules. The schema-5 merge is serving on the managed Mac.

| Operation | Owner and permitted facts | Independence, limits and lifetime |
| --- | --- | --- |
| Games turns | Games runs one inventory, provider download, PGN record, scanned game, or publication turn under the same 60-second deadline. The writer uses two-second admission for recovery and claims. | A provider download retains the 32 MiB cap. A nonempty window is staged durably before record processing. Game acceptance or rejection is atomic with its byte offset and ready order. An unsupported game counts once at its physical boundary. The next claim records a failed turn atomically. Unclaimed work expires while a claimed write resolves its result. Restart and Retry reuse the retained file and checkpoint. |
| Repertoire picker | Openings owns the existing repertoire and practice-color identity and the first authored line as its display example. | The editor reads 50 choices per indexed page with a separate physical read slot, 250 ms deadline and two-million-step SQL limit. A selected choice survives refresh, and branching uses the saved opening's exact repertoire and practice color. Migration seeds the durable projection and an opening save applies its projection row in the same transaction. The projection write counts toward the online row limit. |

Local filesystem calls retain their physical worker until they return.
The turn deadline prevents new work after expiry. A successful claimed
write is interpreted by its durable result.

An unfinished predecessor PGN upload with a saved rejection may point
inside the rejected record. Schema 5 keeps its existing staged bytes,
cursor and counters, and marks it for one-record turns from the beginning.
Archive identity deduplicates previously accepted records. Once replay
finishes, the job stores the physical rejection count.

## Schema-6 Games admission and Study count bounds

[Tempo #109](https://github.com/tempo-v2/tempo/pull/109) ships these rules on
schema 6. The [assembly manifest](current-assembly.json) records the serving
artifacts and the retained schema-5 predecessor.

| Operation | Owner and permitted inputs | Effect, independence and lifetime |
| --- | --- | --- |
| Games commands | Games accepts provider and operation for an import or archive scan on `POST /api/games/jobs`. PGN intake accepts player name and PGN on `POST /api/games/uploads`. | The ordinary endpoint enforces 16 KiB before decoding. Only PGN intake uses the existing upload slots, deadline and 64 MiB decoded PGN limit. Rejected requests leave no job or staged upload. Existing durable jobs retain their original identity, file and checkpoint. |
| Games admission | Store checks the four-job capacity using active user-started jobs. Provider imports and archive scans reuse a matching active provider, operation and player at available capacity. | Capacity checks stop at four matches. The keyed duplicate lookup and capacity check use a partial index over active user-started jobs. Queued children and finished jobs do not add lookup work. Retry uses the same capacity rule and keeps the original job. |
| Study counts | Queue retains its current due, unseen, pause and committed-work semantics. Store uses one read snapshot. The UI renders each total as exact through 10,000 and as 10,000+ above it. | Read at most 10,001 candidates per kind and eligibility class, plus bounded committed work. The wire uses a number for an exact total and `{"at_least":10000}` for a capped total. Rank and display changes have no effect. This read is never required to issue or accept a review. |

## Schema-7 Game and Answer representations

This increment starts from the installed schema-6 Lean release. The
following rules apply to its replacements and to the predecessor state
they interpret.

| Operation and owner | Inputs and effect | Independence and lifetime |
| --- | --- | --- |
| Archive, Games | Normalize one finished orthodox mainline from manual PGN, Lichess or Chess.com. Compare normalized players, learner side, full starting position and moves. Compare UTC day, UTC time paired with UTC day, local date and non-placeholder round only when both records know the same fact. Numeric and named rounds are normalized at intake. Select the compatible row with most shared facts, then lowest rowid. Conflicting known occurrence facts create a distinct game. | Links and display text cannot choose the game. Missing facts can be filled without rekeying. A known result fills a historical unknown; contradictory known results reject the incoming record and advance its checkpoint. Keep historical IDs and unlabelled dates. Encode moves in a bounded versioned binary payload and use at most 16 indexed occurrence probes. |
| Detection, Games runner | Give each versioned detector the addressed game. Comparison also receives a coherent set of authored reply/version facts from Openings. Capture uses only the game. Commit a sealed result and its cursor before applying batches. | Apply at most 117 observations and 128 affected rows per write, including queue trigger writes. Retrying a sealed turn uses its exact facts. Failed work does not undo its sibling. Versioned findings coexist; Tactics retains its original game/ply publication identity. Replay and the Stats qualification consumer use the same Game reader. |
| Answer, Study | Translate predecessor wire into a dataset, attempt and explicit play or reveal. Study accepts the first valid action once and replays exact intent. Store records a typed accepted receipt with the original repeat disposition in the Learning transaction. | A display edit and optional Games failure have no effect. Legacy receipts retain their original interpretation. The browser journals each intent durably before sending, clears only matching resolution, and retries Next separately. Incomplete success replies retain the intent, and display context stays optional. Imported predecessor envelopes retain their original request. |
| File staging, Games I/O owner | Reserve bounded capacity before staging; pass only an ID and memory-only lease to the writer. Reclaim after all leases finish and a fresh indexed durable-reference check succeeds. | No cleanup I/O runs under writer admission or on the writer. Keep two foreground staging slots and one worker slot, with four provisional/orphan file reservations and at most 256 MiB. Retryable exhaustion affects staging; uncertain ownership retains the file. |

## Schema-7 bounded browsing

The application admits each interactive read into its own bounded reader.
Games owns archive and replay, Openings and Tactics own their catalogues,
Settings owns saved preferences, and Study owns current-attempt projection.
The route, cursor or record identity determines which addressed facts the
reader loads. Reads make no durable changes. Archive display text cannot
influence identity, grading, selection, or durable jobs. The UI owns
cancellation, invalidation, and the current page or selection.

Each read family has one physical slot, immediate admission, zero SQLite
lock wait, a 250 ms deadline through serialization, two million cumulative
SQLite steps, and a 2 MiB JSON response limit. The existing Study context
and opponent-move reads share their context slot. Busy, expired, and budget
failures return the existing typed unavailable reply. A cancelled caller
does not free a running slot early. Archive pages keep 50 rows and opening
and tactic pages keep 100. Game projections cap player labels at 256
characters and dates at 64 characters, and omit source URLs over 2 KiB.
The original archive and its semantic identities remain intact.

A page refresh supersedes earlier list reads. Only the current selection
may apply a replay response. A failed read preserves the last successful
view and cannot undo a saved command. Existing response shapes and pending
schema-6 Answer envelopes remain compatible.

## Schema-8 archive rescan cursor

Games owns a frozen archive rescan. The parent captures one inclusive
archive ordinal cutoff for both detector jobs. Store seeks by ordinal
within that cutoff. Games visits one new game per turn and advances that
lane's checkpoint with the final durable apply. Games arriving after the
cutoff get their own scans and add no work to this lookup. Ordinal defines
traversal only. Game identity, detector versions and published tactic
identity retain their existing meanings.

Schema 8 versions the durable cursor with the existing offline database
fence. Migration leaves the archive and job rows intact. A resumed
game-ID cursor retains its cutoff and completed ID prefix while the
runner walks pages of at most 64 ordinals. A plain predecessor ID
without a cutoff freezes one before resuming. A page of completed games
only advances that lane and returns it to the ready queue. An existing
sealed game finishes with its saved file, detector version and offset
before its legacy checkpoint is converted. The 60-second turn, writer
admission and apply budgets continue to cover the resumed work.

## Generated tactic qualification

| Operation | Owner and permitted facts | Independence, limits and lifetime |
| --- | --- | --- |
| Qualify one suggested solution | Chess accepts the validated position, proposed legal roots and scores for all legal moves from a single depth-10 search. An alternative at most 30 CP worse, or preserving the same forced mate, makes the position ambiguous. The best move must be a detector candidate. | The outcome is independent of the motif and display data. Incomplete, terminal or inconsistent evidence cannot establish a verdict. The same rule can serve other generated tactics. |
| Apply one game finding | Games supplies the original game occurrence and move. The catalog publishes only a qualifying capture that differs from the played move. The existing writer validates the exact dataset, detector finding and rule identity, then commits evidence and the catalog or queue change together. | Fresh findings wait for evidence. Existing cards keep eligibility until evaluated. Retirement excludes future issuance and repeats, while narrowing preserves identity and old issued answers. Accepted receipts are replayable. An exact re-delivery or archive rescan retains the committed verdict. |
| Supply analysis | A separately launched worker shares one admitted engine slot with a five-second search deadline per position. Tempo exposes a private owner-only Unix socket with 64 KiB messages and background writer admission. | The server never launches Stockfish. Worker loss does not block Games acceptance or Study. A transient failure requeues with backoff, and late results are checked against the addressed work token. |

## Schema-15 worker and coverage reads

The Store projects the seven exact tactic worker counters from durable
qualification changes. Migration seeds the projection while the service
is stopped. The status client uses a separate owner-only socket and one
250 ms request budget. Work delivery has its own socket and keeps the
existing writer admission and exact verdict replay. Detector batches
accept at most 40 findings and at most 128 affected rows with triggers.

The Coverage owner publishes indexed chunks of 30 gaps with the saved
forecast, keeping its identity, order, model and command receipts.
Pagination reads at most two chunks and no Learning. Personally studied
coverage reads the compact dependencies and current Learning in a separate
bounded snapshot. Only accepted reviews on saved paths affect that score.
Predecessor combined reads compose the same projections. Apply retains
its original model and revision fence. No Study write depends on these
coverage projections.

## Schema-16 tactic submissions and coverage model identity

A worker that has engine evidence retains the exact Submit message in
memory in drain and watch. A known verdict confirms the stored outcome.
An explicit stale-work reply releases the obsolete token. Explicit invalid
evidence uses the existing addressed retry. Busy admission, busy or locked
storage, a lost reply and an unrecognized acknowledgement keep the same
submission pending. Replaying a committed token returns its verdict without
another catalog or counter effect. Restart without a committed verdict can
reanalyze an eligible finding.

Coverage persists the saved forecast model identity. The report read and
an unapplied rank change both compare that identity with the current model.
A saved Apply receipt continues to replay. Migration derives identities
from retained forecasts. Human-readable labels and inherited header flags
cannot affect model eligibility.

## Coverage scan lifetime and bounded Apply

A scan belongs to the Gaps request until publication. Leaving Gaps or losing
the request cancels uncommitted computation. A saved opening and a report
already committed retain their own identities. Coverage admits one physical
scan with a 300-second budget from admission through publication and 32 MiB
each for model input and output. On cancellation, expiry, failure, or service
shutdown the owner terminates and reaps its child before releasing admission.
A fresh cached report reuses its current dataset, repertoire revision, model
and normalized scan identity. A stale scan cannot publish.

Apply owns one atomic order change for the exact saved forecast, guarded by
saved model, repertoire revision and active rank bank. Only reached card IDs,
their existing effective slots, forecast probabilities, and the indexed
global maximum effective opening rank determine new placements. Ties retain
the existing slot order and deterministic card-ID order. Both ranked and
unranked reached cards keep the predecessor interpretation. Prior bank
differences are reconciled before staging any new placements, including after
interruption. Store writes at most 128 rows per turn and activates with the
command receipt. Replaying an accepted command uses the retained receipt.
Unrelated openings, display details, and tactics add no scan to rank preparation.

### Gaps command recovery

Gaps owns browser delivery and acknowledgement for the exact pending Save,
replacement or Apply command. Tempo's validated matching reply establishes
acceptance. The journal records the addressed outcome before removing that
pending command. A late reply can settle only its own journal entry. Labels,
draft edits, view navigation and optional scans do not establish acceptance.
An uncertain reply retains the original request for exact replay across
navigation or reload. Other mounted views observe journal changes without
sending commands. Transient delivery progress and errors expire when their
command settles. The mounted view that receives and records a valid Save
reply from its own delivery attempt may start the optional follow-up scan.
An explicit retry is a delivery attempt. A view that only observes an
acknowledgement displays the accepted Save and can retry the scan
independently. The 32 MiB model limits cover the JSON request and forecast
response streams. Service diagnostics use stderr.

## Schema-18 architecture follow-up

The approved follow-up starts from installed Tempo #137, schema 17, and
Core 0.2.2. It reconciles redundant authored lines in one managed cutover.

| Operation and owner | Allowed inputs and observable behavior | Bounds, lifetime and independence |
| --- | --- | --- |
| Gap review and picker, Coverage and Openings | A report and gap address selects optional analysis. A valid reply can stage a legal move. Malformed or unavailable evidence leaves the existing draft and manual authoring available. A repertoire choice is its saved ID and practice color. | Browse admits one 50-row keyset page at a time. Later pages require an explicit action, and an off-page choice or report label uses an addressed point read. Page and point results are disposable and cannot settle Save or Apply. The Stockfish budget is five seconds within a 5.75-second review deadline. |
| PGN intake, Games and authored Tactics | Give each route one receive permit. Exhaustion returns a typed receive-capacity error on that route before writer admission. | Keep two aggregate receive permits, the existing byte limits and ten-second receive deadline. Completing a Games turn reserves the exact released file against the four-file and 256 MiB staging budget before clearing its durable reference. Cleanup checks leases and the indexed job reference before unlinking. Startup accounts for crash orphans in batches of at most 32 entries. Quota pressure uses the existing rotation with unchanged checkpoint. |
| Full-line activity and browser delivery, Study and Tactics | Every nonempty Study Current and Next projection carries the issued activity mode. Invalid or contradictory mode or payload displays recovery and emits no alternative command. Every full-line Move, Reveal and Tactics Start journals its exact immutable intent before delivery. Matching valid replies and typed terminal decisions settle only their own intents. Move replies add the addressed issued position before the submitted step. The browser verifies that the reported transition yields the returned board before accepting it. Full-line live projections carry the complete legal input for the current solver board. Terminal projections carry an empty input list and display the issued solution at the reported step. | Existing request shapes and saved receipts remain readable. The server reconstructs the before-position from the immutable issued route on exact replay. The new journal carries pending intents across tab close, and imports a surviving predecessor tab's exact journal before removing its session entry. A tab already closed before upgrade has no session envelope to import. Acceptance and subsequent reads or Next retry separately. Display titles and optional data do not determine commands. |
| Opening line identity, Chess and catalog | Chess supplies full canonical starting FEN and ordered canonical moves. Existing-line identity uses repertoire, practice color, canonical route and start ply. Equivalent submissions reuse one representative independently of display name. Explicit New creation retries with the same creation name and canonical route reuse the root. Distinct names on New retain deliberate separate repertoire creation. | Keep the root when present, otherwise the earliest saved row. A group with an active member retains one active line even when its representative was archived. Preserve the prior archive flag when transferring that state. Historical alias rows keep their IDs, names and routes and cannot independently authorize writes. Reconciliation does not change the accepted reply set, Learning, deck, or semantic revisions. A distinct authored route or retirement still changes freshness. Stop managed cutover if inventory requires a cross-repertoire or Learning merge. |
| Gaps acceptance and batches, Openings and Store | Replay accepted Save, replacement and Apply receipts by original identity. A partially completed predecessor batch resumes from its saved cursor and original completed line IDs. New completed lines contribute the actual resolved IDs. | Keep the old accepted encoding. Progress and line IDs commit together, and the final receipt commits with completion under the existing 128 affected-row limit. A current authoritative repertoire change still fences an unaccepted replacement or batch. |

## Schema-19 Games repertoire feedback

| Operation and owner | Inputs and durable effect | Bounds, lifetime and independence |
| --- | --- | --- |
| List eligible repertoires, Games and Openings | Address an archived game and use its learner color with Openings' repertoire choices. Read one color-indexed page and optionally the retained choice by ID. Titles label choices. | 50 choices and one lookahead, one addressed retained choice. No job or content mutation. |
| Request a comparison, Games | Address one game and eligible repertoire. The request carries the observed Openings revision and work generation. Reuse a queued or running pair. A stale request or already current result returns the latest identity without enqueuing. Retry resumes the pair's sealed work when present. Temporary file-access failures retain the sealed basis. Positively missing or invalid content can be recomputed on explicit retry. | At most four active pair jobs, a separate cap within the existing Games runner and writer. One work generation and one completed report per pair. Comparison cannot block archive acceptance or depend on capture analysis. |
| Compare and publish, Openings, Chess and Games | Snapshot the authoritative reply revision and the addressed replies for all learner occurrences. The pure comparator uses canonical positions and legal moves, with the existing single-active-authored-reply policy. Absent, unresolved, and unusable replies are unassessed. Publish a whole completed report with the original move and answer facts. | At most 512 learner decisions and 256 KiB sealed per pair. One existing Games turn per prepare or bounded apply. Checkpoint the legacy mismatch projection in batches of at most 40 decisions. Publish under the exact job generation and sealed checkpoint. A failed replacement preserves the completed report. Capture and optional Study context keep their existing boundaries. |
| Traverse and read, Games | Imports and explicit backfill feed the same pair work. Use the existing archive cutoff and indexed game and repertoire positions. Feedback reads compare the completed basis with the live authored-reply and comparator versions. Recent jobs' new-findings counts remain capture counters. | Visit one addressed pair per feeder turn and advance after it completes. A scoped Retry only requeues its own pair. A feedback GET reads one addressed result with the existing 250 ms, two-million-step and 2 MiB read bounds. Poll only for the visible game and repertoire; obsolete replies have no UI effect. Historical mismatch-only evidence supplies no denominator. |

A relevant reply edit can change outcomes and marks an older report outdated.
Display titles, rank, Learning, provenance, and equivalent moves into a position
leave the comparison basis unchanged. A repeated position at a new ply remains
a separate learner decision. The browser uses the archived learner side and
zero-based pre-move ply for replay. Ordinary Study Next and Answer never read
feedback. No comparison writes Learning, attempts, receipts or queue state.

## Review an opening move from Study

| Operation and owner | Accepted rule | Version, work and failure |
| --- | --- | --- |
| Mark and open, Study UI and Study | Marking only holds the addressed opening card after its accepted answer. Existing Reveal grades Again. The active, completed opening attempt supplies its issued answer. Title, authorship and evidence never determine grading or scheduling. | The mark is in-memory and attempt-scoped. No new wire fields on existing Study commands or receipts. The optional review starts only when opened. |
| Compare saved reply, Openings and analysis readers | Show the current authored reply only when it matches the issued answer and a saved route proves authorship in this repertoire. Show a score for every legal root and similarity from another canonical position in the same repertoire and practice color. Route labels are display data. | Fence each independent optional source by dataset, attempt, answer identity and the reply and line revisions. Existing 250 ms optional reads and five-second engine slot apply. Missing evidence has no effect on grading, preview or Save. |
| Preview and confirm changed reply, Openings and Store | A legal different reply uses the existing continuation and conflict rules. Removal truncates every route which authors the addressed reply before its first owned occurrence. Retire only unsupported reply versions. The user confirms the exact before/after impact. | Requests are at most 16 KiB. Reuse the bounded content preparation slots, ten-second preparation wait, route limits and one 128-write transaction. An over-budget or stale plan has no durable effect. Verify the completed attempt and revisions again at commit. Commit the receipt with the change. Exact replay resolves before current-state checks and produces zero new writes. Accepted Study history is retained. |
