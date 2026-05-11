#!/usr/bin/env python3
"""Report runtime capabilities for source fetching and image generation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"

HOST_VALUES = {"available", "unavailable", "unknown"}


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


def api_available(env: dict[str, str], keys: tuple[str, ...]) -> bool:
    return all(bool(env.get(key)) for key in keys)


def host_value(env: dict[str, str], key: str) -> str:
    value = env.get(key, "unknown").strip().lower()
    if value not in HOST_VALUES:
        return "unknown"
    return value


def combine_capability(api_status: str, host_status: str) -> str:
    if api_status == "available" or host_status == "available":
        return "available"
    if api_status == "unavailable" and host_status == "unavailable":
        return "unavailable"
    return "unknown"


def runtime_mode(source_fetch_capability: str, image_generation_capability: str) -> str:
    if source_fetch_capability == "available" and image_generation_capability == "available":
        return "A"
    if source_fetch_capability == "unavailable" and image_generation_capability == "unavailable":
        return "C"
    return "B"


def build_report(env: dict[str, str]) -> dict[str, str]:
    web_api_status = (
        "available"
        if api_available(env, ("SEARCH_PROVIDER", "SEARCH_API_KEY", "SEARCH_API_ENDPOINT"))
        else "unavailable"
    )
    image_api_status = (
        "available"
        if api_available(
            env,
            ("IMAGE_PROVIDER", "IMAGE_API_KEY", "IMAGE_API_ENDPOINT", "IMAGE_MODEL"),
        )
        else "unavailable"
    )

    host_web_reader = host_value(env, "HOST_WEB_READER")
    host_image_tool = host_value(env, "HOST_IMAGE_TOOL")

    source_fetch_capability = combine_capability(web_api_status, host_web_reader)
    image_generation_capability = combine_capability(image_api_status, host_image_tool)

    mode = runtime_mode(source_fetch_capability, image_generation_capability)
    source_path = (
        "auto_fetch_or_extract"
        if source_fetch_capability == "available"
        else "manual_source_content_required"
    )
    image_path = (
        "generate_image_file"
        if image_generation_capability == "available"
        else "prompt_only_image_pending"
    )

    limitations = []
    if source_fetch_capability != "available":
        limitations.append("source fetching is not available; source_content must be user-provided")
    if image_generation_capability != "available":
        limitations.append("image file generation is not available; image_prompt should still be produced")
    if source_fetch_capability == "unknown" or image_generation_capability == "unknown":
        limitations.append("one or more host capabilities are unknown")

    return {
        "runtime_mode": mode,
        "web_api": web_api_status,
        "image_api": image_api_status,
        "host_web_reader": host_web_reader,
        "host_image_tool": host_image_tool,
        "source_fetch_capability": source_fetch_capability,
        "image_generation_capability": image_generation_capability,
        "selected_source_path": source_path,
        "selected_image_path": image_path,
        "limitations": "; ".join(limitations) if limitations else "none",
    }


def print_text(report: dict[str, str]) -> None:
    print(f"runtime_mode: {report['runtime_mode']}")
    print(f"web_api: {report['web_api']}")
    print(f"image_api: {report['image_api']}")
    print(f"host_web_reader: {report['host_web_reader']}")
    print(f"host_image_tool: {report['host_image_tool']}")
    print(f"source_fetch_capability: {report['source_fetch_capability']}")
    print(f"image_generation_capability: {report['image_generation_capability']}")
    print(f"selected_source_path: {report['selected_source_path']}")
    print(f"selected_image_path: {report['selected_image_path']}")
    print(f"limitations: {report['limitations']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print the runtime report as JSON.")
    args = parser.parse_args()

    env = parse_env(ENV_PATH)
    report = build_report(env)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
