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
The [assembly manifest](current-assembly.json) records the qualified candidate
and installed artifacts. Keep the live database under its existing owner
until the managed cutover.

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
