---
name: image-generation
description: 为 Moomoo 社区话题创建简洁英文背景图 prompt，并生成或标记 750x375 金融新闻 banner 图片。适用于话题包需要背景视觉的场景。
---

# Image Generation

使用本 skill 创建话题背景图 prompt 和图片文件。

## 必读记忆

当话题涉及单个公司或产品时，读取 `knowledge/visual-style.md`。
图片指引只来自来源材料、用户要求和 `knowledge/visual-style.md`。

## 输入

- `topic_theme`
- 已验证的 `source_content`
- 有来源支持的关键公司名和 ticker
- 可用时的 `.env` 图片配置
- `runtime_report.md` 中的 `image_generation_capability`

## Prompt 规则

- 写一个简洁的英文图片生成 prompt。
- 匹配话题主题。
- 只有在公司已被明确识别时，才包含相关公司 logo。
- 对于个股话题，适合时体现公司的视觉身份、产品、颜色和设计语言。
- 来源支持的具体产品实体优先于泛泛业务线措辞。
- 只使用英文文字。
- 请求 750x375 financial news banner。
- 使用官方、现代、市场导向的风格。
- 适合时使用公司品牌色。

## 图片规则

- 当 `image_required=true` 且来源材料足够时，无论图片文件生成能力是否可用，都生成 `image_prompt`。
- 如果 `image_generation_capability=available`，在 run 文件夹下创建 750x375 图片文件。
- 如果 `image_generation_capability` 不可用或未知，将图片状态设为 `image_pending`，并保留图片 prompt。
- 不编造图片路径。

## 交付

返回：

- `image_prompt`
- `image_status`
- `image_path`

## Prompt Source

读取 `references/prompt-sections.md`，了解本 skill 对应的原 prompt 片段。
