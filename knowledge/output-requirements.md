# 输出要求记忆

## 话题类型
- 支持 `event_topic` 和 `earnings_topic`。
- `event_topic` 沿用原 prompt 的事件型标题格式。
- `earnings_topic` 使用专门的收益标题格式。

## Event Topic Title
- 使用原始格式：
  `[Fact-based event]. [Source-backed highlight]. [Discussion question?]`
- 公开标题必须不超过 95 个字符，计入空格、标点和数字。
- 不推断因果。
- 标题保持中立，并面向讨论。

## Earnings Topic Title
- 使用：
  `[Company] to Unveil [Period] Earnings: [Question?]`
- 示例：
  `Apple to Unveil Q2 Earnings: Can iPhone And Mac Demand Deliver A Beat?`
- 如果来源材料是 earnings preview 或 earnings outlook，标题不得包含 `Preview`。
- 标题应围绕即将发布的收益讨论，而非 preview 文章本身。
- 公开标题必须不超过 95 个字符，计入空格、标点和数字。

## Earnings Update Package
- `pre_earnings` 用于业绩发布前的话题预热。
- `post_earnings_update` 用于官方业绩发布后的话题更新；已发布财报结果、财报数据、财报解读和业绩结果复盘默认使用此阶段。
- `post_earnings_update` 默认 `image_required=false`；只有用户明确要求图片时才可生成内部图片产物。
- 收益后更新只改：
  - `Updated Topic Title`
  - `Updated Topic Summary`
- 收益后更新包不得包含 Poll 输出。
- 收益后更新包不得包含公开图片输出。
- 生成 run 文件夹时，来源记录和 review 笔记只作为内部可追溯材料保存。
- 更新标题必须不超过 95 个字符，计入空格、标点和数字。

## Summary Display
- `Topic Summary` 和 `Updated Topic Summary` 必须是两段。
- 第一段放来源支持的事实信息。
- 第二段只放讨论问题，并使用 Markdown 加粗格式：`**Question?**`。
- 问题句不得和事实信息放在同一段。

## hook
- 优先使用来源支持、讨论性较强的实体，避免泛泛表述。
- 来源提到的具体产品、业务线和分析师关注点可作为 hook。
- 如果来源提到 `MacBook Neo` 或 `Mac mini`，可视为来源支持的产品实体。
- 不添加无来源支持的产品名、ticker、指标或因果关系。
