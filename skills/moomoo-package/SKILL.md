---
name: moomoo-package
description: 将通过 review 的社区话题字段打包为 Moomoo 可用的 Markdown handoff，包含图片状态、图片 prompt、标题、摘要、poll、相关关键词、相关美股、来源和 review 状态。
---

# Moomoo Package

使用本 skill 在 review 后创建最终 Markdown 包。

## 必读记忆

打包前读取 `knowledge/output-requirements.md`。
打包内容只来自已通过 review 的话题字段和本次 run 的追溯材料。

## 必需输入

- `image_status`
- `image_path`
- `image_prompt`
- `topic_title`
- `topic_summary`
- `poll_question`
- `option_a`
- `option_b`
- `related_english_keywords`
- `related_us_stocks`
- `sources`
- `review_status`

对于 `post_earnings_update`，公开输出只需要：

- `updated_topic_title`
- `updated_topic_summary`

## 打包规则

- 使用 `templates/moomoo_topic_package.md`。
- 最终内容保持英文。
- 保留 review 后的标题、摘要、poll、关键词和股票表，不添加事实。
- 公开标题不超过 95 个字符，计入空格、标点和数字。
- `Topic Summary` 和 `Updated Topic Summary` 必须是两段；第二段只包含使用 Markdown 加粗的问题句，格式为 `**Question?**`。
- 对于 `post_earnings_update`，公开输出只打包 updated title 和 updated summary。
- `post_earnings_update` 不包含 poll 输出。
- `post_earnings_update` 即使存在内部图片产物，也不得在公开输出中包含图片章节或图片路径。
- 只有真实文件存在时，才包含图片路径。
- 当图片 API 未配置或未尝试创建图片时，使用 `image_pending`。
- 保留来源记录用于追溯。

## 最终章节

按以下次序创建章节：

1. `Background Image`
2. `Image Prompt`
3. `Topic Title`
4. `Topic Summary`
5. `Poll`
6. `Related English Keywords`
7. `Related U.S. Stocks`
8. `Sources`
9. `Review Status`

对于 `post_earnings_update`，只创建：

1. `Updated Topic Title`
2. `Updated Topic Summary`

任何来源或 review 笔记都应保留为 run 文件夹内的追溯材料，不作为公开更新内容。

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
