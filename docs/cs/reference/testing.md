---
title: Možnosti testování
description: Vestavěný QA agent (Quinn) pro automatizaci testů.
sidebar:
  order: 6
---

FMAD poskytuje vestavěného QA agenta pro rychlé generování testů.

## Vestavěný QA agent (Quinn)

Quinn je vestavěný QA agent v modulu FMM (Agile suite). Rychle generuje funkční testy pomocí existujícího testovacího frameworku vašeho projektu — bez konfigurace nebo další instalace.

**Spouštěč:** `QA` nebo `fmad-qa-generate-e2e-tests`

### Co Quinn dělá

Quinn spouští jeden workflow (Automate), který projde pěti kroky:

1. **Detekce testovacího frameworku** — skenuje `package.json` a existující testovací soubory pro váš framework (Jest, Vitest, Playwright, Cypress nebo jakýkoli standardní runner). Pokud neexistuje, analyzuje stack projektu a navrhne jeden.
2. **Identifikace funkcí** — zeptá se, co testovat, nebo automaticky objeví funkce v kódové bázi.
3. **Generování API testů** — pokrývá stavové kódy, strukturu odpovědí, happy path a 1–2 chybové případy.
4. **Generování E2E testů** — pokrývá uživatelské workflow se sémantickými lokátory a asercemi viditelných výsledků.
5. **Spuštění a ověření** — provede generované testy a okamžitě opraví selhání.

Quinn produkuje shrnutí testů uložené do složky implementačních artefaktů vašeho projektu.

### Vzory testů

Generované testy sledují filozofii „jednoduché a udržovatelné“:

- **Pouze standardní API frameworku** — žádné externí utility nebo vlastní abstrakce
- **Sémantické lokátory** pro UI testy (role, popisky, text místo CSS selektorů)
- **Nezávislé testy** bez závislostí na pořadí
- **Žádné hardcoded waity nebo sleep**
- **Jasné popisy**, které se čtou jako dokumentace funkcí

:::note[Rozsah]
Quinn generuje pouze testy. Pro revizi kódu a validaci stories použijte workflow Code Review (`CR`).
:::

### Kdy použít Quinna

- Rychlé pokrytí testy pro novou nebo existující funkci
- Automatizace testů přátelská k začátečníkům bez pokročilého nastavení
- Standardní vzory testů, které může číst a udržovat jakýkoli vývojář
- Malé až střední projekty, kde komplexní testovací strategie není potřeba

## Jak testování zapadá do workflow

Quinn workflow Automate se objevuje ve Fázi 4 (Implementace) mapy workflow Foundry Method. Je navržen ke spuštění **po dokončení celého epicu** — jakmile jsou všechny stories v epicu implementovány a zrevidovány. Typická sekvence:

1. Pro každou story v epicu: implementace pomocí Build (`BD` / `fmad-build`), pak podle potřeby Code Review (`CR`)
2. Po dokončení epicu: generování testů s Quinnem (`QA`)
3. Spuštění retrospektivy (`fmad-retrospective`) pro zachycení získaných zkušeností

Quinn pracuje přímo ze zdrojového kódu bez načítání plánovacích dokumentů (PRD, architektura).

Pro více o tom, kde testování zapadá do celkového procesu, viz [Mapa pracovních postupů](./workflow-map.md).
