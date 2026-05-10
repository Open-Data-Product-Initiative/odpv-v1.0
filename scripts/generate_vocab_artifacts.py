#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from vocab_utils import build_artifacts, load_yaml, read_text, validate_data, write_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate derived ODPV vocabulary artifacts.")
    parser.add_argument("--check", action="store_true", help="Fail if derived artifacts are not in sync.")
    args = parser.parse_args()

    data = load_yaml()
    errors = validate_data(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    artifacts = build_artifacts(data)
    changed = []
    for path, content in artifacts.items():
        if path.exists() and read_text(path) == content:
            continue
        changed.append(path)
        if not args.check:
            write_text(path, content)

    if args.check and changed:
        for path in changed:
            print(f"Out of sync: {path}")
        return 1

    if args.check:
        print("Vocabulary artifacts are in sync")
    else:
        print(f"Generated {len(artifacts)} vocabulary artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
