'''

Seaborn is a powerful Python library for making statistical graphics. It sits on top of Matplotlib, but makes complex plots easier to create with better default styles.

Here’s a breakdown of the different types of plots in Seaborn, their functionalities, and use cases:

📊 1. Categorical Plots

Used when x-axis is categorical (discrete values like gender, city, product type).

sns.countplot()
Shows the frequency/count of categories.
✅ Use case: Number of restaurants by type, number of students in each grade.

sns.barplot()
Shows mean (or other estimator) of a numeric variable for each category.
✅ Use case: Average salary by job role, average rating by restaurant type.

sns.boxplot()
Shows distribution (median, quartiles, outliers).
✅ Use case: Comparing income distribution by gender, marks distribution by class.

sns.violinplot()
Combines boxplot + KDE (distribution curve).
✅ Use case: Detailed view of salary distributions across industries.

sns.stripplot()
Shows individual data points, jittered to avoid overlap.
✅ Use case: Visualizing distribution of students’ marks in each class.

sns.swarmplot()
Like stripplot but arranges points to avoid overlapping.
✅ Use case: Showing small datasets with individual points visible.

📈 2. Distribution Plots

Used to understand the distribution of numerical data.

sns.histplot()
Histogram of values (with optional KDE).
✅ Use case: Age distribution of customers.

sns.kdeplot()
Kernel Density Estimate → smooth curve of probability density.
✅ Use case: Smooth visualization of height/weight distributions.

sns.ecdfplot()
Empirical cumulative distribution.
✅ Use case: Probability of a student scoring less than X marks.

🔗 3. Relational Plots

Used to visualize relationship between two variables.

sns.scatterplot()
Scatter plot with points.
✅ Use case: Height vs Weight, Advertising budget vs Sales.

sns.lineplot()
Line chart (good for time-series).
✅ Use case: Stock price trend over time, daily temperature change.

sns.relplot()
General function to create scatterplot or lineplot with extra facets (rows/columns).
✅ Use case: Sales trend across different product categories.

📉 4. Matrix Plots

Good for correlations and heatmaps.

sns.heatmap()
Color-coded matrix, often used for correlation.
✅ Use case: Correlation between features in a dataset, confusion matrices.

sns.clustermap()
Heatmap with hierarchical clustering.
✅ Use case: Grouping genes in bioinformatics, customer segmentation.

🧑‍🤝‍🧑 5. Pair & Multi-variable Plots

Used for exploring relationships among multiple variables.

sns.pairplot()
Creates scatterplots between all numeric variables.
✅ Use case: EDA (exploratory data analysis) on a dataset with many features.

sns.jointplot()
Scatterplot + histograms for two variables.
✅ Use case: Relationship between age and income, including distribution.

sns.lmplot()
Linear regression fit between two variables.
✅ Use case: Predicting sales from marketing spend.

🌈 6. Regression Plots

Specialized for fitting models.

sns.regplot()
Scatterplot + regression line.
✅ Use case: Relationship between advertising budget and sales revenue.

sns.residplot()
Shows residuals (differences between predicted and actual).
✅ Use case: Checking linear regression fit quality.

🎯 Quick Cheat Sheet by Use Case
Task	Best Plot
Count of categories	countplot
Compare averages	barplot
Compare distributions	boxplot, violinplot
Show all data points	stripplot, swarmplot
Show numeric distribution	histplot, kdeplot
Time-series trend	lineplot
Compare 2 variables	scatterplot, jointplot, regplot
Correlation matrix	heatmap
Explore all features	pairplot

⚡ Now, Seaborn is mostly used in Exploratory Data Analysis (EDA) before modeling, because it quickly shows patterns, distributions, and relationships.



'''



'''

1. Countplot
sns.countplot(x="Category", data=df)


Shows the frequency count of categories.

Use case: How many items belong to each category (like restaurant types, gender counts, etc.).

2. Barplot
sns.barplot(x="Category", y="Value1", data=df)


Plots the mean (or other estimator like median) of a numerical variable for each category.

Use case: Average sales per region, average rating per product type.

3. Boxplot
sns.boxplot(x="Category", y="Value1", data=df)


Shows distribution summary: median, quartiles, and outliers.

Use case: Compare salary distribution across departments, exam score spread across classes.

4. Histogram (with KDE)
sns.histplot(df["Value1"], kde=True)


Shows the distribution of a single variable.

KDE = smooth density curve.

Use case: Age distribution of customers, distribution of product prices.

5. Scatterplot
sns.scatterplot(x="Value1", y="Value2", hue="Category", data=df)


Shows relationship between two numeric variables.

Use case: Height vs Weight, Price vs Sales.

6. Lineplot
sns.lineplot(x=range(len(df)), y="Value2", data=df)


Shows trends over an ordered variable (often time).

Use case: Stock prices over time, temperature trends per month.

7. Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")


Visualizes a matrix (like correlation matrix) using colors.

Use case: Find correlations between numerical variables (e.g., sales vs ads vs profit).

8. Pairplot
sns.pairplot(df[["Value1", "Value2", "Value3"]], diag_kind="kde")


Plots scatterplots for every pair of variables and distributions on the diagonal.

Use case: Explore relationships between multiple features at once (e.g., ML datasets).

9. Jointplot
sns.jointplot(x="Value1", y="Value2", data=df, kind="reg")


Combines scatterplot + distribution plots in one.

Can add regression line with kind="reg".

Use case: Compare two variables and also see their individual distributions (e.g., study hours vs exam scores).

👉 So, in short:

Countplot = frequency of categories

Barplot = average per category

Boxplot = distribution + outliers

Histogram = distribution of a single variable

Scatterplot = relationship between two variables

Lineplot = trend over time/order

Heatmap = correlation/matrix visualization

Pairplot = all variable relationships at once

Jointplot = scatter + distribution combo


'''