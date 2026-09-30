---
title: 에이전트
description: 기본 FMM 에이전트와 스킬 ID, 메뉴 트리거, 주요 워크플로
sidebar:
  order: 2
---

## 기본 에이전트

이 페이지는 Foundry Method와 함께 설치되는 기본 FMM(애자일 제품군) 에이전트를 스킬 ID, 메뉴 트리거, 주요 워크플로와 함께 나열합니다. 각 에이전트는 스킬로 호출됩니다.

## 참고

- 각 에이전트는 설치 프로그램이 생성하는 스킬로 제공됩니다. 스킬 ID(예: `fmad-agent-dev`)를 사용해 에이전트를 호출합니다.
- 트리거는 각 에이전트 메뉴에 표시되는 짧은 메뉴 코드(예: `PRD`)와 유사 매칭 항목입니다.
- QA 테스트 생성은 개발자 에이전트에서 실행할 수 있는 `fmad-qa-generate-e2e-tests` 워크플로 스킬이 처리합니다. [완료된 작업 테스트하기](../build/test-completed-work.md)를 참고하세요.

| 에이전트 | 스킬 ID | 트리거 | 주요 워크플로 |
| --- | --- | --- | --- |
| 분석가(Ember) | `fmad-agent-analyst` | `BP`, `MR`, `DR`, `TR`, `CB`, `WB`, `PC` | 브레인스토밍, 시장 리서치, 도메인 리서치, 기술 리서치, 개요 작성, PRFAQ 챌린지, 프로젝트 컨텍스트 |
| 제품 관리자(Flint) | `fmad-agent-pm` | `PRD`, `CE`, `IR`, `CC` | PRD 생성/업데이트/검증, 에픽과 스토리 생성, 구현 준비 상태(스프린트 계획 게이트), 방향 수정 |
| 아키텍트(Ferris) | `fmad-agent-architect` | `CA`, `IR` | 아키텍처 생성, 구현 준비 상태(스프린트 계획 게이트) |
| 개발자(Cinder) | `fmad-agent-dev` | `BD`, `QA`, `CR`, `SP`, `ER` | Build, QA 테스트 생성, 코드 리뷰, 스프린트 계획, 에픽 회고 |
| UX 디자이너(Sienna) | `fmad-agent-ux-designer` | `CU` | UX 설계 생성 |


## 트리거 유형

에이전트 메뉴 트리거는 구조화된 워크플로 파일을 로드합니다. 트리거 코드를 입력하면 에이전트가 워크플로를 시작하고 각 단계에서 입력을 요청합니다.

예: `PRD`(PRD 생성, 업데이트 또는 검증), `CA`(아키텍처 생성), `BD`(Build)
