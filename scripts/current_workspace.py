#!/usr/bin/env python3
"""Assemble or verify the pinned current Tempo review workspace."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory

from bootstrap_tempo import SetupError, check_repository, checked, run


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
    require_digest(PLANNING / review["guidance_path"], review["guidance_sha256"])
    return review


def verify_checkout(repository, name, pin):
    check_repository(repository, name)
    if checked(["git", "rev-parse", "HEAD"], cwd=repository) != pin:
        raise SetupError(f"Wrong revision for {name}. Expected {pin}.")
    if checked(["git", "status", "--porcelain"], cwd=repository):
        raise SetupError(f"Worktree has local changes: {name}")


def verify(workspace, review):
    for name, pin in review["components"].items():
        verify_checkout(workspace / name, name, pin)
    require_digest(workspace / "Cargo.toml", review["workspace_sha256"])
    require_digest(workspace / "Cargo.lock", review["cargo_lock_sha256"])
    require_digest(workspace / "AGENTS.md", review["guidance_sha256"])
    ui = workspace / "tempo-ui"
    require_digest(ui / "package-lock.json", review["ui_lock_sha256"])
    require_digest(ui / review["core_package"], review["core_package_sha256"])
    print(f"Verified review assembly with Planning {checked(['git', 'rev-parse', 'HEAD'], cwd=PLANNING)}")


def parse_sources(values):
    sources = {}
    for value in values:
        name, separator, path = value.partition("=")
        if name not in COMPONENTS or not separator or not path:
            raise SetupError(f"Expected --source COMPONENT=PATH, got {value!r}")
        sources.setdefault(name, []).append(Path(path).expanduser().resolve())
    return sources


def has_commit(source, pin):
    return run(["git", "-C", source, "cat-file", "-e", f"{pin}^{{commit}}"]).returncode == 0


def assemble(workspace, review, protocol, sources, offline):
    files = {
        "Cargo.toml": (PLANNING / review["workspace_template"]).read_bytes(),
        "Cargo.lock": (PLANNING / review["cargo_lock"]).read_bytes(),
        "AGENTS.md": (PLANNING / review["guidance_path"]).read_bytes(),
        "Makefile": b"include tempo/tools/local.mk\n",
    }
    for filename, content in files.items():
        path = workspace / filename
        if path.is_symlink() or (path.exists() and path.read_bytes() != content):
            raise SetupError(f"Existing workspace file differs: {path}")
    missing = []
    for name, pin in review["components"].items():
        repository = workspace / name
        if repository.exists() or repository.is_symlink():
            verify_checkout(repository, name, pin)
            continue
        source = next((path for path in sources.get(name, ()) if path.is_dir() and has_commit(path, pin)), None)
        if source is None and offline:
            missing.append(f"{name} {pin}")
            continue
        origin = f"https://github.com/tempo-v2/{name}.git"
        if protocol == "ssh":
            origin = f"git@github.com:tempo-v2/{name}.git"
        with TemporaryDirectory(prefix=f".{name}-", dir=workspace) as stage:
            staged = Path(stage) / name
            staged.mkdir()
            checked(["git", "init", "--quiet"], cwd=staged)
            checked(["git", "remote", "add", "origin", origin], cwd=staged)
            checked(["git", "fetch", "--depth=1", str(source) if source else "origin", pin], cwd=staged)
            checked(["git", "checkout", "--detach", "FETCH_HEAD"], cwd=staged)
            verify_checkout(staged, name, pin)
            staged.rename(repository)
    if missing:
        raise SetupError("Exact commits unavailable offline:\n" + "\n".join(missing))
    for filename, content in files.items():
        path = workspace / filename
        if not path.exists():
            with path.open("xb") as output:
                output.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--protocol", choices=("https", "ssh"), default="https")
    parser.add_argument("--source", action="append", default=[], metavar="COMPONENT=PATH",
                        help="try this local Git object store before GitHub; repeat as needed")
    parser.add_argument("--offline", action="store_true", help="report missing exact commits without remote fetches")
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    if (workspace / ".planning").resolve() != PLANNING:
        raise SetupError("Use the .planning checkout inside the selected workspace")
    if checked(["git", "status", "--porcelain"], cwd=PLANNING):
        raise SetupError("Planning checkout has local changes")
    review = load_review()
    if not args.verify:
        assemble(workspace, review, args.protocol, parse_sources(args.source), args.offline)
    verify(workspace, review)


if __name__ == "__main__":
    try:
        main()
    except (OSError, SetupError, ValueError, KeyError) as error:
        sys.exit(f"Tempo assembly: {error}")
