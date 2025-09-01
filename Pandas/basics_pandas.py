#common imports

import pandas as pd


#basics

def basics():
    import pandas as pd

    print("version - ", pd.__version__)
    print("show versions - ", pd.show_versions())


    mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
    }

    myvar = pd.DataFrame(mydataset)

    print(myvar)


#series
'''Panda series converts a list in one dimentional array'''
def series():

    a = [1, 7, 2]
    myvar = pd.Series(a)
    print("myvar series - ")
    print(myvar,"\n")

    print("first element - ") #to access a particular element in myvar
    print(myvar[0],"\n")

    #can create labels for the elements in the array

    myvar = pd.Series(a, index = ["x", "y", "z"])
    print("my var series with labels - ")
    print(myvar,"\n")

    print("element with label - ") #to access a particular element in myvar
    print(myvar['y'],"\n")


def series_dict():
    '''Panda series can also convert a dictionary in one dimentional array'''
    mydict = {'a': 1, 'b': 2, 'c': 3}
    myvar = pd.Series(mydict)
    print("myvar series from dict - ")
    print(myvar,"\n")

    print("element with label - ") #to access a particular element in myvar
    print(myvar['b'],"\n")





#dataframe
'''Panda dataframe converts a dictionary in two dimentional array'''
def dataframe():
    data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }

    #without index labels
    myvar = pd.DataFrame(data)
    
    
    #with index labels
    myvarl = pd.DataFrame(data, index = ["day1", "day2", "day3"])

    print("dataframe without index labels - ")
    print(myvar, "\n")

    print("dataframe with index labels - ")
    print(myvarl, "\n")

    print("accessing a particular row without label - ")
    print(myvar.loc[0], "\n")

    print("accessing a particular row with label - ")
    print(myvarl.loc["day2"], "\n")


#to load different file formats into dataframe
def load_files():

    #csv
    df = pd.read_csv('data.csv')

    print("csv file - ")
    print(df, "\n")

load_files()

