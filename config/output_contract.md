# 输出契约

## 输入 Brief

每次运行都应把用户输入整理为以下字段：

- `topic_theme`
- `source_links`
- `source_content`
- `special_requirements`
- `platform`
- `image_required`
- `topic_type`
- `earnings_stage`

当用户没有明确提供 `topic_type` 或 `earnings_stage` 时，agent 可根据主题和来源材料保守判断。判断不充分时，应在内部 review 笔记中标明不确定性。

## 完整话题包

以下类型使用完整话题包：

- `event_topic`
- `earnings_topic` + `pre_earnings`

完整话题包必须按次序包含以下公开 Markdown 章节：

1. `Background Image`
2. `Image Prompt`
3. `Topic Title`
4. `Topic Summary`
5. `Poll`
6. `Related English Keywords`
7. `Related U.S. Stocks`
8. `Sources`
9. `Review Status`

公开 `Topic Title` 必须不超过 95 个字符。字符数按 Python `len(title)` 口径计算，计入空格、标点和数字。

公开 `Topic Summary` 必须是两段：第一段放事实信息，第二段只放讨论问题。第二段必须使用 Markdown 加粗格式：`**Question?**`。

## 收益后更新包

以下类型使用收益后更新包：

- `earnings_topic` + `post_earnings_update`

收益后更新包只允许包含以下公开 Markdown 章节：

1. `Updated Topic Title`
2. `Updated Topic Summary`

收益后更新包不得包含公开 `Poll` 输出，也不得包含公开图片、关键词、相关美股、来源或 review 状态章节。来源记录和 review 笔记只作为 run 文件夹中的内部追溯材料保存。

公开 `Updated Topic Title` 必须不超过 95 个字符。字符数按 Python `len(title)` 口径计算，计入空格、标点和数字。

公开 `Updated Topic Summary` 必须是两段：第一段放事实信息，第二段只放讨论问题。第二段必须使用 Markdown 加粗格式：`**Question?**`。

## 内部追溯文件

每次生成可在 `outputs/runs/<run_id>/` 下保存内部追溯文件。内部追溯文件不属于公开 Markdown 包，不改变完整话题包或收益后更新包的公开章节。

建议文件：

- `runtime_report.md`：保存网页读取能力、图片生成能力、宿主能力声明、运行模式和降级限制。
- `topic_brief.md`：保存标准化后的输入 brief、话题类型判断和用户要求。
- `source_notes.md`：保存来源执行路径、来源链接、抽取文本摘要、可用事实、公开错误、限制和来源充分性判断。
- `review_report.md`：保存 review 状态、阻塞问题、修改建议和发布就绪判断。
- `final_package.md`：保存符合公开输出契约的最终 Markdown。

## 运行能力模式

运行前应判断两类能力：

- `source_fetch_capability`：网页读取或来源抽取能力。
- `image_generation_capability`：图片文件生成能力。

能力可以来自 `.env` 中的 API 配置，也可以来自宿主能力声明：

- `HOST_WEB_READER`
- `HOST_IMAGE_TOOL`

宿主能力允许值为 `available`、`unavailable`、`unknown`。未声明时按 `unknown` 处理，不直接视为可用。

总模式：

- `Mode A`：网页读取能力和图片生成能力都可用。可自动获取来源并生成图片文件。
- `Mode B`：只具备其中一项能力。缺网页读取能力时依赖用户提供 `source_content`；缺图片能力时仍生成 `image_prompt`，图片状态为 `image_pending`。
- `Mode C`：两项能力都不可用。依赖用户提供 `source_content`；来源足够时仍生成 `image_prompt`，图片状态为 `image_pending`。

当 `image_required=true` 且来源材料足够时，无论图片文件生成能力是否可用，都应生成 `image_prompt`。图片文件是否生成取决于 `image_generation_capability`。

来源不足时，可保存内部失败说明，但公开输出仍必须只包含一行中文 `<ERROR>`。

## 来源研究路径

来源研究使用三条路径：

- `manual_source_content`：用户提供足够且相关的 `source_content`，直接验证并整理 supported facts。
- `extract_from_links`：`source_content` 不足，存在 `source_links`，且 `source_fetch_capability=available`，尝试抽取正文。
- `insufficient_source`：正文为空、不可读、不相关，或只有链接但无法读取，或链接抽取失败。

URL、页面标题和 URL slug 不能作为事实证据。只有抽取到的可读正文或用户提供的 `source_content` 可作为事实来源。

## 失败输出

如果来源材料不足，必须准确输出一行中文错误：

```text
<ERROR>来源材料不足：{一行原因}</ERROR>
```

允许的主要原因：

- `未提供来源正文，且当前无法读取链接`
- `来源正文为空或不可读`
- `来源内容与主题不相关`
- `链接抽取失败，未得到可用正文`
- `抽取内容与主题不相关`

公开错误只保留一个主要原因。当写入 run 文件夹时，详细限制保存在 `source_notes.md`。
