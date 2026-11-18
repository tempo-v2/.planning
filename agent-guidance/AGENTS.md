# AGENTS.md — Tempo 2 working instructions

## Purpose

Tempo 2 is a small application for one active user. Make the requested feature work, keep the code understandable, and publish the result so the next person or agent can continue from it.

Prefer the simplest implementation that satisfies the actual requirement. Preserve the existing component boundaries and learning data. Do not turn a small feature into an architecture project.

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

Use the latest agreed implementation as the base. Reference SHAs in an old prompt are comparison evidence, not instructions to reset or downgrade newer code. A default branch is not automatically the active integration baseline.

Preserve unrelated and in-progress changes. Do not reset, stash, delete, overwrite or stage another worker's files simply to make the checkout clean. Use a task branch/worktree and explicit file ownership where needed. Separate development/test outputs from artifacts served by the running installation.

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

Before adding an interface, state:

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

Measure a suspected interactive bottleneck before redesigning it. Prefer bounded reads and indexed operations; avoid whole-history validation or full-catalog polling on every move. Do not add a cache or service just because it might be faster.

## 8. Keep coordination and review proportional

Use one implementation owner by default. Parallel workers need disjoint files/worktrees and explicit integration ownership. Do not create a hierarchy of managers for a small feature.

Use a focused independent Guardian-like review for significant changes. Its job is to catch ownership drift, duplicated rules and real correctness risks. It is not a paperwork gate or an instruction to expand scope.

Keep one existing run ledger current. Handoffs should identify the actual source, changed behavior, checks, publication evidence and first unfinished step.

## 9. Final report

State what changed and why, what meaningful checks passed, what limitations remain, and the publication evidence required by section 1. Report installation only when it was actually performed and observed.

For a PR, explain the user-visible problem, the change and resulting behavior. Link companion PRs when needed. Leave the repository and handoff understandable enough that another agent does not have to reconstruct the work.

