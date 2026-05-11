# Community Topic Agent

本仓库是一个可迁移的本地 agent，用于创建面向 Moomoo 的英文美股社区话题包。

## 必读文件
- 社区话题生成：`knowledge/output-requirements.md`、`knowledge/topic-taxonomy.md`、`knowledge/visual-style.md`、`knowledge/examples.md`
- 社区话题生成：`config/project_rules.md`、`config/output_contract.md`、`config/language_policy.md`
- 社区话题生成：相关的 `skills/*/SKILL.md` 文件

## 生成边界
- `knowledge/` 记录可复用的输出要求、示例、话题分类和视觉风格指引。
- 每个话题的事实基础只能来自来源 URL 的抽取文本、用户笔记和特殊要求。
- 不得从 URL、页面标题、URL slug、ticker 热度或通用市场记忆推断事实。

## 工作流
1. 使用 `scripts/check_runtime.py` 判断网页读取和图片生成能力，并保存 `runtime_report.md`。
2. 使用 `skills/topic-intake` 整理用户的话题请求。
3. 使用 `skills/source-research` 获取或验证来源文本。
4. 当 `image_required=true` 且来源足够时，使用 `skills/image-generation` 创建图片 prompt；图片文件是否生成取决于运行能力。
5. 使用 `skills/topic-compose` 起草话题字段。
6. 使用 `skills/topic-review` 验证事实、因果、语气、ticker 格式和输出形态。
7. 使用 `skills/moomoo-package` 创建最终 Markdown 包。

## 运行说明
- 如存在 `.env`，读取其中配置。
- 不要提交 `.env`。
- 只能使用英文查询检索。
- 最终社区话题内容保持英文。
- 输出保存到 `outputs/runs/<run_id>/`。
- 收益后更新包只改标题和摘要，不包含 poll 输出。
