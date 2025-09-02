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

    #json
    dfj = pd.read_json('data.json')

    
    print("csv file - ")
    print(df, "\n") #prints the whole dataframe

    print("json file - ")
    print(dfj, "\n") #prints the whole dataframe

    print(pd.options.display.max_rows) #prints the max rows that can be displayed
    

#data cleaning
def data_cleaning():
    df = pd.read_csv('data_clean.csv')

    print(df.to_string(), "\n") #prints the whole dataframe

    dfc = df.dropna() #drops the rows with null values
    print("after dropping null values - ")
    print(dfc.to_string(), "\n")


def data_replacement():
    df = pd.read_csv('data_clean.csv')

    print(df.to_string(), "\n") #prints the whole dataframe

    dfr = df.fillna(130) #replaces the null values with 130
    print("after replacing null values - ")
    print(dfr.to_string(), "\n")

    dfc = df.fillna({'Calories':130, 'Duration':45}) #replaces the null values in specific columns
    print("after replacing null values to column - ")
    print(dfc.to_string(), "\n")



#dropping a column with null values using name 
def data_drop_column():
    df = pd.read_csv('data_clean.csv')


    df.dropna(subset = ['Calories'], inplace=True) #drops the rows with null values in specific column

    '''when using inplace=True, the original dataframe is modified and nothing is returned so,
    reassigning it to another variable like df = df.dropna(subset = ['Calories'], inplace=True)  
    will return NoneType error'''

    print(df.to_string())


#changing the format of data
def change_format():

    df = pd.read_csv('data_w_date.csv')

    print(df.to_string(), "\n") #prints the whole dataframe

    # df['Date'] = df['Date'].str.strip("'")
    df['Date'] = pd.to_datetime(df['Date'], format='mixed') #changes the format of date column to datetime
    print("after changing the format of date column - ")
    print(df.to_string(), "\n")





#to find out if it row has duplicate rows
def duplicate_rows():
    df = pd.read_csv('data_w_date.csv')

    print(df.duplicated())

    df.drop_duplicates(inplace=True) #drops the duplicate rows
    print(df.to_string())


#relationship between two columns
def relation_columns():
    df = pd.read_csv('data_clean.csv')

    print(df.to_string(), "\n") #prints the whole dataframe

    print("relation between two columns - ")
    print(df.corr().to_string(), "\n") #prints the relation between two columns


relation_columns()
