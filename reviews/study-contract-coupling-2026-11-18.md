# Study contract coupling review — 18 November 2026

This review records the audited source pins and original findings. See the
[shared Study reconciliation](../plans/usable-release/STATE.md#shared-study-decision-contracts-november-18-2026)
for the subsequent implementation and verification.

## Decision

The neutral display-name change addresses the reported dependency on its branch, but the combined intended release is not yet qualified. The consolidated UX branch still contains the name-dependent continuation rule; current main contains the name fix but lacks the UX branch's whole-attempt success check. This review also found a previous-release receipt recovery failure, another display-to-control dependency in recovery messages, and a provenance-dependent new-tactic admission seam.

Update the canonical agent guidance now. Before another Study/wire release, integrate the intended source combination and close the continuation and previous-release recovery findings below. Existing component boundaries remain useful; the evidence supports small explicit contract repairs rather than a new architecture.

This is a source and focused consumer-execution review, not an installed-runtime certification. No application runtime code, user data or installed service was changed.

## 1. Source boundary and scope

| Repository | Main reviewed | Additional consolidated UX source |
| --- | --- | --- |
| tempo | af20ea4f31721cd69f6e058d0daf48658a9b7d36 | 8c7c3691e919d10309a7528dd28a32fd6724b7ea |
| tempo-ui | 7777eebb7f485891ec2eb3fe84ab4b12f5845c0c | 349edde5ece77bba572774561c7fd3b367535618 |
| tempo-store | 67ee08d8de89943844e654d54e4b4d7f6808de3a | e6a7b9fcf3d4f042578189b6f1b98f39112ebff2 |
| tempo-chess | 406a573c2145c7b9408a543266171e33e6793f9d | Relevant UX application consumers also inspected |
| tempo-learning | 10fd7783685a70e05f3ae2a606d8d25deaddf1ef | Relevant UX application consumers also inspected |
| tempo-queue | 8ad7feda5c56982ee0411ef44309f69bb360d783 | Relevant UX application consumers also inspected |
| tempo-study | 73b2482dfb2ae652220727b87451fdb4a5110807 | Current main matches the existing audited snapshot |
| tempo-types | a8e46c9b9442f1180ec33b8035cef1c713414b66 | Current main matches the existing audited snapshot |
| tempo-core-components | e9a1d160a729bc9fbbddaf16427625301cc9498a | UI-main vendored package 0.2.2 inspected |
| .planning guidance base | 324c101a40719af6ff341c937d1d5a587d1efdae | feat/installed-release-handoff |

The application, UI and Store branches are **diverged**, not a simple older/newer sequence. Relative to the UX pins, main is respectively 4 ahead/4 behind, 5 ahead/6 behind, and 4 ahead/3 behind. Main lacks the consolidated progress/collection/history work. A source fix merged to main does not establish that the installed UX checkpoint contains it. [Application comparison][app-compare]; [UI comparison][ui-compare].

The review covered the actual Study consumer and controller, wire validators, app issuance and command handlers, typed and serialized receipts, Store serialization/constraints, content import/reimport, Chess metadata/identity consumers, Learning transitions, Queue admission/order, and the actual vendored Core source. It searched metadata names and their aliases, null/presence conditions, source/ID parsing and message comparisons, then inspected behavior-bearing uses. Retrieval included 105 current app/Store source-and-test artifacts, 91 UX source files, and all 47 Chess, 17 Learning, 20 Queue, 25 Study and 15 Types Rust source files. Study/Types were freshly verified against current main; their production logic contains explicit lifecycle/grade/revision contracts and opaque IDs, with no display-name/source/family inference found. These are coverage/integrity counts, not behavioral test counts or a claim of equal scrutiny of every line.

## 2. How the original defect escaped

The earlier review was too narrow at the exact decision boundary. The first two observations below concern this conversation's earlier deliverables: the saved review packet REVIEW.md and prompts/01_FEEDBACK_CONTINUATION.md. Those are supplied-history evidence from the earlier task output, not claims inferred from Git history. The remaining observations are supported by the pinned repository links below.

- The previous review packet explicitly reread the completion condition and identified latest-move correctness being confused with whole-attempt assessment. It did not challenge the neighboring name guard.
- The implementation prompt said to preserve success treatment for a “clean tactic.” Its acceptance case likewise covered a clean multi-decision tactic. That wording carried a family distinction into implementation without identifying its owner or contract.
- The app's UI boundary journey drives `createStudyController` and explicitly calls Next after completing an opening. It does not exercise the React consumer that decides whether Next happens automatically.
- The UX outcome test varies activity and assessment around a nameless fixture. The newer name test validates an allowed payload shape. Neither keeps the same exercise fixed while changing or omitting its display name through the actual continuation path.
- Receipt tests cover same-version restart and replay. A prior rule already warned that allowance receipts contain serialized wire replies, but that specific representation was not included in upgrade qualification.

These are observable coverage gaps, not claims about anyone's intentions. The shared grader and package dependency graph can be correct while a downstream UI condition introduces an unowned rule. An interface review must establish what the consumer does with the field, not just where the field came from. [Controller-only journey][ui-boundary]; [opening and durability tests][opening-tests]; [UX outcome test][outcome-test].

The original chain was content label → stored attempt display name → optional wire field → UI classification/continuation → presence or absence of a Next command. The meaningful counterfactual is the same activity and result with only that label varied.

### The broader pattern: deriving policy from available representation

The deeper failure is an incomplete semantic contract. The code had a field shape and an implementation location, but no enforced account of which decisions that field was allowed to influence. A consumer could turn an observed correlation into an operational rule while remaining inside the allowed package graph.

The name condition compressed three claims into one expression:

1. The optional repertoire name is absent.
2. Therefore the exercise is a tactic.
3. Therefore it should continue automatically.

Only the first claim follows from the field's display contract. The classification and continuation rule need independent authority. This is why “do not branch on repertoire_name” is an insufficient general response: the same inference can be moved to a new field, helper or adapter.

The appropriate general term is semantic coupling: behavior depends on meaning that the boundary did not promise. In this case that coupling arose through inferred policy. The preventive obligation is to establish the intended decision and its basis before choosing fields to implement it.

### What the existing instructions allowed

The previous guidance asked ownership questions “before adding an interface.” This bug reused an existing field inside an existing consumer. A material product decision was therefore possible without triggering that design step.

Package ownership also left a gap. The UI can legitimately own automatic continuation, so “put UI behavior in the UI” does not establish what the continuation policy should be. Implementation ownership and policy authority are separate questions.

The instruction to preserve existing behavior was similarly incomplete. It is important to preserve user data, accepted rules and useful completed work. Existing code and tests nevertheless cannot establish that every distinction they contain is intended. The earlier “clean tactic” prompt demonstrated a positive case; it did not establish that openings should wait or that missing metadata identifies a tactic.

These are concrete instruction and specification gaps. We cannot reconstruct every internal reasoning step of the implementing agents, and the findings do not justify attributing motives.

The baseline sources are the [earlier canonical guidance][baseline-guidance],
[planning entry point][baseline-readme], [scaffold interfaces][baseline-interfaces]
and [behavior examples][baseline-behavior]. The proposed rule also applies to
authors of task prompts and handoffs, so an example cannot silently become the
next agent's exclusive product requirement.

### Why tidier code alone would not fix the pattern

| Proposed change | Remaining failure if meaning is still unestablished |
| --- | --- |
| Rename the display field | The consumer still chooses behavior from incidental information |
| Add exercise_kind or can_continue | The producer can derive it from the same unsupported name-presence inference |
| Replace a string with an enum | A well-typed value can carry an invented rule |
| Extract a shared helper | Every caller can consistently apply the same unjustified rule |
| Move the rule to the server | Centralization does not establish a valid product requirement |
| Add tests around existing examples | Correlated fixtures and implementation-derived assertions can preserve the assumption |
| Ban content-family branches everywhere | Legitimate Chess interpretation and Queue policy can be obscured or broken |
| Require user approval for every detail | Routine work stalls without resolving which choices are materially semantic |

The implementation order should be: intended behavior, requirement/contract basis, decision owner, justified inputs, implementation, then evidence that the contract holds. Meaning must constrain the implementation before the implementation becomes the explanation for its own tests.

### A minimal decision contract before coding

For a change that affects commands, workflow, eligibility, priority, identity, learning, authorization, persistence, recovery or a claim that a result was accepted, record five short answers in the existing task or PR:

| Part | Question |
| --- | --- |
| Behavior | What observable operation, transition or durable effect is intended? |
| Basis and owner | What current requirement or accepted contract establishes it, for which runtime/profile/release, and who owns the decision? |
| Inputs | Which semantic facts are sufficient, and what establishes those facts? |
| Independence | Which nearby presentation, representation or context must be free to change without changing this decision? |
| Lifetime | Which values can survive import, caching, persistence, restart or a release, and which consumers must still interpret them? |

This is not a new design-document ceremony or a registry of every branch. One note can cover a cohesive feature. Formatting, layout and reversible local implementation choices remain autonomous when action semantics are unchanged. When a material policy choice is unresolved, identify it explicitly, continue independent work, and ask only if the ambiguity cannot be resolved from the authorized task and current contract.

For the reported case, first state the continuation rule using the intended activity, completion, whole-attempt outcome and delivery status. Then establish the appropriate owner. Only then select the input fields. Display name never becomes a candidate basis merely because it happens to correlate with content family in current fixtures.

Teach illustrates the positive case: its acknowledgement behavior follows an explicit activity and teaching rule. Changing Test to Teach can legitimately change the flow. Changing “London System” to another name cannot establish that change.

### Make the wrong dependency harder to express

After the rule is established, give decision code only the semantic inputs it needs. A small continuation function can accept activity, completion, assessment and delivery state; it need not receive the entire view containing titles and provenance. Rendering can receive the display fields independently.

This is a local boundary in the existing owner. It does not require another service, a general policy engine or a new server round trip. A type annotation alone is insufficient in unchecked JavaScript; the implementation must actually honor the input boundary and the owner must remain the authoritative path.

If the consumer lacks a required fact, complete that contract at the producer/owner. For recovery controls, the controller already knows whether storage is unavailable or refresh is required. It should expose that state directly rather than requiring the screen to infer it from prose. For eligibility, Queue should receive explicit normalized policy facts. For a content edit, an application caller should invoke the owning learning transition rather than invent a replacement by constructing convenient default state.

A new field does not complete this work if its producer still infers the value from an incidental representation. Trace the derivation until the fact's basis is clear. The rule concerns meaning, not variable names.

### Define independence before constructing tests

For a decision, hold its authorized semantic facts fixed and vary irrelevant representation. The resulting command sequence and durable semantic effects should remain equivalent; pixels and display-only persisted metadata may differ as intended.

Also specify a change that should alter the decision. Testing only invariance could reward an implementation that ignores every input. Teach versus Test, clean versus corrected outcome, or an intentional theme-selection change supplies a meaningful positive control when relevant.

This gives two obligations:

- Authorized semantic changes produce their declared effects.
- Presentation or representation changes do not acquire new effects.

The name-present/renamed/omitted check is one instance. The same principle applies to recovery-state/message pairs, normalized membership/source attribution, equivalent supported content-mutation entrypoints, and historical accepted results read by a newer release.

Tests should exercise the actual consuming path and be based on the declared rule. A test that copies the implementation's predicate establishes agreement with itself, not the policy's validity. Keep the existing failure/replay checks as enforcement of this prior design decision.

### Related findings have distinct mechanisms

| Finding | Specific failure | Contract that was incomplete |
| --- | --- | --- |
| Name controls continuation | Consumer promotes display information into workflow | Permitted inputs and independence of the continuation decision |
| Error wording controls actions | Consumer reconstructs an operational state from prose | Controller's public recovery-state contract |
| Provenance controls admission | An intentional policy depends on an implicit legacy encoding | Membership normalization, missing-data and import/reimport semantics |
| Generic import resets learning | Public paths independently choose different transitions | Authority and semantics of each supported content mutation |
| Historical reply fails after upgrade | A saved wire representation outlives its decoder assumptions | Lifetime, readers and version compatibility |

They share incomplete meaning, authority or lifetime at a boundary. They do not all have the same concrete cause or require the same repair. In particular, metadata can legitimately support a declared search operation; a stable source token can legitimately establish identity; an explicit origin fact can legitimately influence priority. The permitted role depends on the decision's contract.

An unrelated example makes the generality clear: an organization label is not an administrative grant, payment-description text is not settlement evidence, and a timeout is not evidence that a command was uncommitted. Replacing any of these with a tidier derived flag leaves the defect intact unless the producer establishes the correct fact.

### Instruction discovery is part of prevention

The planning README previously directed agents to BEHAVIOR and INTERFACES as general acceptance/interface sources. BEHAVIOR still marks the initial same-day-repeat policy as an established requirement; INTERFACES describes wire version 1 and the original placement of controller/validator code in Core; READING_GUIDE names historical refactor branches.

See the pinned [planning entry point][baseline-readme],
[behavior baseline][baseline-behavior], [interface baseline][baseline-interfaces]
and [reading guide][baseline-reading] for those specific statements.

This is an observed source-authority ambiguity, not proof that those documents caused the name condition. An agent nevertheless should not have to infer the governing runtime or override historical instructions from memory.

The accompanying change therefore makes the canonical guidance the first entry point, adds a planning-root AGENTS pointer, and scopes the old documents explicitly as scaffold history. It preserves still-applicable identity, atomicity and whole-attempt invariants. The current component ownership description distinguishes Core components, UI browser transport/recovery and application server commands.

A repository update does not automatically refresh a copied instruction file on another machine. Adoption requires the assembled workspace to read the updated canonical guidance; the README now makes that requirement explicit.

### Practical limit

Instructions cannot prove that an agent will never consider a shortcut. They can forbid silently promoting one into product policy, require the semantic basis before implementation, and make narrow interfaces exclude irrelevant inputs by default. Focused review and tests then check a design that was already explicit rather than discovering its intended meaning after code exists.


## 3. Findings

### F1 — Continuation correctness is split across diverged branches

**Priority: P2 correctness defects; block qualification of the combined Study release until reconciled.**

In UX `StudyOutcome.jsx`, `canAutoAdvanceTactic` requires `!view.repertoire_name` as well as complete status, Test/Practice and Good assessment. App uses it to schedule Next. StudyPage also infers “Tactics” and decision-progress visibility from an absent name.

In current main, the new `exercise_name` is display-only. However, App computes success/automatic continuation from completion, non-Teach activity and `feedback.correct`; it omits the whole-attempt assessment. A correct final move after a miss consequently receives the success cue and timed Next, and the visible Again message is suppressed. The saved fixture outcome remains Again. This review did not observe a saved grade being changed to Good.

Actual consumer control-flow traces:

| Fixed exercise/result | Name present | Name changed | Name omitted |
| --- | --- | --- | --- |
| UX, clean Test | next → answer | next → answer | next → answer → next |
| Main, clean Test | next → answer → next | Same | Same |
| UX, Test completed after a miss | next → answer → answer; waits | Same | Same |
| Main, Test completed after a miss | next → answer → answer → next; success cue | Same | Same |

Practice exhibits the same branch-specific continuation decisions. Both branches require explicit Teach acknowledgement. UX requests Next after accepted acknowledgement; main still needs another manual Next.

**Owner and repair:** UI continuation consumes explicit activity, completion and whole-attempt outcome; the learning rule remains in its existing owner. Integrate the neutral name with the UX outcome behavior, preserving both invariants and Teach's explicit acknowledgement. Use a neutral helper name. Do not take either App file wholesale and silently discard the other branch's behavior.

Sources: [UX outcome][ux-outcome], [UX display][ux-page], [main App][main-app], [main outcome display][main-page].

### F2 — An accepted previous-release allowance command cannot finish recovery after the wire upgrade

**Priority: P1 release blocker for the Study wire upgrade.**

A reachable sequence is: previous release accepts “Learn more tactics,” saves the allowance and receipt, loses its response, and leaves the browser's exact command pending. The new release then replays that command against the same saved database.

The trace crosses all relevant boundaries:

1. App serializes the complete Empty Study reply, including schema version 4, into `ReceiptResult::TacticsAllowance.reply`.
2. Store writes that string and the allowance increment atomically.
3. The new Store loads the receipt unchanged.
4. App's replay branch deserializes and returns the saved view unchanged. The old numeric schema header survives; the new Study version constant is not reapplied.
5. The new UI preserves the pending recovery envelope but accepts only Study schema version 5.
6. Validation fails before pending is cleared. Every Retry sends the same command and receives the same rejected historical reply.

The allowance is not duplicated. The user is stuck recovering an effect that already happened.

The real current controller was executed with the old pending command and an old-reply fixture. Both startup and Retry rejected with “Expected a Study wire view with schema_version 5”; the original submission ID and pending envelope remained unchanged. This establishes the consumer failure together with the traced server path; it is **not** an executed Rust/copied-database replay.

| Saved command family | Persisted result | Current reply behavior | Upgrade disposition |
| --- | --- | --- | --- |
| Answer, Acknowledge, GiveUp, Skip, Abandon | Typed AnswerResult | Reproject pinned issued content and attempt into current Study view | No stale-header defect found in this path; real old-DB replay still required |
| Learn more tactics | Serialized complete Empty Study reply | Return saved wire reply | Version-4 receipt rejected by version-5 UI |
| Repertoire Save | Serialized content reply | Return saved reply | Content contract deliberately remains version 4 |
| Tactic capture Save | Serialized content reply | Return saved reply | Content contract deliberately remains version 4 |

**Owner and repair:** app wire compatibility and client validation must support the historical accepted result. Normalize the recognized historical shape or explicitly support it at the consumer boundary while preserving the accepted facts and command identity. Do not reapply the allowance, invent a new submission ID, discard pending, or recompute the historical summary from today's state. Include cross-midnight replay. Acceptance against the previous-release database must clear pending only after validated success while leaving the saved allowance/day, store revision and receipt count unchanged; repeating the same accepted command must still have one durable effect.

Sources: [raw allowance write/replay][allowance], [previous raw-reply producer][old-allowance], [wire constants][wire], [Store persistence][store], [receipt loading][load-study], [new validator][validator].

### F3 — Recovery controls depend on human-facing error prose

**Priority: P2; another instance of presentation data controlling workflow.**

Both UI branches use `state.issue?.startsWith("Recovery storage")` to hide or disable controls. The controller has an explicit private `storageUnavailable` fact, but its public render state supplies only a message. Changing that message to “Browser storage is unavailable…” makes the same initial controls appear and changes the computed disabled state. The same string channel also carries the special value `"refresh"` alongside arbitrary errors.

**Owner and repair:** the controller should publish a small explicit issue/recovery kind or capabilities. Human prose remains display-only. Test that message changes do not change available actions.

The controller independently blocks unsafe mutations; no data-loss bypass was demonstrated. This is a confirmed UI contract defect, not evidence that a wording change corrupts the database. [StudyActions][actions]; [controller][controller]; [render-state contract][controller-type].

### F4 — Selected-theme admission depends on legacy provenance and DeckId spelling

**Priority: P2; supported import-path inconsistency and policy contract hardening.**

Theme selection is an intentional policy. Its input representation is the concern:

Converter → transfer provenance strings → compiled/persisted ContentItem → `memberships()` parses `tempo1:catalog-metadata:` JSON and DeckId naming → target/rank map → Queue restricts and orders new tactics.

The converter emits the structured membership entry for an installed catalog directory, but its repository/pinned-pack path emits only simpler pack attribution. The application ignores that simpler attribution for membership. The published converter was executed on identical synthetic valid pack bytes through both paths: source identity, board, moves, setup and label matched, but only the installed-directory result contained the membership JSON.

With explicit selected themes, missing, malformed or differently encoded membership can exclude an otherwise equivalent unseen tactic. Due reviews and optional practice use the broader candidate set and are unaffected by this filter. A later richer reimport does not necessarily repair it: `apply_tactic_transfer` deliberately preserves existing items byte for byte, including older metadata.

**Owner and repair:** normalize legacy membership into explicit, validated catalog policy facts at the import boundary. Keep attribution separately. Preserve the intended theme policy and existing learning. Test both supported conversion paths, existing-item reimport and intentional policy changes. A small typed record/adapter is sufficient.

No installed user dataset or private legacy asset was inspected, and no Rust end-to-end run was performed. This finding establishes the representation and converter-path asymmetry; it does not establish how many installed tactics are affected. [Converter][converter]; [membership consumer][membership]; [Queue contract][queue]; [reimport preservation][import].

### F5 — Public repertoire mutation APIs still expose inconsistent learning/identity semantics

**Priority: P2 before new editor or automation entrypoints; preexisting reset finding remains.**

Public `import_pgn/apply_catalog` can operate on a daily application. Generic repertoire semantic changes go through `publish_import`, which writes default LearningState and clears lifetime `first_introduced`. The browser's dedicated replacement command calls `DailyLearning::changed_answer`, preserving that evidence. Thus the same kind of change can affect lifetime introduction accounting differently depending on the entrypoint.

The current browser re-import route uses the dedicated safer path. The local transfer CLI is tactics-only. No current browser call into the problematic generic repertoire path was established.

Separately, the legacy Chess `RepertoirePgnParser` explicitly uses one `repertoire` string as both identity and label. A new caller treating it as a display name could create new identity on rename. The existing `compile_repertoire` interface already separates stable ID and label, and the browser uses that separation.

**Owner and repair:** narrow/reject unsupported generic daily mutations or give supported operations one explicit Learning transition. Retire or clearly narrow the ambiguous legacy parser before adding another consumer. Do not blindly replace generic merge with full replacement: omitted-route semantics differ.

Sources: [generic import][import], [browser replacement][repertoires], [legacy parser][legacy-parser], [separated compiler][compiler].

## 4. Legitimate policies and remaining questions

The audit did not treat every content-family or source branch as a defect.

| Reviewed boundary | Disposition |
| --- | --- |
| Teach acknowledgement | Explicit activity and learning transition; retain it |
| Chess ContentKind and learner color | Domain facts used for legal content interpretation |
| Queue DailyKind, introduction/frontier rules | Declared selection policy; retain the explicit distinction |
| Queue group labels | Presentation only; validation uses actual targets and membership |
| App safe exercise-name projection | Withholds tactic labels that could reveal motifs; legitimate disclosure choice as long as presence does not control workflow |
| Store legacy display-name JSON key | New Rust field keeps `serde(default, rename = "repertoire_name")`; old saved attempts remain readable |
| UX collection repertoire SQL column | Written from explicit ContentKind; a family index, not a display-name heuristic |
| Core board | Explicit mode, readOnly/lock, legal destinations and identity/revision; no hidden Study/title/source policy found |
| Learning Human/External source enum | Explicit evidence policy, not human-facing attribution |
| Reserved Chess source tokens | Validated identity encoding with a declared producer/consumer |

Two narrower items should remain visible:

- Personal-capture first-review priority uses the reserved `tempo:capture-save` provenance marker. Capture's ungraded introduction is already an explicit Learning transition. The marker affects priority only; no current metadata-editing path or demonstrated user defect was found. Give this intentional origin fact a named contract/decoder when hardening the shared metadata boundary.
- The UX collection blocks an active tactic's solution but still exposes label/provenance, potentially including its motif. This is an unresolved spoiler-policy question for an explicitly opened collection, not an established progression defect or data-integrity blocker.

The actual UI-main Core package was downloaded and inspected: version 0.2.2, blob 80909f571276e25a477fb05414f079f800e00c7a. All 16 bundled source/package files byte-match the reviewed Core main. That is artifact/source evidence, not a rendered-browser check.

## 5. Verification performed and limits

| Check | Result | What it establishes |
| --- | --- | --- |
| Main dependency-free UI suites | 22 passed, zero failed | Existing covered contracts pass despite the new findings |
| UX dependency-free UI suites | 21 passed, zero failed | Same limitation |
| Actual App control-flow harness | 42 completed scenarios | Name-dependent commands and corrected-result behavior at the consuming logic |
| Accepted result followed by failed Next | 12 cases across both branches, Test/Teach, three names | Retry sends only Next; one final fixture receipt remains |
| Old allowance reply into real controller | Startup and Retry both reject; exact pending command retained | Consumer half of historical wire incompatibility |
| Actual StudyActions pre-JSX conditions | Message wording changes available/disabled controls | Recovery-message coupling |
| Published Python converter, two paths | Equivalent synthetic content, different membership provenance | Import-path asymmetry |
| Full main UI test attempt | 22 passed; board-sounds module could not load missing chess.js | Not a complete green suite |

The dependency-free command was `node --test *.scenarios.js test/recovery.test.js test/tactic_commands.test.js`, run within each reviewed UI snapshot.

The scratch App harness executes the actual source control statements and actual controller/validator, with deterministic minimal hooks/timers and fixture HTTP. It substitutes JSX rendering, board/audio and the server. It compares the same exercise under fixed IDs/clock and records commands, fixture receipts and recovery envelopes. Thirty scenarios cover five activity/outcome combinations × three names × two branches; twelve add interrupted Next.

It is not a React render, browser journey or database durability test. React/esbuild and Rust/cargo were unavailable here. No Rust suites, actual previous-release saved-database replay, installed Mac inspection or production session test ran. No user data was changed. The absence of additional findings in the inspected paths is a scoped review result, not proof that no semantic coupling remains anywhere.

Local review evidence was captured in the audit workspace as consumer-results.json, audit_consumer.mjs, UI_AUDIT.md, contract-audit.md, FINDINGS.md and check_converter_paths.py. This report records the durable findings, source pins, relevant commands and qualification limits.

## 6. Guidance change and smallest corrective sequence

The accompanying canonical `agent-guidance/AGENTS.md` adds enforceable review blockers:

Its new opening section first requires the behavior, basis/owner, permitted
inputs, independence and lifetime to be established before implementation or
prompt authoring. It applies to existing consumers and small predicates as well
as new interfaces. Narrow decision inputs, tracing derived facts to their basis,
and explicit handling of missing facts provide the implementation discipline.
The following review and execution checks enforce that prior contract:

1. Identify the owner and explicit semantic contract for every shared Study decision based on name/title/source/content family; remove presentation proxies from the consumer.
2. Trace producer, import/reimport and alias behavior, persistence/receipt representation, wire version/validator, actual UI consumer and durable outcome/recovery.
3. Require the same completed exercise with name present, changed and omitted. Control baseline/clock/IDs and compare commands, identity/replay behavior and assessment/learning/receipt effects, allowing expected display-only differences.
4. Interrupt Next after accepted Answer/Acknowledge and prove Retry sends only Next. Separately test uncertain acceptance with the original immutable command.
5. For wire changes, replay previous actually installed release pending commands against a disposable copy of its saved database, covering typed and raw-wire receipts and pending envelopes.
6. Qualify one combined component/artifact set when feature and fix branches diverge.

These are conditional requirements for affected boundaries, not database/browser gates for unrelated cosmetic changes. The guidance preserves publication completion, proportional verification, small public interfaces and existing owners. An independent review requested two clarifications—deterministic invariance comparison and reimport/metadata retention in the trace—and both were incorporated.

Recommended order:

1. Reconcile the intended UI/app/Store source set and preserve both metadata independence and whole-attempt truthful outcomes.
2. Repair old allowance receipt compatibility and prove prior-release recovery against a database copy.
3. Replace recovery-message control flow with an explicit controller contract.
4. Normalize theme membership/origin facts and close generic repertoire mutation/identity seams before expanding editor/integration entrypoints.

These runtime fixes are findings/recommendations, not implemented changes in this documentation review. Do not label the application release qualified until the material execution gaps above are closed.

## Sources

[app-compare]: https://github.com/tempo-v2/tempo/compare/8c7c3691e919d10309a7528dd28a32fd6724b7ea...af20ea4f31721cd69f6e058d0daf48658a9b7d36
[ui-compare]: https://github.com/tempo-v2/tempo-ui/compare/349edde5ece77bba572774561c7fd3b367535618...7777eebb7f485891ec2eb3fe84ab4b12f5845c0c
[ui-boundary]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/tests/ui_boundary.mjs
[opening-tests]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/tests/contracts/opening_release.rs
[outcome-test]: https://github.com/tempo-v2/tempo-ui/blob/349edde5ece77bba572774561c7fd3b367535618/test/study_outcome.test.js
[ux-outcome]: https://github.com/tempo-v2/tempo-ui/blob/349edde5ece77bba572774561c7fd3b367535618/StudyOutcome.jsx
[ux-page]: https://github.com/tempo-v2/tempo-ui/blob/349edde5ece77bba572774561c7fd3b367535618/StudyPage.jsx
[main-app]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/App.jsx
[main-page]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/StudyPage.jsx
[allowance]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/src/application/optional_tactics.rs
[old-allowance]: https://github.com/tempo-v2/tempo/blob/8c7c3691e919d10309a7528dd28a32fd6724b7ea/src/application/optional_tactics.rs
[wire]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/src/wire.rs
[store]: https://github.com/tempo-v2/tempo-store/blob/67ee08d8de89943844e654d54e4b4d7f6808de3a/src/sqlite_store.rs
[load-study]: https://github.com/tempo-v2/tempo-store/blob/67ee08d8de89943844e654d54e4b4d7f6808de3a/src/sqlite_store/load_study.rs
[validator]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/validate_study_view.js
[actions]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/StudyActions.jsx
[controller]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/study_controller.js
[controller-type]: https://github.com/tempo-v2/tempo-ui/blob/7777eebb7f485891ec2eb3fe84ab4b12f5845c0c/study_controller.d.ts
[converter]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/tools/tactics/convert.py
[membership]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/src/application/tactic_preferences.rs
[queue]: https://github.com/tempo-v2/tempo-queue/blob/8ad7feda5c56982ee0411ef44309f69bb360d783/src/daily.rs
[import]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/src/application/import_pgn.rs
[repertoires]: https://github.com/tempo-v2/tempo/blob/af20ea4f31721cd69f6e058d0daf48658a9b7d36/src/application/repertoires.rs
[legacy-parser]: https://github.com/tempo-v2/tempo-chess/blob/406a573c2145c7b9408a543266171e33e6793f9d/src/repertoire_pgn_parser.rs
[compiler]: https://github.com/tempo-v2/tempo-chess/blob/406a573c2145c7b9408a543266171e33e6793f9d/src/compile_repertoire.rs
[baseline-guidance]: https://github.com/tempo-v2/.planning/blob/324c101a40719af6ff341c937d1d5a587d1efdae/agent-guidance/AGENTS.md
[baseline-readme]: https://github.com/tempo-v2/.planning/blob/324c101a40719af6ff341c937d1d5a587d1efdae/README.md
[baseline-interfaces]: https://github.com/tempo-v2/.planning/blob/324c101a40719af6ff341c937d1d5a587d1efdae/INTERFACES.md
[baseline-behavior]: https://github.com/tempo-v2/.planning/blob/324c101a40719af6ff341c937d1d5a587d1efdae/BEHAVIOR.md
[baseline-reading]: https://github.com/tempo-v2/.planning/blob/324c101a40719af6ff341c937d1d5a587d1efdae/READING_GUIDE.md
