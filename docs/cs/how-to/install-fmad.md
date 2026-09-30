---
title: "Jak nainstalovat FMAD"
description: Průvodce instalací FMAD ve vašem projektu krok za krokem
sidebar:
  order: 1
---

Použijte příkaz `npx skills add DavidBatoDev/fmad-method` a poté `fmad setup` k nastavení FMAD ve vašem projektu s výběrem modulů a AI nástrojů.

## Kdy to použít

- Začínáte nový projekt s FMAD
- Přidáváte FMAD do existující kódové báze
- Aktualizujete stávající instalaci FMAD

:::note[Předpoklady]
- **Node.js** 20.12+ (vyžadováno pro instalátor)
- **Git** (doporučeno)
- **AI nástroj** (Claude Code, Cursor nebo podobný)
:::

## Kroky

### 1. Spusťte instalátor

```bash
npx skills add DavidBatoDev/fmad-method
```

### 2. Zvolte umístění instalace

Instalátor se zeptá, kam nainstalovat soubory FMAD:

- Aktuální adresář (doporučeno pro nové projekty, pokud jste adresář vytvořili sami a spouštíte z něj)
- Vlastní cesta

### 3. Vyberte své AI nástroje

Vyberte, které AI nástroje používáte:

- Claude Code
- Cursor
- Ostatní

Každý nástroj má svůj vlastní způsob integrace skills. Instalátor vytvoří drobné prompt soubory pro aktivaci workflow a agentů — jednoduše je umístí tam, kde je váš nástroj očekává.

:::note[Povolení skills]
Některé platformy vyžadují explicitní povolení skills v nastavení, než se zobrazí. Pokud nainstalujete FMAD a nevidíte skills, zkontrolujte nastavení vaší platformy nebo se zeptejte svého AI asistenta, jak skills povolit.
:::

### 4. Zvolte moduly

Instalátor zobrazí dostupné moduly. Vyberte ty, které potřebujete — většina uživatelů chce pouze **Foundry Method** (modul pro vývoj softwaru).

### 5. Následujte výzvy

Instalátor vás provede zbytkem — vlastní obsah, nastavení atd. Poté otevřete svůj AI nástroj ve složce projektu a požádejte skill `fmad`, aby spustil `fmad setup`.

## Co získáte

```text
váš-projekt/
├── _fmad/
│   ├── fmm/            # Vaše vybrané moduly
│   │   └── config.yaml # Nastavení modulu (pokud byste ho někdy potřebovali změnit)
│   ├── core/           # Povinný základní modul
│   └── ...
├── _fmad-output/       # Generované artefakty
├── .claude/            # Claude Code skills (pokud používáte Claude Code)
│   └── skills/
│       ├── fmad-help/
│       ├── fmad-persona/
│       └── ...
└── .cursor/            # Cursor skills (pokud používáte Cursor)
    └── skills/
        └── ...
```

## Ověření instalace

Spusťte `fmad-help` pro ověření, že vše funguje, a zjistěte, co dělat dál.

**FMAD-Help je váš inteligentní průvodce**, který:
- Potvrdí, že vaše instalace funguje
- Ukáže, co je dostupné na základě nainstalovaných modulů
- Doporučí váš první krok

Můžete mu také klást otázky:
```
fmad-help I just installed, what should I do first?
fmad-help What are my options for a SaaS project?
```

## Řešení problémů

**Instalátor vyhodí chybu** — Zkopírujte výstup do svého AI asistenta a nechte ho to vyřešit.

**Instalátor fungoval, ale něco nefunguje později** — Vaše AI potřebuje kontext FMAD, aby pomohla. Podívejte se na [Jak získat odpovědi o FMAD](./get-answers-about-fmad.md) pro návod, jak nasměrovat AI na správné zdroje.
