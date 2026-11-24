#!/usr/bin/env python3
"""Reconstruct or verify the historical multi-repository Tempo review workspace."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from bootstrap_tempo import SetupError, check_repository, checked


PLANNING = Path(__file__).resolve().parents[1]
MANIFEST = PLANNING / "plans/usable-release/current-assembly.json"
COMPONENTS = {
    "tempo", "tempo-chess", "tempo-core-components", "tempo-learning",
    "tempo-queue", "tempo-store", "tempo-study", "tempo-types", "tempo-ui",
}


def require_digest(path, expected):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    if digest.hexdigest() != expected:
        raise SetupError(f"Content does not match manifest: {path}")


def load_review():
    review = json.loads(MANIFEST.read_text())["predecessor_assembly"]["review"]
    pins = review["components"]
    if pins.keys() != COMPONENTS or not all(re.fullmatch("[0-9a-f]{40}", pin) for pin in pins.values()):
        raise SetupError("Current assembly must pin every runtime component by full commit")
    require_digest(PLANNING / review["workspace_template"], review["workspace_sha256"])
    require_digest(PLANNING / review["cargo_lock"], review["cargo_lock_sha256"])
    require_digest(PLANNING / "agent-guidance/AGENTS.md", review["guidance_sha256"])
    return review


def verify(workspace, review):
    for name, pin in review["components"].items():
        repository = workspace / name
        check_repository(repository, name)
        if checked(["git", "rev-parse", "HEAD"], cwd=repository) != pin:
            raise SetupError(f"Wrong revision for {name}. Expected {pin}.")
        if checked(["git", "status", "--porcelain"], cwd=repository):
            raise SetupError(f"Worktree has local changes: {name}")
    require_digest(workspace / "Cargo.toml", review["workspace_sha256"])
    require_digest(workspace / "Cargo.lock", review["cargo_lock_sha256"])
    require_digest(workspace / "AGENTS.md", review["guidance_sha256"])
    ui = workspace / "tempo-ui"
    require_digest(ui / "package-lock.json", review["ui_lock_sha256"])
    require_digest(ui / review["core_package"], review["core_package_sha256"])
    print(f"Verified review assembly with Planning {checked(['git', 'rev-parse', 'HEAD'], cwd=PLANNING)}")


def assemble(workspace, review, protocol):
    if any(entry.name != ".planning" for entry in workspace.iterdir()):
        raise SetupError("Assembly requires a new workspace containing only its .planning checkout")
    for name, pin in review["components"].items():
        origin = f"https://github.com/tempo-v2/{name}.git"
        if protocol == "ssh":
            origin = f"git@github.com:tempo-v2/{name}.git"
        repository = workspace / name
        repository.mkdir()
        checked(["git", "init", "--quiet"], cwd=repository)
        checked(["git", "remote", "add", "origin", origin], cwd=repository)
        checked(["git", "fetch", "--depth=1", "origin", pin], cwd=repository)
        checked(["git", "checkout", "--detach", "FETCH_HEAD"], cwd=repository)
    for destination, source in (
        ("Cargo.toml", PLANNING / review["workspace_template"]),
        ("Cargo.lock", PLANNING / review["cargo_lock"]),
        ("AGENTS.md", PLANNING / "agent-guidance/AGENTS.md"),
    ):
        (workspace / destination).write_bytes(source.read_bytes())
    (workspace / "Makefile").write_text("include tempo/tools/local.mk\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--protocol", choices=("https", "ssh"), default="https")
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    if (workspace / ".planning").resolve() != PLANNING:
        raise SetupError("Use the .planning checkout inside the selected workspace")
    if checked(["git", "status", "--porcelain"], cwd=PLANNING):
        raise SetupError("Planning checkout has local changes")
    review = load_review()
    if not args.verify:
        assemble(workspace, review, args.protocol)
    verify(workspace, review)


if __name__ == "__main__":
    try:
        main()
    except (OSError, SetupError, ValueError, KeyError) as error:
        sys.exit(f"Tempo assembly: {error}")
