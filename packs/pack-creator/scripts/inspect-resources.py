#!/usr/bin/env python3
"""List regular Pack resources for author review; this is not a Lorelum validator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


RESOURCE_DIRS = ("references", "assets", "scripts")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List regular files in a Pack's resource directories without executing them."
    )
    parser.add_argument("pack_root", type=Path, help="Path to the Pack root to inspect.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.pack_root.resolve()
    resources: dict[str, list[str]] = {directory: [] for directory in RESOURCE_DIRS}

    for directory in RESOURCE_DIRS:
        directory_root = root / directory
        if not directory_root.is_dir() or directory_root.is_symlink():
            continue
        for path in sorted(directory_root.rglob("*")):
            if path.is_symlink() or not path.is_file():
                continue
            resources[directory].append(path.relative_to(root).as_posix())

    print(
        json.dumps(
            {
                "packRoot": str(root),
                "resources": resources,
                "note": "Inventory only. Run lore validate for Pack structural diagnostics.",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
