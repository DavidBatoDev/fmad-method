---
title: Options de Testing
description: Le workflow QA intégré pour l’automatisation des tests.
sidebar:
  order: 6
---

FMAD propose un workflow QA[^1] intégré pour une génération rapide de tests.

## Workflow QA Intégré

Le workflow QA intégré (`fmad-qa-generate-e2e-tests`) fait partie du module FMM (suite Agile), disponible via l’agent Developer. Il génère rapidement des tests fonctionnels en utilisant le framework de test existant de votre projet — aucune configuration ni installation supplémentaire requise.

**Déclencheur :** `QA` (via l’agent Developer) ou `fmad-qa-generate-e2e-tests`

### Ce que le Workflow QA Fait

Le workflow QA exécute un processus unique (Automate) qui parcourt cinq étapes :

1. **Détecte le framework de test** — analyse `package.json` et les fichiers de test existants pour identifier votre framework (Jest, Vitest, Playwright, Cypress, ou tout runner standard). Si aucun n’existe, analyse la pile technologique du projet et en suggère un.
2. **Identifie les fonctionnalités** — demande ce qu’il faut tester ou découvre automatiquement les fonctionnalités dans le codebase.
3. **Génère les tests API** — couvre les codes de statut, la structure des réponses, le chemin nominal, et 1-2 cas d’erreur.
4. **Génère les tests E2E** — couvre les parcours utilisateur avec des localisateurs sémantiques et des assertions sur les résultats visibles.
5. **Exécute et vérifie** — lance les tests générés et corrige immédiatement les échecs.

Le workflow QA produit un résumé de test sauvegardé dans le dossier des artefacts d’implémentation de votre projet.

### Patterns de Test

Les tests générés suivent une philosophie « simple et maintenable » :

- **APIs standard du framework uniquement** — pas d’utilitaires externes ni d’abstractions personnalisées
- **Localisateurs sémantiques** pour les tests UI (rôles, labels, texte plutôt que sélecteurs CSS)
- **Tests indépendants** sans dépendances d’ordre
- **Pas d’attentes ou de sleeps codés en dur**
- **Descriptions claires** qui se lisent comme de la documentation fonctionnelle

:::note[Portée]
Le workflow QA génère uniquement des tests. Pour la revue de code et la validation des stories, utilisez plutôt le workflow Code Review (`CR`).
:::

### Quand Utiliser le QA Intégré

- Couverture de test rapide pour une fonctionnalité nouvelle ou existante
- Automatisation de tests accessible aux débutants sans configuration avancée
- Patterns de test standards que tout développeur peut lire et maintenir
- Projets petits et moyens où une stratégie de test complète n’est pas nécessaire

## Comment les Tests S’Intègrent dans les Workflows

Le workflow Automate du QA intégré apparaît dans la Phase 4 (Implémentation) de la carte de workflow méthode FMAD. Il est conçu pour s’exécuter **après qu’un epic complet soit terminé** — une fois que toutes les stories d’un epic ont été implémentées et revues. Une séquence typique :

1. Pour chaque story de l’epic : implémenter avec Build (`BD` / `fmad-build`), puis ajouter Code Review (`CR`) si nécessaire
2. Après la fin de l’epic : générer les tests avec `QA` (via l’agent Developer)
3. Lancer la rétrospective (`fmad-retrospective`) pour capturer les leçons apprises

Le workflow QA travaille directement à partir du code source sans charger les documents de planification (PRD, architecture).

Pour en savoir plus sur la place des tests dans le processus global, consultez la [Carte des Workflows](./workflow-map.md).

## Glossaire

[^1]: QA (Quality Assurance) : assurance qualité, ensemble des processus et activités visant à garantir que le produit logiciel répond aux exigences de qualité définies.
