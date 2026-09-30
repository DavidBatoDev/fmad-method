---
title: "Začínáme"
description: Nainstalujte FMAD a vytvořte svůj první projekt
---

Vytvářejte software rychleji pomocí pracovních postupů řízených AI se specializovanými agenty, kteří vás provedou plánováním, architekturou a implementací.

## Co se naučíte

- Nainstalovat a inicializovat Foundry Method pro nový projekt
- Používat **FMAD-Help** — vašeho inteligentního průvodce, který ví, co dělat dál
- Zvolit správnou hloubku plánování pro vaši práci
- Postupovat fázemi od požadavků k fungujícímu kódu
- Efektivně používat agenty a pracovní postupy

:::note[Předpoklady]
- **Node.js 20.12+** — Vyžadováno pro instalátor
- **Git** — Doporučeno pro správu verzí
- **AI-powered IDE** — Claude Code, Cursor nebo podobné
- **Nápad na projekt** — I jednoduchý stačí pro učení
:::

:::tip[Nejsnadnější cesta]
**Instalace** → `npx skills add DavidBatoDev/fmad-method`, poté `fmad setup`
**Zeptejte se** → `fmad-help what should I do first?`
**Tvořte** → Nechte FMAD-Help vás provést workflow po workflow
:::

## Seznamte se s FMAD-Help: Váš inteligentní průvodce

**FMAD-Help je nejrychlejší způsob, jak začít s FMAD.** Nemusíte si pamatovat workflow nebo fáze — prostě se zeptejte a FMAD-Help:

- **Prozkoumá váš projekt** a zjistí, co už bylo uděláno
- **Ukáže vaše možnosti** na základě nainstalovaných modulů
- **Doporučí, co dál** — včetně prvního povinného úkolu
- **Odpoví na otázky** jako „Mám nápad na SaaS, kde začít?“

### Jak používat FMAD-Help

Spusťte ho ve vašem AI IDE vyvoláním skillu:

```
fmad-help
```

Nebo ho spojte s otázkou pro kontextové poradenství:

```
fmad-help I have an idea for a SaaS product, I already know all the features I want. where do I get started?
```

FMAD-Help odpoví s:
- Co je doporučeno pro vaši situaci
- Jaký je první povinný úkol
- Jak vypadá zbytek procesu

### Řídí i pracovní postupy

FMAD-Help nejen odpovídá na otázky — **automaticky se spouští na konci každého workflow** a řekne vám přesně, co dělat dál. Žádné hádání, žádné prohledávání dokumentace — jen jasné pokyny k dalšímu povinnému workflow.

:::tip[Začněte zde]
Po instalaci FMAD okamžitě vyvolejte skill `fmad-help`. Detekuje, jaké moduly máte nainstalované, a navede vás ke správnému výchozímu bodu pro váš projekt.
:::

## Pochopení FMAD

FMAD vám pomáhá vytvářet software prostřednictvím řízených pracovních postupů se specializovanými AI agenty. Proces probíhá ve čtyřech fázích:

| Fáze | Název          | Co se děje                                              |
| ---- | -------------- | ------------------------------------------------------- |
| 1    | Analýza        | Brainstorming, průzkum, product brief nebo PRFAQ *(volitelné)* |
| 2    | Plánování      | Vytvoření požadavků (PRD nebo specifikace)              |
| 3    | Solutioning    | Návrh architektury podle potřeby                         |
| 4    | Implementace   | Implementace každé změny nebo naplánované story, volitelně pomocí automatizované orchestrace |

**[Otevřete Mapu pracovních postupů](../reference/workflow-map.md)** pro prozkoumání fází, workflow a správy kontextu.

Hloubka plánování je flexibilní:

| Hloubka | Nejlepší pro | Kontext před implementací |
| --- | --- | --- |
| **Přímá** | Jasné opravy, funkce, issues nebo existující specifikace | Záměr, issue nebo specifikace |
| **Produktové plánování** | Produkty, platformy a složité funkce | PRD a volitelný UX návrh |
| **Plné solutioning** | Koordinované, rizikové nebo mezisystémové iniciativy | PRD, UX, architektura, epicy, stories a sprint plán |

:::note
Nejde o oddělené implementační cesty. Všechny vstupy se sbíhají do `fmad-build`; plánování pouze mění množství dostupného kontextu.
:::

## Instalace

Otevřete terminál v adresáři vašeho projektu a spusťte:

```bash
npx skills add DavidBatoDev/fmad-method
```

Při výzvě k výběru vyberte požadované skills včetně `fmad` a záznamů modulů `fmod-method` a `fmod-core-tools`. Poté otevřete AI IDE ve složce projektu a požádejte skill `fmad`, aby spustil `fmad setup`.

Instalátor vytvoří dvě složky:
- `_fmad/` — agenti, workflow, úkoly a konfigurace
- `_fmad-output/` — prozatím prázdná, ale zde se budou ukládat vaše artefakty

:::tip[Váš další krok]
Otevřete vaše AI IDE ve složce projektu a spusťte:

```
fmad-help
```

FMAD-Help detekuje, co jste dokončili, a doporučí přesně, co dělat dál. Můžete mu také klást otázky jako „Jaké mám možnosti?“ nebo „Mám nápad na SaaS, kde začít?“
:::

:::note[Jak načítat agenty a spouštět workflow]
Každý workflow má **skill**, který vyvoláte jménem ve vašem IDE (např. `fmad-prd`). Váš AI nástroj rozpozná název `fmad-*` a spustí ho — nemusíte načítat agenty zvlášť. Můžete také vyvolat agentní skill přímo pro obecnou konverzaci (např. `fmad-agent-pm` pro PM agenta).
:::

:::caution[Nové chaty]
Vždy začněte nový chat pro každý workflow. Tím předejdete problémům s kontextovými omezeními.
:::

## Krok 1: Zvolte hloubku plánování

Použijte z fází 1–3 tolik, kolik vaše práce potřebuje. U jasné, ohraničené práce můžete přejít přímo ke [Kroku 2](#krok-2-sestavte-svůj-projekt). **Pro každý workflow používejte nové chaty.**

:::tip[Kontext projektu (volitelné)]
Před začátkem zvažte vytvoření `project-context.md` pro dokumentaci vašich technických preferencí a pravidel implementace. Tím zajistíte, že všichni AI agenti budou dodržovat vaše konvence v průběhu celého projektu.

Vytvořte ho ručně na `_fmad-output/project-context.md` nebo ho vygenerujte po architektuře pomocí `fmad-generate-project-context`. [Zjistit více](../explanation/project-context.md).
:::

### Fáze 1: Analýza (volitelná)

Všechny workflow v této fázi jsou volitelné:
- **brainstorming** (`fmad-brainstorming`) — Řízená ideace
- **průzkum** (`fmad-deep-recon`) — Navrhne prompt pro váš vlastní nástroj hloubkového výzkumu, zpracuje hotovou zprávu do stručného shrnutí pro navazující práci, nebo výzkum provede přímo — tržní, doménový, technický, konkurenční, uživatelský a akademický — s ověřováním tvrzení a životním cyklem obnovy
- **product-brief** (`fmad-product-brief`) — Doporučený základní dokument, když je váš koncept jasný
- **prfaq** (`fmad-prfaq`) — Working Backwards výzva pro zátěžový test a zformování vašeho produktového konceptu

### Fáze 2: Plánování (podle potřeby)

Pro práci, které prospívá produktové plánování:
1. Vyvolejte **PM agenta** (`fmad-agent-pm`) v novém chatu
2. Spusťte workflow `fmad-prd` (`fmad-prd`)
3. Výstup: `PRD.md`

:::note[UX Design (volitelné)]
Pokud má váš projekt uživatelské rozhraní, vyvolejte **UX-Designer agenta** (`fmad-agent-ux-designer`) a spusťte UX design workflow (`fmad-ux`) po vytvoření PRD.
:::

### Fáze 3: Solutioning (podle potřeby)

**Vytvoření architektury**
1. Vyvolejte **Architect agenta** (`fmad-agent-architect`) v novém chatu
2. Spusťte `fmad-architecture` (`fmad-architecture`)
3. Výstup: Dokument architektury s technickými rozhodnutími

**Vytvoření epiců a stories**

:::tip[Epicy po architektuře]
Epicy a stories se vytvářejí *po* architektuře. Tím vznikají kvalitnější stories, protože architektonická rozhodnutí (databáze, API vzory, tech stack) přímo ovlivňují rozklad práce.
:::

1. Vyvolejte **PM agenta** (`fmad-agent-pm`) v novém chatu
2. Spusťte `fmad-create-epics-and-stories` (`fmad-create-epics-and-stories`)
3. Workflow využívá jak PRD, tak architekturu k vytvoření technicky informovaných stories

**Kontrola připravenosti k implementaci** *(vysoce doporučeno)*
1. Vyvolejte **Architect agenta** (`fmad-agent-architect`) v novém chatu
2. Spusťte `fmad-sprint-planning` (`fmad-sprint-planning`) — otevírá se bránou připravenosti
3. Validuje soudržnost všech plánovacích dokumentů

## Krok 2: Sestavte svůj projekt

Přejděte k implementaci s jakýmkoli dostupným kontextem: přímým požadavkem, issue, specifikací nebo plně naplánovanou story. **Každý workflow by měl běžet v novém chatu.**

U plánované práce spusťte `fmad-build` a určete vybranou story nebo položku sprintu, například: `Implementuj story 2.3 z _fmad-output/planning-artifacts/epics.md`.

### Inicializace plánování sprintu (pro plánovanou práci)

Vyvolejte **Developer agenta** (`fmad-agent-dev`) a spusťte `fmad-sprint-planning` (`fmad-sprint-planning`). Tím se vytvoří `sprint-status.yaml` pro sledování všech epiců a stories.

Když Build v tomto souboru rozpozná vybranou story, během implementace ji přesune do stavu `in-progress` a po dokončení implementace do stavu `review`.

### Cyklus vývoje

Pro každou přímou změnu nebo naplánovanou story opakujte tento cyklus s novými chaty:

| Krok | Agent | Workflow             | Příkaz                     | Účel                               |
| ---- | ----- | -------------------- | -------------------------- | ---------------------------------- |
| 1    | DEV   | `fmad-build`     | `fmad-build`           | Upřesnění, plán, implementace, revize a prezentace |
| 2    | DEV   | `fmad-code-review`   | `fmad-code-review`         | Dodatečná validace kvality *(doporučeno)* |

Revize v Build je součástí každého běhu. `fmad-code-review` je volitelná nezávislá validační vrstva v novém kontextu.

Po dokončení všech stories v epicu vyvolejte **Developer agenta** (`fmad-agent-dev`) a spusťte `fmad-retrospective` (`fmad-retrospective`).

## Co jste dosáhli

Naučili jste se základy budování s FMAD:

- Nainstalovali FMAD a nakonfigurovali ho pro vaše IDE
- Zvolili hloubku plánování odpovídající vaší práci
- Vytvořili plánovací dokumenty (PRD, architektura, epicy a stories)
- Pochopili cyklus vývoje pro implementaci

Váš projekt nyní obsahuje:

```text
váš-projekt/
├── _fmad/                                   # Konfigurace FMAD
├── _fmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Váš dokument požadavků
│   │   ├── architecture.md                  # Technická rozhodnutí
│   │   └── epics/                           # Soubory epiců a stories
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Sledování sprintu
│   └── project-context.md                   # Pravidla implementace (volitelné)
└── ...
```

## Rychlý přehled

| Workflow                              | Příkaz                                     | Agent     | Účel                                            |
| ------------------------------------- | ------------------------------------------ | --------- | ----------------------------------------------- |
| **`fmad-help`** ⭐                    | `fmad-help`                               | Jakýkoli  | **Váš inteligentní průvodce — ptejte se na cokoli!** |
| `fmad-prd`                     | `fmad-prd`                         | PM        | Vytvoření dokumentu požadavků (PRD)             |
| `fmad-architecture`            | `fmad-architecture`                | Architect | Vytvoření dokumentu architektury                |
| `fmad-generate-project-context`       | `fmad-generate-project-context`           | Analyst   | Vytvoření souboru kontextu projektu             |
| `fmad-create-epics-and-stories`       | `fmad-create-epics-and-stories`           | PM        | Rozklad PRD na epicy                            |
| `fmad-sprint-planning`                | `fmad-sprint-planning`                    | DEV       | Brána připravenosti + inicializace sledování sprintu + přehled stavu |
| `fmad-build`                      | `fmad-build`                          | DEV       | Implementace záměru, issue, funkce, opravy nebo story |
| `fmad-code-review`                    | `fmad-code-review`                        | DEV       | Revize implementovaného kódu                    |

## Časté otázky

**Potřebuji vždy architekturu?**
Ne. Architekturu použijte, když je třeba explicitně zachytit technická rozhodnutí nebo mezisystémová omezení. Jasná práce může vstoupit přímo do `fmad-build`; větší iniciativa přináší do stejného workflow plánovací artefakty.

**Mohu později změnit svůj plán?**
Ano. Workflow `fmad-correct-course` (`fmad-correct-course`) řeší změny rozsahu během implementace.

**Co když chci nejdřív brainstormovat?**
Vyvolejte Analyst agenta (`fmad-agent-analyst`) a spusťte `fmad-brainstorming` (`fmad-brainstorming`) před zahájením PRD.

**Musím dodržovat striktní pořadí?**
Ne striktně. Jakmile se naučíte postup, můžete spouštět workflow přímo pomocí Rychlého přehledu výše.

## Získání pomoci

:::tip[První zastávka: FMAD-Help]
**Vyvolejte `fmad-help` kdykoli** — je to nejrychlejší způsob, jak se odpoutat. Zeptejte se na cokoli:
- „Co mám dělat po instalaci?“
- „Zasekl jsem se na workflow X“
- „Jaké mám možnosti pro Y?“
- „Ukaž mi, co bylo dosud uděláno“

FMAD-Help prozkoumá váš projekt, detekuje, co jste dokončili, a řekne vám přesně, co dělat dál.
:::

- **Během workflow** — Agenti vás provázejí otázkami a vysvětleními
- **Komunita** — [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions) (otázky a nápady), [GitHub Issues](https://github.com/DavidBatoDev/fmad-method/issues) (hlášení chyb)

## Klíčové poznatky

:::tip[Zapamatujte si]
- **Začněte s `fmad-help`** — Váš inteligentní průvodce, který zná váš projekt a možnosti
- **Vždy používejte nové chaty** — Začněte nový chat pro každý workflow
- **Hloubka plánování se liší** — přímý záměr i plně naplánované stories vstupují do `fmad-build`
- **FMAD-Help se spouští automaticky** — Každý workflow končí pokyny, co dělat dál
:::

Jste připraveni začít? Nainstalujte FMAD, vyvolejte `fmad-help` a nechte svého inteligentního průvodce ukázat cestu.
