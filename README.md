# DbD Big Data Tracker

## Présentation du Projet

Ce projet est une simulation de plateforme d'ingestion et d'analyse de données en temps réel pour le jeu Dead by Daylight. L'objectif est de capturer les événements d'une partie (positions des survivants, état de santé, progression des objectifs) pour en extraire des insights statistiques et spatiaux.

### Méthodologie

- Modélisation : Utilisation de Pydantic en Python pour garantir l'intégrité des données envoyées.

- Ingestion : Un simulateur Python (`simulation.py`) envoie des données vers une base Warp 10 via des requêtes HTTP (Protocol Protocol).

- Stockage : Base de données orientée séries temporelles (TSDB) pour gérer la haute cardinalité des événements.

- Analyse : Utilisation du langage WarpScript (dossier `WARPSTUDIOSCRIPT`) pour traiter les données directement côté serveur.

## Installation et Configuration

Le projet repose sur une architecture conteneurisée. Pour démarrer l'infrastructure :

Copiez le fichier `.env.example` et renommez-le en `.env`.

Remplissez les variables nécessaires.

Lancez la commande :

```bash
docker-compose up -d
```

### Récupération des Tokens

Une fois le conteneur Warp 10 démarré, vous avez besoin de Tokens (Read/Write) pour que le simulateur puisse communiquer avec la base.

Utilisez la commande

```bash
docker exec -it warp10-bigdata /opt/warp10/bin/warp10.sh tokengen /opt/warp10/tokens/demo-tokengen.mc2
```

Le retour de la commande contiendra les deux tokens, à renseigner dans le `.env`et dans chaque script warpstudio.

## Lancement d'une partie

Pour démarrer la simulation et l'ingestion des données en temps réel :

- Assurez-vous que votre environnement Python est prêt et que les dépendances sont installées.

- Lancez le script de simulation :

```bash
python ./simulation.py
```

### Récupération du match_id

Dès le lancement du script, un identifiant unique appelé `match_id` est généré et affiché dans la console. Cet identifiant est crucial pour vos analyses : il doit être utilisé comme sélecteur dans vos scripts WarpScript pour isoler les données d'une session spécifique parmi l'ensemble des séries temporelles stockées.

## Analyse des Données (WarpScript)

Le projet utilise trois flux d'analyse distincts dans WarpStudio :

### Suivi des Mouvements

Le script `movements.warpscript` récupère les séries temporelles de position (`dbd.survivor.position` et `dbd.killer.position`).

- Fonctionnement : Il extrait les coordonnées de latitude et longitude pour les projeter sur une carte OpenStreetMap.

- Intérêt : Visualiser les trajectoires réelles et les zones de tension (chases) sur la carte du match.

### Progression des Objectifs

Le script `generator_exitdoors_progression.warpscript` compare l'avancement des générateurs et l'ouverture des portes de sortie.

- Fonctionnement : Il utilise un affichage de type step (escalier) pour montrer l'évolution par paliers de la progression (33%, 66%, 100%).

- Intérêt : Analyser la corrélation temporelle entre la fin des réparations et le déclenchement de la phase d'exfiltration.

### Statistiques de Distribution (celui demandé pendant le TP)

Le script `means.warpscript` traite les valeurs numériques (crochets, progression) pour extraire la santé globale de la partie.

- Fonctionnement : À l'aide d'une boucle robuste, il calcule la Moyenne, la Médiane, les Quartiles (Q1​, Q3​) et le 99eˋme percentile.

- Intérêt : Comprendre la répartition des données. Par exemple, une médiane très différente de la moyenne indique que les survivants ont passé beaucoup de temps sur un objectif presque terminé.

## Conclusion

Ce projet démontre la puissance des bases de données de séries temporelles pour le monitoring de jeux vidéo, permettant de passer de données brutes isolées à une compréhension spatiale et statistique complète d'un match.
