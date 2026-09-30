---
title: Modules Officiels
description: Les deux modules livrés avec FMAD et comment créer votre propre module
sidebar:
  order: 5
---

FMAD est livré avec deux modules : `fmod-method` (code `method`), qui regroupe les skills de livraison, et `fmod-core-tools` (code `core-tools`), qui contient le hub `fmad` et les outils autonomes. Il n’existe pas de modules additionnels officiels.

:::tip[Installer des Modules]
Exécutez `npx skills add DavidBatoDev/fmad-method` et sélectionnez les skills souhaités, en incluant `fmad` et les enregistrements de modules `fmod-method` et `fmod-core-tools`. Demandez ensuite au skill `fmad` d’exécuter `fmad setup`.
:::

## Modules Communautaires

Tout le monde peut écrire son propre module : un dossier `fmod-<code>` contenant un enregistrement `fmod.toml`.
