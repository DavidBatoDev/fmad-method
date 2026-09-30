---
title: 欢迎使用 FMAD 方法
description: 具备专业智能体、引导式工作流与智能规划的 AI 驱动开发框架
---

FMAD 方法（**F**oundry **M**ethod for **A**gile AI-Driven **D**evelopment）是 FMAD 方法生态中的 AI 驱动开发框架模块，覆盖从构思、规划到智能体实施的完整软件交付流程。它提供专业智能体、引导式工作流和可随项目复杂度调整的智能规划，无论是修复 bug 还是构建企业级平台都适用。

如果你已经习惯使用 Claude、Cursor 或 GitHub Copilot 这类 AI 编码助手，现在就可以开始。

## 新手入门？先从教程开始

理解 FMAD 的最快方式是亲自尝试。

- **[FMAD 入门教程](./tutorials/getting-started.md)** — 安装并理解 FMAD 如何工作
- **[工作流地图](./reference/workflow-map.md)** — FMM 阶段、工作流与上下文管理的全景视图

:::tip[只想直接上手？]
安装 FMAD 后运行 `fmad-help`，它会根据你的项目状态和已安装模块给出下一步建议。
:::

## 如何使用这些文档

这些文档按你的目标分成四个部分：

| 部分 | 用途 |
| --- | --- |
| **教程** | 学习导向。通过分步引导带你做成一件事。第一次使用建议从这里开始。 |
| **操作指南** | 任务导向。解决具体问题的实用文档，例如“如何自定义智能体”。 |
| **说明** | 理解导向。深入讲解概念与架构，适合回答“为什么”。 |
| **参考** | 信息导向。提供智能体、工作流和配置项的技术规格。 |

## 扩展与自定义

想用自己的智能体、工作流或模块扩展 FMAD？你可以编写自己的 skill 或模块（一个带有 `fmod.toml` 记录的 `fmod-<code>` 文件夹）。如需自定义现有智能体和工作流，请使用 `fmad-customize` skill。

## 你需要准备什么

FMAD 可与任何支持自定义系统提示词或项目上下文的 AI 编码助手配合使用，常见选择包括：

- **[Claude Code](https://code.claude.com)** — Anthropic 的 CLI 工具（推荐）
- **[Cursor](https://cursor.sh)** — AI 优先的代码编辑器
- **[Codex CLI](https://github.com/openai/codex)** — OpenAI 的终端编码智能体

你需要了解一些基础软件工程概念，例如版本控制、项目结构和敏捷工作流。即使没有使用过 FMAD 风格智能体系统，也可以从这些文档开始上手。

## 加入社区

获取帮助、分享成果，或参与贡献：

- **[GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions)** — 与其他 FMAD 用户交流、提问、分享想法
- **[GitHub](https://github.com/DavidBatoDev/fmad-method)** — 源代码、问题和贡献

## 下一步

准备好开始了吗？**[从 FMAD 入门教程开始](./tutorials/getting-started.md)**，构建你的第一个项目。
