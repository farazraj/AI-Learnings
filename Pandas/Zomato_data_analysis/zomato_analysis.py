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


#to display clean dataframe
def show_cleaned_data():
    print('CSV data after cleaning rate column:')
    print (df.to_string(), "\n")

#to check null
def check_null():
    print('check null values in each column : ')
    print(df.isnull())

    print('\ncheck sum of null values in each column : ')
    print(df.isnull().sum())


def check_rest_type():
    #a seaborn chart to display number of restaurants of each type

    ax = sns.countplot(x = df['listed_in(type)'], palette = diff_colors('listed_in(type)'), hue= df['listed_in(type)'], legend = True)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')

    plt.xlabel('Types Of Restaurants')
    plt.ylabel('Number of Restaurants')
    plt.title('Number of Restaurants of each type')
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()

#total votes given to each type of restaurant  
def votes_rest_type():
    
    df_votes = df.groupby(df['listed_in(type)'])['votes'].sum().reset_index()
    
    ax = sns.barplot(x = 'listed_in(type)', y = 'votes', data = df_votes, palette = diff_colors('listed_in(type)'), hue = 'listed_in(type)', legend = True)

    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')

    plt.xlabel('Types Of Restaurants')
    plt.ylabel('Votes Given')
    plt.title('Votes Given to each type of restaurant')
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()



#Most voted restaurant
def most_voted_restaurant():
    df_mv = df['votes'].max()

    most_voted = df.loc[df['votes'] == df_mv, ['name', 'votes', 'rate', 'approx_cost(for two people)', 'listed_in(type)']]

    print(most_voted.to_string(), "\n")


#Online order availibility
def online_order():
    ax = sns.countplot(x = df['online_order'], palette = diff_colors('online_order'), hue= df['online_order'], legend = True)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')
    plt.xlabel('Online Order Availability')
    plt.ylabel('Number of Restaurants')
    plt.title('Number of Restaurants with Online Order Availability')
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()


#Rate Analysis for number of retaurants with similar ratings
def rate_analysis():

    ax = sns.countplot(x = df['rate'], palette = diff_colors('rate'), hue= df['rate'], legend = True)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge')
    plt.xlabel('Rates')
    plt.ylabel('Number of Restaurants')
    plt.title('Number of Restaurants with rates')
    plt.xticks(rotation=45)  # Rotate labels if overlapping
    plt.tight_layout()
    plt.show()


#rating comparisons between online and offline restaurants
def rate_comparison():
    plt.figure(figsize=(10,6))   # create figure
    plt.suptitle("Zomato Rate Comparison", fontsize=16, fontweight="bold") #to give a super title above the titkle of the figure
    plt.gcf().canvas.manager.set_window_title("Zomato Rate Comparison")  # 👈 rename Figure 1
    
    sns.boxplot(x = 'online_order', y = 'rate', data = df, palette = diff_colors('online_order'), hue = 'online_order', legend = True)
    plt.xlabel('Online Order Availability')
    plt.ylabel('Rates')
    plt.title('Rate Comparison between Online and Offline Restaurants')
    plt.tight_layout()
    plt.show()


#Order mode preference by restaurant types(using pivot table and heatmap)
def order_mode_preference():
    pivot_table = df.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc = 'size', fill_value = 0) #aggfunc = size counts the rows in the groupby, if aggfunc = count be used we need to give value column to count like *value ='name'*.

    sns.heatmap(pivot_table, annot=True, fmt='d',cmap= 'YlGnBu')
    plt.gcf().canvas.manager.set_window_title("#Order mode preference by restaurant types")  # 👈 rename Figure 1
    plt.title('Heatmap for order mode analysis')
    plt.xlabel('Online Order')
    plt.ylabel('Listed In (Type)')
    plt.show()







# === Switch Dictionary ===
switch = {
    "1": show_cleaned_data,
    "2": check_null,
    "3": check_rest_type,
    "4": votes_rest_type,
    "5": most_voted_restaurant,
    "6": online_order,
    "7": rate_analysis,
    "8": rate_comparison,
    "9": order_mode_preference
}


# === Menu Function ===
def main():
    while True:
        print("\n=== Restaurant Data Analysis Menu via Zomato ===")
        print("1. Show Cleaned Data")
        print("2. Check Null Values")
        print("3. Check Restaurant Types")
        print("4. Votes by Restaurant Type")
        print("5. Most Voted Restaurant")
        print("6. Online Order Analysis")
        print("7. Rate Analysis")
        print("8. Rate Comparison")
        print("9. Order Mode Preference")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "10":
            print("Exiting program. Goodbye!")
            break
        elif choice in switch:
            switch[choice]()  # call selected function
        else:
            print("Invalid choice, please select a valid option.")


# === Run Automatically When File is Executed ===
if __name__ == "__main__":
    main()










