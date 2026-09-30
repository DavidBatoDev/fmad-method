---
title: "Premiers pas"
description: Installer FMAD et développer votre premier projet
---

Accélérez le développement de vos applications grâce à des workflows alimentés par l’IA et des agents spécialisés qui vous guident dans la planification, l’architecture et l’implémentation.

## Ce que vous allez apprendre

- Installer et initialiser la méthode FMAD pour un nouveau projet
- Utiliser **FMAD-Help** — votre guide intelligent qui sait quoi faire ensuite
- Choisir la profondeur de planification adaptée à votre travail
- Progresser dans les phases, de la définition des exigences au code fonctionnel
- Utiliser efficacement les agents et les workflows

:::note[Prérequis]
- **Node.js 20.12+** — Nécessaire pour l’installation
- **Git** — Recommandé pour la gestion de versions
- **IDE avec IA intégrée** — Claude Code, Cursor ou équivalent
- **Une idée de projet** — Même simple, elle fera l’affaire pour commencer
:::

:::tip[Le chemin le plus rapide]
**Installer** → `npx skills add DavidBatoDev/fmad-method`, puis `fmad setup`
**Demander** → `fmad-help que dois-je faire en premier ?`
**Développez** → Laissez FMAD-Help vous guider, workflow par workflow
:::

## Découvrez FMAD-Help : votre guide intelligent

**FMAD-Help est le moyen le plus rapide de démarrer avec FMAD.** Pas besoin de mémoriser les workflows ou les phases — posez simplement votre question et FMAD-Help saura :

- **Inspecter votre projet** pour voir ce qui a déjà été fait
- **Vous présenter vos options** en fonction des modules installés
- **Vous recommander la prochaine étape** — y compris la première tâche obligatoire
- **Répondre à vos questions**, par exemple : « J’ai une idée de SaaS, par où commencer ? »

### Comment utiliser FMAD-Help

Dans votre IDE IA, invoquez le skill :

```
fmad-help
```

Ou accompagnez-le d’une question pour obtenir des conseils contextualisés :

```
fmad-help J’ai une idée de produit SaaS, je connais déjà toutes les fonctionnalités que je veux. Par où dois-je commencer ?
```

FMAD-Help vous indiquera :

- Ce qui est recommandé pour votre situation
- Quelle est la première tâche obligatoire
- À quoi ressemble le reste du processus

### Il intervient aussi dans les workflows

FMAD-Help ne se contente pas de répondre aux questions — **il se lance automatiquement à la fin de chaque workflow** pour vous indiquer exactement la suite. Finies les devinettes et les recherches dans la doc : vous recevez des instructions claires sur le prochain workflow à exécuter.

:::tip[Commencez ici]
Après avoir installé FMAD, invoquez immédiatement le skill `fmad-help`. Il détectera les modules que vous avez installés et vous orientera vers le bon point de départ pour votre projet.
:::

## Comprendre FMAD

FMAD vous aide à développer des logiciels grâce à des workflows guidés par des agents IA spécialisés. Le processus s’articule en quatre phases :

| Phase | Nom            | Ce qui se passe                                                |
|-------|----------------|----------------------------------------------------------------|
| 1     | Analyse        | Brainstorming, recherche, product brief ou PRFAQ _(optionnel)_ |
| 2     | Planification  | Définir les exigences (PRD[^1] ou spécification technique)     |
| 3     | Solutioning    | Concevoir l’architecture selon les besoins                      |
| 4     | Implémentation | Implémenter chaque changement ou story planifiée, éventuellement via une orchestration automatisée |

**[Ouvrez la carte des workflows](../reference/workflow-map.md)** pour explorer les phases, les workflows et la gestion du contexte.

La profondeur de planification reste flexible :

| Profondeur | Idéal pour | Contexte disponible avant l’implémentation |
|---|---|---|
| **Directe** | Corrections, fonctionnalités, issues ou spécifications claires | Intention, issue ou spécification |
| **Planification produit** | Produits, plateformes et fonctionnalités complexes | PRD et conception UX optionnelle |
| **Solutioning complet** | Initiatives coordonnées, risquées ou multi-systèmes | PRD, UX, architecture, epics, stories et plan de sprint |

:::note
Il ne s’agit pas de voies d’implémentation distinctes. Tous les points d’entrée convergent vers `fmad-build`; la planification ne change que la quantité de contexte disponible.
:::

## Installation

Ouvrez un terminal dans le répertoire de votre projet et exécutez :

```bash
npx skills add DavidBatoDev/fmad-method
```

À l’invite de sélection, choisissez les skills souhaités en incluant `fmad` et les enregistrements de modules `fmod-method` et `fmod-core-tools`. Ouvrez ensuite votre IDE avec IA dans le dossier du projet et demandez au skill `fmad` d’exécuter `fmad setup`.

L’installateur crée deux dossiers :

- `_fmad/` — agents, workflows, tâches et configuration
- `_fmad-output/` — vide pour le moment, mais c’est là que seront enregistrés vos artefacts

:::tip[Votre prochaine étape]
Ouvrez votre IDE avec IA dans le dossier du projet et exécutez :

```
fmad-help
```

FMAD-Help détectera ce que vous avez déjà accompli et vous recommandera exactement la suite. Vous pouvez aussi lui poser des questions comme « Quelles sont mes options ? » ou « J’ai une idée de SaaS, par où devrais-je commencer ? »
:::

:::note[Comment charger les agents et exécuter les workflows]
Chaque workflow possède une **skill** que vous invoquez par son nom dans votre IDE (par ex. `fmad-prd`). Votre outil IA reconnaîtra le nom `fmad-*` et l’exécutera — pas besoin de charger les agents séparément. Vous pouvez aussi invoquer directement une skill d’agent pour une conversation générale (par ex. `fmad-agent-pm` pour l’agent PM).
:::

:::caution[Nouveaux chats]
Démarrez toujours un nouveau chat pour chaque workflow. Cela évite les problèmes liés aux limites de contexte de l’IA.
:::

## Étape 1 : Choisir la profondeur de planification

Utilisez les phases 1 à 3 selon les besoins du travail. Pour un changement clair et délimité, vous pouvez passer directement à l’[Étape 2](#étape-2-développer-votre-projet). **Utilisez un nouveau chat pour chaque workflow.**

:::tip[Contexte projet (optionnel)]
Avant de commencer, pensez à créer `project-context.md` pour documenter vos préférences techniques et vos règles d’implémentation. Ainsi, tous les agents IA respecteront vos conventions tout au long du projet.

Créez-le manuellement à l’emplacement `_fmad-output/project-context.md`, ou générez-le après l’architecture avec `fmad-generate-project-context`. [En savoir plus](../explanation/project-context.md).
:::

### Phase 1 : Analyse (optionnelle)

Tous les workflows de cette phase sont optionnels. [**Vous ne savez pas lequel choisir ?**](../explanation/analysis-phase.md)

- **brainstorming** (`fmad-brainstorming`) — Idéation guidée
- **research** (`fmad-deep-recon`) — Rédigez un prompt de recherche approfondie pour votre propre outil IA, transformez un rapport terminé en synthèse exploitable en aval, ou menez la recherche ici — marché, domaine, technique, concurrentiel, voix des utilisateurs et académique — avec vérification des affirmations et cycle de rafraîchissement
- **product-brief** (`fmad-product-brief`) — Document fondateur recommandé une fois votre concept bien défini
- **prfaq** (`fmad-prfaq`) — Exercice Working Backwards pour tester et affiner votre concept produit

### Phase 2 : Planification (selon les besoins)

Pour les travaux qui bénéficient d’une planification produit :

1. Exécutez `fmad-prd` dans un nouveau chat — précisez votre intention (Create / Update / Validate) ou laissez le skill vous la demander
2. Résultat : `prd.md`, `addendum.md`, `.memlog.md`

:::note[Intentions de `fmad-prd`]

- **Create** — exploration guidée à partir de zéro ; le skill nomme le dossier de travail et vous accompagne jusqu’à l’obtention d’un PRD dont vous serez fier
- **Update** — pointez vers un PRD existant et un changement à apporter ; le skill met en évidence les conflits avant d’appliquer les modifications
- **Validate** — critiquez un PRD finalisé à l’aide d’une liste de contrôle et générez un rapport HTML des constatations
:::


:::note[Design UX (optionnel)]
Si votre projet comporte une interface utilisateur, invoquez l'**agent UX Designer** (`fmad-agent-ux-designer`) et lancez le workflow de design UX (`fmad-ux`) après avoir créé votre PRD.
:::

### Phase 3 : Solutioning (selon les besoins)

**Créer l’architecture**

1. Invoquez l'**agent Architecte** (`fmad-agent-architect`) dans un nouveau chat
2. Exécutez `fmad-architecture` (`fmad-architecture`)
3. Résultat : document d’architecture avec les décisions techniques

**Créer les epics et les stories**

:::tip[Après l’architecture]
Les epics et stories sont créés *après* l’architecture. Cela produit des stories de meilleure qualité, car les décisions d’architecture (choix de la base de données, patterns d’API, pile technologique) influencent directement la façon dont le travail doit être découpé.
:::

1. Invoquez l'**agent PM** (`fmad-agent-pm`) dans un nouveau chat
2. Exécutez `fmad-create-epics-and-stories` (`fmad-create-epics-and-stories`)
3. Le workflow s’appuie sur le PRD et l’architecture pour créer des stories techniquement fondées

**Vérification de la préparation à l’implémentation** *(fortement recommandée)*

1. Invoquez l'**agent Architecte** (`fmad-agent-architect`) dans un nouveau chat
2. Exécutez `fmad-sprint-planning` (`fmad-sprint-planning`) — il s’ouvre sur le jalon de préparation
3. Valide la cohérence de l’ensemble des documents de planification

## Étape 2 : Développer votre projet

Passez à l’implémentation avec le contexte disponible : demande directe, issue, spécification ou story entièrement planifiée. **Chaque workflow doit être exécuté dans un nouveau chat.**

Pour un travail planifié, invoquez `fmad-build` et indiquez la story ou l’élément de sprint sélectionné, par exemple : `Implémente la story 2.3 depuis _fmad-output/planning-artifacts/epics.md`.

### Initialiser la planification de sprint (pour le travail planifié)

Invoquez l'**agent Développeur** (`fmad-agent-dev`) et exécutez `fmad-sprint-planning` (`fmad-sprint-planning`). Cette commande crée `sprint-status.yaml` pour suivre tous les epics et stories.

Lorsque Build retrouve la story sélectionnée dans ce fichier, il la passe à `in-progress` pendant l’implémentation, puis à `review` quand l’implémentation est terminée.

### Le cycle de développement

Pour chaque changement direct ou story planifiée, répétez ce cycle dans de nouveaux chats :

| Étape | Agent | Workflow            | Commande            | Objectif                             |
|-------|-------|---------------------|---------------------|--------------------------------------|
| 1     | DEV   | `fmad-build`    | `fmad-build`    | Clarifier, planifier, implémenter, réviser et présenter |
| 2     | DEV   | `fmad-code-review`  | `fmad-code-review`  | Validation qualité supplémentaire *(recommandée)* |

La revue de Build fait partie de chaque exécution. `fmad-code-review` est une couche facultative de validation indépendante dans un contexte neuf.

Après avoir terminé toutes les stories d’un epic, invoquez l'**agent Développeur** (`fmad-agent-dev`) et exécutez `fmad-retrospective` (`fmad-retrospective`).

## Ce que vous avez accompli

Vous maîtrisez maintenant les bases du développement avec FMAD :

- Installation et configuration de FMAD pour votre IDE
- Choix d’une profondeur de planification adaptée au travail
- Création des documents de planification (PRD, Architecture, Epics & Stories)
- Compréhension du cycle de développement pour l’implémentation

Votre projet contient désormais :

```text
your-project/
├── _fmad/                                   # Configuration FMAD
├── _fmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Document d’exigences
│   │   ├── architecture.md                  # Décisions techniques
│   │   └── epics/                           # Fichiers epic et story
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Suivi de sprint
│   └── project-context.md                   # Règles d’implémentation (optionnel)
└── ...
```

## Référence rapide

| Workflow                              | Commande                              | Agent     | Objectif                                                        |
|---------------------------------------|---------------------------------------|-----------|-----------------------------------------------------------------|
| **`fmad-help`** ⭐                    | `fmad-help`                           | Tous      | **Votre guide intelligent — posez n’importe quelle question !**  |
| `fmad-prd`                            | `fmad-prd`                            | Tous      | Créer, mettre à jour ou valider un PRD                          |
| `fmad-architecture`            | `fmad-architecture`            | Architect | Créer le document d’architecture                                |
| `fmad-generate-project-context`       | `fmad-generate-project-context`       | Analyst   | Créer le fichier de contexte projet                             |
| `fmad-create-epics-and-stories`       | `fmad-create-epics-and-stories`       | PM        | Décomposer le PRD en epics                                      |
| `fmad-sprint-planning`                | `fmad-sprint-planning`                | DEV       | Jalon de préparation + initialisation du suivi de sprint + vue d’état        |
| `fmad-build`                      | `fmad-build`                      | DEV       | Implémenter une intention, une issue, une fonctionnalité, un correctif ou une story |
| `fmad-code-review`                    | `fmad-code-review`                    | DEV       | Revoir le code implémenté                                       |

## Questions fréquentes

**Ai-je toujours besoin d’une architecture ?**
Non. Utilisez l’architecture lorsque les décisions techniques ou contraintes multi-systèmes doivent être explicites. Un travail clair peut entrer directement dans `fmad-build`; une initiative plus vaste fournit ses artefacts de planification au même workflow.

**Puis-je modifier mon plan en cours de route ?**
Oui. Le workflow `fmad-correct-course` gère les changements de périmètre en cours d’implémentation.

**Et si je veux d’abord brainstormer ?**
Invoquez l’agent Analyste (`fmad-agent-analyst`) et exécutez `fmad-brainstorming` (`fmad-brainstorming`) avant de commencer votre PRD.

**Dois-je suivre un ordre strict ?**
Pas strictement. Une fois le flux maîtrisé, vous pouvez exécuter les workflows directement en vous référant au tableau ci-dessus.

## Obtenir de l’aide

:::tip[Premier réflexe : FMAD-Help]
**Invoquez `fmad-help` à tout moment** — c’est le moyen le plus rapide de vous débloquer. Posez-lui n’importe quelle question :

- « Que dois-je faire après l’installation ? »
- « Je suis bloqué sur le workflow X »
- « Quelles sont mes options pour Y ? »
- « Montre-moi ce qui a été fait jusqu’ici »

FMAD-Help inspecte votre projet, détecte ce que vous avez accompli et vous indique exactement la prochaine étape.
:::

- **Pendant les workflows** — Les agents vous guident à l’aide de questions et d’explications
- **Communauté** — [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions) pour les questions, [GitHub Issues](https://github.com/DavidBatoDev/fmad-method/issues) pour signaler des bugs

## Points clés à retenir

:::tip[Retenez ceci]
- **Commencez par `fmad-help`** — Votre guide intelligent qui connaît votre projet et vos options
- **Utilisez toujours de nouveaux chats** — Démarrez un nouveau chat pour chaque workflow
- **La profondeur de planification varie** — une intention directe et une story entièrement planifiée entrent toutes deux dans `fmad-build`
- **FMAD-Help se lance automatiquement** — Chaque workflow se termine par des conseils sur la prochaine étape
:::

Prêt à commencer ? Installez FMAD, invoquez `fmad-help`, et laissez votre guide intelligent vous accompagner.

## Glossaire

[^1]: PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi.
[^2]: Epic : grand ensemble de fonctionnalités ou de travaux qui peut être décomposé en plusieurs user stories.
[^3]: Story (User Story) : description courte et simple d’une fonctionnalité du point de vue de l’utilisateur ou du client. Elle représente une unité de travail implémentable en un court délai.
[^4]: UX (User Experience) : expérience utilisateur, englobant l’ensemble des interactions et perceptions d’un utilisateur face à un produit. Le design UX vise à créer des interfaces intuitives, efficaces et agréables en tenant compte des besoins, des comportements et du contexte d’utilisation.
[^5]: Multi-tenant : architecture logicielle où une seule instance de l’application sert plusieurs clients (tenants) tout en maintenant leurs données isolées et sécurisées les unes des autres.
