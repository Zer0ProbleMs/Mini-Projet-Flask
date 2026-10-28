# Mini-Projet Flask : sujet 30 (salles de cours)
Par : Daris KOKIC
Groupe : A2

Projet Flask (BUT Informatique, cours DIW) : gestion des salles de cours
et de leurs types, avec interface CRUD et page de filtre.

**Note :** le code se trouve sur la branche `main` (le merge des deux branches
ne fonctionnait malheureusement pas après de multiples essaies).

## Lancer le projet

    python -m flask --debug --app app run

Puis ouvrir http://127.0.0.1:5000

## Contenu

- `/accueil` : accueil du site web
- `/type-salle/show` : types de salle (ajout, modification, suppression)
- `/salle-cours/show` : salles de cours (ajout, modification, suppression)
- `/salle-cours/filtre` : page de filtre
