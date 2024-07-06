# Snow-Crash

## Introduction

**Snow-Crash** est un projet de sécurité informatique conçu pour tester et améliorer les compétences en reverse engineering, en analyse de vulnérabilités, et en exploitation. Il s'agit d'une série de niveaux (ou challenges) où chaque niveau présente un fichier exécutable ou un script que vous devez analyser pour obtenir le mot de passe du niveau suivant.

## Objectif

L'objectif principal du projet Snow-Crash est de progresser à travers les différents niveaux en obtenant les mots de passe cachés dans chaque challenge. Chaque niveau est conçu pour tester différentes compétences en sécurité informatique, telles que :

- Reverse engineering
- Analyse de la mémoire
- Exploitation des failles de sécurité
- Manipulation des fichiers et des permissions
- Utilisation des outils de débogage et de traçage

## Prérequis

Avant de commencer le projet Snow-Crash, il est recommandé d'avoir des connaissances de base dans les domaines suivants :

- Systèmes d'exploitation Unix/Linux
- Langage de programmation C et Perl
- Utilisation des outils de débogage comme gdb
- Utilisation des outils de traçage comme strace et ltrace
- Connaissance des commandes shell de base

## Structure du Projet

Le projet est structuré en une série de niveaux. Chaque niveau contient les éléments suivants :

- Un exécutable ou un script à analyser.
- Un fichier `token` ou un mot de passe caché que vous devez trouver pour accéder au niveau suivant.
- Des permissions spécifiques sur les fichiers et les répertoires pour ajouter de la complexité au challenge.

## Comment Démarrer

1. **Connexion :** Connectez-vous au serveur ou à la machine virtuelle où le projet Snow-Crash est hébergé.
2. **Accéder au Niveau Actuel :** Utilisez le mot de passe du niveau précédent pour vous connecter au nouveau niveau. Par exemple :
   ```sh
   ssh level01@<hostname>
   password: <password from level00>
   ```
3. **Analyser le Fichier :** Examinez le fichier exécutable ou le script fourni pour le niveau actuel. Utilisez des outils comme `gdb`, `strace`, `ltrace`, `strings`, et d'autres pour analyser le comportement du programme.
4. **Trouver le Mot de Passe :** Identifiez et exploitez les vulnérabilités ou les failles pour trouver le mot de passe du niveau suivant.
5. **Passer au Niveau Suivant :** Utilisez le mot de passe trouvé pour accéder au niveau suivant.

## Outils Recommandés

- **gdb** : Un débogueur pour les programmes en C et C++.
- **strace** : Un outil de traçage des appels système.
- **ltrace** : Un outil de traçage des appels de fonctions de bibliothèque.
- **strings** : Un outil pour extraire les chaînes de caractères imprimables d'un fichier.
- **netcat (nc)** : Un outil pour lire et écrire des données sur des connexions réseau en utilisant les protocoles TCP ou UDP.

## Conclusion

Snow-Crash est un projet passionnant et éducatif pour quiconque souhaite améliorer ses compétences en sécurité informatique. En progressant à travers les niveaux, vous acquerrez une expérience pratique précieuse dans l'analyse de programmes, la découverte de vulnérabilités et l'exploitation des failles de sécurité. Profitez du challenge et bon hacking !

---
