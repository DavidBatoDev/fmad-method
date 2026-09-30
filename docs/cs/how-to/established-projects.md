---
title: "Existující projekty"
description: Jak používat Foundry Method na existujících kódových bázích
sidebar:
  order: 5
---

Používejte Foundry Method efektivně při práci na existujících projektech a starších kódových bázích.

Tento návod pokrývá základní workflow pro zapojení se do existujících projektů s Foundry Method.

:::note[Předpoklady]
- Foundry Method nainstalován (`npx skills add DavidBatoDev/fmad-method`, poté `fmad setup`)
- Existující kódová báze, na které chcete pracovat
- Přístup k AI-powered IDE (Claude Code nebo Cursor)
:::

## Krok 1: Vyčistěte dokončené plánovací artefakty

Pokud jste dokončili všechny PRD epicy a stories procesem FMAD, vyčistěte tyto soubory. Archivujte je, smažte nebo se spoléhejte na historii verzí. Nenechávejte tyto soubory v:

- `docs/`
- `_fmad-output/planning-artifacts/`
- `_fmad-output/implementation-artifacts/`

## Krok 2: Vytvořte kontext projektu

:::tip[Doporučeno pro existující projekty]
Vygenerujte `project-context.md` pro zachycení vzorů a konvencí vaší existující kódové báze. Tím zajistíte, že AI agenti budou při implementaci změn dodržovat vaše zavedené postupy.
:::

Spusťte workflow pro generování kontextu projektu:

```bash
fmad-generate-project-context
```

Toto skenuje vaši kódovou bázi a identifikuje:
- Technologický stack a verze
- Vzory organizace kódu
- Konvence pojmenování
- Přístupy k testování
- Vzory specifické pro framework

Vygenerovaný soubor můžete zkontrolovat a upravit, nebo ho vytvořit ručně na `_fmad-output/project-context.md`.

[Zjistit více o kontextu projektu](../explanation/project-context.md)

## Krok 3: Udržujte kvalitní projektovou dokumentaci

Vaše složka `docs/` by měla obsahovat stručnou, dobře organizovanou dokumentaci, která přesně reprezentuje váš projekt:

- Záměr a obchodní zdůvodnění
- Obchodní pravidla
- Architektura
- Jakékoli další relevantní informace o projektu

Pro složité projekty zvažte použití workflow `fmad-document-project`. Nabízí varianty, které proskenují celý váš projekt a zdokumentují jeho aktuální stav.

## Krok 3: Získejte pomoc

### FMAD-Help: Váš výchozí bod

**Spusťte `fmad-help` kdykoli si nejste jisti, co dělat dál.** Tento inteligentní průvodce:

- Prozkoumá váš projekt a zjistí, co už bylo uděláno
- Ukáže možnosti na základě nainstalovaných modulů
- Rozumí dotazům v přirozeném jazyce

```
fmad-help I have an existing Rails app, where should I start?
fmad-help How much planning does this change need before implementation?
fmad-help Show me what workflows are available
```

FMAD-Help se také **automaticky spouští na konci každého workflow** a poskytuje jasné pokyny, co přesně dělat dál.

### Volba hloubky plánování

Veškerá implementace používá `fmad-build`; rozsah určuje, jaký kontext připravíte předem:

| Rozsah                         | Doporučený přístup                                                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Jasné aktualizace či doplnění** | Vstupte přímo do `fmad-build` s požadavkem, issue nebo existující specifikací. |
| **Velké změny či doplnění**    | Připravte užitečné PRD, UX, architekturu, epic, story a sprint kontext a pak předejte vybranou práci do `fmad-build`. |

### Během tvorby PRD

Při vytváření briefu nebo přímém přechodu na PRD zajistěte, aby agent:

- Našel a analyzoval vaši existující projektovou dokumentaci
- Přečetl si správný kontext o vašem aktuálním systému

Agenta můžete navést explicitně, ale cílem je zajistit, aby se nová funkce dobře integrovala s vaším existujícím systémem.

### Úvahy o UX

Práce na UX je volitelná. Rozhodnutí nezávisí na tom, zda váš projekt má UX, ale na:

- Zda budete pracovat na změnách UX
- Zda jsou potřeba významné nové UX návrhy nebo vzory

Pokud vaše změny představují jednoduché aktualizace existujících obrazovek, se kterými jste spokojeni, plný UX proces je zbytečný.

### Úvahy o architektuře

Při práci na architektuře zajistěte, aby architekt:

- Používal správné zdokumentované soubory
- Skenoval existující kódovou bázi

Věnujte zde zvláštní pozornost, abyste předešli znovuvynalézání kola nebo rozhodnutím, která neodpovídají vaší existující architektuře.

## Další informace

- **[Rychlé opravy](./quick-fixes.md)** — Opravy chyb a ad-hoc změny
- **[FAQ pro existující projekty](../explanation/established-projects-faq.md)** — Časté otázky o práci na existujících projektech
