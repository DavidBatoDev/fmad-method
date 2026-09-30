---
title: Agenti
description: Výchozí FMM agenti s jejich skill ID, spouštěči nabídky a primárními workflow
sidebar:
  order: 2
---

## Výchozí agenti

Tato stránka uvádí výchozí FMM (Agile suite) agenty, kteří se instalují s Foundry Method, společně s jejich skill ID, spouštěči nabídky a primárními workflow. Každý agent se vyvolává jako skill.

## Poznámky

- Každý agent je dostupný jako skill, generovaný instalátorem. Skill ID (např. `fmad-dev`) se používá k vyvolání agenta.
- Spouštěče jsou krátké kódy nabídky (např. `CP`) a fuzzy shody zobrazené v nabídce každého agenta.
- Generování QA testů zajišťuje workflow skill `fmad-qa-generate-e2e-tests`, dostupný přes Developer agenta.

| Agent                       | Skill ID             | Spouštěče                                    | Primární workflow                                                                                   |
| --------------------------- | -------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Analyst (Ember)              | `fmad-analyst`       | `BP`, `MR`, `DR`, `TR`, `CB`, `WB`, `DP`     | Brainstorm, průzkum trhu, doménový výzkum, technický výzkum, tvorba briefu, PRFAQ výzva, dokumentace projektu |
| Product Manager (Flint)      | `fmad-pm`            | `CP`, `VP`, `EP`, `CE`, `IR`, `CC`           | Tvorba/validace/editace PRD, tvorba epiců a stories, připravenost implementace, korekce kurzu       |
| Architect (Ferris)         | `fmad-architect`     | `CA`, `IR`                                    | Tvorba architektury, připravenost implementace                                                      |
| Developer (Cinder)          | `fmad-agent-dev`     | `BD`, `QA`, `CR`, `SP`, `ER`                  | Build, generování QA testů, revize kódu, plánování sprintu, retrospektiva epicu |
| UX Designer (Sienna)         | `fmad-ux-designer`   | `CU`                                          | Tvorba UX designu                                                                                   |


## Typy spouštěčů

Spouštěče nabídky agentů načítají strukturovaný soubor workflow. Zadejte kód spouštěče a agent zahájí workflow a vyzve vás k zadání vstupu v každém kroku.

Příklady: `CP` (tvorba PRD), `CA` (tvorba architektury), `BD` (Build)
