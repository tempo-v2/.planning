#!/usr/bin/env python3
"""Run the initial cross-repository interface qualification. No installs or Git writes."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.workspace.expanduser().resolve()
    for tool in ("cargo", "node"):
        if not shutil.which(tool):
            raise SystemExit("Missing prerequisite: " + tool)
    steps = [
        [sys.executable, str(root / ".planning/scripts/check_architecture.py") , str(root)],
        [sys.executable, str(root / ".planning/scripts/check_architecture.py"), "--self-test"],
        [sys.executable, str(root / ".planning/scripts/test_bootstrap_workspace.py")],
        ["cargo", "fmt", "--all", "--", "--check"],
        ["cargo", "test", "--workspace"],
        ["cargo", "clippy", "--workspace", "--all-targets", "--", "-D", "warnings"],
        ["cargo", "build", "-p", "tempo"],
        ["node", "--test", str(root / "tempo-core-components/test/study.test.js")],
        ["node", "--test", str(root / "tempo/tests/ui_boundary.mjs")],
    ]
    for command in steps:
        print("Running: " + " ".join(command), flush=True)
        subprocess.run(command, cwd=root, check=True)
    print("Interface qualification passed. This does not qualify SQLite durability or real chess/FSRS algorithms.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.returncode)
