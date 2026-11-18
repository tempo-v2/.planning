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

The instructions below reproduce historical source pins in isolated
directories. Keep their database and build outputs separate and use current
tooling for development startup. In these older trees, `make start`
can displace installed Tempo.

## Reconstruct checkpoint 04

The [manifest](manifest.json) pins the component commits, toolchain, Core tarball and original installed artifact hashes. The [ledger](STATE.md) records which evidence applies to checkpoint 04.

Use an empty directory. Keep any existing workspace and its database in place. This example uses Git, Python 3, Make, Rust 1.98.1 and Node 26.12.0 as recorded in the manifest.

```sh
git clone --branch feat/installed-release-handoff https://github.com/tempo-v2/.planning.git .planning
python3 - <<'PY'
from pathlib import Path
import json
import shutil
import subprocess

planning = Path(".planning")
release = planning / "plans" / "usable-release"
with (release / "manifest.json").open() as source:
    checkpoint = json.load(source)["04"]
for repo, revision in checkpoint["repositories"].items():
    if repo == ".planning":
        continue
    branch = "feat/readable-modules" if repo == "tempo-types" else "feat/consolidated-release"
    subprocess.run(["git", "clone", "--no-checkout", "--single-branch", "--branch", branch,
                    f"https://github.com/tempo-v2/{repo}.git", repo], check=True)
    subprocess.run(["git", "-C", repo, "checkout", "--detach", revision], check=True)
shutil.copyfile(planning / "workspace.template.toml", "Cargo.toml")
shutil.copyfile(release / "workspace-04.Cargo.lock", "Cargo.lock")
guidance = planning / "agent-guidance" / "AGENTS.md"
if guidance.exists() and not Path("AGENTS.md").exists():
    shutil.copyfile(guidance, "AGENTS.md")
Path("Makefile").write_text("include tempo/tools/local.mk\n")
PY
```

The checked-in UI lock consumes the Core tarball bundled in `tempo-ui/vendor`. It needs no sibling source override. These are the commands for producing the optimized binary and UI used for the release.

```sh
cargo build --release --locked -p tempo
make build-ui
```

The original binary and served web hashes identify the recorded Mac
installation. A build from a different checkout path or host can have
different native binary bytes.

See the [Mac operations and recovery instructions](https://github.com/tempo-v2/tempo/blob/cf94c79cc69820e1819ad32a4112a20b452ca1d6/OPENING.md).

## Reconstruct the November 18 main candidate

Use an empty directory with the Rust and Node versions recorded for
`main-candidate-2026-11-18` in the manifest. This candidate uses the same
workspace Cargo lock as checkpoint 04 and consumes the Core 0.2.2 tarball from
the UI repository.

```sh
git clone https://github.com/tempo-v2/.planning.git .planning
git -C .planning fetch origin refs/pull/4/head
git -C .planning checkout --detach FETCH_HEAD
python3 - <<'PY'
from pathlib import Path
import json
import shutil
import subprocess

planning = Path(".planning")
release = planning / "plans" / "usable-release"
candidate = json.loads((release / "manifest.json").read_text())["main-candidate-2026-11-18"]
for repo, revision in candidate["repositories"].items():
    url = f"https://github.com/tempo-v2/{repo}.git"
    subprocess.run(["git", "clone", "--no-checkout", url, repo], check=True)
    pull = candidate["pull_requests"][repo]
    subprocess.run(["git", "-C", repo, "fetch", "origin", f"refs/pull/{pull}/head"], check=True)
    subprocess.run(["git", "-C", repo, "checkout", "--detach", revision], check=True)
shutil.copyfile(planning / "workspace.template.toml", "Cargo.toml")
shutil.copyfile(planning / candidate["workspace_lock"]["path"], "Cargo.lock")
Path("Makefile").write_text("include tempo/tools/local.mk\n")
PY
cargo build --locked -p tempo
make build-ui
```

## Build the shared Study candidate

Use a separate assembled workspace with the revisions in the [shared Study
ledger](STATE.md#shared-study-decision-contracts-november-18-2026). For each
changed component, clone its repository and fetch its linked PR head using
`git fetch origin refs/pull/PR_NUMBER/head`. Check out the listed commit. For
reused components, check out the listed main commit.

Use the workspace template, Cargo lock and Core package described above.
Run `cargo build --release --locked -p tempo` and, in the UI repository, run
`npm ci` and `npm run build`. For local qualification, serve that UI build with
the matching binary and a disposable SQLite database.
