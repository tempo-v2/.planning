# Tempo 2 planning

Contracts, decisions, and release evidence for Tempo. The current Lean runtime
builds from the Tempo repository with its UI and packaged Core.

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

Use the [assembly manifest](plans/usable-release/current-assembly.json) to
identify the Lean candidate and installed release, and
[workspace instructions](plans/usable-release/WORKSPACE.md) to build or
reconstruct the selected profile. Use disposable data and a separate port
for development. Managed installation is a separate release operation.

## Reading and contributing

Begin with [READING_GUIDE.md](READING_GUIDE.md). Each component README maps a
question or public concept to a source file and a runnable example. Rust files
start with purpose/when-to-use documentation and keep usage scenarios in their
own `#[cfg(test)]` module. Public root imports remain convenient; implementation
files are named for the concepts they explain.

## Development checks

For Lean, run `cargo test --locked`, `cargo clippy --locked --all-targets -- -D warnings`,
and `npm --prefix ui run build` inside the Tempo checkout. The
[release ledger](plans/usable-release/STATE.md) records the applicable
browser, migration and artifact checks. Historical components and checks
are described in the workspace instructions.
