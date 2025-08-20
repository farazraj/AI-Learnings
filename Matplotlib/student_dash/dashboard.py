import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/marks.csv")


# Bar Chart of Average Marks
def avg_scores():
    """Function to plot average scores by subject."""
    avg_scores = df.mean(numeric_only=True)
    plt.figure()
    avg_scores.plot(kind="bar", color="skyblue")
    plt.title("Average Scores by Subject")
    plt.ylabel("Marks")
    plt.savefig("screenshots/avg_scores.png")
    plt.show()


# Scatter Plot (Math vs Science)

def scatter_math_science():
    """Function to plot scatter plot of Math vs Science."""
    plt.figure()
    plt.scatter(df["Math"], df["Science"], color="green")
    plt.title("Math vs Science Performance")
    plt.xlabel("Math Marks")
    plt.ylabel("Science Marks")
    plt.savefig("screenshots/math_vs_science.png")
    plt.show()

# Pie Chart (Pass vs Fail in English, pass >= 50)
def pass_fail_english():
    """Function to plot pie chart of pass vs fail in English."""
    plt.figure()
    pass_count = (df["English"] >= 50).sum()
    fail_count = (df["English"] < 50).sum()
    exp = [0, 0.1]  # explode the first slice (pass)
    plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%', explode=exp, shadow=True)
    plt.title("English Subject Pass/Fail")
    plt.savefig("screenshots/pass_fail.png")
    plt.show()


#total percent scored by each student
def total_percent():
    """Function to plot bar of total percent scored by each student."""
    #keeping the name as index to exclude name from the df, for  mean(axis=1) to work
    df = df.set_index("Name")
    plt.figure()
    total_percent = df.mean(axis=1)
    total_percent.plot(kind="bar", color="orange")
    plt.title("Total Percent Scored by Each Student")
    plt.ylabel("Total Percent")
    plt.savefig("screenshots/total_percent.png")
    plt.show()


#to show the overall performance of the student
def overall_performance(name):
    '''Function to plot overall performance of students in all subjects.
    '''
     
    data_frame = pd.read_csv("data/marks.csv")
    
    #keeping the name as index so that op.bar_label(op.containers[0]) works
    data_frame = df.set_index("Name")

    try:
        plt.figure()
        student_scores = data_frame.loc[name]
        op = student_scores.plot(kind="bar", color="purple")
        op.bar_label(op.containers[0])
        plt.title(f"Overall Performance of {name}")
        plt.ylabel("Marks")
        plt.savefig(f"screenshots/overall_performance_{name}.png")
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}. Please check the student name and try again.")




#to show the overall performance of the student without keeping name as an index
def overall_performance2(name):
    '''Function to plot overall performance of students in all subjects.'''

    try:
        plt.figure()
        student_scores = df[df["Name"] == name].iloc[0, 1:]  # skip "Name" column
        op = student_scores.plot(kind="bar", color="green")
        
        # Add values on top of bars
        for bar in op.patches:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2,
                     height + 1,
                     f"{height:.0f}",
                     ha="center", va="bottom", fontsize=10)
        
        plt.title(f"Overall Performance of {name}")
        plt.ylabel("Marks")
        plt.savefig(f"screenshots/overall_performance_{name}.png")
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}. Please check the student name and try again.")
