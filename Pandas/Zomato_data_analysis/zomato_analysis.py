''' This is a project to analyze the Zomato restaurant data using Pandas library in Python.'''

#Common imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


#to read the the csv and put it in the dataframe also clean it so that teh dataframe can be used for futher
#analysis

df = pd.read_csv('Zomato-data-.csv')

print(df.head().to_string(), "\n")


#to create a function to clean the rate column so that it only displays rate and not '/5' and plain ratings
def clean_rate(r):
    r = str(r).split('/')
    if len(r) > 0:
        try:
            return float(r[0])
        except:
            return np.nan

#to apply different colors in the dataframe for each column
def diff_colors(x):
    unique_types = df[x].nunique()
    colors = [plt.cm.plasma(random.random()) for _ in range(unique_types)]

    return colors
        
df['rate'] = df['rate'].apply(clean_rate)

print('After cleaning the rate column:')
print (df.head().to_string(), "\n")


#to check null
def check_null():
    print('check null values in each column : ')
    print(df.isnull())

    print('\ncheck sum of null values in each column : ')
    print(df.isnull().sum())


def check_rest_type():
    #a seaborn chart to display number of restaurants of each type

    ax = sns.countplot(x = df['listed_in(type)'], palette = diff_colors('listed_in(type)'))
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')

    plt.xlable = 'Types Of Restaurants'
    plt.ylabel = 'Number of Restaurants'
    plt.title = 'Number of Restaurants of each type'
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()

    
def votes_rest_type():
    ax = sns.barplot(x = df['listed_in(type)'], y = df['votes'], palette = diff_colors('listed_in(type)'))

    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')

    plt.xlable = 'Types Of Restaurants'
    plt.ylabel = 'Votes Given'
    plt.title = 'Votes Given to each type of restaurant'
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()

votes_rest_type()






