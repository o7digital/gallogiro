# Intégration Toast — préparation, aucune connexion active

## Accès à obtenir de Charles et de Toast

Confirmer le titulaire du compte Toast, le type d’intégration autorisé (Standard en lecture seule ou intégration custom/partenaire approuvée), les restaurants concernés et leurs GUID, l’environnement et son hostname. Faire provisionner le clientId/clientSecret et autoriser chaque restaurant. Ne pas transmettre de secrets dans le chat, Git ou le navigateur.

L’authentification doit être réalisée par un service serveur via `/authentication/v1/authentication/login`. Conserver les secrets dans l’environnement serveur, renouveler les jetons à expiration et envoyer le Bearer ainsi que `Toast-Restaurant-External-ID` pour les ressources propres à un établissement.

Source : https://doc.toasttab.com/doc/devguide/authentication.html

## Lecture des données

| Besoin | Accès à demander |
| --- | --- |
| Menus et prix publiés | `menus:read` pour Menus V2 ; `menus.channel:read` et Menus V3 pour un partenaire de commande |
| Ruptures et disponibilité des articles | `stock:read` |
| Restaurants et disponibilité de prise de commandes | `restaurants:read` |
| Calendrier des commandes | `digital_schedule:read` |
| Configuration nécessaire selon le périmètre | `config:read` |

Ces accès de lecture figurent dans l’offre Standard, sauf Menus V3. Vérifier l’éligibilité et les scopes effectivement attribués au compte avant de développer. Aucun accès n’a été demandé ni testé ici.

Sources : https://doc.toasttab.com/doc/devguide/devApiAccessScopes.html et https://doc.toasttab.com/doc/devguide/apiScopes.html

## Architecture proposée

Créer ultérieurement un adaptateur serveur avec cache par GUID de restaurant. Conserver les identifiants des menus, articles et modificateurs ; traiter leurs règles de prix et plages de disponibilité. Utiliser les webhooks menus/stock quand ils sont autorisés. À défaut, contrôler les métadonnées des menus toutes les 1 à 5 minutes et recharger seulement en cas de changement ; prévoir une récupération du stock après événement manqué. Définir une politique de données périmées et conserver le lien de commande existant en secours.

Avant toute commande native, recontrôler le stock et demander le calcul final à `/prices` plutôt que calculer arbitrairement taxes et total. Tester sur un restaurant de test les options, suppléments, horaires et erreurs réseau.

Source : https://doc.toasttab.com/doc/cookbook/apiIntegrationChecklistOrdering.html

## Droits distincts à ne pas confondre

- Création de commandes : `orders.orders:write` ; lecture des commandes soumises : `orders:read` avec `orders.channel:read`. Autres droits selon fonctionnalités : `orders.items:write`, `orders.delivery_info:write`, `orders.discounts:write`, `orders.channel:void`.
- Paiement : `credit_cards.authorization:write` pour autoriser une carte ; `orders.payments:write` pour ajouter des paiements à une commande existante. Valider avec Toast le parcours, les exigences de certification et de traitement des cartes avant toute implémentation.
- Fidélité : la spécification Loyalty décrit une interface que le fournisseur implémente et que Toast appelle. Elle ne constitue pas une autorisation de lire les comptes Toast Loyalty. Faire confirmer par Toast le produit, le partenariat et les droits adaptés au besoin de Charles.

Sources : https://doc.toasttab.com/doc/devguide/apiScopes.html et https://doc.toasttab.com/openapi/loyalty/overview/

## Passage en production ultérieur

1. Créer `/en/` et `/es/`, traductions validées, titres/descriptions par langue, canonical et hreflang réciproques, sitemap et redirection de la racine décidée avec Charles.
2. Créer les pages restaurants avec adresses, téléphones et horaires vérifiés ; données structurées Restaurant et cohérence avec Google Business Profile. Aucun avis ni prix inventé.
3. Faire valider les données réelles et les droits d’usage des images, conserver la direction artistique V2.
4. Choisir l’hébergement Astro statique et un service serveur distinct si Toast est intégré ; prévoir préproduction, secrets, journalisation et retour arrière.
5. Recette avec Charles, puis autorisation explicite avant publication ou modification DNS. Cette étape reste strictement locale.
