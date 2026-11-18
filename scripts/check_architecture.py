#!/usr/bin/env python3
"""Check the initial Tempo dependency contract using Cargo's interpretation.

All declared dependency kinds count, including optional, dev, build and target
specific dependencies. Root workspace patches are allowed; member manifests
cannot refer to a sibling source tree. Direct Rust include/path escapes are
checked conservatively; dynamic include paths require an explicit local source.
This gate is not a Rust parser, process sandbox, or proof about macro-generated
code. Compilation and application contract tests are separate checks.
"""
import argparse
import copy
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unittest


CONTRACT = Path(__file__).resolve().parents[1] / "contracts" / "dependencies.json"


def within(path, directory):
    try:
        path.resolve().relative_to(directory.resolve())
        return True
    except ValueError:
        return False


def tempo_name(name):
    return name == "tempo" or name.startswith("tempo-")


def metadata_errors(metadata, root, allowed):
    """Pure metadata checks, also used by the negative self-tests."""
    errors = []
    packages = metadata.get("packages", [])
    by_id = {package["id"]: package for package in packages}
    members = [by_id.get(identity) for identity in metadata.get("workspace_members", [])]
    if any(member is None for member in members):
        errors.append("workspace contains an unresolved package identity")
    member_names = [member["name"] for member in members if member is not None]
    if set(member_names) != set(allowed) or len(member_names) != len(allowed):
        errors.append("workspace members must be exactly: " + ", ".join(sorted(allowed)))
    if Path(metadata.get("workspace_root", "")).resolve() != root.resolve():
        errors.append("Cargo workspace root differs from the requested workspace")
    for name in allowed:
        identities = [package for package in packages if package["name"] == name]
        if len(identities) != 1:
            errors.append("{} resolves to {} source/version identities (expected one)".format(name, len(identities)))
    for package in packages:
        name = package["name"]
        if tempo_name(name) and name not in allowed:
            errors.append("unexpected Tempo package: " + name)
    for package in members:
        if package is None or package["name"] not in allowed:
            continue
        name = package["name"]
        repository = root / name
        if Path(package["manifest_path"]).resolve() != (repository / "Cargo.toml").resolve():
            errors.append(name + " must be the package in its own repository directory")
        if package.get("source") is not None:
            errors.append(name + " workspace member must resolve to its local checkout")
        for target in package.get("targets", []):
            if not within(Path(target["src_path"]), repository):
                errors.append(name + " target source escapes its repository: " + target["src_path"])
        for dependency in package.get("dependencies", []):
            # `name` is the real package; `rename` is only its source-code alias.
            dependency_name = dependency["name"]
            kind = dependency.get("kind") or "normal"
            target = dependency.get("target") or "all targets"
            if tempo_name(dependency_name) and dependency_name not in allowed[name]:
                errors.append("{} -> {} is forbidden ({}; {}; alias {})".format(
                    name, dependency_name, kind, target, dependency.get("rename") or dependency_name))
            path = dependency.get("path")
            if path and not within(Path(path), repository):
                errors.append(name + " has a dependency path outside its repository; use a root patch: " + path)
    return errors


INCLUDE = re.compile(r'\binclude(?:_str|_bytes)?\s*!\s*[(\[{]\s*(?P<argument>[^\n]*)')
PATH_ATTRIBUTE = re.compile(r'#\s*\[\s*(?:path\s*=|cfg_attr\s*\([^]]*?\bpath\s*=)\s*(?P<argument>[^\n]*)')
LITERAL = re.compile(r'^(?:"(?P<plain>[^"\\]*)"|r(?P<hashes>#{0,16})"(?P<raw>.*?)"(?P=hashes))\s*[,\])}]')


def direct_source_errors(source, source_path, repository):
    errors = []
    # Leave Rust syntax parsing to rustc. Comments with include examples can be
    # avoided in source; this intentionally conservative check is easy to audit.
    for expression in (INCLUDE, PATH_ATTRIBUTE):
        for match in expression.finditer(source):
            literal = LITERAL.match(match.group("argument"))
            if literal is None:
                errors.append(str(source_path) + ": dynamic or escaped include/path is not allowed by the scaffold contract")
                continue
            value = literal.group("plain") if literal.group("plain") is not None else literal.group("raw")
            if not within(source_path.parent / value, repository):
                errors.append(str(source_path) + ": include/path escapes repository: " + value)
    return errors


def source_errors(root, allowed):
    errors = []
    for name in allowed:
        repository = root / name
        for directory, subdirectories, filenames in os.walk(repository, followlinks=False):
            subdirectories[:] = [item for item in subdirectories if item not in {".git", "target"}]
            for item in subdirectories:
                candidate = Path(directory) / item
                if candidate.is_symlink() and not within(candidate, repository):
                    errors.append(str(candidate) + ": source directory symlink escapes repository")
            for filename in filenames:
                if not filename.endswith(".rs"):
                    continue
                source_path = Path(directory) / filename
                if not within(source_path, repository):
                    errors.append(str(source_path) + ": Rust source escapes repository")
                    continue
                errors.extend(direct_source_errors(source_path.read_text(encoding="utf-8"), source_path, repository))
    return errors


def self_test(allowed):
    root = Path("/fixture/tempo-v2")
    packages = []
    for name, dependencies in allowed.items():
        packages.append({
            "id": name + "@0.1.0", "name": name, "version": "0.1.0", "source": None,
            "manifest_path": str(root / name / "Cargo.toml"), "targets": [],
            "dependencies": [{"name": dependency, "kind": None, "target": None, "path": None, "rename": None}
                             for dependency in dependencies],
        })
    baseline = {"packages": packages, "workspace_members": [package["id"] for package in packages], "workspace_root": str(root)}

    class ContractTests(unittest.TestCase):
        def test_allowed_graph(self):
            self.assertEqual(metadata_errors(baseline, root, allowed), [])

        def test_forbidden_edge_cannot_hide_behind_kind_target_or_alias(self):
            for kind in [None, "dev", "build"]:
                value = copy.deepcopy(baseline)
                study = next(package for package in value["packages"] if package["name"] == "tempo-study")
                study["dependencies"].append({"name": "tempo-store", "kind": kind, "rename": "innocent", "target": "cfg(unix)", "path": None})
                self.assertTrue(any("tempo-study -> tempo-store is forbidden" in error for error in metadata_errors(value, root, allowed)))

        def test_duplicate_identity_and_sibling_path_are_rejected(self):
            value = copy.deepcopy(baseline)
            duplicate = copy.deepcopy(value["packages"][0])
            duplicate["id"] += "#other-source"
            value["packages"].append(duplicate)
            self.assertTrue(any("source/version identities" in error for error in metadata_errors(value, root, allowed)))
            value = copy.deepcopy(baseline)
            study = next(package for package in value["packages"] if package["name"] == "tempo-study")
            study["dependencies"][0]["path"] = str(root / "tempo-types")
            self.assertTrue(any("dependency path outside" in error for error in metadata_errors(value, root, allowed)))

        def test_direct_source_confinement(self):
            repository = root / "tempo-study"
            source = repository / "src" / "lib.rs"
            self.assertEqual(direct_source_errors('include!("local.rs");', source, repository), [])
            self.assertTrue(direct_source_errors('include!("../../tempo-store/src/lib.rs");', source, repository))
            self.assertTrue(direct_source_errors('#[path = "../../tempo-store/src/lib.rs"] mod store;', source, repository))
            self.assertTrue(direct_source_errors('#[cfg_attr(unix, path = "../../tempo-store/src/lib.rs")] mod store;', source, repository))
            self.assertTrue(direct_source_errors('include!(concat!(env!("OUT_DIR"), "/source.rs"));', source, repository))

    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests))
    return 0 if result.wasSuccessful() else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--cargo", default="cargo", help="Cargo executable (default: cargo)")
    parser.add_argument("--self-test", action="store_true", help="Run focused allowed/forbidden metadata and source examples")
    args = parser.parse_args()
    allowed = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if args.self_test:
        return self_test(allowed)
    root = args.workspace.resolve()
    command = [args.cargo, "metadata", "--format-version", "1", "--all-features", "--locked", "--manifest-path", str(root / "Cargo.toml")]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        metadata = json.loads(result.stdout)
        errors = metadata_errors(metadata, root, allowed) + source_errors(root, allowed)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print("Architecture check could not run: " + str(error), file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError):
            print(error.stderr.strip(), file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print("FAIL: " + error, file=sys.stderr)
        return 1
    print("Architecture contract passed: seven unique Rust packages, allowed dependency directions, and confined source paths.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
