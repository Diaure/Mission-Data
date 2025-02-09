import folium
from folium.plugins import MarkerCluster
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static

try:
    tour1_2022 = pd.read_csv(https://github.com/Diaure/Mission-Data/blob/main/CSV/meilleurs_candidats_tour1_22.csv, sep=',', encoding='utf-8')
    tour1_2022_sans_nan = tour1_2022.dropna()

    BN_BNA_sup_5_2022 = pd.read_csv(https://github.com/Diaure/Mission-Data/blob/main/CSV/BN_BNA_sup_5_2022.csv,sep=',', encoding='utf-8')
    sup5_BN_BNA_sans_nan = BN_BNA_sup_5_2022.dropna()
    sup5_BN_BNA_sans_nan['Tour'] = sup5_BN_BNA_sans_nan['Tour'].astype(str)
    tours = list(sup5_BN_BNA_sans_nan['Tour'].unique()) 
except Exception as e:
    st.error(f"An error occurred: {e}") 

# centrer la carte sur la France
latitude_centre, longitude_centre = 46.603354, 1.888152
map_departement = folium.Map(location=[latitude_centre, longitude_centre], zoom_start=6)

# créer un dictionnaire pour stocker les groupes par candidat
groupes_candidats = {}

# parcours la liste des candidats afin de créer un groupe pour chacun
for candidat in tour1_2022_sans_nan["Candidats"].unique():
    groupe = folium.FeatureGroup(name=candidat)  # créee le groupe pour un candidat
    marker_cluster = MarkerCluster().add_to(groupe)  # ajoute du clustering

    # filtrer les données selon le candidat
    df_filtre = tour1_2022_sans_nan[tour1_2022_sans_nan["Candidats"] == candidat]

    # code pour ajouter des marqueurs avec texte
    for _, row in df_filtre.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            tooltip=f"<b>{candidat}<br><b>Département:</b> {row['Départements']}<br><b>Score:</b> {row['Votes']}",
            icon=folium.Icon(color="blue")
        ).add_to(marker_cluster)

    # Ajout du groupe à la carte
    groupes_candidats[candidat] = groupe
    map_departement.add_child(groupe)

# contrôle des groupes sur la carte
folium.LayerControl().add_to(map_departement)

#---------------------------------------------------

latitude_centre, longitude_centre = 46.603354, 1.888152
map_sup5 = folium.Map(location=[latitude_centre, longitude_centre], zoom_start=6)


groupes_tours = {}
for tour in tours:
    filtre = sup5_BN_BNA_sans_nan[sup5_BN_BNA_sans_nan['Tour'] == tour] 
    groupe = folium.FeatureGroup(name=f"Tour {tour}")  
    marker_cluster = MarkerCluster().add_to(groupe)

    for _, row in filtre.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            tooltip=f"<b>Commune:</b> {row['Libellé de la commune']}<br><b>Blancs et nuls:</b> {row['Blancs et nuls']}<br><b>Blancs, nuls et abstentions:</b> {row['Blancs_nuls et abstentions']}",
            icon=folium.Icon(color='purple')
        ).add_to(marker_cluster)

    groupe.add_to(map_sup5) 
    groupes_tours[tour] = groupe  

folium.LayerControl(collapsed=False).add_to(map_sup5)


st.title("Cartes géographiques")
st.header("Résultats par département des votes à l'issu du premier tour 2022 ")
folium_static(map_departement, width=1000, height=700)

st.title("Communes où les votes blancs et nuls dépassent 5%")
folium_static(map_sup5, width=1000, height=700)
