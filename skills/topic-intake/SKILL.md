---
name: topic-intake
description: 将用户提供的社区话题输入整理为结构化 brief，用于生成 Moomoo 美股话题。适用于请求中包含 topic_theme、source links、source content、由截图转写的文本、笔记或特殊要求，并且需要在研究或起草前整理输入的场景。
---

# Topic Intake

使用本 skill 将用户的原始请求转换为标准 input brief。

## 必填字段

返回包含以下字段的 brief：

- `topic_theme`
- `source_links`
- `source_content`
- `special_requirements`
- `platform`
- `image_required`
- `topic_type`
- `earnings_stage`

`platform` 默认设为 `moomoo`。
`image_required` 默认设为 `true`。
当 `earnings_stage=post_earnings_update` 时，`image_required` 默认设为 `false`；只有用户明确要求图片时才设为 `true`，且图片只作为内部 run 产物。
当用户未明确提供 `topic_type` 或 `earnings_stage` 时，基于主题和来源材料保守判断；判断不足时，在 `classification_notes` 中说明。

## 规则

- 已发布财报结果、财报数据、财报解读或业绩结果复盘，默认判为 `earnings_topic` + `post_earnings_update`。
- 财报发布前预期、预告、展望或机构预览，默认判为 `earnings_topic` + `pre_earnings`。
- 经济数据、宏观数据和公司事件默认判为 `event_topic`。
- 将 `topic_theme` 视为方向，不视为证据。
- 将 `source_content` 视为主要事实材料。
- 在内容被抽取前，`source_links` 只作为归属和可追溯信息。
- 将 `special_requirements` 视为偏好；如果与来源文本冲突，以来源文本为准。
- 不添加事实、ticker、日期、价格变动或解释。

## 交付

使用 `templates/topic_brief.md` 保存 `topic_brief.md`。
当需要来源抽取或验证时，将 brief 交给 `source-research`。
只有在 `source_content` 已足够时，才可直接交给 `topic-compose`。

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
