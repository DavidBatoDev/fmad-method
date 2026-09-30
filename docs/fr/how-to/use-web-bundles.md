---
title: 'Utiliser les Web Bundles'
description: Installer un web bundle FMAD comme Google Gemini Gem ou ChatGPT Custom GPT
---

Les web bundles s’installent depuis la release GitHub **[web-bundles-v1.0.0](https://github.com/DavidBatoDev/fmad-method/releases)**. Les ZIP sont produits à partir du dossier [`web-bundles/`](https://github.com/DavidBatoDev/fmad-method/tree/main/web-bundles) du dépôt.

## Pourquoi une seule porte d’entrée

La release GitHub est le seul chemin d’installation pris en charge pour la bibliothèque. Chaque mise à jour de la bibliothèque est publiée sous forme de release GitHub taguée, et le tag le plus récent contient les bundles actuels.

## Installer un bundle

1. Choisissez un bundle parmi ceux de la release.
2. Téléchargez son ZIP depuis la release. Chaque ZIP contient un seul bundle.
3. Ouvrez son `INSTRUCTIONS.md` et repérez les étapes **Gemini Gem** ou **ChatGPT Custom GPT** correspondant à votre plateforme.
4. Suivez les étapes : créez le Gem ou le Custom GPT, téléversez les fichiers de connaissance, collez le bloc d’instructions, sauvegardez.

## Prérequis

- **Pour les Gemini Gems** : abonnement Gemini Advanced.
- **Pour les ChatGPT Custom GPTs** : plan Plus, Pro, Business ou Enterprise.
- Pour les bundles qui utilisent **Deep Research** (actuellement Étude de marché et analyse sectorielle), activez-le depuis la barre de prompt (Outils → Deep Research). Deep Research a ses propres limites de plan.

## Personnaliser le persona

Le fichier `INSTRUCTIONS.md` de chaque bundle (dans le ZIP) inclut un **exemple de substitution de persona** au-dessus du séparateur de la zone à coller. Remplacez le bloc `[persona]` dans vos instructions installées par l’exemple de substitution pour changer le persona sans modifier le protocole. Vous pouvez aussi créer votre propre persona de zéro ; le protocole reste le même.

## Ce que vous obtenez

- Un Gem ou Custom GPT réutilisable dédié à une capacité de planification FMAD.
- Des artefacts finalisés (briefs, PRD, rapports de recherche, spécifications UX) prêts à déposer dans votre IDE pour l’implémentation.
- Les conversations de planification se déroulent sur votre abonnement LLM web existant au lieu de consommer des tokens IDE facturés.

:::caution[Dérive du persona]
Les LLM web abandonnent parfois le persona au cours de longues sessions. Si le modèle commence à parler hors personnage, rappelez-lui son persona ou démarrez une nouvelle session.
:::

## Créer le vôtre

Pour transformer un skill FMAD existant en web bundle, prenez comme modèle un répertoire de bundle existant dans `web-bundles/`. Empaquetez le `SKILL.md` du skill, un `INSTRUCTIONS.md` contenant les étapes d’installation et le bloc à coller, ainsi que les fichiers de données dont le skill a besoin. Reprenez le persona par défaut de l’agent FMAD correspondant lorsqu’il existe, et ajoutez un exemple de persona alternatif. Soumettez votre bundle à la bibliothèque en ouvrant une PR sur [FMAD-METHOD](https://github.com/DavidBatoDev/fmad-method) qui ajoute le répertoire du bundle et une entrée dans `web-bundles/bundles.json`.
