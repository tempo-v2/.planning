# Tempo 2 planning

Cross-repository contracts, decisions, and setup for independent Git source
trees. Seven Rust packages compose one application; the UI and reusable Core
packages are separate.

## Start here

Start with the canonical agent guidance and the current release/workspace ledger.
Identify the accepted behavior and selected runtime before choosing implementation
inputs. A dependency diagram establishes allowed imports; it does not authorize
a consumer to invent policy from an available field.

| Document | Purpose |
| --- | --- |
| [agent-guidance/AGENTS.md](agent-guidance/AGENTS.md) | Current working instructions, including behavior authority before implementation |
| [plans/usable-release/STATE.md](plans/usable-release/STATE.md) and [WORKSPACE.md](plans/usable-release/WORKSPACE.md) | Release history, source/artifact handoff and scope to reconcile with the current task |
| [READING_GUIDE.md](READING_GUIDE.md) | Scaffold-era concept map; use current component paths and scope |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Ownership and allowed dependency graph |
| [INTERFACES.md](INTERFACES.md) | Production interface and ownership map, followed by retained scaffold history |
| [BEHAVIOR.md](BEHAVIOR.md) | Historical scaffold expectations B01–B15; some learning policies were superseded |
| [contracts/dependencies.json](contracts/dependencies.json) | Machine-readable dependency rules |
| [VERIFICATION.md](VERIFICATION.md) | Source baseline, executed checks and remaining limits |

## Workspace setup

Use the current review pins in
[the assembly manifest](plans/usable-release/current-assembly.json). Clone
Planning into `.planning` in a new workspace, then from its parent run:

```sh
python3 -B .planning/scripts/current_workspace.py .
python3 -B .planning/scripts/current_workspace.py . --verify
```

This assembles exact published revisions and verifies the Cargo lock, UI lock,
Core package and canonical guidance. It preserves existing workspaces. A
different or dirty checkout fails verification. The Planning checkout used to
assemble is reported as part of the result. For Git over SSH add
`--protocol ssh`.

Build the verified review workspace with `cargo build --locked -p tempo` and
`make build-ui`. Use a disposable database and development port for checks.
Managed installation is a separate release operation. The older bootstrap and
scaffold checks are historical tools for reconstructing their own profile.


## Reading and contributing

Begin with [READING_GUIDE.md](READING_GUIDE.md). Each component README maps a
question or public concept to a source file and a runnable example. Rust files
start with purpose/when-to-use documentation and keep usage scenarios in their
own `#[cfg(test)]` module. Public root imports remain convenient; implementation
files are named for the concepts they explain.

## Development checks

Use `cargo test -p tempo-study` (or the affected package) for isolated component
work. `cargo doc --workspace --no-deps --open` builds the API reading surface. UI checks run with `node --test` from `tempo-core-components`; they need no
Rust process or database. `cargo test -p tempo --test contracts` checks application
composition. `node --test tempo/tests/ui_boundary.mjs` checks the real Rust/UI
protocol after building `tempo`.

The full qualification script is for the initial cross-repository contract and
changes spanning its boundaries. It checks the dependency graph, negative
architecture cases, workspace migration, Rust contracts/lints and warning-free documentation, UI behavior, and
the actual stdio round trip. It does not qualify real PGN parsing, FSRS, SQLite
constraints/durability, or browser rendering.

The demo is process-local and uses known chess fixtures. Its JSON-line transport
can also be inspected with `cargo run -p tempo -- stdio`. The normal next/answer
path has no game-provider dependency.
