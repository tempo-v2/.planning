#!/usr/bin/env python3
"""Clone Tempo2's separate repositories and create a local Cargo workspace.

Requires Python 3.9+, Git, and an installed Rust/Cargo toolchain >= 1.85.
Existing repository files are preserved. An exact earlier generated workspace
manifest is upgraded with local dependency patches after saving a backup.
Nothing is committed or pushed.
"""

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlsplit


ORG = "tempo-v2"
RUST_REPOS = (
    "tempo-types", "tempo-study", "tempo-queue", "tempo-learning",
    "tempo-chess", "tempo-store", "tempo",
)
REPOS = (".planning",) + RUST_REPOS + ("tempo-core-components",)
MIN_RUST = (1, 85, 0)
MARKER = "# Created by tempo-v2 bootstrap; package metadata stays standalone.\n"
LEGACY_WORKSPACE = (
    "# Local aggregation only: each member remains a separate Git repository.\n"
    "[workspace]\n"
    'resolver = "3"\n'
    "members = [\n"
    + "".join('    "' + name + '",\n' for name in RUST_REPOS)
    + "]\n"
    + 'exclude = [".planning", "tempo-core-components"]\n'
)
WORKSPACE = (
    LEGACY_WORKSPACE
    + "\n# Local development overrides; component release dependencies stay versioned.\n"
    + "[patch.crates-io]\n"
    + "".join(name + ' = { path = "' + name + '" }\n' for name in RUST_REPOS)
)


class SetupError(Exception):
    """An actionable setup error; no cleanup or destructive repair is attempted."""


def run(argv, cwd=None, capture=True):
    return subprocess.run(
        [str(arg) for arg in argv], cwd=cwd, text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        check=False,
    )


def checked(argv, cwd=None):
    result = run(argv, cwd=cwd)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise SetupError("Command failed: {}\n{}".format(shlex.join(argv), detail))
    return result.stdout.strip()


def existing_directory(path):
    while not path.exists():
        path = path.parent
    if not path.is_dir():
        raise SetupError("Expected a directory: {}".format(path))
    return path


def version_tuple(text):
    match = re.search(r"\b(\d+)\.(\d+)\.(\d+)", text)
    if not match:
        raise SetupError("Cannot identify the tool version: {}".format(text))
    return tuple(int(value) for value in match.groups())


def preflight_tools(destination):
    for tool in ("git", "cargo", "rustc"):
        if not shutil.which(tool):
            hint = " Install Rust using https://rustup.rs/ first." if tool != "git" else " Install Git first."
            raise SetupError("Required command is missing: {}.{}".format(tool, hint))
    directory = existing_directory(destination)
    for tool in ("rustc", "cargo"):
        value = checked([tool, "--version"], cwd=directory)
        if version_tuple(value) < MIN_RUST:
            raise SetupError("{}; this scaffold requires Rust and Cargo >= 1.85.".format(value))
        print(value)


def canonical_origin(url):
    """Compare repository identity, without printing credentials from an origin."""
    if url.startswith("git@github.com:"):
        path = url.split(":", 1)[1]
    else:
        parsed = urlsplit(url)
        if parsed.scheme not in ("https", "ssh") or parsed.hostname != "github.com":
            return None
        if parsed.query or parsed.fragment or parsed.port is not None:
            return None
        path = parsed.path.lstrip("/")
    path = path.rstrip("/")
    if path.endswith(".git"):
        path = path[:-4]
    return path.casefold()


def check_repository(path, name):
    if path.is_symlink():
        raise SetupError("Repository directory is a symlink; choose a regular directory: {}".format(path))
    if not path.is_dir():
        raise SetupError("Existing repository path is not a directory: {}".format(path))
    top = run(["git", "-C", path, "rev-parse", "--show-toplevel"])
    if top.returncode or Path(top.stdout.strip()).resolve() != path.resolve():
        raise SetupError("Existing path is not its own Git working tree: {}".format(path))
    head = run(["git", "-C", path, "rev-parse", "--verify", "HEAD^{commit}"])
    if head.returncode:
        raise SetupError(
            "Incomplete or unborn checkout: {}. Finish cloning or check out a commit, then rerun."
            .format(path)
        )
    # Read the stored URL, not `remote get-url`, which expands insteadOf rules.
    remote = run(["git", "-C", path, "config", "--get", "remote.origin.url"])
    try:
        identity = canonical_origin(remote.stdout.strip())
    except ValueError:
        identity = None
    if remote.returncode or identity != (ORG + "/" + name).casefold():
        raise SetupError("Origin does not identify {}/{}: {}".format(ORG, name, path))


def manifest_for(name):
    return (
        MARKER + "[package]\n"
        + 'name = "' + name + '"\n'
        + 'version = "0.1.0"\n'
        + 'edition = "2024"\n'
        + 'rust-version = "1.85"\n'
        + 'license = "MIT"\n'
        + 'repository = "https://github.com/' + ORG + "/" + name + '"\n\n'
        + "[dependencies]\n"
    )


def source_for(name):
    if name == "tempo":
        return "main.rs", 'fn main() {\n    println!("Tempo 2 application scaffold.");\n}\n'
    return "lib.rs", (
        "//! " + name + ": Tempo2 component scaffold.\n"
        "//!\n"
        "//! Public contracts and behavior will be implemented in this repository.\n"
    )


def check_regular_file(path):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise SetupError("Expected a regular file or an absent path: {}".format(path))


def check_scaffold(path, name):
    """Refuse ambiguous scaffolds; a known interrupted generation can be resumed."""
    manifest = path / "Cargo.toml"
    check_regular_file(manifest)
    check_regular_file(path / ".gitignore")
    if manifest.exists() and manifest.read_text(encoding="utf-8") != manifest_for(name):
        return  # An existing package owns its sources and targets.
    source_dir = path / "src"
    if source_dir.is_symlink() or (source_dir.exists() and not source_dir.is_dir()):
        raise SetupError("Expected a regular source directory: {}".format(source_dir))
    source_name, _ = source_for(name)
    source = source_dir / source_name
    check_regular_file(source)
    if not manifest.exists() and source_dir.exists() and any(source_dir.iterdir()):
        raise SetupError("Source exists without a Cargo manifest; preserve and configure it manually: {}".format(path))
    if manifest.exists() and not source.exists() and source_dir.exists() and any(source_dir.iterdir()):
        raise SetupError("The generated target is absent but other source exists; resolve it manually: {}".format(path))


def check_workspace(destination):
    manifest = destination / "Cargo.toml"
    check_regular_file(manifest)
    if not manifest.exists() or manifest.read_text(encoding="utf-8") in (LEGACY_WORKSPACE, WORKSPACE):
        return
    # Preserve a customized workspace only when Cargo confirms the same members.
    result = run([
        "cargo", "metadata", "--format-version", "1", "--no-deps", "--offline", "--locked",
        "--manifest-path", manifest,
    ], cwd=destination)
    if result.returncode:
        raise SetupError(
            "Existing Cargo.toml differs from this scaffold and cannot be validated offline. "
            "It was not changed. Resolve its Cargo metadata error first:\n" + result.stderr.strip()
        )
    try:
        metadata = json.loads(result.stdout)
        ids = set(metadata["workspace_members"])
        members = {
            Path(package["manifest_path"]).resolve().parent
            for package in metadata["packages"] if package["id"] in ids
        }
        expected = {destination / name for name in RUST_REPOS}
        valid = Path(metadata["workspace_root"]).resolve() == destination and members == expected
    except (KeyError, TypeError, ValueError):
        valid = False
    if not valid:
        raise SetupError("Existing Cargo.toml does not describe exactly the seven expected Rust members; it was not changed.")


def preflight_destination(destination):
    directory = existing_directory(destination)
    inside_git = run(["git", "-C", directory, "rev-parse", "--git-dir"])
    if inside_git.returncode == 0:
        raise SetupError("Choose a workspace directory outside every existing Git repository: {}".format(destination))
    for name in REPOS:
        path = destination / name
        if path.exists() or path.is_symlink():
            check_repository(path, name)
            if name in RUST_REPOS:
                check_scaffold(path, name)
    check_workspace(destination)


def write_new(path, content):
    if path.exists():
        print("Preserved {}".format(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also prevents a late-arriving file from being overwritten.
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    print("Created   {}".format(path))


def configure_workspace(destination):
    """Upgrade only our exact former manifest; custom workspaces are never rewritten."""
    manifest = destination / "Cargo.toml"
    check_regular_file(manifest)
    if not manifest.exists():
        write_new(manifest, WORKSPACE)
        return
    current = manifest.read_bytes().decode("utf-8")
    if current != LEGACY_WORKSPACE:
        print("Preserved {}".format(manifest))
        if current != WORKSPACE:
            print("Customized workspace retained. If local patches are missing, merge entries from .planning/workspace.template.toml.")
        return
    backup = destination / "Cargo.toml.before-local-patches"
    check_regular_file(backup)
    if backup.exists() and backup.read_bytes().decode("utf-8") != current:
        raise SetupError("Workspace backup already contains different work; nothing was overwritten: {}".format(backup))
    write_new(backup, current)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         prefix=".tempo-workspace-", dir=destination, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(WORKSPACE)
        os.chmod(temporary, manifest.stat().st_mode & 0o777)
        check_regular_file(manifest)
        if manifest.read_bytes().decode("utf-8") != current:
            raise SetupError("Workspace changed during setup; it was not overwritten. Rerun after reviewing it.")
        os.replace(temporary, manifest)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink()
    print("Upgraded local workspace with sibling dependency patches; backup: {}".format(backup))


def check_local_resolution(destination):
    """Prevent an unpublished Tempo dependency from resolving to a different package."""
    output = checked([
        "cargo", "metadata", "--format-version", "1", "--manifest-path", str(destination / "Cargo.toml"),
    ], cwd=destination)
    try:
        metadata = json.loads(output)
        seen = set()
        for package in metadata["packages"]:
            name = package["name"]
            if name not in RUST_REPOS:
                continue
            if name in seen or package.get("source") is not None \
                    or Path(package["manifest_path"]).resolve().parent != destination / name:
                raise SetupError("Tempo dependency did not resolve uniquely to its sibling checkout: {}".format(name))
            seen.add(name)
        if seen != set(RUST_REPOS):
            raise SetupError("Cargo resolution did not contain exactly the expected seven local Tempo packages.")
    except (KeyError, TypeError, ValueError) as error:
        raise SetupError("Cargo returned invalid package metadata: {}".format(error)) from error
    print("Verified all Tempo dependencies resolve to the sibling checkouts.")


def scaffold(path, name):
    manifest = path / "Cargo.toml"
    generated = not manifest.exists() or manifest.read_text(encoding="utf-8") == manifest_for(name)
    if generated:
        write_new(manifest, manifest_for(name))
        source_name, content = source_for(name)
        write_new(path / "src" / source_name, content)
    else:
        print("Preserved existing Cargo package: {}".format(path))
    write_new(path / ".gitignore", "/target/\n")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "destination", nargs="?", type=Path,
        default=Path.home() / "Developer" / "tempo-v2",
        help="local parent directory (default: ~/Developer/tempo-v2)",
    )
    parser.add_argument("--protocol", choices=("https", "ssh"), default="https", help="clone transport (default: https)")
    parser.add_argument("--no-check", action="store_true", help="skip dependency resolution and cargo check; Git and Rust are still required")
    return parser.parse_args(argv)


def main(argv=None):
    if sys.version_info < (3, 9):
        raise SetupError("Python 3.9 or newer is required.")
    args = parse_args(argv)
    destination = args.destination.expanduser().resolve()
    preflight_tools(destination)
    preflight_destination(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for name in REPOS:
        path = destination / name
        if path.exists():
            print("Using existing repository: {}".format(path))
            continue
        url = (
            "git@github.com:{}/{}.git".format(ORG, name)
            if args.protocol == "ssh"
            else "https://github.com/{}/{}.git".format(ORG, name)
        )
        print("Cloning {}...".format(name), flush=True)
        if run(["git", "clone", "--", url, path], capture=False).returncode:
            raise SetupError("Clone failed for {}. Completed clones were preserved; fix the cause and rerun.".format(name))
        check_repository(path, name)
    # New upstream contents are checked before any scaffold files are written.
    for name in RUST_REPOS:
        check_scaffold(destination / name, name)
    for name in RUST_REPOS:
        scaffold(destination / name, name)
    configure_workspace(destination)
    if not args.no_check:
        check_local_resolution(destination)
        print("Checking the workspace...", flush=True)
        if run(["cargo", "check", "--workspace"], cwd=destination, capture=False).returncode:
            raise SetupError("Cargo check failed. All files were preserved; resolve the reported error and rerun.")
    else:
        print("Dependency resolution and Cargo check skipped (--no-check).")
    print("\nWorkspace ready: {}".format(destination))
    print("Seven Cargo packages; nine separate Git repositories. No parent Git repository was created.")
    print("Existing package sources were preserved; any newly generated files are local and uncommitted.")
    print("Package metadata stays standalone; local workspace patches connect versioned Tempo dependencies.")
    print("\nNext commands:")
    print("  cd " + shlex.quote(str(destination)))
    print("  cargo check --workspace")
    print("  cargo test --workspace")
    print("\nReview and commit changes separately in each component repository:")
    for name in RUST_REPOS:
        print("  " + shlex.join(["git", "-C", str(destination / name), "status", "--short"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (SetupError, OSError, UnicodeError) as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        sys.exit(1)
