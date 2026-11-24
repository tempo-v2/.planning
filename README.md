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
| [Lean operation contract](plans/usable-release/lean-operation-contract.md) | Current runtime ownership, operation behavior and work limits |
| [READING_GUIDE.md](READING_GUIDE.md) | Scaffold-era concept map; use current component paths and scope |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Predecessor ownership and dependency graph |
| [INTERFACES.md](INTERFACES.md) | Predecessor interface and ownership map, followed by retained scaffold history |
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

For Lean, start with the [operation contract](plans/usable-release/lean-operation-contract.md)
and the README at the pinned Tempo revision. The
[reading guide](READING_GUIDE.md) maps the older multi-repository components.

## Development checks

For Lean, run `cargo test --locked`, `cargo clippy --locked --all-targets -- -D warnings`,
and `npm --prefix ui run build` inside the Tempo checkout. The
[release ledger](plans/usable-release/STATE.md) records the applicable
browser, migration and artifact checks. Historical components and checks
are described in the workspace instructions.
