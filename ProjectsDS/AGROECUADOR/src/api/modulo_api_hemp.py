import pandas as pd
import numpy
import requests
import json
                                                                    # @Elsa TH

def rochi (url):
    
    df = pd.read_csv("https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv")
    df = df.dropna()
    df = df.reset_index(drop=True)
    df['Criteria'] = df['Effects'] + ',' + df['Flavor']
    df

    return df