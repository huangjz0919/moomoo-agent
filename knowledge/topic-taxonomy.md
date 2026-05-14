# 话题分类

## topic_type

### event_topic
- 用于公司事件、指数里程碑、产品发布、股价变动、分析师观点、行业主题和宏观相关讨论话题。
- 经济数据和宏观数据默认使用此类型，除非来源明确是在讨论某家公司已发布或即将发布的业绩。
- 标题格式遵循原社区话题 prompt。

### earnings_topic
- 用于即将发布的业绩、业绩展望、业绩预览、已发布结果和结果后更新。
- 收益话题按阶段采用不同规则。

## earnings_stage

### pre_earnings
- 用于官方业绩结果发布前。
- 来源材料可以包含 earnings preview、分析师展望、市场预期、财报发布前预告或机构预览。
- 标题使用 `[Company] to Unveil [Period] Earnings: [Question?]`。
- 标题不得包含 `Preview`。

### post_earnings_update
- 用于官方业绩结果发布后。
- 来源材料是已发布财报结果、财报数据、财报解读或业绩结果复盘时，默认使用此阶段。
- 为已有话题生成更新内容。
- 公开更新输出只包含 updated title 和 updated summary。
- 不包含 poll 输出。
