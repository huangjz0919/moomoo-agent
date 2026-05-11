# 示例记忆

本文档是 agent 生成时可读取的短 pattern 记忆，用于模仿标题、摘要问题和 source-backed hooks。
长说明和人工解释放在 `docs/examples.md`。

## Apple Q2 Earnings Topic

### Earnings Title Pattern
`Apple to Unveil Q2 Earnings: Can iPhone And Mac Demand Deliver A Beat?`

### Summary Question Pattern
`**Will investors focus more on iPhone and Mac demand, or on services growth and June-quarter guidance?**`

### Useful Source-Backed Hooks
- iPhone demand
- Mac demand
- MacBook Neo
- Mac mini
- June-quarter guidance
- Services growth
- App Store performance

### 说明
- 即使来源是 earnings preview，标题也避免使用 `Preview`。
- 有来源支持的具体产品 hook，通常比宽泛业务线措辞更适合讨论。
- 所有产品引用都必须有来源支持。

## Nvidia Event Topic

### Event Title Pattern
`Nvidia Hits ATH. BofA: It's Sitting On A Pile Of Cash. Will The Rally Continue?`

### Event Summary Question Pattern
`**Will investors focus more on Nvidia's balance sheet strength or valuation risk from here?**`

### 说明
- 事件型话题可保留原 prompt 的事件加问题标题格式。
- 分析师评论需要标明归属。
- 公开标题必须不超过 95 个字符，计入空格、标点和数字。
- 除非来源说明因果关系，不要把单独的分析师评论写成股价变动原因。
