---
title: "如何安装 FMAD"
description: 在项目中安装 FMAD 的分步指南
sidebar:
  order: 1
---

使用 `npx skills add DavidBatoDev/fmad-method`（随后运行 `fmad setup`）在项目中安装 FMAD，并按需选择模块和 AI 工具。

## 何时使用

- 使用 FMAD 启动新项目
- 将 FMAD 添加到现有代码库
- 更新现有的 FMAD 安装

:::note[前置条件]
- **Node.js** 20.12+（安装程序必需）
- **Git**（推荐）
- **AI 工具**（Claude Code、Cursor 或类似工具）
:::

## 步骤

### 1. 运行安装程序

```bash
npx skills add DavidBatoDev/fmad-method
```

### 2. 选择安装位置

安装程序会询问在哪里安装 FMAD 文件：

- 当前目录（如果你自己创建了目录并从该目录运行，推荐用于新项目）
- 自定义路径

### 3. 选择你的 AI 工具

选择你使用的 AI 工具：

- Claude Code
- Cursor
- 其他

每种工具都有自己的 skills 集成方式。安装程序会生成用于激活工作流和智能体的轻量提示文件，并放到该工具约定的位置。

:::note[启用 Skills]
某些平台需要你在设置中手动启用 skills 才会显示。如果你已经安装 FMAD 但看不到 skills，请检查平台设置，或直接询问你的 AI 助手如何启用 skills。
:::

### 4. 选择模块

安装程序会显示可用的模块。选择你需要的模块——大多数用户只需要 **Foundry Method**（软件开发模块）。

### 5. 按照提示操作

安装程序会引导你完成剩余步骤——设置、工具集成等。完成后，在项目文件夹中打开你的 AI 工具，让 `fmad` skill 运行 `fmad setup`。

## 你将获得

以下目录结构仅作示例。工具相关目录会随你选择的平台变化（例如可能是
`.claude/skills`、`.cursor/skills` 或 `.kiro/skills`），并不一定会同时出现。

```text
your-project/
├── _fmad/
│   ├── fmm/            # 你选择的模块
│   │   └── config.yaml # 模块设置（后续如需可修改）
│   ├── core/           # 必需核心模块
│   └── ...
├── _fmad-output/       # 生成产物
├── .claude/            # Claude Code skills（如使用 Claude Code）
│   └── skills/
│       ├── fmad-help/
│       ├── fmad-persona/
│       └── ...
└── .cursor/            # Cursor skills（如使用 Cursor）
    └── skills/
        └── ...
```

## 验证安装

运行 `fmad-help` 来验证一切正常并查看下一步操作。

**FMAD-Help 是你的智能向导**，它会：
- 确认你的安装正常工作
- 根据你安装的模块显示可用内容
- 推荐你的第一步

你也可以向它提问：
```
fmad-help 我刚安装完成，应该先做什么？
fmad-help 对于 SaaS 项目我有哪些选项？
```

## 故障排除

**安装程序抛出错误**——将输出复制粘贴到你的 AI 助手中，让它来解决问题。

**安装程序工作正常但后续出现问题**——你的 AI 需要 FMAD 上下文才能提供帮助。请参阅[如何获取关于 FMAD 的答案](./get-answers-about-fmad.md)了解如何将你的 AI 指向正确的来源。
