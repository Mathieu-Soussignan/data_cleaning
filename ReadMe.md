# Nettoyage des Données du Dataset Housing Price avec Streamlit

## Description
Ce projet est une application Streamlit qui permet de nettoyer et d'analyser les données du dataset "Housing Price". Le tableau de bord interactif offre différentes fonctionnalités, y compris l'aperçu des données, le nettoyage des valeurs manquantes, l'analyse exploratoire et la possibilité de télécharger les données nettoyées. L'application est divisée en plusieurs pages pour faciliter la navigation et offrir une expérience utilisateur plus fluide.

## Fonctionnalités
1. **Aperçu des Données** :
   - Affichage des premières lignes du dataset.
   - Visualisation de l'image associée au projet.

2. **Nettoyage des Valeurs Manquantes** :
   - Suppression de la colonne "Id".
   - Suppression des colonnes ayant plus de 50% de valeurs manquantes.
   - Imputation des valeurs manquantes pour les colonnes numériques (par la moyenne) et pour les colonnes catégorielles (par la valeur la plus fréquente).
   - Affichage des valeurs manquantes à chaque étape pour assurer le suivi du nettoyage.

3. **Analyse Exploratoire** :
   - Affichage des statistiques descriptives des colonnes numériques.
   - Visualisation de la distribution des valeurs via un histogramme interactif.

4. **Téléchargement des Données Nettoyées** :
   - Enregistrement des données nettoyées dans un fichier CSV.
   - Possibilité de télécharger le fichier des données nettoyées directement depuis l'application.

## Prérequis
- **Python 3.12+**
- **Streamlit**
- **Pandas**
- **Seaborn** (pour les visualisations statistiques)
- **Matplotlib**

## Installation
1. Clonez ce repository :
   ```sh
   git clone https://github.com/Mathieu-Soussignan/data_cleaning.git
   ```
2. Accédez au dossier du projet :
   ```sh
   cd data_cleaning
   ```
3. Installez les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

## Lancer l'Application
Pour lancer l'application Streamlit, exécutez la commande suivante dans votre terminal :
```sh
streamlit run app.py
```
Cela ouvrira une application web dans votre navigateur, vous permettant de naviguer entre les différentes pages.

## Structure de l'Application
- **Aperçu des Données** : Cette page permet à l'utilisateur de visualiser les premières lignes du dataset "Housing Price" et de vérifier sa structure.
- **Nettoyage des Valeurs Manquantes** : Cette page guide l'utilisateur dans les différentes étapes de nettoyage des valeurs manquantes.
- **Analyse Exploratoire** : La page d'analyse exploratoire offre une analyse visuelle des données avec des histogrammes et des descriptions statistiques.
- **Téléchargement des Données Nettoyées** : Cette page permet de sauvegarder et télécharger les données nettoyées.

## Utilisation
1. **Navigation** : Utilisez le menu latéral pour naviguer entre les différentes pages.
2. **Filtrage des Données** : Vous pouvez choisir une colonne spécifique pour visualiser un histogramme, vous permettant d'explorer la distribution des données.
3. **Téléchargement** : Une fois le nettoyage terminé, vous pouvez télécharger les données nettoyées.

## Contributions
Les contributions sont les bienvenues. Si vous avez des suggestions pour améliorer le projet, veuillez ouvrir une demande ou envoyer une pull request.

## Licence
Ce projet est sous licence MIT.

## Auteurs
- [Mathieu Soussignan](https://www.mathieu-soussignan.com) - Développeur IA / Data

