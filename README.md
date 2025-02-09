# 📊 **Analyse des Votes Blancs, Nuls et de l'Abstention en France**

## 🏛 **Contexte du Projet**

**Client** : Association Citoyenne (fictive) pour la Reconnaissance du Vote Blanc et Nul

**Objectif** : Étudier l'évolution des votes blancs, nuls et de l'abstention en France depuis 1995 et leur impact potentiel sur les élections présidentielles.

L'association considère que certains abstentionnistes voteraient blanc ou nul si ces votes étaient reconnus. L'évolution de l'abstention est donc un élément central de l'analyse.

## 🎯 **Objectifs de l'Analyse**

1. **Analyse de l'évolution des votes blancs et nuls** au niveau national depuis 1995.
2. **Étude de la corrélation entre l'abstention et les votes blancs et nuls.** 
3. **Analyse locale (par commune et/ou département) des élections présidentielles de 2022** (1er et 2nd tour) : identifier les zones où ces votes arrivent en tête ou en 2e position.
4. **Modélisation des votes blancs, nuls et de l’abstention comme des candidats distincts** et comparaison avec les résultats officiels. 
5. **Visualisation des résultats sous forme de cartes interactives.**


## 📂 **Données Utilisées**  

Les données proviennent du portail officiel [data.gouv.fr](https://www.data.gouv.fr/fr/pages/donnees-des-elections/).

📌 **Jeux de données utilisées** :

* Résultats des élections présidentielles en France depuis 1995.

* Résultats détaillés des élections de 2022 (1er et 2nd tour).

* Taux d'abstention pour chaque élection.

* Découpage administratif des communes et départements français.

## 📊 Résultats

1. **Dashboard Power BI**<br>
Vous trouverez les résultas dans les détails [ici](lien dashboard github et pdf google)<br>
🔹 Évolution des votes blancs et nuls depuis 1995.<br>

![tffgf](./images/Evolution%20nombre%20de%20votes%20BN%20et%20BNA.PNG) <br>

![tffgf](./images/Evolution%20part%20BNA%20inscrits%20votants%20exprimés.PNG) <br>

🔹 Corrélation entre votes blancs, nuls et abstention.<br>

![tffgf](./images/correlation.PNG) <br>

🔹 Impact local des votes blancs et nuls sur l’élection de 2022.<br>

![tffgf](./images/Impact%20local%20votes%20BN.PNG) <br>

![tffgf](./images/Impact%20local%20votes%20BNA.PNG) <br>

2. **Cartes interactives des résultats**<br>
🔹 Communes où ces votes dépassent 5%.<br>
🔹 Départements où ces votes atteignent le second tour.<br>

## 📌 Livrables attendus  

* ✔️ Analyse détaillée des tendances des votes blancs et nuls <br>
* ✔️ Présentation des résultats des élections en intégrant ces votes comme candidats <br>
* ✔️ Visualisations interactives et cartes géographiques<br>

⚠️**Note** : Dans les livrables les sigles suivants seront utilisés:<br>
* **BN** = Blancs et Nuls<br>
* **BNA** = Blancs, nuls et abstentions

## 📑 Méthodologie

1. **Nettoyage et préparation des données** (suppression des incohérences, fusion des sources de données, création des candidats **`blancs et nuls`** et **`blancs, nuls et abstentions`**).

2. **Analyse temporelle** de l’évolution des votes blancs et nuls depuis 1995.

3. **Corrélation entre votes blancs, nuls et abstention**.

4. **Analyse locale des résultats de 2022** :

* Classement des votes blancs, nuls et abstention comme des "candidats".

* Cartographie des communes où ces votes dépassent 5%.

5. **Visualisation des données** sous forme de tableaux, graphiques et cartes interactives.<br>

## 🏆 **Auteurs & Contributions**

Projet réalisé dans le cadre d’un projet scolaire de Data Analyst.<br>
Contributions : [Aurélie GABU]() - [GitHub](https://github.com/Diaure/Projects) / [LinkedIn]()

## 📌 Sources

Données issues de [data.gouv.fr](https://www.data.gouv.fr/fr/pages/donnees-des-elections/).


## 📜 Licence

Projet open-source sous licence MIT. Vous êtes libres de l'utiliser et de le modifier avec attribution.  
