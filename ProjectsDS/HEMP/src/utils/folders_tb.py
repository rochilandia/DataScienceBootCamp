# @rochilandia

import pandas as pd


# Función para abrir el dataset. Convertir el csv en dataframe
url="https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv"

def open_dataset():
   """ 
    Dataframe de la url = "https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv"
   """
   df = pd.read_csv(url)
   return df