#!/usr/bin/env python3
"""Choose the source-research path without performing network extraction."""

from __future__ import annotations

from dataclasses import dataclass


ERROR_PREFIX = "<ERROR>来源材料不足："
ERROR_SUFFIX = "</ERROR>"

REASON_NO_READABLE_LINKS = "未提供来源正文，且当前无法读取链接"
REASON_EMPTY_OR_UNREADABLE = "来源正文为空或不可读"
REASON_UNRELATED_CONTENT = "来源内容与主题不相关"
REASON_EXTRACTION_FAILED = "链接抽取失败，未得到可用正文"
REASON_UNRELATED_EXTRACTED = "抽取内容与主题不相关"

SOURCE_CONTENT_STATES = {"sufficient", "empty", "unreadable", "insufficient", "unrelated"}
SOURCE_FETCH_CAPABILITIES = {"available", "unavailable", "unknown"}
EXTRACTION_STATES = {"not_attempted", "success", "failed", "empty", "unrelated"}


@dataclass(frozen=True)
class SourcePathDecision:
    selected_source_path: str
    source_sufficiency: str
    public_error: str
    next_skill: str
    handoff_reason: str


def public_error(reason: str) -> str:
    return f"{ERROR_PREFIX}{reason}{ERROR_SUFFIX}"


def decide_source_path(
    *,
    source_content_state: str,
    has_source_links: bool,
    source_fetch_capability: str,
    extraction_state: str = "not_attempted",
) -> SourcePathDecision:
    if source_content_state not in SOURCE_CONTENT_STATES:
        raise ValueError(f"invalid source_content_state: {source_content_state}")
    if source_fetch_capability not in SOURCE_FETCH_CAPABILITIES:
        raise ValueError(f"invalid source_fetch_capability: {source_fetch_capability}")
    if extraction_state not in EXTRACTION_STATES:
        raise ValueError(f"invalid extraction_state: {extraction_state}")

    if source_content_state == "sufficient":
        return SourcePathDecision(
            selected_source_path="manual_source_content",
            source_sufficiency="sufficient",
            public_error="",
            next_skill="image-generation",
            handoff_reason="user-provided source_content is sufficient and relevant",
        )

    if source_content_state == "unrelated":
        return insufficient(REASON_UNRELATED_CONTENT)

    if has_source_links and source_fetch_capability == "available":
        if extraction_state == "not_attempted":
            return SourcePathDecision(
                selected_source_path="extract_from_links",
                source_sufficiency="pending_extraction",
                public_error="",
                next_skill="source-research",
                handoff_reason="source_links can be extracted with available source fetching capability",
            )
        if extraction_state == "success":
            return SourcePathDecision(
                selected_source_path="extract_from_links",
                source_sufficiency="sufficient",
                public_error="",
                next_skill="image-generation",
                handoff_reason="extracted source text is sufficient and relevant",
            )
        if extraction_state == "unrelated":
            return insufficient(REASON_UNRELATED_EXTRACTED)
        return insufficient(REASON_EXTRACTION_FAILED)

    if has_source_links:
        return insufficient(REASON_NO_READABLE_LINKS)

    return insufficient(REASON_EMPTY_OR_UNREADABLE)


def insufficient(reason: str) -> SourcePathDecision:
    return SourcePathDecision(
        selected_source_path="insufficient_source",
        source_sufficiency="insufficient",
        public_error=public_error(reason),
        next_skill="stop",
        handoff_reason=reason,
    )
