# 用户安装

本文档用于安装和运行 Community Topic Agent，生成面向 Moomoo 的英文美股社区话题包。

## 获取文件

使用 Git：

```bash
git clone https://github.com/huangjz0919/moomoo-agent.git
cd moomoo-agent
```

或下载 release zip：

```bash
curl -L -o community-topic-agent-user-v0.1.1.zip \
  https://github.com/huangjz0919/moomoo-agent/releases/download/v0.1.1/community-topic-agent-user-v0.1.1.zip

unzip community-topic-agent-user-v0.1.1.zip
cd community-topic-agent-user-v0.1.1
```

也可以在 GitHub Releases 页面下载最新 zip：

```text
https://github.com/huangjz0919/moomoo-agent/releases
```

## 创建 `.env`

复制环境模板：

```bash
cp .env.example .env
```

`.env` 只保存在本地，不要提交真实 key。

## `.env` 字段说明

来源读取：

- `SEARCH_PROVIDER`：资讯详情页读取服务名称。使用 Codex 读取网页时可留空。
- `SEARCH_API_KEY`：资讯详情页读取 API key。使用 Codex 读取网页时可留空。
- `SEARCH_API_ENDPOINT`：资讯详情页读取 API 地址，可填写官方地址、代理地址或企业网关地址。
- `SEARCH_MAX_RESULTS`：检索结果数量上限。
- `SOURCE_FETCH_TIMEOUT_SECONDS`：每次读取资讯详情页的等待秒数。

图片生成：

- `IMAGE_PROVIDER`：图片生成服务名称。使用 Codex 宿主生图时可留空。
- `IMAGE_API_KEY`：图片生成 API key。使用 Codex 宿主生图时可留空。
- `IMAGE_API_ENDPOINT`：图片生成 API 地址，可填写官方地址、代理地址或企业网关地址。
- `IMAGE_MODEL`：图片生成模型名称，启用图片 API 时填写。
- `IMAGE_SIZE`：目标图片尺寸，默认 `750x375`。

宿主能力：

- `HOST_WEB_READER`：当前工具环境是否能直接读取网页。
- `HOST_IMAGE_TOOL`：当前工具环境是否能直接生成图片。
- 允许值：`available`、`unavailable`、`unknown`。

输出设置：

- `OUTPUT_ROOT`：话题包和中间产物保存目录。
- `DEFAULT_PLATFORM`：默认发布平台。

## 推荐配置

在 Codex 中使用网页读取和生图能力时，可在 `.env` 中设置：

```bash
HOST_WEB_READER=available
HOST_IMAGE_TOOL=available
```

如果不确认宿主能力，保留默认值：

```bash
HOST_WEB_READER=unknown
HOST_IMAGE_TOOL=unknown
```

## Endpoint 用途

`SEARCH_API_ENDPOINT` 和 `IMAGE_API_ENDPOINT` 是 API 请求地址。没有 API 或使用 Codex 宿主能力时可以留空。

需要经过代理、企业网关或兼容服务时，在这里填写对应地址。

## Codex 用法

在 Codex 中打开项目目录。创建 `.env` 后，提供：

- `topic_theme`
- `source_links`
- `source_content`
- `special_requirements`

如果 Codex 可以读取网页，`source_links` 可用于来源读取。如果无法读取网页，请提供足够的 `source_content`。

## Claude Code 用法

在 Claude Code 中打开项目目录。创建 `.env` 后，按仓库入口说明生成话题包。

如果网页读取能力不可用，请提供足够的 `source_content`。如果图片生成能力不可用，仍会生成图片 prompt，并将图片状态记录为 `image_pending`。

## Cursor 用法

在 Cursor 中打开项目目录，并启用仓库规则文件。创建 `.env` 后，提供话题主题、来源链接或来源正文，以及特殊要求。

## Server 用法

server 环境需要能运行 Python 脚本并读取项目文件。创建 `.env` 后，可查看运行能力：

```bash
python3 scripts/check_runtime.py
```

server 没有网页读取或图片生成能力时，按无 API 模式使用：提供 `source_content`，图片保留为 prompt-only 状态。

## 无 API 模式

没有来源读取 API，也没有宿主网页读取能力时，必须提供足够的 `source_content`。

没有图片 API，也没有宿主生图能力时，只生成图片 prompt，图片状态为 `image_pending`。

## 示例

Apple Q2、Nvidia ATH 和 Palantir 收益后更新的输入映射见 `docs/examples.md`。
