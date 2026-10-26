# Conventions du projet

## Développement
- Ne pas demander de confirmation pour chaque fichier ou correction.
- Définir un plan court, puis l'exécuter lorsque la demande est suffisamment claire.
- Lire le code, les tests et les conventions avant toute modification.
- Respecter l'architecture et le style existants.
- Utiliser des noms, messages d'erreur, docstrings et commentaires en français.
- Ajouter des annotations de types et une docstring courte à chaque nouvelle fonction.
- Respecter PEP 8.

## Tests et corrections
- Ajouter des tests pour chaque nouvelle fonctionnalité.
- Conserver les tests existants et ne jamais les modifier uniquement pour les faire passer.
- Exécuter les tests après chaque étape importante.
- Analyser les échecs, corriger leur cause et relancer les tests.
- Limiter les tentatives de correction à cinq cycles maximum.
- Vérifier la qualité du code, le diff Git et l'état du dépôt avant de conclure.
- Ne jamais prétendre qu'un test a réussi sans l'avoir réellement exécuté.
- Exécuter `./check.sh` après chaque modification significative et avant de conclure.
- Ne jamais supprimer, désactiver, contourner ou affaiblir un test existant pour obtenir une suite de tests réussie.

## Sécurité et périmètre
- Ne jamais supprimer de données, publier, pousser du code, déployer ou modifier des services en production sans autorisation explicite.
- Ne modifier que les fichiers nécessaires au projet et à la fonctionnalité demandée.
- Ne jamais effectuer de commit sans autorisation explicite.

## Rapport final
- Indiquer les fichiers modifiés, les fonctionnalités ajoutées, les commandes de test exécutées, les résultats, les problèmes restants et les limites des vérifications.