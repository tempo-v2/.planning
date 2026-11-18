# AGENTS.md — Tempo 2 working instructions

## Purpose

Tempo 2 is a small application for one active user. Make the requested feature work, keep the code understandable, and publish the result so the next person or agent can continue from it.

Prefer the simplest implementation that satisfies the actual requirement. Preserve the existing component boundaries and learning data. Do not turn a small feature into an architecture project.

## 0. Establish behavior before choosing its implementation

Before adding or changing a decision that affects commands, workflow, eligibility, priority, authorization, identity, learning, persistence, recovery, or a claim that an outcome was accepted, state the intended rule before choosing its predicate. This applies to small conditions, defaults and adapters inside existing code as well as new interfaces. Being the implementation owner does not authorize inventing the product rule.

Use a few lines or a small table in the existing task/PR; group related decisions rather than documenting every branch:

| Question | Required answer |
| --- | --- |
| Behavior | What observable operation, transition or durable effect is intended? |
| Basis and owner | Which current requirement or accepted contract establishes it, for which runtime/profile/release, and which component owns the decision? |
| Inputs | Which declared semantic facts may determine it, and who establishes those facts? |
| Independence | What nearby presentation, representation or context may change without changing that decision? |
| Lifetime | Can any input, result or pending command survive import, caching, persistence, restart or a release change; who must still interpret it? |

Existing code, fixtures and examples show what was built; they are not sufficient authority that every observed distinction is intended. A positive example does not establish an exclusive category: “a clean tactic continues” does not establish “only tactics continue.” Preserve user data and accepted semantics. Establish the basis of an undocumented distinction touched by the task before carrying it forward.

Apply the same discipline when writing implementation prompts, acceptance criteria or handoffs. State the semantic rule and label illustrative examples; do not turn an example or existing quirk into a new requirement for the next agent.

Treat data according to its declared role in the decision. Display text, stable identity, policy inputs, authoritative results and delivery state can coexist in one response without becoming interchangeable. Do not derive policy from correlations, names, optional-field presence, message wording, identifier spelling or incidental representation unless that derivation is itself an explicit owned contract. Missing or unknown data has the outcome declared by that contract; it must not silently select a different activity, identity, permission or mutation.

Give decision code only the semantic inputs it needs. Prefer a small function or value in the existing owner over passing an unrestricted view/content/storage object. If a required fact or operation is missing, complete the smallest contract at its owner before implementing the consumer. Trace any derived value to its basis: adding an enum, capability, adapter or shared helper does not fix an unjustified inference in its producer. Do not duplicate an owner's transition by constructing convenient default state in a caller.

Before implementation, identify both a semantic change that should alter the result and an irrelevant change that must not. Derive expected observations from the stated rule, then exercise the actual consumer. Tests that repeat the chosen predicate or only preserve correlated fixtures cannot establish the rule.

Use task intent and current accepted contracts to resolve ordinary reversible implementation choices autonomously. Layout, styling, local mechanics and code organization need no separate approval when their semantic effects are unchanged. When a material policy choice is unresolved, identify it explicitly and continue independent work; ask a focused question only if competing interpretations materially change intent and cannot be resolved from the authorized scope. Do not fill the gap with a hidden fallback.

These rules apply across Tempo. The Study-specific examples and checks below illustrate them; they are not an exhaustive list of forbidden shortcuts.

## 1. Completion includes publication

For any task that changes repository code, tests or documentation, do not report completion until the intended changes are committed and one of these outcomes is verified:

1. **Feature branch:** the branch is pushed and a pull request is open against the correct integration branch. An existing open PR for that branch may be updated. Its head must contain the intended commits. You must verify the PR contains the intended changes before reporting completion.
2. **Main:** when direct-main work or merging is authorized and consistent with the repository workflow, the intended result is pushed to main and the remote commit is verified.

The usual path is a feature branch and PR. This rule does not instruct you to bypass protection, force-push shared history, merge an unreviewed change, or choose an older main branch as the base.

A local commit, a passing test suite, a pushed branch without its required PR, or an unverified push does not meet this completion rule. In a multi-repository change, publish every changed repository and link the corresponding PRs/commits. Record the compatible component versions needed to build the result.

Verify publication by reading back the remote branch/PR or main reference. Report the actual commit IDs and PR URLs. Keep **implemented**, **tested**, **published**, **merged**, and **installed** as separate statuses.

If access, an approval restriction or another genuine blocker prevents publication, preserve the work and report **blocked — unpublished**, the specific cause, and the exact remaining step. Do not silently call the task complete. Continue all other authorized work first, and do not request authorization already provided in the session.

For a read-only review or a proven no-change result, deliver the findings/evidence without manufacturing a code change or empty PR. If the task requests a repository report, publish that report under the same rule.

## 2. Start from the actual current work

Read applicable repository instructions and the current release/run ledger. Inspect the current branch, recent relevant commits, worktree status and local changes before editing.

Read the tracked canonical guidance for each task: `.planning/agent-guidance/AGENTS.md` from the assembled workspace, or `agent-guidance/AGENTS.md` inside this planning repository. An older copied root file does not replace it; retain applicable local additions.

Establish the active contract and its scope before using a historical example or current implementation as a specification. Explicit current user decisions and accepted contracts for the selected runtime govern behavior. Source pins and tests establish implementation/evidence; scaffold documents and earlier prompts may describe another profile or a superseded policy. Resolve a conflict explicitly rather than selecting the most convenient source or treating the newest filename as authority.

Use the latest agreed implementation as the base. Reference SHAs in an old prompt are comparison evidence, not instructions to reset or downgrade newer code. A default branch is not automatically the active integration baseline.

Preserve unrelated and in-progress changes. Do not reset, stash, delete, overwrite or stage another worker's files simply to make the checkout clean. Use a task branch/worktree and explicit file ownership where needed. Separate development/test outputs from artifacts served by the managed installation. Use the guarded development entry points for local startup and build. Installed lifecycle authority comes from the managed registration and explicit release operation, including while the service is stopped.

Reconcile reported new work once, narrow the remaining task, and proceed. Do not repeat repository-wide discovery after every small change.

## 3. Keep responsibilities in their existing components

| Component | Owns | Must not own |
| --- | --- | --- |
| Core Components | Reusable board, controls, layout and local input behavior | Study workflow, HTTP, persistence, grading or scheduling |
| Tempo UI | Pages, presentation state, preferences, shortcuts, sound, transport and exact-command recovery | Eligibility, chess grading, FSRS or database access |
| Tempo application | Commands, public replies, coordination, safe projections and transaction orchestration | A second implementation of domain rules |
| Chess | Legal moves, positions, notation, PGN/content interpretation and chess grading | Queue policy, database connections or browser state |
| Study | Generic attempt progression and sticky whole-attempt assessment | Chess-specific rules, scheduling or storage |
| Learning | Learning transitions, teaching policy and scheduler adapter | UI behavior or queue presentation order |
| Queue | Selection, eligibility projection, ordering and deferral | Chess/FSRS implementations or durable transaction execution |
| Store | Bounded reads, atomic writes, constraints and receipts | Deciding what an answer means or how to schedule it |
| Types | Small stable shared identifiers and values | A universal framework or collection of every component's internals |
| Planning | Shared contracts, source/artifact handoff and one useful ledger | Another execution or runtime subsystem |

Use public interfaces between components. Do not reach into another component's private modules or database tables. Domain logic receives values; it does not fetch data through Store/HTTP/browser handles.

Consume Core through its built, versioned package in the normal app. Source-tree aliases are not a substitute for qualifying the package boundary.

## 4. Design small, explicit interfaces

Apply section 0 before changing behavior through any interface, including an existing one. When defining or changing its contract, state:

- Who calls it and who owns the decision?
- What exact inputs are required?
- What result is returned, including empty, invalid and failed outcomes?
- What state can it change?
- Which identity/version/time facts make the operation valid?
- What happens when a write is delivered again?

Then choose the smallest concrete type/function/trait that expresses that contract. Reuse an existing operation when it has the same meaning. Keep reads separate from commands with side effects.

Use named values instead of ambiguous Boolean switches or loosely structured dictionaries at public boundaries. Add short producer/consumer and “when to use this” explanations where they help. Prefer files named for one concept or operation, with focused examples next to public Rust types/functions.

An interface is not complete because it compiles. Exercise it through its real consumer. Test the external behavior and important failure cases, rather than duplicating the implementation in a test.

Keep persisted identity, uniqueness and reference integrity in Store's real primary-key, unique and foreign-key constraints, rather than relying on UI conventions alone.

Do not introduce a generic event bus, service locator, universal repository abstraction, plugin framework, large configuration language, alternate scheduler or duplicate controller for a hypothetical future feature. Add abstraction when a concrete current need justifies it.

Keep one authoritative production path for each responsibility. When replacing a path, remove or explicitly retire the old path instead of leaving two competing implementations active. Keep test/demo adapters clearly outside normal runtime composition; do not use them as silent production fallbacks.

### Review blocker: presentation data must not become policy

Block a change when shared Study code chooses behavior from a title, name, display label, source/provenance string, content family, identifier spelling, or the presence/absence of optional display data until the author identifies the decision's owner and the explicit contract that carries it. An ownership explanation is not enough if the implementation still uses a display field as a proxy: change the consumer to use the semantic contract.

`exercise_name` has one job: display. Giving the same exercise a name, renaming it or omitting that name must not change its commands, grading, scheduling, allowance accounting, acknowledgement, continuation or recovery. Do not infer “tactic” from an absent repertoire name. Do not rename such a proxy and leave the policy implicit.

Study workflow uses the declared activity mode, completion state, authoritative whole-attempt assessment and move feedback as appropriate. Teach acknowledgement follows the Teach contract. A correct final move is not proof of a clean attempt: earlier misses remain part of the saved outcome. A UI success cue or automatic continuation must respect that distinction.

Content-specific behavior can be legitimate in its owning component: for example, Chess interprets repertoire content, and Queue can apply an explicitly declared admission policy. Keep that distinction in typed, validated facts with a documented producer and consumer. Human-facing provenance and identifier conventions must not quietly substitute for eligibility, priority or learning facts. Prefer a small adapter or value type over a new framework.

The same rule applies to errors. Carry recovery capabilities and issue kinds explicitly from their owner; do not enable, disable or route actions by matching human-facing message text. Browser recovery belongs to its UI controller, so this rule does not imply moving every interaction decision to the server.

### Trace the decision through the actual consumer

For changes at a shared workflow or metadata/policy boundary, follow the value and the decision through:

1. The producer and any import/normalization adapter, including reimport, alias merging and metadata-preservation behavior.
2. The persisted record, schema/defaults and receipt representation.
3. The wire response, version and client validator.
4. The actual consumer: render conditions, selectors, timers, keyboard actions and emitted commands.
5. The accepted durable outcome and retry/restart behavior.

Reviewing a shared grader or a package dependency graph does not cover downstream policy. Search old field names, aliases, nullable fields, message comparisons and ID/provenance parsing as well as the new type. Identify each branch that can change behavior, its owner and its semantic input. If two exercises share an activity contract, a content-family difference in their flow needs an explicit product/domain rule.

Keep this evidence short and concrete in the PR: decision/owner/contract, producer → storage → wire → consumer, and the relevant verification results. Missing ownership or an implicit policy input blocks approval; documentation alone does not cure an implementation violation.

## 5. Preserve the current learning and content contracts

Keep Teach, scheduled Test and Practice distinct. Teaching acknowledgement is not a successful recall grade. A tactic has one whole-puzzle result; a correction does not turn an earlier miss into a clean result. Practice leaves scheduling and introduction allowances unchanged.

Keep existing content/learning identity, version checks, quota accounting and the configured study calendar. Current policy comes from the current accepted contract, not a retired example. Do not restore old mandatory same-day repeats or forced-tomorrow review rules as incidental cleanup.

The UI renders authoritative outcomes and selection facts. It must not reconstruct the scheduler or count displayed cards as accepted introductions. A changing opening frontier is not a fixed session total.

Preserve the current dataset, imported content and learning accumulated since delivery. Old permission to discard Tempo 1 history is not permission to reset Tempo 2.

## 6. Make retries and presentation truthful

Separate an accepted result from loading the next activity. If a result was saved but Next fails, show the saved result and retry Next. If acceptance is uncertain, retry the original immutable command rather than issuing a new grading operation.

Preserve dataset, target, content-version, attempt and revision checks. Changes to wire responses must account for saved receipts and pending commands; do not break them by adding mandatory fields without compatibility.

Treat history, preferences, summaries and catalog browsing as reads/presentation unless an explicit command says otherwise. They must not silently grade, skip, introduce or reschedule.

Never send a hidden answer key to a blind-test client and rely on CSS to conceal it. Expose only the context and moves authorized at that stage. Use the issued content version when explaining or replaying an attempt.

Cancel stale input, promotion choices and timers when their owning activity changes. Keep board viewing state separate from the authoritative attempt.

## 7. Verify according to the change

Run the smallest meaningful checks that cover changed behavior and concrete risks.

- Pure component/appearance work uses component checks.
- Interaction changes get a focused browser journey where needed.
- Public interface changes get consumer/contract checks.
- Persistence changes get the affected transaction, constraint or migration checks.
- A changed Core package is checked as an installed artifact in its consumer.

Do not require database/lifecycle suites for unrelated UI changes. Do not repeat broad tests when unchanged source and dependencies already have valid evidence. Record what was reused and why. Do not declare live runtime behavior verified from source alone.

Use disposable data for synthetic grades, clock changes, failure injection and destructive content cases. Use the supported lifecycle for an authorized installation and verify the running artifact combination separately.

### Required checks for affected Study and wire boundaries

These checks apply when a change affects the boundary described in section 4, including removal of an accidental dependency. They are not a blanket requirement for unrelated appearance work.

- **Metadata invariance:** run the same completed exercise with its display name present, changed and omitted through the actual consumer. Clone the same baseline and control clock/ID allocation so comparisons are meaningful. Compare the ordered command sequence, identity/replay behavior and durable assessment, learning and receipt effects; they must match, allowing the expected display-only metadata differences. Use relevant activity and assessment cases, including clean completion, completion after a miss, and Teach acknowledgement. Hold semantic inputs fixed. Do not test a copied predicate instead of the consumer or assume a validator test proves UI behavior.
- **Accepted answer, interrupted Next:** save the answer, interrupt/fail Next, then Retry. Verify that Retry sends only Next, preserves the saved result, and does not send another Answer/Acknowledge or create another grade. Separately, when acceptance is uncertain, verify replay of the original immutable command and identity before continuation.
- **Previous-release recovery:** for a wire change, replay pending commands from the previous actually installed release against a disposable copy of its saved database. Cover accepted commands whose response was lost as well as unaccepted pending commands. Inventory typed receipts that are reprojected, serialized wire replies that are returned verbatim, and client recovery envelopes; test each affected representation. Verify the original command identity, one durable effect, a client-accepted response and successful recovery. A current-version restart test or a compatible field alias does not establish this.
- **Compatible candidate:** when fixes and feature work have diverged, qualify the combined intended candidate and record its component/artifact versions. Do not count a fix tested on an older main branch as qualification of the newer UX release, or drop another branch's correctness checks while integrating it.

Use the smallest representative set that covers the affected contracts, and reuse unchanged evidence where justified. A fixture transport can establish a consumer decision or rejection; it cannot establish a real saved-database replay. State that limit. If a required material check cannot run, report the specific unverified behavior and do not claim that runtime change is ready to release. A documentation-only change can be published with those runtime limits clearly recorded.

Measure a suspected interactive bottleneck before redesigning it. Prefer bounded reads and indexed operations; avoid whole-history validation or full-catalog polling on every move. Do not add a cache or service just because it might be faster.

## 8. Keep coordination and review proportional

Use one implementation owner by default. Parallel workers need disjoint files/worktrees and explicit integration ownership. Do not create a hierarchy of managers for a small feature.

Use a focused independent Guardian-like review for significant changes. Start with the behavior/basis/owner/input decision from section 0 while the design is still small; then inspect implementation and evidence. Its job is to catch invented policy, ownership drift, duplicated rules and real correctness risks. For the boundaries in sections 4 and 7, the reviewer must inspect the actual consuming path and run the required focused checks; the author reporting a shared-grader test is not sufficient. It is not a paperwork gate or an instruction to expand scope.

Keep one existing run ledger current. Handoffs should identify the actual source, changed behavior, checks, publication evidence and first unfinished step.

## 9. Final report

State what changed and why, what meaningful checks passed, what limitations remain, and the publication evidence required by section 1. Report installation only when it was actually performed and observed.

For a PR, explain the user-visible problem, the change and resulting behavior. Link companion PRs when needed. Leave the repository and handoff understandable enough that another agent does not have to reconstruct the work.
