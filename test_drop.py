import pandas as pd
import streamlit as st

# 1. Titre de l'application
st.title("Nettoyage des données du dataset Housing Price")

# 2. Chargement des données
data_url = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
data = pd.read_csv(data_url)
st.write("Aperçu des premières lignes du dataset :", data.head())

# 3. Supprimer la colonne "Id"
data = data.drop("Id", axis='columns')

# Vérification des valeurs manquantes après suppression de la colonne "Id"
st.subheader("Valeurs manquantes après suppression de la colonne 'Id'")
st.write(data.isnull().sum())

# 4. Supprimer les colonnes avec plus de 50% de valeurs manquantes
percent_missing = data.isnull().sum() * 100 / len(data)
columns_to_drop = percent_missing[percent_missing > 50].index
data = data.drop(columns=columns_to_drop)
st.subheader("Colonnes supprimées ayant plus de 50% de valeurs manquantes")
st.write(list(columns_to_drop))

# Vérification des valeurs manquantes après suppression des colonnes
st.subheader("Valeurs manquantes après suppression des colonnes ayant plus de 50% de valeurs manquantes")
st.write(data.isnull().sum())

# 5. Remplir les valeurs manquantes pour le reste des colonnes
# - Pour les colonnes numériques, on remplace par la moyenne
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_features:
    if data[col].isnull().sum() > 0:
        data[col] = data[col].fillna(data[col].mean())

# Vérification des valeurs manquantes après imputation des colonnes numériques
st.subheader("Valeurs manquantes après imputation des colonnes numériques")
st.write(data.isnull().sum())

# - Pour les colonnes avec des mots (catégorielles)
categorical_features = data.select_dtypes(include=['object']).columns
for col in categorical_features:
    if data[col].isnull().sum() > 0:
        data[col] = data[col].fillna(data[col].mode()[0])

# Vérification des valeurs manquantes après imputation des colonnes catégorielles
st.subheader("Valeurs manquantes après imputation des colonnes catégorielles")
st.write(data.isnull().sum())

# 6. Vérifier s'il reste des valeurs manquantes
st.subheader("Valeurs manquantes restantes après imputation")
st.write(data.isnull().sum())

# 7. Enregistrer les données nettoyées dans un fichier CSV
data.to_csv("clean_data.csv", index=False)
st.success("Les données nettoyées ont été sauvegardées dans 'clean_data.csv'.")

# Ajouter une option de téléchargement du fichier CSV
st.download_button(
    label="Télécharger les données nettoyées",
    data=data.to_csv(index=False),
    file_name='clean_data.csv',
    mime='text/csv'
)