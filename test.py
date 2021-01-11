# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:56:24 2021

@author: Nadia
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_folium import folium_static
import folium
import warnings
warnings.filterwarnings("ignore")


df_ville = pd.read_excel(r'C:\Users\Nadia\Ville.xlsx')

#TITRE

st.markdown("<h1 style='text-align: center; color: black;'>INDICE DE PERFORMANCE ENVIRONNEMENTAL</h1>", unsafe_allow_html=True)
st.markdown("![Region Sud](https://nsm09.casimages.com/img/2020/12/17//20121704061016813117177105.jpg)") 


#SIDEBAR

st.sidebar.title("INFORMATION ASSOCIATION")

#NOM ASSOCIATION
user_input = st.sidebar.text_input("Nom de l'association")

#NBR PERSONNE ASSOC
user_input = st.sidebar.text_input("Nombre de personnes dans l’association/club")

#NOM MANIF SPORT
user_input = st.sidebar.text_input("Nom de la manifestation sportive")


# LISTE DEROULANTE VILLE
localisation=  st.sidebar.selectbox("Lieu de la manifestation", (df_ville['Commune']))

#LOCALISATION FOLIUM
df_localisation =df_ville[df_ville['Commune']==localisation]
m = folium.Map(location=[df_localisation['Latitude'],df_localisation['Longitude']],zoom_start=7)
folium.Marker(location=[df_localisation['Latitude'],df_localisation['Longitude']]).add_to(m)
folium_static(m)


#DUREE MANIFESTATION
user_input = st.sidebar.text_input("Nombre de jours de la manifestation")


#TYPE ACTIVITE
user_input = st.sidebar.text_input("Type d’activité sportive")

#TYPE DE PARTICIPANTS
add_selectbox = st.sidebar.selectbox("Niveau sportif",
    ('Amateur','Professionnel'))

#NBR PARTICIPANTS
user_input = st.sidebar.text_input("Nombre de participants")



#INDICATEURS   
st.markdown("<h1 style='text-align: center; color: black;'>LES INDICATEURS</h1>", unsafe_allow_html=True) 
#st.title("LES INDICATEURS")
 
#INDICATEURS1
st.markdown("<h1 style='text-align: center; color: black;'> GESTION ET VALORISATION DES DÉCHETS</h1>", unsafe_allow_html=True) 
#st.header("Indicateur 1: Gestion des dechets")


add_selectbox1= st.selectbox('Réduction des déchets ?',('-','Oui','Non'))
point1= 0
if add_selectbox1=='Oui':
   point1= point1 + 1 


add_selectbox2= st.selectbox('Tri Sélectif ?',('-','Oui','Non'))
if add_selectbox2=='Oui':
   point1= point1 + 1 
 
add_selectbox3= st.selectbox("Si oui : Collecte et traitement de déchets spéciaux ?",('-','Mégots',"Compostage","Capsules de café/thé","Stickers" ))
if add_selectbox3 == 'Mégots': 
   point1= point1 + 1 
if add_selectbox3 == "Compostag": 
   point1= point1 + 1 
if add_selectbox3 == "Capsules de café/thé":
   point1= point1 + 1    
if add_selectbox3 == "Stickers":
   point1= point1 + 1  
 

add_selectbox4= st.selectbox('Actions de valorisation et gestion des déchets sportifs ?',('-','Oui','Non'))
if add_selectbox4=='Oui':
   point1= point1 + 1 

add_selectbox5= st.selectbox('Restauration sur place ?',('-','Oui','Non'))

   
add_selectbox6= st.selectbox("Si oui ",('-','Local/Circuits courts ',"BIO","Couverts biodégradables ou durables","Doggy bag" ))
if add_selectbox6 == 'Local/Circuits courts': 
   point1= point1 + 1 
if add_selectbox3 == "BIO": 
   point1= point1 + 1 
if add_selectbox3 == "Couverts biodégradables ou durables":
   point1= point1 + 1    
if add_selectbox3 == "Doggy bag":
   point1= point1 + 1     



#INDICATEURS2
st.markdown("<h1 style='text-align: center; color: black;'>SENSIBILISATION A L’ECORESPONSABILITE</h1>", unsafe_allow_html=True) 


add_selectbox7= st.selectbox('Campagne d’informations grand public dédiée sur site ?',('-','Oui','Non'))

point2= 0

add_selectbox8= st.selectbox("Si oui : De quel type ?",('-','Actions de sensibilisation sur site via une association spécialisée',"Panneaux d’affichage informatifs","Jeux concours" ))


if add_selectbox8 == 'Actions de sensibilisation sur site via une association spécialisée': 
   point2= point2 + 2 
if add_selectbox8 == "Panneaux d’affichage informatifs": 
   point2= point2 + 2 
if add_selectbox8 == "Jeux concours":
   point2= point2 + 2     

add_selectbox9= st.selectbox('Actions de formation auprès des personnels d’organisation ?',('-','Oui','Non'))
if add_selectbox9=='Oui':
   point2= point2 + 2 


#INDICATEURS3
st.markdown("<h1 style='text-align: center; color: black;'>CONSOMMATION D’EAU</h1>", unsafe_allow_html=True)

add_selectbox10= st.selectbox("Solutions de réduction de la consommation d’eau ? ",('-','Réducteur de débit intérieur (type douches)',"Réducteur de débit extérieur (type tuyaux de rinçage)","Chasse d’eau à vitesse" ))

point3= 0
if add_selectbox10 =='Réducteur de débit intérieur (type douches)':
   point3= point3 + 2 
if add_selectbox10 =="Réducteur de débit extérieur (type tuyaux de rinçage)":
   point3= point3 + 2
if add_selectbox10 =="Chasse d’eau à vitesse":
   point3= point3 +2 


user_input = st.text_input("Quantité totale d’eau potable utilisée en m3")
#formule de calcul a trouver pour remettre la qualité m3 par utilisateur  

add_selectbox11= st.selectbox('Récupération des eaux de pluie ?',('-','Oui','Non'))
if add_selectbox11=='Oui':
   point3= point3 + 2  


#INDICATEURS4
st.markdown("<h1 style='text-align: center; color: black;'> CONSOMMATION ÉLECTRIQUE</h1>", unsafe_allow_html=True)

user_input = st.text_input("Quantité kw:h")
#formule de calcul a trouver pour remettre la qualité kw/h par utilisateur 

add_selectbox12= st.selectbox("Energies renouvelables ? ",('-','Panneaux solaires',"Électricité verte (abonnement spécifique)","Energie hydraulique grâce aux courants marins" ))

point4= 0
if add_selectbox12 =='Panneaux solaires':
   point4= point4 + 2 
if add_selectbox12 =="Électricité verte (abonnement spécifique)":
   point4= point4 + 2
if add_selectbox12 =="Energie hydraulique grâce aux courants marin":
   point4= point4 + 2

add_selectbox13= st.selectbox("Solutions de réduction électrique?",('-','Détecteur de mouvements',"Mise en veille automatique du matériel informatique" ))
if add_selectbox13 =='Détecteur de mouvements':
   point4= point4 + 2 
if add_selectbox13 =="Mise en veille automatique du matériel informatique":
   point4= point4 + 2

add_selectbox14= st.selectbox('Production autonome en énergies renouvelables ?',('-','Oui','Non'))
if add_selectbox14=='Oui':
   point4= point4 + 1 



#INDICATEURS5
st.markdown("<h1 style='text-align: center; color: black;'>MOUILLAGES ET BOUÉES DE RÉGATESE</h1>", unsafe_allow_html=True)

add_selectbox15= st.selectbox('Utilisation de bouées ?',('-','Oui','Non'))

point5= 0
if add_selectbox15=='Oui':
   point5= point5 + 3
   
st.write("Si non : Passage à l'indicateur 6")   
         
add_selectbox16= st.selectbox("Dispositifs de sensibilisation aux écosystèmes fragiles ? ",('-','Mouillages hors herbiers de posidonie ',"Utilisation d’applications dédiées de type DONIA ","Utilisation de bouées géostationnaires" ))         
if add_selectbox16 =='Mouillages hors herbiers de posidonie':
   point5= point5 + 1 
if add_selectbox12 =="Utilisation d’applications dédiées de type DONIA":
   point5= point5 + 1
if add_selectbox12 =="Utilisation de bouées géostationnaires":
   point5= point5 + 1 

#INDICATEURS6
st.markdown("<h1 style='text-align: center; color: black;'>DÉPLACEMENT DES ÉQUIPAGES ET DU PUBLIC</h1>", unsafe_allow_html=True)

st.write("PROBLEMATIQUE : Un organisateur aura des difficultés à renseigner ces données. Du coup, est-il possible de faire remplir ces données par les utilisateurs dans un questionnaire « participants » et de les intégrer dans le scoring final ?")


add_selectbox17= st.selectbox("Modes de déplacements des équipages? ",('-','Transports en commun',"Covoiturage","Véhicule individuel","Vélo","Voiture éléctrique","A pieds"))         

point6=0
if add_selectbox17 =='Transports en commun':
   point6= point6 + 4 
if add_selectbox17 =="Covoiturage":
   point6= point6 +4
if add_selectbox17 =="Véhicule individuel":
   point6= point6 + 0
if add_selectbox17 =="Vélo":
   point6= point6 + 4
if add_selectbox17 =="Voiture éléctrique":
   point6= point6 + 4
if add_selectbox17 =="A pieds":
   point6= point6 + 4 

user_input = st.text_input("Distance domicile/lieu de la manifestation ?")
st.write("PROBLEMATIQUE : trouver calcul ratio km/personne")


#INDICATEURS7
st.markdown("<h1 style='text-align: center; color: black;'>QUALITÉ DES EMBARCATIONS</h1>", unsafe_allow_html=True)

add_selectbox18= st.selectbox('Embarcations écoconçues ?',('-','Oui','Non'))
point7= 0
if add_selectbox18=='Oui':
   point7= point7 + 2 

add_selectbox19= st.selectbox('Les produits d’entretien sont-ils biodégradables ?',('-','Oui','Non'))
if add_selectbox19=='Oui':
   point7= point7 + 2 
   
add_selectbox20= st.selectbox('Solutions alternatives antifouling ?',('-','Oui','Non'))
if add_selectbox20=='Oui':
   point7= point7 + 1 



#INDICATEURS8
st.markdown("<h1 style='text-align: center; color: black;'>QUALITÉ DES INSTALLATIONS ACCUEILLANTES</h1>", unsafe_allow_html=True)

add_selectbox21= st.selectbox('Le port de plaisance est-il certifié « Ports Propres » ?',('-','Oui','Non'))
point8= 0
if add_selectbox21=='Oui':
   point8= point8 + 2 

add_selectbox22= st.selectbox('La base nautique est-elle basse consommation (R12) ?',('-','Oui','Non'))
if add_selectbox22=='Oui':
   point8= point8 + 2 
   
add_selectbox23= st.selectbox('Adhésion à une Charte zéro plastique  ?',('-','Oui','Non'))
 

add_selectbox24= st.selectbox("Si oui ",('-','Charte Région',"Charte Ligue"))         

if add_selectbox24 =='Charte Région':
   point8= point8 + 1 
if add_selectbox24 =="Charte Ligue":
   point8= point8 + 1

#TABLEAU RESULTAT
st.markdown("<h1 style='text-align: center; color: black;'>TABLEAU RESULTAT</h1>", unsafe_allow_html=True)

df = pd.DataFrame({'Indicateurs': ['GESTION ET VALORISATION DES DÉCHETS',"SENSIBILISATION A L’ECORESPONSABILITE","CONSOMMATION D’EAU",'CONSOMMATION ÉLECTRIQUE',"MOUILLAGES ET BOUÉES DE RÉGATES","DÉPLACEMENT DES ÉQUIPAGES ET DU PUBLIC","QUALITÉ DES EMBARCATIONS","QUALITÉ DES INSTALLATIONS ACCUEILLANTES"],
                   'Indices': [point1, point2, point3, point4,point5, point6, point7, point8]})
df = df.rename(columns={'Indicateurs':'index'}).set_index('index')
df

total= point1+point2+point3+point4+point5+point6+point7+point8

st.write('Votre total est de', ((total*20)/32), 'sur 20.')



placeholder = st.empty()
df = pd.DataFrame(dict(r=[point1,point2,point3,point4, point5,point6, point7, point8],theta=["GESTION/VALORISATION DES DÉCHETS","SENSIBILISATION ECORESPONSABILITE","CONSOMMATION D’EAU","CONSOMMATION ÉLECTRIQUE","MOUILLAGES/BOUÉES DE RÉGATES","DÉPLACEMENT ÉQUIPAGES/PUBLIC","QUALITÉ DES EMBARCATIONS","QUALITÉ INSTALLATIONS ACCUEILLANTES"]))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
placeholder.write(fig)


chart_data = pd.DataFrame({'Indicateurs': ['GESTION ET VALORISATION DES DÉCHETS',"SENSIBILISATION A L’ECORESPONSABILITE","CONSOMMATION D’EAU",'CONSOMMATION ÉLECTRIQUE',"MOUILLAGES ET BOUÉES DE RÉGATES","DÉPLACEMENT DES ÉQUIPAGES ET DU PUBLIC","QUALITÉ DES EMBARCATIONS","QUALITÉ DES INSTALLATIONS ACCUEILLANTES"],
                   'Indices': [point1, point2, point3, point4,point5, point6, point7, point8]})
st.bar_chart(chart_data)
        
#RECOMMANDATIONS
st.markdown("<h1 style='text-align: center; color: orange;'>RECOMMANDATIONS</h1>", unsafe_allow_html=True)


if point1<2:
    st.text("GESTION ET VALORISATION DES DÉCHETS:" '''Lorem ipsum dolor sit amet, consectetur adipiscing 
elit.Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point2<2:
    st.text("SENSIBILISATION A L’ECORESPONSABILITE:" '''Lorem ipsum dolor sit amet, consectetur adipiscing 
elit.Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point3<3:
    st.text("CONSOMMATION D’EAU:" '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point4<2:
    st.text("CONSOMMATION ÉLECTRIQUE:" '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point5<2:
    st.text("MOUILLAGES ET BOUÉES DE RÉGATES:" '''Lorem ipsum dolor sit amet, consectetur adipiscing 
elit.Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point6<2:
    st.text("DÉPLACEMENT DES ÉQUIPAGES ET DU PUBLIC:"'''Lorem ipsum dolor sit amet, consectetur adipiscing 
elit.Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point7<2:
    st.text("QUALITÉ DES EMBARCATIONS:" '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

if point8<2:
    st.text("QUALITÉ DES INSTALLATIONS ACCUEILLANTES:" '''Lorem ipsum dolor sit amet,consectetur adipiscing 
elit.Nunc scelerisque nibh libero, eget elementum augue porttitor ac..''')

