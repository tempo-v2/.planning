# Interface scaffold verification

Prepared and checked 2026-11-17. These results describe the source in this
cross-repository change, not a release installed on Andy's machine.

## Verified starting GitHub state

| Repository | Inspected `main` commit | Finding |
| --- | --- | --- |
| `.planning` | `9e1303a8916ec8a63a17e0f404654a6c67f3adab` | Architecture and behavior documents present; README still initial; bootstrap absent |
| `tempo-types` | `6b1a19946ecc42bfea587d3161b1911c1cf99d2f` | Cargo manifest, initial library and ignore file pushed |
| `tempo-study` | `44575875bbe773cbcd5613c5b6685f072c1d1802` | Same scaffold structure |
| `tempo-queue` | `3718e15d5aa05e37f614f42a9cd903d3737eb59c` | Same scaffold structure |
| `tempo-learning` | `5db4dea94818a231cd1c36fd8610a4b9bb0a344b` | Same scaffold structure |
| `tempo-chess` | `3a64b09db5924b6f55daf59232828b0e766eecf2` | Same scaffold structure |
| `tempo-store` | `c93c288edb841855ff39908d8d86ab62f37e6a8e` | Same scaffold structure |
| `tempo` | `3e3eae94da597db55d270b494b141a2044c4659a` | Cargo manifest and initial application binary pushed |
| `tempo-core-components` | `705e79f14693e0d3d5cb9421f48e11b30b66dfff` | README and license only, as expected from bootstrap |

Each full tree was checked and cloned at that commit. No AGENTS.md files were
present. The initial ownership/behavior documents match the reviewed baseline.

## Executed evidence

Toolchain: Rust/Cargo 1.85.0, Node 24.22.1, Python 3.12.14 (the
Python scripts are also syntax-checked against the Python 3.9 grammar).

| Check | Result |
| --- | --- |
| Workspace compilation | Passed |
| Rust formatting and strict Clippy, all workspace targets | Passed |
| Study | 3 tests passed, including non-chess grading |
| Chess | 7 tests passed, including semantic changes and tactic conflicts |
| Queue | 6 tests passed, including malicious ordering/group output |
| Learning | 9 tests passed, including stale positives and scheduler memory |
| Store | 8 tests passed, including rollback, source/receipt coherence and dataset reuse |
| Application integration | 15 tests passed through the actual application path |
| UI component/controller | 10 tests passed |
| Actual Rust process ↔ UI controller | 3 tests passed, including lost reply and invalid command |
| Dependency/source boundary gate | Passed against resolved Cargo metadata |
| Architecture negative checks | 4 tests passed |
| Workspace configuration migration | 4 tests passed |
| Executable demonstration | Repertoire, multi-decision tactic miss/correction, fresh repeat, empty queue |

The 48 Rust tests, 13 Node tests and 8 focused Python checks total 69 tests.
The gate and build/lint checks are additional. Test commands are collected in
`scripts/qualify_scaffold.py`; component checks can run independently.

## Review corrections included

Independent review found and closed the following interface issues before this
handoff: scheduler state/settings must persist behind a versioned contract;
feedback must carry the compared content version; game network I/O must occur
outside the Study-owning object; ordering validation must enforce grouping as
well as set membership; Store must verify learning/assessment/receipt coherence
and retain used identities for empty datasets.

## Limits

- Memory transactions are tested. SQLite constraints, disk persistence, migrations
  and crash/restart recovery are not implemented or qualified.
- PGN parsing, canonicalization, comparison, intervals and order use declared
  fixtures. The multi-decision fixture demonstrates the protocol; it is not an
  authored tactical puzzle. No chess engine or FSRS implementation is claimed.
- UI serialization/controller/render output is checked. A graphical board,
  browser event binding and production HTTP deployment are not implemented.
- Snapshot interchange currently uses JSON, not enriched PGN. New non-chess
  product families will extend concrete App/Store/UI models; generic Study is
  already demonstrated separately.
- The consistent Store snapshot currently contains the full dataset and history.
  Efficient bounded reads at larger scale remain a possible API evolution.
- Packages are unpublished development versions; local root patches select the
  intended sources. No independent release/package-consumption qualification is
  implied.

GitHub branch creation from the connected integration returned HTTP 403
(`Resource not accessible by integration`); shell Git has no push credential.
The source is therefore delivered as checked changes against the commits above.
Running the delivery helper can apply, qualify, commit and push feature branches
using the user's normal Git configuration. It never merges main.
