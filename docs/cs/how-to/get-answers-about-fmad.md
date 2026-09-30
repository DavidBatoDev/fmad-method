---
title: "Jak získat odpovědi o FMAD"
description: Použijte LLM k rychlému zodpovězení vašich otázek o FMAD
sidebar:
  order: 3
---

## Začněte zde: FMAD-Help

**Nejrychlejší způsob, jak získat odpovědi o FMAD, je skill `fmad-help`.** Tento inteligentní průvodce zodpoví více než 80 % všech otázek a je vám k dispozici přímo ve vašem IDE při práci.

FMAD-Help je víc než vyhledávací nástroj — umí:
- **Prozkoumat váš projekt** a zjistit, co už bylo dokončeno
- **Rozumět přirozenému jazyku** — ptejte se běžnou řečí
- **Přizpůsobit se nainstalovaným modulům** — zobrazí relevantní možnosti
- **Automaticky se spouštět po workflow** — řekne vám přesně, co dělat dál
- **Doporučit první povinný úkol** — žádné hádání, kde začít

### Jak používat FMAD-Help

Zavolejte ho jménem ve vaší AI relaci:

```
fmad-help
```

:::tip
V závislosti na vaší platformě můžete také použít `/fmad-help` nebo `$fmad-help`, ale samotné `fmad-help` by mělo fungovat všude.
:::

Spojte ho s dotazem v přirozeném jazyce:

```
fmad-help I have a SaaS idea and know all the features. Where do I start?
fmad-help What are my options for UX design?
fmad-help I'm stuck on the PRD workflow
fmad-help Show me what's been done so far
```

FMAD-Help odpoví:
- Co je doporučeno pro vaši situaci
- Jaký je první povinný úkol
- Jak vypadá zbytek procesu

## Kdy použít tohoto průvodce

Použijte tuto sekci, když:
- Chcete pochopit architekturu nebo interní fungování FMAD
- Potřebujete odpovědi mimo to, co FMAD-Help nabízí
- Zkoumáte FMAD před instalací
- Chcete prozkoumat zdrojový kód přímo

## Kroky

### 1. Vyberte si zdroj

| Zdroj                | Nejlepší pro                              | Příklady                     |
| -------------------- | ----------------------------------------- | ---------------------------- |
| **Složka `_fmad`**   | Jak FMAD funguje — agenti, workflow, prompty | „Co dělá PM agent?“        |
| **Celý GitHub repo** | Historie, instalátor, architektura        | „Co se změnilo v poslední verzi?“ |

Složka `_fmad` se vytvoří při instalaci FMAD. Pokud ji ještě nemáte, naklonujte si repo.

### 2. Nasměrujte AI na zdroj

**Pokud vaše AI umí číst soubory (Claude Code, Cursor atd.):**

- **FMAD nainstalován:** Nasměrujte na složku `_fmad` a ptejte se přímo
- **Chcete hlubší kontext:** Naklonujte si [celé repo](https://github.com/DavidBatoDev/fmad-method)

**Pokud používáte ChatGPT nebo Claude.ai:**

Otevřete [dokumentaci FMAD](https://davidbatodev.github.io/fmad-method/).

### 3. Položte svou otázku

:::note[Příklad]
**O:** „Řekni mi nejrychlejší způsob, jak něco vytvořit s FMAD“

**A:** Spusťte `fmad-build`. Předejte přímý záměr, issue, specifikaci nebo naplánovanou story; workflow využije dostupný kontext a zvolí potřebnou hloubku upřesnění, plánování, implementace a revize.
:::

## Co získáte

Přímé odpovědi o FMAD — jak agenti fungují, co dělají workflow, proč jsou věci strukturované tak, jak jsou — bez čekání na odpověď od někoho jiného.

## Tipy

- **Ověřte překvapivé odpovědi** — LLM se občas mýlí. Zkontrolujte zdrojový soubor nebo se zeptejte v [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions).
- **Buďte konkrétní** — „Co dělá krok 3 PRD workflow?“ je lepší než „Jak funguje PRD?“

## Stále jste uvízli?

Zkusili jste přístup přes LLM a stále potřebujete pomoc? Nyní máte mnohem lepší otázku k položení.

| Kanál                     | Použijte pro                                |
| ------------------------- | ------------------------------------------- |
| GitHub Discussions        | Otázky, nápady a požadavky na funkce        |
| GitHub Issues             | Hlášení chyb                                |

**GitHub Discussions:** [github.com/DavidBatoDev/fmad-method/discussions](https://github.com/DavidBatoDev/fmad-method/discussions)

**GitHub Issues:** [github.com/DavidBatoDev/fmad-method/issues](https://github.com/DavidBatoDev/fmad-method/issues) (pro jasné chyby)
