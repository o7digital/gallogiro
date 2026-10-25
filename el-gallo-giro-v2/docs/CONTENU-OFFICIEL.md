# Contenu officiel intégré — collecte du 25 octobre 2026

La V2 Astro + React conserve sa Cubana d’ouverture, ses photos immersives, sa palette et ses polices. Les données du menu et des restaurants sont séparées des composants. La maquette travaille sur une copie locale datée des pages publiques : aucune API Toast active, aucune modification du site officiel, des DNS ou de Toast.

## Contenu repris

- 12 établissements, avec adresses et téléphones tels que publiés sur https://gallogiro.com/ ; liens de menu propres à chaque établissement et commande via les pages officielles hébergées par Toast.
- 89 références distinctes de produits. Onze menus importés indépendamment : 89 produits à Claremont, Anaheim, Bellflower, Canoga Park, East LA, Lynwood, Panorama City, Santa Ana et Van Nuys ; 79 à Fontana ; 88 à Huntington Park. Soit 968 entrées locales, sans appliquer automatiquement un prix ou une disponibilité d’un établissement à un autre.
- Catégories : Tortas, Double Tortas, Tacos Grande, Tacos Regular, Burritos, Family Packs, Breakfast, Salads, Desserts, Aguas Frescas, Other Beverages, puis les sous-catégories Bakery (Bolillo, Conchas, Danes, Feite, Fino, Galletas, Pan de Muerto).
- Noms et descriptions EN officiels, traductions éditoriales ES, prix affichés dans les listes de menus. Aucune estimation lorsqu’un prix n’est pas affiché.
- 61 photos identifiées sur les fiches Santa Ana et la page d’accueil officielle (4 Torta Box). Les 28 autres références ont une présentation typographique « photo non disponible », sans photo d’un autre plat.
- 81 groupes d’options publiés sur les fiches accessibles de Santa Ana : ingrédients, suppléments, protéines et tailles, avec montants et contraintes affichés. Les formats accessibles incluent 16/20/32/44 oz, gallon et 5 gallons selon la boisson ; café/champurrado 12/20/96 oz. Ces options ne sont affichées que pour Santa Ana et uniquement comme référence : la sélection et le calcul final restent sur Toast.
- Histoire et méthodes de préparation issues de la page d’accueil ; catering et contact issus de https://gallogiro.com/catering et https://gallogiro.com/contact-us.
- Mi Gallo Rewards : règle de 10 Gallitos par dollar affichée officiellement, lien d’inscription Toast explicitement associé à Anaheim. Pas de seuil de récompense ajouté.
- Cartes cadeaux : lien officiel https://gallogiro.com/gift-card-purchase ; aucun montant ou condition inventé.

Le restaurant sélectionné est conservé dans localStorage, y compris après changement de langue et rechargement. Le panneau de commande permet également de changer de restaurant. Une navigation mobile expose les sections, la fidélité et les cartes cadeaux.

## Informations manquantes ou à confirmer

1. **San Fernando** : l’URL officielle liée depuis l’accueil est identifiée, mais plusieurs consultations du menu échouent. Aucun menu ni prix d’un autre restaurant ne s’y substitue. La page locale invite à ouvrir son menu officiel.
2. **Horaires hebdomadaires complets** : non exposés dans la représentation accessible des pages actuelles. Le navigateur local reçoit une vérification Cloudflare ; l’outil web montre « All hours » sans le détail. Aucun statut « ouvert maintenant » n’a été importé. Chaque fiche renvoie vers le site officiel pour consulter les horaires. Des anciens sous-domaines de commande sont encore indexés avec des horaires et prix différents ; ils n’ont pas été fusionnés avec les menus actuels.
3. **Claremont** : l’accueil publie le même téléphone que Fontana, sous le nom « 888 S Indian Hill Blvd ». Le nom de ville provient de son adresse. Le téléphone est repris avec une mention de confirmation nécessaire.
4. **East LA** : la source publie « West Whittier Boulevard » sans numéro de rue. Aucun numéro n’a été ajouté ; le manque est indiqué dans la fiche.
5. **Prix à zéro sur les fiches** : de nombreuses fiches produit exposent `$0` tandis que la liste du menu expose un prix réel. Les zéros ne sont jamais présentés comme des prix. La valeur de la liste est conservée, ou « voir tailles et prix » si elle manque. Les suppléments sont affichés comme dans la source, sans prétendre calculer un panier.
6. **Options et images** : 20 fiches Santa Ana restent inaccessibles après nouvelle tentative ; certaines autres n’exposent ni photo ni description (notamment les doubles tortas). Aucun détail n’a été extrapolé. Les menus des autres établissements ont leur propre relevé de prix, mais leurs fiches d’options n’ont pas été importées. Elles restent accessibles via leurs liens officiels.
7. **Cartes cadeaux et fidélité** : les destinations sont identifiées depuis les liens officiels, mais leurs formulaires complets ne sont pas exposés par l’outil web. Aucune inscription, commande ou transaction de test n’a été envoyée.
8. **Langue** : aucune version espagnole complète des pages sources n’a été trouvée. Les traductions ES sont éditoriales, basées sur les informations EN publiées, sans promesse supplémentaire. Les URLs SEO EN/ES restent une étape future.
9. **Histoire** : le contenu historique exploitable est celui de la page d’accueil. Les chemins `/about`, `/our-story` et `/story` n’étaient pas accessibles ; aucun contenu historique supplémentaire n’a été créé.

## Organisation des fichiers et reproduction

- `src/data/menus.json` : chaque relevé local et ses produits, prix, catégories, traductions, URL source, date et restaurant.
- `src/data/products.json` : identité des produits, photos avec URL et page source, groupes d’options et périmètre Santa Ana.
- `src/data/locations.json` : coordonnées, liens réels, provenance et champs horaires explicitement absents.
- `src/data/site.json` : histoire, catering, fidélité et cartes cadeaux, EN/ES et sources.
- `research/` : captures textuelles et relevés utilisés, conservés pour contrôler l’import sans nouvelle requête réseau. Les erreurs de consultation y sont également conservées.
- `scripts/import-content.py` puis `scripts/translate-content.py` : régénération à partir de ces captures (les photos manquantes sont téléchargées si nécessaire). Ils ne constituent pas une synchronisation programmée.
- `node scripts/verify-content.mjs` : cohérence des sources, prix, traductions et périmètres.

## Validation locale

- Chromium à 390, 768 et 1440 px, EN et ES : catégories, recherche, fiches produit, panneau de commande, navigation et absence de débordement horizontal validés.
- Changement des 12 restaurants, nombre d’articles propre à chaque menu, comportement de San Fernando sans import et conservation du choix après rechargement vérifiés.
- Images locales des produits chargées, liens internes résolus et destinations externes contrôlées par rapport aux sources officielles. Certains liens officiels restent inaccessibles à l’outil web comme indiqué ci-dessus.
- Vérifications du clavier et compilation : voir le résultat final de cette étape dans VALIDATION.md.
- Contrôle sur appareils physiques, Safari/iOS, horaires confirmés et validation éditoriale finale de Charles restent à réaliser avant publication.

Les vulnérabilités npm déjà relevées dans la V2 fournie restent documentées dans VALIDATION.md ; aucune migration majeure du framework n’a été mélangée à l’import de contenu.

Le scénario navigateur est conservé dans `scripts/browser-check.cjs`. Playwright a été installé dans `/tmp/gallogiro-qa` pour ce contrôle, sans changer les dépendances de l’application : `NODE_PATH=/tmp/gallogiro-qa/node_modules node scripts/browser-check.cjs`. Les captures et résultats de contrôle sont dans `/tmp/gallogiro-qa/`.
