---
title: Các agent
description: Các agent mặc định của FMM cùng skill ID, trigger menu và workflow chính
sidebar:
  order: 2
---

## Các Agent Mặc Định

Trang này liệt kê các agent mặc định của FMM (bộ Agile suite) được cài cùng với Foundry Method, bao gồm skill ID, trigger menu và workflow chính của chúng. Mỗi agent được gọi dưới dạng một skill.

## Ghi Chú

- Mỗi agent đều có sẵn dưới dạng một skill do trình cài đặt tạo ra. Skill ID, ví dụ `fmad-dev`, được dùng để gọi agent.
- Trigger là các mã menu ngắn, ví dụ `CP`, cùng với các fuzzy match hiển thị trong menu của từng agent.
- Việc tạo test QA do workflow skill `fmad-qa-generate-e2e-tests` đảm nhận, khả dụng thông qua Developer agent.

| Agent | Skill ID | Trigger | Workflow chính |
| --------------------------- | -------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| Analyst (Ember) | `fmad-analyst` | `BP`, `MR`, `DR`, `TR`, `CB`, `WB`, `DP` | Brainstorm, Market Research, Domain Research, Technical Research, Create Brief, PRFAQ Challenge, Document Project |
| Product Manager (Flint) | `fmad-pm` | `CP`, `VP`, `EP`, `CE`, `IR`, `CC` | Create/Validate/Edit PRD, Create Epics and Stories, Implementation Readiness, Correct Course |
| Architect (Ferris) | `fmad-architect` | `CA`, `IR` | Create Architecture, Implementation Readiness |
| Developer (Cinder) | `fmad-agent-dev` | `BD`, `QA`, `CR`, `SP`, `ER` | Build, QA Test Generation, Code Review, Sprint Planning, Epic Retrospective |
| UX Designer (Sienna) | `fmad-ux-designer` | `CU` | Create UX Design |

## Các Loại Trigger

Trigger trong menu agent sẽ nạp một file workflow có cấu trúc. Bạn gõ mã trigger, agent sẽ bắt đầu workflow và nhắc bạn nhập thông tin ở từng bước.

Ví dụ: `CP` (Create PRD), `CA` (Create Architecture), `BD` (Build)
