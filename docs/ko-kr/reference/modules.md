---
title: 공식 모듈
description: FMAD에 포함된 두 모듈과 직접 모듈을 만드는 방법
sidebar:
  order: 5
---

FMAD는 두 개의 공식 모듈로 제공됩니다. `fmod-method`(코드 `method`)는 전달 스킬을, `fmod-core-tools`(코드 `core-tools`)는 `fmad` 허브와 단독 실행 도구를 제공합니다. 이 두 모듈 외에 공식 추가 모듈은 없습니다.

:::tip[모듈 설치]
`npx skills add DavidBatoDev/fmad-method`를 실행하고 원하는 스킬과 함께 `fmad`, 모듈 레코드 `fmod-method`, `fmod-core-tools`를 선택하세요. 그런 다음 `fmad` 스킬에 `fmad setup`을 실행해 달라고 요청하면 `_fmad/` 아래에 공유 런타임과 모듈 스크립트가 설치됩니다.
:::

## 커뮤니티 모듈

누구나 자신만의 모듈을 만들 수 있습니다. 모듈은 `fmod.toml` 레코드가 있는 `fmod-<code>` 폴더입니다.
