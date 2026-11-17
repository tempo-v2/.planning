"""Focused checks for local patch creation and the exact-known workspace upgrade."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("bootstrap_tempo", Path(__file__).with_name("bootstrap_tempo.py"))
bootstrap = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bootstrap)


class WorkspaceUpgradeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="tempo-workspace-check-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.manifest = self.root / "Cargo.toml"
        self.backup = self.root / "Cargo.toml.before-local-patches"

    def test_fresh_workspace_has_all_local_patches(self):
        bootstrap.configure_workspace(self.root)
        text = self.manifest.read_text()
        self.assertIn("[patch.crates-io]", text)
        for name in bootstrap.RUST_REPOS:
            self.assertIn(name + ' = { path = "' + name + '" }', text)
        self.assertFalse(self.backup.exists())

    def test_known_previous_manifest_is_backed_up_and_upgrade_is_idempotent(self):
        original = bootstrap.LEGACY_WORKSPACE.encode()
        self.manifest.write_bytes(original)
        self.manifest.chmod(0o640)
        bootstrap.configure_workspace(self.root)
        self.assertEqual(self.backup.read_bytes(), original)
        self.assertEqual(self.manifest.read_bytes(), bootstrap.WORKSPACE.encode())
        self.assertEqual(self.manifest.stat().st_mode & 0o777, 0o640)
        first = (self.manifest.read_bytes(), self.backup.read_bytes())
        bootstrap.configure_workspace(self.root)
        self.assertEqual((self.manifest.read_bytes(), self.backup.read_bytes()), first)

    def test_customized_manifest_is_never_rewritten(self):
        for original in [
            (bootstrap.LEGACY_WORKSPACE + "\n[profile.dev]\nopt-level = 1\n").encode(),
            bootstrap.LEGACY_WORKSPACE.replace("\n", "\r\n").encode(),
        ]:
            self.manifest.write_bytes(original)
            bootstrap.configure_workspace(self.root)
            self.assertEqual(self.manifest.read_bytes(), original)
            self.assertFalse(self.backup.exists())

    def test_conflicting_backup_refuses_upgrade_without_overwriting_either_file(self):
        self.manifest.write_text(bootstrap.LEGACY_WORKSPACE)
        self.backup.write_text("existing user's backup\n")
        with self.assertRaises(bootstrap.SetupError):
            bootstrap.configure_workspace(self.root)
        self.assertEqual(self.manifest.read_text(), bootstrap.LEGACY_WORKSPACE)
        self.assertEqual(self.backup.read_text(), "existing user's backup\n")


if __name__ == "__main__":
    unittest.main()
