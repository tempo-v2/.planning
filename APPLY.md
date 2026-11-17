# Apply the Tempo 2 planning bundle

This bundle contains the reviewed planning documents and workspace setup script.
The GitHub integration could read the repository but returned HTTP 403 for writes,
so these files have not been published to `.planning`.

The patch targets the original `tempo-v2/.planning` scaffold at commit
`b8909884e7e83b48e333956aeb51ede14cea67b4`. It updates `README.md`, adds
`ARCHITECTURE.md`, `BEHAVIOR.md`, and `scripts/bootstrap_tempo.py`, and leaves
`LICENSE` untouched. The script's executable file mode is included.

## Set up and review

Requirements: Git, Python 3.9+, and installed Rust/Cargo 1.85 or newer. The setup
script clones all nine repositories and creates the seven-package local Cargo
workspace. Component scaffold files remain local and uncommitted.

For a first extraction and setup on macOS or Linux:

```sh
unzip "$HOME/Downloads/tempo2_setup.zip" -d "$HOME/Downloads/tempo2_setup"
python3 "$HOME/Downloads/tempo2_setup/tempo-planning/scripts/bootstrap_tempo.py" "$HOME/Developer/tempo-v2"
git -C "$HOME/Developer/tempo-v2/.planning" apply --check "$HOME/Downloads/tempo2_setup/tempo-planning.patch"
git -C "$HOME/Developer/tempo-v2/.planning" apply --index "$HOME/Downloads/tempo2_setup/tempo-planning.patch"
git -C "$HOME/Developer/tempo-v2/.planning" diff --cached --stat
git -C "$HOME/Developer/tempo-v2/.planning" diff --cached
```

If patch validation fails, inspect the repository changes before applying it.
The patch remains in Downloads; it is not copied into the repository. Review the
staged four-file change, then commit and push manually using your normal GitHub
authentication. A suitable commit message is `Document Tempo 2 contracts and add
workspace setup`; the intended destination is `.planning`'s `main` branch.

The application and component repositories are not pushed by these instructions.
After publication, the README's setup command can use the script directly from
the cloned `.planning` repository. To enter the workspace, run
`cd "$HOME/Developer/tempo-v2"` in your shell.

## Bundle validation

The patch was checked and applied with real Git in a fresh local fixture using
the original README, then every resulting file was byte-compared with the
reviewed deliverables. Exactly four files changed, the license fixture was
unchanged, and Git recorded the script as executable. The ZIP was checked for
CRC errors and contains no caches. Rust/Cargo compilation was unavailable in the
authoring environment; the script runs `cargo check --workspace` on your machine.
