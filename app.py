import pandas as pd
import streamlit as st

# Création d'un Dashboard multi-pages avec Streamlit
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Aperçu des données", "Nettoyage des valeurs manquantes", "Téléchargement des données nettoyées"])

# 1. Aperçu des données
if page == "Aperçu des données":
    st.title("Aperçu des données du dataset Housing Price")
    st.image("./assets/data_scientist.png", caption="Housing Price!", use_column_width=True)

    # Chargement des données
    data_url = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
    data = pd.read_csv(data_url)
    st.write("Aperçu des premières lignes du dataset :", data.head())

# 2. Nettoyage des valeurs manquantes
elif page == "Nettoyage des valeurs manquantes":
    st.title("Nettoyage des valeurs manquantes")
    
    # Chargement des données
    data_url = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
    data = pd.read_csv(data_url)
    
    # Supprimer la colonne "Id"
    data = data.drop("Id", axis='columns')
    st.subheader("Valeurs manquantes après suppression de la colonne 'Id'")
    st.write(data.isnull().sum())

    # Supprimer les colonnes avec plus de 50% de valeurs manquantes
    percent_missing = data.isnull().sum() * 100 / len(data)
    columns_to_drop = percent_missing[percent_missing > 50].index
    data = data.drop(columns=columns_to_drop)
    st.subheader("Colonnes supprimées ayant plus de 50% de valeurs manquantes")
    st.write(list(columns_to_drop))

    # Vérification des valeurs manquantes après suppression des colonnes
    st.subheader("Valeurs manquantes après suppression des colonnes ayant plus de 50% de valeurs manquantes")
    st.write(data.isnull().sum())

    # Remplir les valeurs manquantes pour le reste des colonnes
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mean())

    st.subheader("Valeurs manquantes après imputation des colonnes numériques")
    st.write(data.isnull().sum())

    categorical_features = data.select_dtypes(include=['object']).columns
    for col in categorical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mode()[0])

    st.subheader("Valeurs manquantes après imputation des colonnes catégorielles")
    st.write(data.isnull().sum())

    # Vérifier s'il reste des valeurs manquantes
    st.subheader("Valeurs manquantes restantes après imputation")
    st.write(data.isnull().sum())

# 3. Téléchargement des données nettoyées
elif page == "Téléchargement des données nettoyées":
    st.title("Télécharger les données nettoyées")
    
    # Charger les données nettoyées
    data_url = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
    data = pd.read_csv(data_url)
    data = data.drop("Id", axis='columns')
    percent_missing = data.isnull().sum() * 100 / len(data)
    columns_to_drop = percent_missing[percent_missing > 50].index
    data = data.drop(columns=columns_to_drop)
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mean())
    categorical_features = data.select_dtypes(include=['object']).columns
    for col in categorical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mode()[0])

    # Enregistrer les données nettoyées dans un fichier CSV
    data.to_csv("clean_data.csv", index=False)
    st.success("Les données nettoyées ont été sauvegardées dans 'clean_data.csv'.")

    # Ajouter une option de téléchargement du fichier CSV
    st.download_button(
        label="Télécharger les données nettoyées",
        data=data.to_csv(index=False),
        file_name='clean_data.csv',
        mime='text/csv'
    )
