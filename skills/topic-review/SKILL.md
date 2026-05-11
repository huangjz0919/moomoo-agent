---
name: topic-review
description: 在打包前审查 Moomoo 社区话题草稿，检查事实支持、因果、中立性、ticker 格式、ASCII 标点、摘要长度、poll 均衡性和来源充分性。
---

# Topic Review

使用本 skill 在起草后、最终打包前审查内容。

## Review Checks

- 来源充分性：来源材料为空、不可读、只有 URL 或与主题无关时，必须停止输出。
- 事实：每个论断都必须由 topic theme、source content 或 special requirements 支持。
- URL 处理：除非抽取文本存在，URL 不作为事实证据。
- 因果：避免无来源支持的因果措辞。
- 事实分离：不要把两个独立事实写成因果句。
- 缺失细节：省略无支持的细节，不猜测。
- 标题：Title Case，中立且面向讨论，不超过 95 个字符，计入空格、标点和数字。
- 摘要：最多 70 个英文词，两段；第二段必须只包含一个使用 Markdown 加粗的问题句，格式为 `**Question?**`。
- Poll：中立、面向讨论，两个选项均衡。
- Ticker 格式：摘要中使用 `$Company Name (TICKER.US)$`。
- 风格：英文、ASCII 标点、官方语气。

## 输出

使用 `templates/review_report.md` 保存 `review_report.md`。

返回：

- `review_status`: `pass`, `hold`, or `fail`
- `blocking_issues`
- `revision_notes`
- `publish_ready`

来源材料不足时使用 `fail`，公开错误使用 `<ERROR>来源材料不足：{一行原因}</ERROR>`。
来源材料足够但需要修改时使用 `hold`。
只有话题包可供 Moomoo 人工发布时才使用 `pass`。

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
