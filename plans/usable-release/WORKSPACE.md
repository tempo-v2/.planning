# Tempo workspace and development

Use the matching Tempo and UI tooling in an assembled workspace. The
root Makefile includes `tempo/tools/local.mk`. With the single-service
launcher from [Tempo #17](https://github.com/tempo-v2/tempo/pull/17),
`make start` builds the checkout and restarts the registered Mac service
on its existing database and port. It closes verified development copies.
`make start-dev` defaults to port 41823 and
`.local/development/study.sqlite`. For a separate existing development
database, use `make start-dev TEMPO_DB=PATH`.
Create a new explicit development file with `make init-dev TEMPO_DB=PATH`.
`make build-ui` checks the output before installing packages or building.
See [Mac operating instructions](https://github.com/tempo-v2/tempo/blob/main/OPENING.md)
for development and the explicit installed lifecycle.

## Assemble the current review candidate

From an empty workspace with this Planning checkout at `.planning`, run
`python3 -B .planning/scripts/current_workspace.py .`. Its
[manifest](current-assembly.json) records the exact review revisions and
separately identifies the installed baseline. The same program's `--verify`
mode checks those revisions, the locks, packaged Core and canonical guidance
without changing the workspace. Use that check before combined qualification.

Pass `--source COMPONENT=PATH` for each local Git object store. The assembler
checks for the pinned commit even if the source checkout has a different HEAD
or local edits. It fetches from GitHub only when the exact commit is absent from
all supplied stores. Add `--offline` to report missing pins without a network
request. Rerun with additional sources to resume. Already assembled components
must still match their pins and be clean.

Historical assembly and recovery instructions are available in the [prior workspace instructions](https://github.com/tempo-v2/.planning/blob/f71f80fa7c168993a8d5979be10102bc70fd64ae/plans/usable-release/WORKSPACE.md) and the [prior release ledger](https://github.com/tempo-v2/.planning/blob/f71f80fa7c168993a8d5979be10102bc70fd64ae/plans/usable-release/STATE.md).
