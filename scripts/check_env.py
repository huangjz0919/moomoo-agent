#!/usr/bin/env python3
"""Validate local .env settings for the community topic agent."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
EXAMPLE_PATH = ROOT / ".env.example"

REQUIRED_KEYS = [
    "SEARCH_PROVIDER",
    "SEARCH_API_KEY",
    "SEARCH_API_ENDPOINT",
    "SEARCH_MAX_RESULTS",
    "SOURCE_FETCH_TIMEOUT_SECONDS",
    "IMAGE_PROVIDER",
    "IMAGE_API_KEY",
    "IMAGE_API_ENDPOINT",
    "IMAGE_MODEL",
    "IMAGE_SIZE",
    "OUTPUT_ROOT",
    "DEFAULT_PLATFORM",
]

OPTIONAL_KEYS = [
    "HOST_WEB_READER",
    "HOST_IMAGE_TOOL",
]

HOST_CAPABILITY_VALUES = {"available", "unavailable", "unknown", ""}


def parse_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail when .env or required values are missing.")
    args = parser.parse_args()

    example = parse_env(EXAMPLE_PATH)
    env = parse_env(ENV_PATH)

    expected_example_keys = REQUIRED_KEYS + OPTIONAL_KEYS
    missing_from_example = [key for key in expected_example_keys if key not in example]
    if missing_from_example:
        print("ERROR: .env.example missing keys:")
        for key in missing_from_example:
            print(f"- {key}")
        return 1

    if not ENV_PATH.exists():
        print("WARN: .env not found. Copy .env.example to .env for API-backed automation.")
        return 1 if args.strict else 0

    missing_values = [key for key in REQUIRED_KEYS if not env.get(key)]
    if missing_values:
        print("WARN: .env has empty required values:")
        for key in missing_values:
            print(f"- {key}")
        return 1 if args.strict else 0

    if env.get("IMAGE_SIZE") != "750x375":
        print("ERROR: IMAGE_SIZE must be 750x375")
        return 1

    invalid_host_values = [
        key for key in OPTIONAL_KEYS if env.get(key, "") not in HOST_CAPABILITY_VALUES
    ]
    if invalid_host_values:
        print("ERROR: host capability values must be available, unavailable, or unknown:")
        for key in invalid_host_values:
            print(f"- {key}={env.get(key)}")
        return 1

    print("OK: environment settings are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
