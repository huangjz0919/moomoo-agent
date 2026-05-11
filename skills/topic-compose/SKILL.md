---
name: topic-compose
description: 基于已验证来源材料，起草英文 Moomoo 社区话题字段，包括标题、两段摘要、poll、相关英文关键词和相关美股。
---

# Topic Compose

使用本 skill 在来源验证后起草主要社区话题字段。

## 必读记忆

可用时读取仓库内生成记忆：

- `knowledge/output-requirements.md`
- `knowledge/topic-taxonomy.md`
- `knowledge/examples.md`

事实基础只来自来源材料、用户笔记和特殊要求。

## 输入

- 已验证的 topic brief
- 标准化后的 `source_content`
- `sources`
- `special_requirements`
- 可用时的图片 prompt 数据

## 标题

- 使用 Title Case。
- 公开标题不超过 95 个字符，计入空格、标点和数字。
- 结构：基于事实的事件加面向讨论的问题。
- 当标题超过 95 个字符时，保留主要事实和讨论问题，删除次要事实点。
- 对于 `earnings_topic` 且阶段为 `pre_earnings`，使用 `[Company] to Unveil [Period] Earnings: [Question?]`。
- 即使来源是 earnings preview，收益话题标题也不得包含 `Preview`。
- 分析师或机构评论需要归属。
- 不陈述推断出的因果关系。

## 摘要

- 写两段。
- 第一段：事实信息补充。
- 第二段：一个独立讨论问题，并使用 Markdown 加粗格式：`**Question?**`。
- 问题句不得和事实信息放在同一段。
- 建议长度 40 到 60 个英文词，最多 70 个英文词。
- 使用 sentence case。
- 提及美股时使用 `$Company Name (TICKER.US)$`。

## Poll

- 创建一个中立问题和两个选项。
- 不为 `post_earnings_update` 创建 poll 输出。
- 没有特殊 poll 方向时，默认使用 bullish vs bearish 或 upside vs downside。
- 选项保持均衡且平行。
- 不暗示无来源支持的因果关系。

## Related Feed

- 生成与来源支持主题相关的英文关键词。
- 生成相关美股，主要公司放在第一位。
- 包含来源文本直接提到的相关公司。
- 只有在合适且非推测时，才包含行业同类公司。

## 全局规则

- 最终字段使用英文。
- 使用 ASCII 标点。
- 语气保持中立、官方。
- 不编造事实、数字、日期、评级、目标价、股价变动、催化因素或解释。

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
