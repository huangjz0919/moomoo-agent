# 来源研究执行路径

## 目的

定义 `source-research` 如何从用户输入和 runtime 能力中选择来源处理路径，并在来源不足时给出中文公开错误。

## 路径

### manual_source_content
- 适用条件：用户提供的 `source_content` 有实质内容，且与 `topic_theme` 相关。
- 行为：直接验证来源充分性，整理 supported facts，写入 `source_notes.md`，然后交给后续生成步骤。
- 限制：仍需执行事实和因果审查；不能把 `topic_theme` 当作证据。

### extract_from_links
- 适用条件：`source_content` 不足，用户提供 `source_links`，且 `source_fetch_capability=available`。
- 行为：使用 API 或宿主网页读取能力抽取正文；抽取成功且相关时，整理 supported facts 并继续。
- 检索 fallback：当用户未提供可用正文和可抽取链接，但检索配置可用时，可基于 `topic_theme` 使用英文查询寻找来源；检索结果仍必须抽取到可读正文后才能作为事实来源。
- 限制：URL、页面标题和 URL slug 不能作为事实证据；只有抽取到的可读正文可作为事实来源。

### insufficient_source
- 适用条件：
  - `source_content` 为空、不可读或与主题无关。
  - 只有 `source_links`，但 `source_fetch_capability` 为 `unavailable` 或 `unknown`。
  - 链接抽取失败，未得到可用正文。
  - 抽取内容与主题无关。
- 行为：写入内部 `source_notes.md` 或失败说明，公开输出中文 `<ERROR>`，不生成部分话题包。

## 中文错误输出

公开失败输出使用一行中文：

```text
<ERROR>来源材料不足：{一行原因}</ERROR>
```

允许的主要原因：

- `未提供来源正文，且当前无法读取链接`
- `来源正文为空或不可读`
- `来源内容与主题不相关`
- `链接抽取失败，未得到可用正文`
- `抽取内容与主题不相关`

公开错误只保留一个主要原因。详细限制、尝试过的来源和失败细节写入 `source_notes.md`。
