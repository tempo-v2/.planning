#!/usr/bin/env python3
"""Verify the assembled workspace guidance against this Planning checkout."""

import argparse
import hashlib
from pathlib import Path
import sys


CANONICAL_GUIDANCE = Path(__file__).resolve().parents[1] / "agent-guidance" / "AGENTS.md"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace_guidance", type=Path, help="assembled workspace AGENTS.md")
    args = parser.parse_args()

    try:
        canonical = CANONICAL_GUIDANCE.read_bytes()
        workspace = args.workspace_guidance.read_bytes()
    except OSError as error:
        print(f"Cannot read Tempo guidance: {error}", file=sys.stderr)
        return 1

    digest = hashlib.sha256(canonical).hexdigest()
    if workspace != canonical:
        print(
            f"Stale Tempo guidance at {args.workspace_guidance}. "
            f"Expected SHA-256 {digest} from {CANONICAL_GUIDANCE}.",
            file=sys.stderr,
        )
        return 1

    print(f"Current Tempo guidance SHA-256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
