# Tempo 2 planning

Cross-repository contracts, decisions, and setup for independent Git source
trees. Seven Rust packages compose one application; the UI and reusable Core
packages are separate.

## Start here

Read the canonical agent guidance, current state and exact assembly manifest, then open the selected restart task.
Identify the accepted behavior and selected runtime before choosing implementation
inputs. A dependency diagram establishes allowed imports; it does not authorize
a consumer to invent policy from an available field.

| Document | Purpose |
| --- | --- |
| [agent-guidance/AGENTS.md](agent-guidance/AGENTS.md) | Current working instructions, including behavior authority before implementation |
| [plans/usable-release/STATE.md](plans/usable-release/STATE.md) and [WORKSPACE.md](plans/usable-release/WORKSPACE.md) | Current source and installation identities, release gates and setup |
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

Use the affected component README. Each component README maps a
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

Run the current assembly verifier before qualifying a review build. The live
boundary check uses managed HTTP with disposable SQLite. The original
scaffold qualification belongs to its historical source profile. The current
release gate is being assembled under T54; see the [current state](plans/usable-release/STATE.md)
for open gates and links to prior evidence.
