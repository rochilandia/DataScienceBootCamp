# @ElsaTH

import pandas as pd
import numpy
import matplotlib.pyplot as plt 
from folder_tb import open_dataset
import mining_data_tb

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


#PIE CHART
#1. Find the subject: the student must find the project itself. This is something he/she
#wants to do.
#2. Find the data related to the project: research where it can be and if it is accessible
#from the public.
#3. Define a hypothesis: find something you can conclude with your data.
#4. Define the necessary steps to demonstrate or not your hypothesis.
#5. With the code structure defined and using Python
#6. Document all the steps

def piechart ('Subject','Data',	'Hypothesis', 'Steps', 'Code','Document'):
    chart = pd.DataFrame({'Subject': 3, 'Data': 5, 'Hypothesis': 7,'Steps':2, 'Code': 3, 'Document': 2}, index=['Days'])
    chart
  
    labels = 'Subject',	'Data',	'Hypothesis', 'Steps', 'Code', 'Document'
    fracs = [3, 5, 7, 2, 3, 2]
    fig1, ax1 = plt.subplots()
    ax1.pie(labels=labels, autopct='%5.0f%%', x=index, shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

...


def effects (rating):
    """
    Representación de la gráfica de los efectos de la hoja de Cannabis segun su "variedad"
    """

    fig = go.Figure(data=go.Scatter(x=rating['Effects'], y=rating['Strain'],mode='lines')) # hover text goes here
    fig.update_layout(title='Effects of Cannabis leaf over Strain',
        xaxis_title="Effects", yaxis_title="Strains")
    fig.show()
    

...


def cannabistype (rating):
    """
    Representación de los efectos dependiendo del tipo de hoja
    """
    fig = go.Figure(data=go.Scatter(x=rating['Effects'],y=rating['Type'],mode='lines')) # hover text goes here
    fig.update_layout(title='Effects depending on the Type of Cannabis leaf',
        xaxis_title="Effects",yaxis_title="Type")    
    fig.show()
    
    

def coutliers(rating):
    """
    Representación de outliers 
    """
    plt.boxplot(rating.Flavor,
            notch=True, patch_artist=None,
            capprops=dict(color="#DC7633",markerfacecolor='g'),
            medianprops=dict(color="orange", alpha=0.3),
            whiskerprops=dict(color="green",alpha=0.9, markersize=17,linestyle = 'dotted'),
            flierprops=dict(color="#DC7633",alpha=0.9, markersize=5,markerfacecolor="#DC7633", marker='o'),
            boxprops=dict(color="orange",alpha=0.9, markersize=5),
            showmeans=dict(color="green",alpha=0.9, markersize=5),
            showfliers=dict(color="green",alpha=0.9, markersize=5),
            showbox=dict(color="green",alpha=0.9, markersize=5),
            showcaps=dict(color="green",alpha=0.9, markersize=5)
          )          
    plt.title("OUTLIERS",size=14, color="#0E6655")
    plt.xticks([1], ['Flavor'])
    plt.xlabel('Flavor', size=14, color="#0E6655")
    plt.show()


...


def flavor(rating):
    fig = plt.figure()
    ax = fig.add_subplot(111)
#Your df.plot code with ax parameter here
    rating.plot.bar(stacked=True, rot=0, alpha=0.5, legend=True, ax=fig.gca())

    labels = ['' for item in ax.get_xticklabels()]
    ax.set_xticklabels(labels)
    ax.set_xlabel('Flavors')
    fig.subplots_adjust(bottom=.1*rating.index.nlevels)
    plt.show()


...


def bargraph(rating):
    rating.plot(kind="bar",figsize=(10, 8),color=["#D5F5E3","#C39BD3","#DC7633","#5D6D7E","#85C1E9"])
    plt.title('Flavor', size=20, color="#138D75")
    plt.xlabel('Rating', size=14, color="#138D75")
    plt.ylabel('Strain',size=14, color="#138D75")
    plt.xticks(rotation=0,FontSize=12)
    plt.yticks(rotation=0,FontSize=12)

    plt.show()


def histo(rating):
    rating['Strain'].hist(bins=5)
    rating['Rating'].hist(bins=5)
    rating['Type'].hist(bins=5)
    plt.xticks(rotation=90)