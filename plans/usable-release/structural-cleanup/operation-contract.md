# Structural cleanup operation contract

## Supported operations

Keep desktop and private phone Study with one active attempt per dataset. Keep authored repertoire PGN import, browse, rename, replacement and suspend/resume; manual tactic capture and paged tactic browsing; manual PGN game import and paged replay of stored games. Retain the normalized tactics CLI import as explicit offline administration. Keep managed serve/init, health/context and the Settings controls for retained preferences. Existing schedules, active issued versions and accepted effects survive the transition. For a retained activity issued inside a connected run, keep the exact active attempt and version, then return to ordinary Next. Discard only the run continuation. Phone uses the same Study and context contracts, versioned pending envelopes and receipt recovery as desktop. Remove connected-run opt-in and phone Build access, including its API allowlist. Phone does not need Repertoires to establish dataset identity.

Retire connected runs, warmups, Study presence, optional Practice and extra allowance, review marks and saved/opened reviews, optional explanation and provenance enrichment, corrective Games analysis, remote game refresh, automatic tactics ingestion from Games, all reports, coverage and gap analysis, Phone Build, all model/engine/provider workers, portable restore and repertoire reset, fixture runtime and one-off maintenance commands. Remove registrations, callers, lifecycle hooks and data readers unique to these features. Keep inert data in the verified archive. Retire Concede and Abandon as new commands after protecting their accepted receipts. Retired commands may return a typed retirement result. They may not enter the former pipeline. Existing Practice attempts are retired without grading and remain accessible in the archive. Retain Give Up for Test as one failed assessment plus correction. Teach may be skipped without grading.

## Learning and ordering

Learning owns schedule/availability and the introduction policy. Preserve current FSRS and configured study calendar. Teach is an acknowledgement, consumes one introduction from the corresponding opening or tactics budget and does not create a successful recall. Existing issued lessons can complete across rollover. Test records its first assessment once. A miss produces one correction obligation and continues correction on the already active attempt. Only a still-open correction whose active attempt has been released is eligible for issuance from the plan. Finishing correction closes that exact obligation without another assessment or new introduction. Keep schedule/assessment effects already saved under older releases. No new same-day repeat is invented.

Queue builds one stable plan per study day. Outstanding correction work sorts first, followed by due Test ordered by due day, then Teach. Within each ordinary group use stable target identity as the final tie-breaker. Only the authoritative Learning facts and content admission/suspension/version participate. No relevance, route rotation, model, timestamp-of-request, or current-game input participates. Skip atomically closes the active attempt and defers its exact issued work for the current study day, with no additional grade. A new obligation is independent of the deferral. Resume skipped accepts a dataset, day and submission ID and advances a day-local cutoff to the latest deferral at acceptance. Deferred work returns at its original priority. Exact replay does not advance the cutoff for later skips or a later day. One addressed miss can elevate work without renumbering other entries. Opening and tactics budgets are independent. Keep the persisted opening cap and expose it through Settings alongside the current tactics cap and themes. Remove CLI configure. Theme filters govern admission of new tactics, so a theme change invalidates membership and counts. Preserve authored repertoire prerequisite/frontier eligibility as compact batch input. Only an eligible successor can enter the Teach group. Progress reports ready work by activity and family, deferred work separately, and spent and remaining introductions for the current study day. It never counts a displayed or issued lesson as spent.

## Operation boundaries

| Operation | Owner and work | Result |
| --- | --- | --- |
| Health/context | Runtime and Store, process/schema plus one dataset metadata read, no Study startup dependency | Individual readiness, dataset identity or typed unavailable |
| Resume | Store and Study, one active pointer, attempt and issued definition, no ranking | Active attempt or typed missing/incompatible |
| Next | Queue and Store, resume first, indexed ready checks capped at 32, at most one hydrated definition, atomic issue | Issue, preparing, or done with proved complete usable membership |
| Answer, Teach, Give Up, correction | Study/Learning decides; Store reads and writes addressed attempt, issued content identity, Learning, one receipt and addressed work/count delta or dirty marker | Acceptance is returned independently of enrichment, plan, summary and subsequent Next |
| Skip | Queue and Store, addressed issued work and receipt; keep deferral in authoritative facts until same-day resume or rollover | Defer once without a grade; increment bounded deferred counts or dirty marker |
| Resume skipped | Queue records a day-local resume marker, clears deferral logically and schedules a batch if an addressed update cannot prove completeness | Accept once, Next may be preparing |
| Progress | Store summary head and one bounded count projection | Current counts, updating or unavailable |
| Browse | Store, addressed record or indexed pagination with an explicit limit of 50 | Page, missing or invalid cursor |
| Rename/suspend/resume | Store, conditional metadata set on addressed repertoire and expected metadata revision. Already-equal values are idempotent; a different value at a stale revision conflicts. Suspension may dirty eligibility without rewriting downstream history | Accepted/idempotent, missing, conflict or invalid |
| Content preview/save | Chess parses only the submitted document; Store checks addressed revision/preview basis and applies changed definitions and lineage only | Preview or bounded atomic save; oversized changes need explicit offline import |
| Games import | Explicit manual PGN preview and apply; bounded accepted writes through the writer; addressed game identity and receipt | Atomic batch or retry; no Learning or rank effects for game-only data |
| Games job status | If an import is still in progress, read one job envelope | Read-only status, no apply or worker admission |
| Settings | UI handles appearance/sound and Store backs retained shared preferences. Day/allowance changes dirty eligible projections only when their semantic values change | Current value and validated save |
| Static UI | Same managed assets and access boundary for desktop and private phone Study | Bounded asset read, independent of Study readiness |

The initial limits are 16 KiB for ordinary JSON bodies, 2 MiB for content and Games input bodies and 10 seconds total for disposable parse/admission including body waits. Foreground content and Games apply accept at most 128 affected authoritative records per transaction, counting downstream changes for that batch. Larger mutations must use explicit offline administration with bounded batches or receive an over-budget result before acceptance. Games import accepts a bounded manual batch through the writer, with an optional separate read-only status envelope for an admitted job. The legacy status route must never apply a batch. The initial application writer admits at most eight waiting operations, runs one transaction at a time and rejects new operations after a two-second admission wait. Accepted writes carry receipt identity; a delivery timeout does not discard them. Large authored imports and plan generation use explicit bounded batch work outside request handling. Stage and clean at most 128 projection rows per transaction; final generation publication checks indexed completeness metadata and switches one head. T05 carries these ceilings to the capability owners. T55 calibrates elapsed-time budgets separately without weakening deterministic limits.

## Identity, invalidation and recovery

The basis is dataset, study day/calendar/policy, content availability/version and the authoritative planning epoch. Capture it with the input facts in one coherent read. Only the captured basis can authorize publication. The projection head carries generation and freshness. Summary publication checks a separate captured count basis and is unaffected by a rank-only revision; membership or count changes fence any affected builder. Plan and summary support independent dirty state. Issued work/obligation identity belongs to authoritative attempt or Learning state, can be replayed across generation cleanup and includes an obligation revision. A later miss for the same target/version has its own revision. An older result cannot consume it.

| Event | Plan | Summary |
| --- | --- | --- |
| Valid accepted intermediate move, exact replay, rename, games-only import | No change | No change |
| Clean terminal Test | Close exact Test work, fence stale plan builds | Decrement compatible addressed ready work or mark dirty |
| First miss or Give Up | Record the assessment once and the new correction revision, fence stale plans | Account for the exact transition or mark dirty |
| Correction completion | Close only that revision and fence stale plans | Account for the completed correction or mark dirty |
| Teach or skip | Update the issued work in the same transaction, mark dirty if needed and fence stale plans | Apply spent/deferred count delta or mark dirty |
| Resume skipped, new/changed/retired content, suspend/resume, qualification hold/release while cutting over, day/calendar or allowance change | Membership dirty until a complete batch or proved local update | Dirty until compatible counts |
| Rank policy revision only | Keep valid order during refresh | No change |
| Build failure, absent projections or stale summary | Next prepares unless active attempt can resume; valid writes still accept | Updating or unavailable |

Check that the envelope addresses the current dataset before receipt resolution. For the correct dataset, consult the original operation family and submission identity, compare the immutable payload and return any accepted result before current attempt/version or projection checks. A changed payload for the same submission identity conflicts. Any finite retired-command recovery follows these same checks. Old projections fall back only to a bounded, truthful acceptance envelope if the former view depends on retired data. UI keeps one unresolved durable command owner across navigation, retries the original payload and does not synthesize another command on a lost reply. A known acceptance followed by failed Next retries Next alone. Retained typed and serialized receipt encodings and browser recovery envelopes are inventoried and tested before wire changes. Retired-route acceptance is protected with finite read-only receipt resolution where older clients can have pending writes. Unaccepted retired commands receive explicit retirement. For legacy pending commands over new input caps, use bounded existing receipt resolution by original identity and fingerprint. If no accepted receipt exists, return over-budget and preserve the local draft for explicit resubmission. Unknown external callers are investigated under T13/T37 before deleting their reachable interfaces.

For each contract test, alter one semantic fact such as issued revision, obligation revision, suspension or day and expect the corresponding issue/reject/rebuild transition. Then poison unrelated historical rows, presentation metadata or retired evidence without changing the operation result or touching those reads. Exercise actual consumers and real SQLite on disposable copies. A missing plan/summary must leave acceptance available; no full-selector or snapshot fallback.

## Persistence capability boundaries

T05 releases each capability separately. An operation receives its own port or
concrete input facts. The composition root alone may assemble more than one port.
The older all-purpose Store remains transitional until the real consumers move.

| Capability | Required address and fact boundary | Failure and delivery |
| --- | --- | --- |
| Dataset identity | Singleton dataset ID. The runtime context owner may additionally read actual schema in the same SQLite statement. | Missing or unreadable metadata is unavailable. No attempt, content or Learning read. |
| Study resume | Dataset and active pointer or explicit attempt ID, then the issued target/version and current admissibility for that attempt. | Missing or incompatible activity is distinct from empty work. Does not contact a plan or ranker. |
| Study acceptance | Original command identity and fingerprint. For new work, exact attempt revision, issued target/version, required Learning row and obligation identity. | Existing matching receipt wins before evaluating current work. New successful mutation writes attempt, Learning if applicable, receipt and bounded projection delta or dirty signal atomically. |
| Content authoring | Dataset, addressed authored document and relevant metadata or content revision, and validated bounded changes. | Same-value conditional metadata set is idempotent. Reject unrelated or excess change before entering the writer. A stale signed content preview needs a new preview. |
| Manual Games apply | Dataset, import command ID and fingerprint, and prepared valid addressed game records. | Batch is indivisible, replayable, and has no Study effects. A query of job status reads its envelope only. |
| Explicit administration | Separate operator entry point and matching archive/dataset identity. | Full data may be inspected or converted here. No adapter can substitute this capability for a missing foreground one. |

The runtime durable writer takes an immutable, operation-specific proposal.
Its input contains the relevant address/basis and either the original command
identity or the captured projection basis. It must be possible to validate the
proposal's row limit before enqueueing. The queue retains at most eight waiting
proposals, with one separately counted executing transaction. Admission checks
the original request deadline and a two-second queue budget on a monotonic clock.
If the proposal expires while waiting, the writer claims neither the proposal
nor its data and records an explicit pre-acceptance outcome. Once the writer
claims a valid proposal, transport cancellation is independent of its short
transaction. Committed results resolve by receipt or by a fenced projection
head; a dropped response never makes a second mutation valid. The runtime
writer serializes bounded foreground and background turns; computation and
provider I/O remain outside it. T43 owns the running queue and must demonstrate
that continuous foreground work cannot starve a ready apply. T61–T63 own
actual publication adoption. Fixtures provide explicit narrow methods and
must fail on unsupported capability without invoking snapshot or catalog reads.
