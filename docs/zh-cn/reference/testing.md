---
title: "测试选项"
description: 内置 QA workflow：做什么、何时使用、边界是什么
sidebar:
  order: 6
---

FMAD 提供内置 QA workflow，用于快速生成可运行测试。

## 内置 QA Workflow

内置 QA workflow（`fmad-qa-generate-e2e-tests`）是 FMM 模块的一部分，通过 Developer 智能体调用。目标是用你现有测试栈快速落地测试，不要求额外配置。

**触发方式：**
- 菜单触发器：`QA`（通过 Developer 智能体）
- skill：`fmad-qa-generate-e2e-tests`

### QA Workflow 会做什么

QA Automate 流程通常包含 5 步：
1. 检测现有测试框架（如 Jest、Vitest、Playwright、Cypress）
2. 确认待测功能（手动指定或自动发现）
3. 生成 API 测试（状态码、结构、主路径与错误分支）
4. 生成 E2E 测试（语义定位器 + 可见结果断言）
5. 执行并修复基础失败项

**默认风格：**
- 仅使用标准框架 API
- UI 测试优先语义定位器（角色、标签、文本）
- 测试互相独立，不依赖顺序
- 避免硬编码等待/休眠

:::note[范围边界]
QA workflow 只负责”生成测试”。如需实现质量评审与故事验收，请配合代码审查 workflow（`CR` / `fmad-code-review`）。
:::

### 何时用内置 QA

- 要快速补齐某个功能的测试覆盖
- 团队希望先获得可运行基线，再逐步增强
- 项目暂不需要完整测试治理体系

## 测试放在流程的哪个位置

按 FMAD workflow-map，测试位于阶段 4（实施）：

1. epic 内逐个 story：使用 Build（`BD` / `fmad-build`）实施，并按需追加代码审查（`CR` / `fmad-code-review`）
2. epic 完成后：用 `QA`（通过 Developer 智能体）统一生成/补齐测试
3. 最后执行复盘（`fmad-retrospective`）

内置 QA workflow 主要依据代码直接生成测试，不加载上游规划产物（如 PRD、architecture）。

## 相关参考

- [官方模块](./modules.md)
- [工作流地图](./workflow-map.md)
- [智能体参考](./agents.md)
