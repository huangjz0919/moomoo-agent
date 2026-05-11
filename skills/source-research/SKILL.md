---
name: source-research
description: 获取、抽取、验证并摘要用于 Moomoo 社区话题生成的英文来源材料。适用于 source links 需要网页文本抽取、需要英文检索，或需要判断 source_content 是否足够且相关的场景。
---

# Source Research

使用本 skill 在起草前获取或验证来源材料。

## 输入

- `topic_theme`
- `source_links`
- `source_content`
- `special_requirements`
- 可用时的 `.env` 检索配置
- `runtime_report.md` 中的 `source_fetch_capability`

## 工作流

1. 如果 `source_content` 已经充实且相关，选择 `manual_source_content`，并将其保留为主要来源。
2. 如果 `source_content` 不足、提供了 source links，且 `source_fetch_capability=available`，选择 `extract_from_links`，尽可能抽取可读的文章或页面文本。
3. 如果来源材料仍不足且检索配置存在，基于 `topic_theme` 派生英文查询。
4. 使用 `templates/source_notes.md` 保存来源笔记，包含 selected source path、public error、URL、可用标题、抽取事实和限制。
5. 如果材料为空、不可读、只有 URL，或与主题无关，选择 `insufficient_source`，并返回中文一行 `<ERROR>`。

## 规则

- 只能使用英文查询检索。
- 不得从 URL、页面标题或 URL slug 推断事实。
- 在抽取到可读内容前，不把 URL 当作证据。
- 当 `source_fetch_capability` 不可用或未知时，不把 source links 当作足够来源。
- 如果只有部分事实可用，只保留有支持的事实，并把无支持字段标为 unavailable。
- 除非抽取到的来源文本明确说明，不添加因果解释。
- 来源不足公开错误格式为 `<ERROR>来源材料不足：{一行原因}</ERROR>`。
- 公开错误只保留一个主要原因；详细限制写入 `source_notes.md`。

## 交付

返回：

- normalized `source_content`
- `sources`
- `source_limitations`
- `research_status`
- `selected_source_path`
- `public_error`
- `source_notes.md`

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
