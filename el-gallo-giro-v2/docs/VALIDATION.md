# Validation locale V2

Archive extraite sans écrasement dans `el-gallo-giro-v2/`. README et instructions lus. Design, photos, couleurs, typographies et liens existants conservés.

- `npm ci` réussi ; Node installé compatible avec les engines du verrouillage (v26.5.1). Pour une installation reproductible future, préférer Node 22 LTS compatible aux versions spécifiées par le README.
- `npm run dev -- --host 127.0.0.1 --port 4322` : http://127.0.0.1:4322/.
- `npm run build` réussi, sortie `dist/`.
- Chromium : captures inspectées à 390, 768 et 1440 px, EN et ES ; pas de débordement horizontal. Vérification des images après chargement différé.
- Les cinq filtres retournent respectivement 6, 2, 2, 1 et 1 cartes dans les deux langues et aux trois largeurs.
- Recherche `sAnTa aNa` : un résultat ; `zzzz` : message vide traduit ; effacement : liste restaurée.
- Dialogue : ouverture, fermeture, Escape, accès clavier et retour de focus ; lien inchangé vers https://gallogiro.com/order. Pas de commande réelle envoyée.
- Correction : titre et description accessibles associés au dialogue avec aria-labelledby et aria-describedby. Aucun changement visuel.
- Aucune erreur JavaScript lors du contrôle final. Après compilation, le serveur de développement a été redémarré pour renouveler le cache de transformation React.

## Limites et suite

Les contrôles sont réalisés dans Chromium avec tailles simulées, pas sur appareils physiques Safari/iOS. Le changement de langue reste local, sans URLs SEO distinctes. Les menus, villes et textes restent ceux de la maquette ; aucune synchronisation Toast active.

L’audit npm du verrouillage fourni remonte 5 vulnérabilités : Astro critique, sharp/zod/zod-to-ts élevées, esbuild faible. L’outil propose une migration majeure vers Astro 7.4.2 ; elle reste à préparer et vérifier avant production dans une tâche dédiée, sans modifier le design validé. Aucun audit fix --force appliqué.

Aucun push ni déploiement pour cette étape locale ; aucun changement du site gallogiro.com ou des DNS. Plan d’intégration et de passage en production : PLAN-TOAST.md.
