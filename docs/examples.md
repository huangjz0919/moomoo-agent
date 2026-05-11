# 示例指南

本文档用于人工理解输入映射，不作为生成规则来源。生成规则以 `config/`、`knowledge/` 和 `skills/` 为准。

本文档说明常见输入如何映射到话题类型、收益阶段和公开输出形态。

## 通用判断

- `topic_theme` 只作为方向。
- `source_content` 是事实基础。
- `source_links` 只有在正文可读后才可作为事实依据。
- `hook` 指来源支持的讨论素材点，可用于标题问题、摘要问题、poll 或关键词。
- 公开标题不超过 95 个字符，计入空格、标点和数字。
- 摘要必须是两段：第一段放事实信息，第二段只放加粗讨论问题。
- 加粗讨论问题格式为 `**Question?**`。

## Apple Q2 Earnings Outlook

适用场景：来源材料是收益发布前的展望、预期或机构观点。

输入特征：

- `topic_theme`: Apple Q2 earnings outlook
- `source_content`: 提到 Apple 将发布 Q2 earnings，并包含 iPhone demand、Mac demand、services growth、June-quarter guidance 等讨论点。
- `special_requirements`: 可为空。

字段映射：

- `topic_type`: `earnings_topic`
- `earnings_stage`: `pre_earnings`
- `image_required`: `true`
- 公开输出：完整话题包

可用 `hook`：

- iPhone demand
- Mac demand
- services growth
- June-quarter guidance
- App Store performance

标题示例：

```text
Apple to Unveil Q2 Earnings: Can iPhone And Mac Demand Deliver A Beat?
```

摘要问题示例：

```text
**Will investors focus more on iPhone and Mac demand, or on services growth and June-quarter guidance?**
```

判断理由：

- 来源材料讨论的是业绩发布前的预期，不是已发布结果。
- 标题使用收益预告格式，但不使用 `Preview`。
- `hook` 均来自来源材料，不添加未支持的产品、ticker 或指标。

## Nvidia ATH

适用场景：来源材料是公司事件、股价里程碑、分析师观点或行业主题。

输入特征：

- `topic_theme`: Nvidia all-time high and BofA commentary
- `source_content`: 提到 Nvidia reached an all-time high，并提到 BofA 对 cash position 的评论。
- `special_requirements`: 可为空。

字段映射：

- `topic_type`: `event_topic`
- `earnings_stage`: `not_applicable`
- `image_required`: `true`
- 公开输出：完整话题包

可用 `hook`：

- all-time high
- BofA commentary
- cash position
- AI chip demand
- valuation risk

标题示例：

```text
Nvidia Hits ATH. BofA Cites Its Cash Position. Will The Rally Continue?
```

摘要问题示例：

```text
**Will investors focus more on Nvidia's balance sheet strength or valuation risk from here?**
```

判断理由：

- 这不是收益主题，所以使用 `event_topic`。
- 分析师评论需要归属为 BofA。
- 如果来源没有说明因果关系，不把 all-time high 写成由 BofA 评论导致。

## Palantir Post-Earnings Update

适用场景：来源材料是收益发布后的正式结果，且目标是更新已有话题。

输入特征：

- `topic_theme`: Palantir Q1 post-earnings update
- `source_content`: 提到 Q1 revenue、EPS、U.S. revenue growth、commercial RDV、share performance 等已发布信息。
- `special_requirements`: 可为空。

字段映射：

- `topic_type`: `earnings_topic`
- `earnings_stage`: `post_earnings_update`
- `image_required`: `false`
- 公开输出：收益后更新包

可用 `hook`：

- revenue beat
- adjusted EPS beat
- U.S. revenue growth
- U.S. commercial RDV
- valuation pressure

标题示例：

```text
Palantir Q1 Earnings Beat Estimates: Can Growth Outrun Valuation Pressure?
```

摘要示例：

```text
$Palantir Technologies (PLTR.US)$ Q1 revenue reached $1.63B (+85% Y/Y), beating the $1.54B estimate, as U.S. revenue surged 104% Y/Y. Adjusted EPS of $0.33 topped the $0.28 consensus, and U.S. commercial RDV rose 112% Y/Y to $4.92B. Despite the beat, PLTR shares have fallen roughly 30% over six months.

**Can accelerating AI-driven growth and expanding backlog close the gap between strong fundamentals and persistent valuation concerns?**
```

判断理由：

- 来源材料是已发布结果，所以使用 `post_earnings_update`。
- 收益后更新包只包含 `Updated Topic Title` 和 `Updated Topic Summary`。
- 不输出 poll、图片、关键词、相关美股、来源或 review 状态章节。
- 标题为 74 个字符，低于 95 字符上限。
