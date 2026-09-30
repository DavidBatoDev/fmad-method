---
title: "官方模块"
description: FMAD 自带的两个官方模块，以及如何编写你自己的模块
sidebar:
  order: 5
---

FMAD 通过模块组织能力。FMAD 只发布两个官方模块，你可以在安装时按需选择其中的 skills；除此之外没有其他官方附加模块。

:::tip[安装模块]
运行 `npx skills add DavidBatoDev/fmad-method`，选择所需的 skills，并包含 `fmad` 以及模块记录 `fmod-method` 和 `fmod-core-tools`。然后让 `fmad` skill 运行 `fmad setup`。
:::

## 先看总览

| 模块 | 代码 | 最适合 | 核心能力 |
| --- | --- | --- | --- |
| Foundry Method（`fmod-method`） | `method` | 从规划到交付的日常开发 | 规划、构建、评审与复盘等交付 skills |
| Core Tools（`fmod-core-tools`） | `core-tools` | 设置、帮助与通用辅助 | `fmad` 中枢 skill 与独立工具 |

## Foundry Method（`method`）

FMAD 的交付 skills，覆盖从规划到构建、评审与复盘的完整流程。

- **模块记录：** `fmod-method`

## Core Tools（`core-tools`）

`fmad` 中枢 skill（安装设置、状态检查与下一步建议），以及头脑风暴、party mode、自定义等独立工具。

- **模块记录：** `fmod-core-tools`

## 编写自己的模块

任何人都可以编写自己的模块：一个包含 `fmod.toml` 模块记录及其 skills 的 `fmod-<code>` 文件夹。详见 [安装自定义和社区模块](../how-to/install-custom-modules.md)。

:::note[模块可以组合安装]
模块之间不是互斥关系。你可以按项目需要增量添加 skills，之后重新运行 `fmad setup` 同步配置。
:::

## 相关参考

- [测试选项](./testing.md)
- [技能（Skills）参考](./commands.md)
- [工作流地图](./workflow-map.md)
