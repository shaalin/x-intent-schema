#!/usr/bin/env python3
"""Validate example JSON files against the x-intent schema."""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Missing dependency: pip install jsonschema")
    sys.exit(1)


def main():
    repo_root = Path(__file__).parent
    schema_path = repo_root / "schemas" / "x-intent" / "v1" / "schema.json"
    examples_dir = repo_root / "examples"

    with open(schema_path) as f:
        schema = json.load(f)

    validator = jsonschema.Draft202012Validator(schema)

    examples = sorted(examples_dir.glob("*.json"))
    if not examples:
        print("No examples found")
        sys.exit(1)

    failed = []
    for example_path in examples:
        with open(example_path) as f:
            example = json.load(f)

        errors = list(validator.iter_errors(example))
        if errors:
            failed.append((example_path.name, errors))
            print(f"FAIL {example_path.name}")
            for err in errors:
                print(f"  - {err.message}")
        else:
            print(f"OK   {example_path.name}")

    if failed:
        print(f"\n{len(failed)} file(s) failed validation")
        sys.exit(1)

    print(f"\nAll {len(examples)} examples valid")


if __name__ == "__main__":
    main()
