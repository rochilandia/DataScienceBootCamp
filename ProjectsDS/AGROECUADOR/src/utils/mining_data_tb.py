# @rochilandia

import pandas as pd
import numpy as np
from folder_tb import open_dataset

import requests
import matplotlib.pyplot as plt
import json
import seaborn as sns 
from seaborn import kdeplot
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.colors import n_colors
from plotly.subplots import make_subplots
import nbconvert as nb
import nbformat
%matplotlib inline 
import plot as pltt
import pycountry as pc 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import os # accessing directory structure



def open_datafreame(data):
    """
    limpieza de datos
    """
    df = pd.read_csv("https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv")
    df = df.dropna()
    df = df.reset_index(drop=True)
    list(df.columns)
    df.dtypes
    df



def regroup(data):
    """
    reorganizar los datos por el nro. de rating asifgnado
    """
    rating = df.groupby("Rating").max()
    rating.dtypes
    rating.shape
    rating.columns

    return rating



def cleaning (data):
    """
    buscar la manera de mostrar los datos de interes
    """
   rating.columns
   rating.shape
   rating.dtypes
   rating['Effects'].astype
   rating.reset_index(inplace=True)
   rating

   



