# Lean operation contract

Tempo #104 used `4f97e742b0f259ba3c26109d69aa365d570439f8` on Lean schema 2 as its baseline. Keep live data, first-answer Good/Again, FSRS, the repeat deck, opening preferences, provider imports, and scanner-driven tactic publication. This contract governs Lean. The older structural-cleanup contract remains evidence for the predecessor.

| Operation | Owner and permitted facts | Effect and lifetime |
| --- | --- | --- |
| Study resume and Next | Study identifies the active attempt. Queue uses the committed deck, prepared availability, due times, previous card kind and saved new-opening policy. | Resume first. Check at most 32 prepared entries and hydrate at most one definition. Missing or stale membership means preparing. Done requires a complete exhausted order. No catalog fallback. |
| Answer | Study validates dataset, attempt and immutable submission. Chess grades the issued moves. Learning computes FSRS. Queue draws and places Again. | Store atomically accepts one grade, schedule, receipt and repeat obligation. If fresh membership is unavailable, the obligation retains its original draw and blocks only subsequent issuance until placed once. Saved answers replay before current-attempt checks. Prior accepted response encodings remain readable. |
| Prepared membership | Store captures the revision and owns publication. Queue owns ordering. Use card identity, kind, active status, due or unseen state, saved rank and reservations. | Apply addressed deltas in the original mutation. Initial seeding and its cursor commit together in turns of at most 128 affected rows. While seeding, every authoritative mutation updates its addressed entry in the same transaction, including inserts behind the cursor. Only an exhausted cursor may mark the queue ready. Any future builder that computes from an independent snapshot must fence publication against that snapshot’s original revision. Never use stale membership to issue new work. Use exact Lean due times, with no new calendar or review policy. |
| Games | Provider adapters supply normalized games. Runner owns checkpoints and retries. Scanner returns versioned observations, and Tactics publishes puzzles through its existing intake. | Archive acceptance, scanning and publication have separate durable progress and retry. Status reads never advance jobs. No provider, scan or optional enrichment gates Study acceptance or issuance. |
| Content and settings | Chess validates submitted content. Openings owns the repertoire destination, position and one-active-reply rule. Settings saves one authoritative value per preference. | Online content saves that would change more than 128 rows reject atomically with an offline import path. Settings and catalog mutations update only their addressed facts and affected projection. Large Games uploads retain the 64 MiB limit and run in bounded, resumable batches. |

The runtime has one write connection, at most eight waiting proposals, two seconds to enter execution, and at most four foreground turns ahead of a waiting background apply. A claimed proposal can finish after a disconnect. Parse, network, ranking, and scanning run outside write transactions. Offline writers acquire the same exclusive database lock as the service. Ordinary JSON uses the 16 KiB budget. Deliberate PGN inputs have a separate bounded path. Online applies count all affected rows, including projection changes.

Display titles, provenance, optional game metadata and equivalent representation do not change acceptance or queue policy. A changed authoritative due time, card availability, saved rank or committed repeat position may change selection. Qualification uses the real HTTP and browser consumers, read-only SQL access checks and row budgets, writer contention, restarted imports, and original pending Answer envelopes from the preceding installed build on disposable data.

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
