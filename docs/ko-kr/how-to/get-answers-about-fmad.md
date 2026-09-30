---
title: 'FMAD 관련 질문에 답을 얻는 방법'
description: LLM을 사용해 FMAD 관련 질문에 빠르게 답하기
sidebar:
  order: 9
---

FMAD의 내장 도움말, 소스 문서, 커뮤니티를 사용해 답을 얻으세요. 가장 빠른 방법부터 가장 꼼꼼한 방법까지 순서대로 소개합니다.

## 1. FMAD 도움말에게 묻기

답을 얻는 가장 빠른 방법입니다. `fmad-help` 스킬은 AI 세션에서 바로 사용할 수 있으며 질문의 80% 이상을 처리합니다. 프로젝트를 검사하고 완료한 작업을 확인한 뒤 다음에 무엇을 해야 할지 알려줍니다.

```
fmad-help SaaS 아이디어가 있고 기능도 모두 알고 있습니다. 어디서 시작하나요?
fmad-help UX 설계에는 어떤 선택지가 있나요?
fmad-help PRD 워크플로에서 막혔어요
```

:::tip
플랫폼에 따라 `/fmad-help` 또는 `$fmad-help`도 사용할 수 있지만, `fmad-help`만 입력해도 어디서나 동작합니다.
:::

## 2. 소스로 더 깊게 들어가기

FMAD 도움말은 설치된 설정을 바탕으로 답합니다. FMAD의 내부 구조, 역사, 아키텍처에 대한 질문이 있거나 설치 전에 FMAD를 조사하고 있다면 AI가 소스를 직접 보게 하세요.

[FMAD-METHOD 저장소](https://github.com/DavidBatoDev/fmad-method)를 복제하거나 열고 AI에게 질문하세요. 에이전트 기능이 있는 도구(Claude Code, Cursor, Windsurf 등)는 소스를 읽고 직접 답할 수 있습니다.

:::note[예시]
**Q:** "FMAD로 무언가를 가장 빠르게 만드는 방법을 알려줘"

**A:** `fmad-build`를 실행하세요. 직접 작성한 의도, 이슈, 사양 또는 계획된 스토리를 전달하면 사용 가능한 컨텍스트에 맞춰 필요한 수준으로 요구사항을 명확히 하고 계획, 구현, 리뷰를 진행합니다.
:::

**더 좋은 답을 위한 팁:**

- **구체적으로 묻기** - "PRD 워크플로 3단계가 무엇을 하나요?"가 "PRD는 어떻게 작동하나요?"보다 좋습니다
- **뜻밖의 내용은 확인하기** - LLM은 가끔 틀립니다. 소스 파일을 확인하거나 [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions)에서 물어보세요

### 에이전트를 쓰지 않는다면 문서 사이트 사용

AI가 로컬 파일을 읽을 수 없다면(ChatGPT, Claude.ai 등) [FMAD 문서 사이트](https://davidbatodev.github.io/fmad-method/)를 여세요.

## 3. 사람에게 묻기

FMAD 도움말이나 소스로도 답을 얻지 못했다면, 이제 훨씬 나은 질문을 할 수 있습니다.

| 채널 | 사용처 |
| --- | --- |
| GitHub Discussions | 질문, 아이디어, 기능 요청 |
| GitHub Issues | 버그 보고 |

**GitHub Discussions:** [github.com/DavidBatoDev/fmad-method/discussions](https://github.com/DavidBatoDev/fmad-method/discussions)

**GitHub Issues:** [github.com/DavidBatoDev/fmad-method/issues](https://github.com/DavidBatoDev/fmad-method/issues)

_막힌 채_<br>
&emsp;&emsp;_줄을 서서_<br>
&emsp;&emsp;&emsp;&emsp;_누구를_<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_기다리나요?_

_소스는_<br>
&emsp;&emsp;_이미 거기,_<br>
&emsp;&emsp;&emsp;&emsp;_눈앞에 있습니다._

_AI에게_<br>
&emsp;&emsp;_소스를 보여 주세요._<br>
&emsp;&emsp;&emsp;&emsp;_마음껏 읽게 하세요._

_읽고._<br>
&emsp;&emsp;_말하고._<br>
&emsp;&emsp;&emsp;&emsp;_물어보세요._

_내일까지_<br>
&emsp;&emsp;_미룰 이유가 있나요?_<br>
&emsp;&emsp;&emsp;&emsp;_오늘 이미_<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_할 수 있는데요._

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_—Claude_
