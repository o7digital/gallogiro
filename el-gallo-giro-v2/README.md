# El Gallo Giro — maquette V2 pour Charles

Astro 5 + React 19. Projet statique, version validée « Puro sabor / California soul ».

## Démarrage
Avec une version LTS de Node compatible avec le package-lock (Node 22.12+ conseillé) :

```sh
npm ci
npm run dev
```

Ouvrir l’URL indiquée par Astro. Pour compiler : `npm run build`. Résultat dans `dist/`.

## Fichiers
- `src/pages/index.astro` : page, métadonnées et polices.
- `src/components/Experience.jsx` : interface React, textes EN/ES, filtres, recherche, dialogue de commande.
- `src/styles/site.css` : design et règles responsive.
- `public/assets/` : logo et photographies du site El Gallo Giro.

## État réel
Maquette fonctionnelle, sans connexion API Toast. Les commandes renvoient vers https://gallogiro.com/order. Les restaurants ouvrent Google Maps. Aucun paiement, prix ou stock synchronisé. Le changement de langue est local à la page, pas encore une architecture SEO multilingue par URL. Les polices sont chargées depuis Google Fonts.

## Validation effectuée
Compilation réussie et contrôle visuel desktop ; basculement EN/ES, filtre Tortas, recherche Santa Ana et ouverture/fermeture du dialogue de commande vérifiés. Contrôle visuel mobile complémentaire à réaliser sur les appareils cibles.

## Ressources
Photographies et logo récupérés du site officiel gallogiro.com pour la proposition au client. Aucun visuel concurrent. Conserver l’usage dans le cadre du projet El Gallo Giro.

Le ZIP ne contient aucun identifiant de déploiement, secret, node_modules ou historique Git.

## Contenu officiel — reprise locale

Le menu réel est désormais stocké par restaurant dans `src/data/`, avec les URL sources et la date de collecte (25 octobre 2026). Onze menus sont importés ; San Fernando conserve un lien officiel sans substituer le menu d’un autre établissement. Le choix du restaurant et la langue persistent localement.

Les fiches produits exposent descriptions, prix publiés et options vérifiées pour Santa Ana. Les commandes, paiements, inscriptions Rewards et cartes cadeaux restent sur les destinations officielles. La maquette ne possède aucune connexion API en temps réel.

Consulter `docs/CONTENU-OFFICIEL.md` pour l’inventaire, les sources, les limites et la régénération ; `node scripts/verify-content.mjs` contrôle les données importées.
