# Community Topic Agent

用于生成面向 Moomoo 的英文美股社区话题包。

## 使用方式

1. 下载或 clone 项目文件。
2. 复制 `.env.example` 为 `.env`。
3. 按需要声明宿主网页读取和图片生成能力。
4. 在 Codex、Claude Code、Cursor 或 server 环境中打开项目目录。
5. 提供 `topic_theme`、`source_links`、`source_content` 和 `special_requirements`。
6. 生成物保存到 `outputs/runs/<run_id>/`。

## 环境能力

如果当前工具环境可以读取网页和生成图片，可在 `.env` 中设置：

```bash
HOST_WEB_READER=available
HOST_IMAGE_TOOL=available
```

如果没有网页读取能力，请提供足够的 `source_content`。

如果没有图片生成能力，仍会生成图片 prompt，并将图片状态记录为 `image_pending`。

## 安装说明

详见 `docs/install.md`。

## 示例

常见输入映射见 `docs/examples.md`。

## 输出

最终话题内容为英文 Markdown，面向 Moomoo 社区发布使用。
