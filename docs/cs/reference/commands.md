---
title: Skills
description: Reference FMAD skills — co to je, jak fungují a kde je najít.
sidebar:
  order: 4
---

Skills jsou předpřipravené prompty, které načítají agenty, spouštějí workflow nebo provádějí úkoly ve vašem IDE. Instalátor FMAD je generuje z vašich nainstalovaných modulů při instalaci. Pokud později přidáte, odeberete nebo změníte moduly, přeinstalujte pro synchronizaci skills (viz [Řešení problémů](#řešení-problémů)).

## Skills vs. spouštěče nabídky agentů

FMAD nabízí dva způsoby zahájení práce a slouží k různým účelům.

| Mechanismus | Jak se vyvolává | Co se stane |
| --- | --- | --- |
| **Skill** | Zadejte název skillu (např. `fmad-help`) ve vašem IDE | Přímo načte agenta, spustí workflow nebo provede úkol |
| **Spouštěč nabídky agenta** | Nejprve načtěte agenta, pak zadejte krátký kód (např. `BD`) | Agent interpretuje kód a spustí odpovídající workflow, přičemž zůstává v charakteru |

Spouštěče nabídky agentů vyžadují aktivní relaci agenta. Používejte skills, když víte, který workflow chcete. Používejte spouštěče, když již pracujete s agentem a chcete přepnout úkol bez opuštění konverzace.

## Jak se skills generují

Když spustíte `npx skills add DavidBatoDev/fmad-method` a vyberete požadované skills, Skills CLI nainstaluje každý vybraný skill agenta, workflow, úkolu a nástroje; poté požádejte skill `fmad`, aby spustil `fmad setup`. Každý skill je adresář obsahující soubor `SKILL.md`, který instruuje AI k načtení odpovídajícího zdrojového souboru a následování jeho instrukcí.

Instalátor používá šablony pro každý typ skillu:

| Typ skillu | Co generovaný soubor dělá |
| --- | --- |
| **Spouštěč agenta** | Načte soubor persony agenta, aktivuje jeho nabídku a zůstává v charakteru |
| **Workflow skill** | Načte konfiguraci workflow a následuje jeho kroky |
| **Task skill** | Načte samostatný soubor úkolu a následuje jeho instrukce |
| **Tool skill** | Načte samostatný soubor nástroje a následuje jeho instrukce |

:::note[Opětovné spuštění instalátoru]
Pokud přidáte nebo odeberete moduly, spusťte instalátor znovu. Přegeneruje všechny soubory skills tak, aby odpovídaly vašemu aktuálnímu výběru modulů.
:::

## Kde žijí soubory skills

Instalátor zapisuje soubory skills do adresáře specifického pro IDE uvnitř vašeho projektu. Přesná cesta závisí na IDE, které jste vybrali během instalace.

| IDE / CLI | Adresář skills |
| --- | --- |
| Claude Code | `.claude/skills/` |
| Cursor | `.cursor/skills/` |
| Windsurf | `.windsurf/skills/` |
| Další IDE | Viz výstup instalátoru pro cílovou cestu |

Každý skill je adresář obsahující soubor `SKILL.md`. Například instalace Claude Code vypadá takto:

```text
.claude/skills/
├── fmad-help/
│   └── SKILL.md
├── fmad-prd/
│   └── SKILL.md
├── fmad-agent-dev/
│   └── SKILL.md
└── ...
```

Název adresáře určuje název skillu ve vašem IDE. Například adresář `fmad-agent-dev/` registruje skill `fmad-agent-dev`.

## Jak objevit vaše skills

Zadejte název skillu ve vašem IDE pro jeho vyvolání. Některé platformy vyžadují povolení skills v nastavení, než se zobrazí.

Spusťte `fmad-help` pro kontextové poradenství k dalšímu kroku.

:::tip[Rychlé objevování]
Generované adresáře skills ve vašem projektu jsou kanonický seznam. Otevřete je v prohlížeči souborů, abyste viděli každý skill s jeho popisem.
:::

## Kategorie skills

### Agentní skills

Agentní skills načítají specializovanou AI personu s definovanou rolí, komunikačním stylem a nabídkou workflow. Po načtení agent zůstává v charakteru a reaguje na spouštěče nabídky.

| Příklad skillu | Agent | Role |
| --- | --- | --- |
| `fmad-agent-dev` | Cinder (Developer) | Implementuje stories s přísným dodržováním specifikací |
| `fmad-pm` | Flint (Product Manager) | Vytváří a validuje PRD |
| `fmad-architect` | Ferris (Architect) | Navrhuje systémovou architekturu |

Viz [Agenti](./agents.md) pro úplný seznam výchozích agentů a jejich spouštěčů.

### Workflow skills

Workflow skills spouštějí strukturovaný, vícekrokový proces bez předchozího načtení persony agenta. Načtou konfiguraci workflow a následují jeho kroky.

| Příklad skillu | Účel |
| --- | --- |
| `fmad-product-brief` | Vytvoření product briefu — řízené discovery, když je váš koncept jasný |
| `fmad-prfaq` | [Working Backwards PRFAQ](../explanation/analysis-phase.md#prfaq-working-backwards) výzva pro zátěžový test vašeho produktového konceptu |
| `fmad-prd` | Vytvoření dokumentu požadavků (PRD) |
| `fmad-architecture` | Návrh systémové architektury |
| `fmad-create-epics-and-stories` | Vytvoření epiců a stories |
| `fmad-code-review` | Spuštění revize kódu |
| `fmad-build` | Implementace přímého záměru, issue, funkce, opravy nebo naplánované story |

Viz [Mapa pracovních postupů](./workflow-map.md) pro kompletní referenci workflow organizovanou podle fází.

### Task a tool skills

Tasks a tools jsou samostatné operace, které nevyžadují kontext agenta nebo workflow.

**FMAD-Help: Váš inteligentní průvodce**

`fmad-help` je vaše primární rozhraní pro objevení, co dělat dál. Zkoumá váš projekt, rozumí dotazům v přirozeném jazyce a doporučuje další povinný nebo volitelný krok na základě nainstalovaných modulů.

:::note[Příklad]
```
fmad-help
fmad-help I have a SaaS idea and know all the features. Where do I start?
fmad-help What are my options for UX design?
```
:::

**Další základní tasks a tools**

Základní modul zahrnuje 8 vestavěných nástrojů — nápovědu, revize, zdokonalování, přizpůsobení a myšlenkové skills (brainstorming, forge idea, party mode). Viz [Základní nástroje](./core-tools.md) pro kompletní referenci.

## Konvence pojmenování

Všechny skills používají prefix `fmad-` následovaný popisným názvem (např. `fmad-dev`, `fmad-prd`, `fmad-help`). Viz [Moduly](./modules.md) pro dostupné moduly.

## Řešení problémů

**Skills se nezobrazují po instalaci.** Některé platformy vyžadují explicitní povolení skills v nastavení. Zkontrolujte dokumentaci vašeho IDE nebo se zeptejte AI asistenta, jak skills povolit. Může být také nutné restartovat IDE nebo znovu načíst okno.

**Očekávané skills chybí.** Skills CLI instaluje pouze skills, které jste vybrali. Spusťte `npx skills add DavidBatoDev/fmad-method` znovu, ověřte výběr skills a poté požádejte skill `fmad`, aby spustil `fmad setup`. Zkontrolujte, že soubory skills existují v očekávaném adresáři.

**Skills z odebraného modulu se stále zobrazují.** Instalátor automaticky nemaže staré soubory skills. Odstraňte zastaralé adresáře z adresáře skills vašeho IDE, nebo smažte celý adresář skills a přeinstalujte pro čistou sadu.
