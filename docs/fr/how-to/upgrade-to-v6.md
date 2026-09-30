---
title: "Comment passer à la v6"
description: Migrer de FMAD v4 vers v6
sidebar:
  order: 3
---

Utilisez l’installateur FMAD pour passer de la v4 à la v6, qui inclut une détection automatique des installations existantes et une assistance à la migration.

## Quand utiliser ce guide

- Vous avez FMAD v4 installé (dossier `.fmad-method`)
- Vous souhaitez migrer vers la nouvelle architecture v6
- Vous avez des artefacts de planification existants à préserver

:::note[Prérequis]
- Node.js 20.12+
- Installation FMAD v4 existante
:::

## Étapes

### 1. Lancer l’installateur

Suivez les [Instructions d’installation](./install-fmad.md).

### 2. Gérer l’installation existante

Quand v4 est détecté, vous pouvez :

- Autoriser l’installateur à sauvegarder et supprimer `.fmad-method`
- Quitter et gérer le nettoyage manuellement

Si votre dossier de méthode FMAD porte un nom différent, vous devrez le supprimer manuellement.

### 3. Nettoyer les skills IDE

Supprimez manuellement les commandes/skills IDE v4 existants - par exemple si vous utilisez Claude Code, recherchez tous les dossiers imbriqués qui commencent par fmad et supprimez-les :

- `.claude/commands/`

Les nouveaux skills v6 sont installés dans :

- `.claude/skills/`

### 4. Migrer les artefacts de planification

**Si vous avez des documents de planification (Brief/PRD/UX/Architecture) :**

Déplacez-les dans `_fmad-output/planning-artifacts/` avec des noms descriptifs :

- Incluez `PRD` dans le nom de fichier pour les documents PRD[^1]
- Incluez `brief`, `architecture`, ou `ux-design` selon le cas
- Les documents divisés peuvent être dans des sous-dossiers au nom descriptif

**Si vous êtes en cours de planification :** Envisagez de recommencer avec les workflows v6. Utilisez vos documents existants comme entrées — les nouveaux workflows de découverte progressive avec recherche web et le mode plan de l’IDE produisent de meilleurs résultats.

### 5. Migrer le développement en cours

Si vous avez des stories[^3] créées ou implémentées :

1. Terminez l’installation v6
2. Placez `epics.md` ou `epics/epic*.md`[^2] dans `_fmad-output/planning-artifacts/`
3. Demandez à l’agent Développeur de planifier et suivre le travail dans l’arbre de tickets (skill `fmad-ticket`)
4. Indiquez à l’agent quels epics/stories sont déjà terminés

## Résultat de la migration

**Structure unifiée v6 :**

```text
votre-projet/
├── _fmad/               # Dossier d'installation unique
│   ├── _config/         # Vos personnalisations
│   │   └── agents/      # Fichiers de personnalisation des agents
│   ├── core/            # Framework core universel
│   └── fmm/             # Module Foundry Method
└── _fmad-output/        # Dossier de sortie (remplace le dossier doc de la v4)
```

## Changements clés

| Concept       | v4                                                      | v6                                       |
|---------------|---------------------------------------------------------|------------------------------------------|
| **Core**      | `_fmad-core` correspondait en réalité à la méthode FMAD | `_fmad/core/` est le framework universel |
| **Method**    | `_fmad-method`                                          | `_fmad/fmm/`                             |
| **Config**    | Fichiers modifiés directement                           | `config.yaml` par module                 |
| **Documents** | Division en fragments obligatoire ou optionnelle        | Totalement flexible, analyse automatique |


## Glossaire
[^1]: PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi.
[^2]: Epic : dans les méthodologies agiles, une grande unité de travail qui peut être décomposée en plusieurs stories. Un epic représente généralement une fonctionnalité majeure ou un ensemble de capacités livrable sur plusieurs sprints.
[^3]: Story (User Story) : une description courte et simple d’une fonctionnalité du point de vue de l’utilisateur. Les stories sont des unités de travail suffisamment petites pour être complétées en un sprint.
