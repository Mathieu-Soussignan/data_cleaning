import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le contenu du fichier Markdown
with open("guide_scaling_data.md", "r", encoding="utf-8") as file:
    guide_scaling = file.read()

# Création d'un Dashboard multi-pages avec Streamlit
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Aperçu des données", "Nettoyage des valeurs manquantes", "Scaling des données", "Téléchargement des données nettoyées", "Guide Scaling"])

# Page pour afficher le guide de scaling
if page == "Guide Scaling":
    st.title("Guide pour le Scaling des Données")
    st.markdown(guide_scaling, unsafe_allow_html=True)

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

    # Remplir les valeurs manquantes pour le reste des colonnes
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mean())

    categorical_features = data.select_dtypes(include=['object']).columns
    for col in categorical_features:
        if data[col].isnull().sum() > 0:
            data[col] = data[col].fillna(data[col].mode()[0])

    st.subheader("Valeurs manquantes restantes après imputation")
    st.write(data.isnull().sum())

# 3. Scaling des données avec justification
elif page == "Scaling des données":
    st.title("Scaling des données")

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

    # Fonction de détection des valeurs aberrantes
    def detecter_valeurs_aberrantes(data, colonne):
        q1 = data[colonne].quantile(0.25)
        q3 = data[colonne].quantile(0.75)
        ecart_interquartile = q3 - q1
        limite_basse = q1 - (1.5 * ecart_interquartile)
        limite_haute = q3 + (1.5 * ecart_interquartile)
        valeurs_aberrantes = data[(data[colonne] < limite_basse) | (data[colonne] > limite_haute)]
        pourcentage = (len(valeurs_aberrantes) / len(data)) * 100
        st.write(f"Colonne : {colonne}")
        st.write(f"Nombre de valeurs aberrantes : {len(valeurs_aberrantes)}")
        st.write(f"Pourcentage de valeurs aberrantes : {pourcentage:.2f}%")
        return pourcentage

    # Explication du choix de la méthode de scaling
    data_scaled = data.copy()
    for col in numerical_features:
        pourcentage_aberrantes = detecter_valeurs_aberrantes(data, col)

        # Choix de la méthode de scaling
        if pourcentage_aberrantes > 0.1:
            st.write("Utilisation de RobustScaler pour cette colonne.")
            scaler = RobustScaler()
        else:
            st.write("Utilisation de MinMaxScaler pour cette colonne.")
            scaler = MinMaxScaler()

        # Appliquer le scaling et afficher les résultats
        data_scaled[[col]] = scaler.fit_transform(data[[col]])
        st.write(data_scaled[[col]].head())

    # Afficher les données après scaling
    st.write("Données après scaling :")
    st.write(data_scaled.head())

# 4. Téléchargement des données nettoyées
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