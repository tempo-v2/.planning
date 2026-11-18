# Reconstruct checkpoint 04

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
Path("Makefile").write_text("include tempo/tools/local.mk\n")
PY
```

The checked-in UI lock consumes the Core tarball bundled in `tempo-ui/vendor`. It needs no sibling source override. These are the commands for producing the optimized binary and UI used for the release.

```sh
cargo build --release --locked -p tempo
make build-ui
```

For a foreground instance, run `make start`. In a fresh workspace this creates a new local database if no default file exists. To continue studying with an existing database, supply its actual path with `make start TEMPO_DB=/path/to/study.sqlite`. The original binary and served web hashes identify the recorded Mac installation. A build from a different checkout path or host can have different native binary bytes.

See the [Mac operations and recovery instructions](https://github.com/tempo-v2/tempo/blob/cf94c79cc69820e1819ad32a4112a20b452ca1d6/OPENING.md).
