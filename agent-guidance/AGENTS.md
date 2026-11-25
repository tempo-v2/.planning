# Tempo engineering instructions

This file is the current project contract. Historical plans and old tests are evidence of previous behavior, not requirements to preserve every feature. Follow explicit current user decisions and the selected task packet when they supersede historical guidance. During structural cleanup, feature simplification and retirement are permitted; unrelated feature expansion is paused.

## 1. Start with the actual source and operation

Read this file, the selected worker packet, the current assembly manifest, and applicable local instructions. The selected Planning checkout owns the canonical bytes of this guidance. In an assembled workspace, verify its root copy with `python3 .planning/scripts/check_guidance_identity.py AGENTS.md` and record the reported SHA-256 with the Planning revision. Repository entry points may add local instructions and refer to this canonical file. Workers verify their checkout, dirty files and relevant released dependencies. The coordinator verifies running-artifact identity once per baseline/install; an unrelated component worker does not repeat it. A clean checkout, default branch, or old prompt SHA does not identify the installed application. Preserve other workers' changes and use the coordinator's file reservations.

Name the operation being changed. State its semantic owner, permitted input facts, read/write set, maximum work, relevant version/day/obligation identity, failure behavior and freshness rule in the operation contract. Use existing contracts when unchanged. Do not derive a product rule from a display field, identifier spelling, optional metadata, a fixture, or an available database column.

## 2. Give each operation only its own capabilities

Pure domain code receives values and returns decisions; it cannot obtain storage, browser, process or network handles. Application handlers receive the smallest coherent storage capability they need. No universal application context, full Snapshot, complete Catalog or all-purpose Store handle in an interactive helper.

Reads must not secretly apply jobs, accept grades, import content or change allowances. Separate an explicit command from querying its status. A missing narrow interface is a task at its owner; do not compensate by loading the entire application and extracting one field.

Routine commands use addressed state and writes. Full snapshots, whole-history validation and global catalog rewrites belong only to explicitly named batch/admin work. PGN interpretation is permitted for an addressed authoring/import/export operation whose actual purpose requires it and whose budget declares it; it is forbidden as incidental work in Next, summary, status or unrelated browsing. Never add a broad fallback to a narrow interface. Unsupported operations return a typed unsupported/unavailable result. Existing user and packet authorization covers the work it actually grants; these classifications do not create repetitive approval steps.

### Extend Tempo through owned interfaces

- Define the smallest typed interface the consumer needs. Specify the owner, permitted inputs, returned facts, empty and failed outcomes, and any version or retry guarantees. Keep source-specific policy, formats, credentials, and private persistence inside the owning adapter.
- A game provider supplies games. A detector supplies findings. The job runner owns retries and checkpoints, and Games owns game acceptance. The selected profile’s operation contract identifies the publication owner and its intake. At the first additional implementation, give it the same owned interface before adding provider or detector branches to downstream callers. Use ordinary functions or concrete types where they suffice.
- Study consumes published, versioned exercises and owns attempt progression and the first accepted assessment. Chess owns legal interpretation and grades the issued moves. Adding or swapping a game provider, detector, or optional analysis source must require zero changes to Study selection, issuance, or grading. Fetch optional game or analysis context separately from accepting or advancing a review.
- Keep dependencies pointed from the caller to the owned interface. Pass typed values across component boundaries. Keep implementation handles and unrelated tables behind their owner. Keep concrete wiring in the application or job composition code. Extend an interface for a demonstrated consumer need and keep it specific to that operation.
- Verify through the real consumer that a new or substituted source can deliver valid input and that an empty or failed optional source leaves unrelated commands and their durable effects independent. Include the expected difference when an authoritative input changes. Review actual calls, reads, and writes along with imports.

## 3. Enforce the prepared-order Study contract

Queue owns one rebuildable ordered plan and its bounded priority updates. Learning owns current availability and every Learning transition. Store enforces addressed identities, versions, constraints and atomic accepted effects. Chess owns legal interpretation. Study, if retained, owns attempt progression and the first accepted assessment.

Next resumes an active attempt first; otherwise it consumes an indexed prepared plan, performs the declared bounded validity checks, and hydrates the chosen version. It never reads game relevance, parses repertoire PGN, loads all definitions/Learning, or invokes an engine/provider. Missing/stale plans yield explicit preparing state and a coalesced background rebuild. No live-selector fallback.

An accepted transition advances only its exact activity/work/obligation identity, retained with authoritative attempt/Learning facts rather than a disposable plan row. An older answer cannot clear a newer miss for the same target/version. Intermediate moves and ungraded Practice do not consume unrelated scheduled work. Receipt and Learning/attempt effect commit atomically with a compatible addressed projection delta or a dirty/rebuild marker; replay has zero new effects. A missing/stale plan or summary must not block valid Answer/Teach/Games acceptance.

Capture coherent planner inputs and their basis together; build outside write transactions. Stage rows and reclaim old generations in bounded write chunks; final publication is a short completeness check and head switch against the original basis. Failed/stale builds cannot overwrite newer work. Rank-only refresh may use the existing order. Membership-dirty selection defaults to preparing until a complete plan or proved bounded update is available. Updating summaries cannot authorize optional work from a stale zero. Qualification hold/release and reset are eligibility changes, even when produced by analysis; evidence-only ranking changes are not. Summary and order have explicit separate freshness states.

## 4. Keep optional work optional

Analysis, explanations, provenance, reports and provider/model refresh cannot gate unrelated acceptance, health, context, status or browsing. A browser timeout/abort does not by itself cancel server work. Every retained disposable job has bounded admission and a whole-operation deadline including queue, lock, pipe and resource waits. Cancellation retains the slot until physical completion is acknowledged. Uncancellable dependencies require bounded isolation/termination or retirement. Fence late results and fairly schedule durable apply work; an accepted durable command resolves through its receipt rather than being silently abandoned.

Keep one durable write owner and short transactions. Declare input/output byte limits, queue capacity/wait, physical worker slots and total deadlines as well as SQL/row budgets. Reject new work before durable acceptance when capacity is unavailable; never discard an already accepted command because its delivery timed out. Do not hide broad work behind a mutex, an unbounded thread, a status poll, an invalidation callback or startup reconciliation. Optional startup work must not prevent basic health/context from being available.

Each UI page/controller declares its endpoint/source set, query identity, invalidation topics, visibility/polling rule and cleanup. Dataset identity comes from the small application context operation. Hidden optional panels do not start engines/providers merely by mounting. Test permitted calls and maximum in-flight deliveries through the mounted consumer; cancel or coalesce obsolete disposable reads while preserving unresolved durable commands.

A failed optional view projection must not turn a known accepted write into an ambiguous command. Carry acceptance identity separately from loading the next activity or enrichment. Keep required blind-test secrets server-side and use issued content versions for retained attempts.

## 5. Prefer one real path and delete the replaced path

Keep the smallest supported production model. Do not preserve fixture runtime branches, public fake APIs, completed maintenance commands, compatibility adapters or unused features solely because tests mention them. Before retirement, inventory actual registrations/callers, independent consumers and retained data/commands; provide an archive or finite migration when needed.

Every replacement task names the old caller/path that disappears. Interfaces without consumer adoption are capability releases, not completed fixes. No permanent duplicate selector, scheduler, controller or silent production fallback. No generic event bus, plugin framework, service mesh, universal repository or configuration language without a concrete demonstrated need.

Keep Types to small stable values. Keep optional analysis attachments out of general content/selection shapes. Keep authored-document validity separate from model readiness. Preserve original data in a verified archive where features are retired; deletion of functionality does not require deletion of the only data copy.

## 6. Prove independence through the real consumer

For an affected operation, prove both a relevant change that must alter behavior and an irrelevant change/failure that must not. Extend the real SQLite tactical-acceptance pattern: poison unrelated payloads, deny forbidden reads, count actual writes and SQL work, and grow unrelated data. A test that returns the same counts while still reading relevance does not prove independence.

Use deterministic limits from the operation contract: forbidden calls/reads equal zero; bounded candidate checks and content hydration; no unrelated writes; no inline batch computation. Use fresh connections or explicit statement-cache handling for preparation-time SQL authorizer tests. Measure runtime queue wait separately from handling and commit time.

Run the smallest meaningful component/consumer/persistence checks for the change. Test races, replay and failure rollback at actual storage/protocol boundaries where affected. Do not count a fixture demo, unchanged stamp, test total or import graph as proof of another operation. The regression must fail when the original forbidden dependency is deliberately reintroduced.

## 7. Coordinator, workers and review

One coordinator owns scope, task state, contracts, interface releases, shared-file reservations, integration and heavy test scheduling. Workers receive one bounded packet with exact files/symbols, prerequisites, first change, forbidden shortcuts, tests and handoff. Workers cannot silently broaden an interface, invent policy, edit another reservation or waive acceptance to finish.

An independent reviewer checks the actual consumer, declared work/failure boundary and deletion of the old path. New findings are assigned a disposition; they are not hidden or automatically turned into a new framework. If blocked, state the missing contract/source/capability and complete independent authorized work.

## 8. Completion means the chosen outcome is verified

Commit changes across every changed repository. Verify each pushed branch and its open pull request against the current integration branch, or verify the remote main commit when direct-main work or merging is authorized. Read the remote result back and confirm it contains the intended changes. Record exact commits, pull request links and compatible component versions in the handoff. If publication is blocked, preserve the work and report what prevented publication and the exact remaining step. Read-only reviews and proven no-change outcomes require no code commit or pull request.

Report implemented, tested, published, merged, installed and observed as separate states. Record exact source/assembly/artifact, meaningful checks and remaining limits. Do not claim project-wide freedom from coupling from a scoped review.

The cleanup closes only when every supported production operation has an owner and an enforced contract, retired paths have no live registration/fallback, integrated race and work tests pass, and the installed composition matches the reviewed one. Keep one current manifest and concise ledger. Archive history separately instead of appending conflicting current instructions.
