---
title: '使用 Web Bundles'
description: 将 FMAD web bundle 安装为 Google Gemini Gem 或 ChatGPT Custom GPT
---

Web bundle 的 ZIP 从 **[GitHub release `web-bundles-v1.0.0`](https://github.com/DavidBatoDev/fmad-method/releases)** 下载。

## 为什么只有一个入口

GitHub release 是架子上唯一支持的安装路径。每次架子更新都会以 tagged GitHub release 发布，最新的 tag 包含当前的 bundle。ZIP 由仓库中的 [`web-bundles/` 文件夹](https://github.com/DavidBatoDev/fmad-method/tree/main/web-bundles) 打包而成。

## 安装步骤

1. 从 [GitHub release](https://github.com/DavidBatoDev/fmad-method/releases) 下载所需 bundle 的 ZIP。每个 ZIP 包含一个 bundle。
2. 打开 ZIP 内的 `INSTRUCTIONS.md`，找到你所用平台（**Gemini Gem** 或 **ChatGPT Custom GPT**）的步骤。
3. 按步骤操作：创建 Gem 或 Custom GPT，上传 knowledge files，粘贴 instructions 块，保存。

## 前置条件

- **Gemini Gems**：Gemini Advanced 订阅。
- **ChatGPT Custom GPTs**：Plus、Pro、Business 或 Enterprise 计划。
- 使用 **Deep Research** 的 bundle（当前是 Market & Industry Research）：在 prompt bar 启用（Tools → Deep Research）。Deep Research 有各自的 plan 限制。

## 自定义 persona

每个 bundle 的 `INSTRUCTIONS.md`（ZIP 内）在 paste boundary 上方有 **Persona Swap Example**。把已安装 instructions 里的 `[persona]` 块换成 swap 示例，即可换 voice 而不动协议。也可以从零写 persona；协议不变。

## 你会得到什么

- 一个可复用的 Gem 或 Custom GPT，scoped 到一项 FMAD 规划能力。
- 打磨好的 artifact（brief、PRD、研究报告、UX spec），可直接丢进 IDE 做实现。
- 规划对话跑在现有 Web LLM 订阅上，而不是 metered IDE token。

:::caution[Persona 漂移]
Web LLM 偶尔在长会话中途掉 persona。若模型开始 out of character，提醒它的 persona 或开新会话。
:::

## 自己构建

要把现有 FMAD skill 变成 web bundle，以 [`web-bundles/`](https://github.com/DavidBatoDev/fmad-method/tree/main/web-bundles) 中现有的 bundle 目录为模板：打包该 skill 的 `SKILL.md`、包含设置步骤和粘贴块的 `INSTRUCTIONS.md`，以及 skill 所需的数据文件。默认 persona 取自对应的 FMAD agent（如有），并附上 swap-example 对比 voice。提交 bundle 到架子：在 [FMAD-METHOD](https://github.com/DavidBatoDev/fmad-method) 开 PR，添加 bundle 目录并在 `web-bundles/bundles.json` 里加条目。
