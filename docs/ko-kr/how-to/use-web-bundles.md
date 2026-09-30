---
title: '웹 번들 사용하기'
description: FMAD 웹 번들을 Google Gemini Gem 또는 ChatGPT Custom GPT로 설치하기
---

웹 번들 ZIP은 [**GitHub 릴리스 `web-bundles-v1.0.0`**](https://github.com/DavidBatoDev/fmad-method/releases)에서 다운로드합니다.

## 한 곳에서 설치하는 이유

GitHub 릴리스가 번들 카탈로그의 유일한 지원 설치 경로입니다. 카탈로그가 업데이트될 때마다 태그가 붙은 GitHub 릴리스로 배포되며, 가장 최근 태그에 현재 번들이 들어 있습니다.

## 설치 단계

1. [GitHub 릴리스](https://github.com/DavidBatoDev/fmad-method/releases)에서 원하는 번들의 ZIP을 다운로드합니다. ZIP 하나에 번들 하나가 들어 있습니다.
2. ZIP 안의 `INSTRUCTIONS.md`를 엽니다. Gemini Gem과 ChatGPT Custom GPT 설정 단계를 안내합니다.
3. 안내된 단계를 따릅니다. Gem 또는 Custom GPT를 만들고, 지식 파일을 업로드하고, 지침 블록을 붙여 넣은 뒤 저장합니다.

## 사전 조건

- **Gemini Gems**: Gemini Advanced 구독.
- **ChatGPT Custom GPTs**: Plus, Pro, Business 또는 Enterprise 플랜.
- **Deep Research**를 사용하는 번들(현재 Market & Industry Research)은 프롬프트 바에서 활성화합니다(Tools → Deep Research). Deep Research에는 별도의 플랜 제한이 있습니다.

## 페르소나 커스터마이징

각 번들의 `INSTRUCTIONS.md`(ZIP 안에 있음)에는 붙여 넣기 경계 위에 **Persona Swap Example**이 포함됩니다. 설치한 지침의 `[persona]` 블록을 교체 예시로 바꾸면 프로토콜을 바꾸지 않고도 목소리를 바꿀 수 있습니다. 직접 새 페르소나를 작성해도 됩니다. 프로토콜은 그대로 유지됩니다.

## 얻는 것

- FMAD의 계획 기능 하나에 특화된 재사용 가능한 Gem 또는 Custom GPT.
- 구현을 위해 IDE에 바로 넣을 수 있는 다듬어진 산출물(제품 개요, PRD, 리서치 보고서, UX 사양).
- 계획 대화가 토큰 사용량에 따라 과금되는 IDE가 아니라 기존 웹 LLM 구독에서 실행됩니다.

:::caution[페르소나 이탈]
웹 LLM은 세션이 길어지면 가끔 페르소나 설정에서 벗어날 수 있습니다. 모델이 설정한 캐릭터와 다른 방식으로 답하기 시작하면 페르소나를 다시 알려 주거나 새 세션을 시작하세요.
:::

## 직접 만들기

각 번들은 FMAD 스킬을 `SKILL.md`, `INSTRUCTIONS.md`, 필요한 데이터 파일로 다시 패키징한 것이며, 기본 페르소나는 해당하는 FMAD 에이전트가 있으면 그 에이전트에서 가져옵니다. 직접 만들려면 [`web-bundles/`](https://github.com/DavidBatoDev/fmad-method/tree/main/web-bundles) 폴더의 기존 번들 디렉터리를 본보기로 삼으세요. 번들을 카탈로그에 제출하려면 `web-bundles/bundles.json` 항목과 번들 디렉터리를 추가하는 PR을 [FMAD-METHOD](https://github.com/DavidBatoDev/fmad-method)에 여세요.
