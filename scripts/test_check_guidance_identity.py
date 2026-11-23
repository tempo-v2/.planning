"""Exercise the assembly guidance check with disposable copies."""

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check_guidance_identity.py")
CANONICAL = SCRIPT.parents[1] / "agent-guidance" / "AGENTS.md"


class GuidanceIdentityTests(unittest.TestCase):
    def run_check(self, guidance):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(guidance)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_current_copy_reports_canonical_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            guidance = Path(directory) / "AGENTS.md"
            guidance.write_bytes(CANONICAL.read_bytes())
            result = self.run_check(guidance)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(hashlib.sha256(CANONICAL.read_bytes()).hexdigest(), result.stdout)

    def test_missing_copy_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_check(Path(directory) / "AGENTS.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot read Tempo guidance", result.stderr)

    def test_stale_copy_fails_and_stays_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            guidance = Path(directory) / "AGENTS.md"
            stale = CANONICAL.read_bytes() + b"\nOlder assembly note.\n"
            guidance.write_bytes(stale)
            result = self.run_check(guidance)
            self.assertEqual(guidance.read_bytes(), stale)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Stale Tempo guidance", result.stderr)


if __name__ == "__main__":
    unittest.main()
