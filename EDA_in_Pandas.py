import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:/Downloads/csv files/world_population.csv")
pd.set_option('display.float_format', lambda x: '%.2f' % x)  # Sets pandas to display float values with 2 decimal places

df.info()  # Displays information about the DataFrame including data types and non-null counts

df.describe()  # Generates descriptive statistics for numerical columns in the DataFrame

df.isnull().sum()  # Counts the number of missing values in each column

df.duplicated().sum()  # Counts the number of duplicate rows in the DataFrame

df.nunique()  # Counts the number of unique values in each column

df.sort_values(by="2022 Population", ascending=False).head(10) # Displays the top 10 rows with the highest '2022 Population'

sns.heatmap(df.corr(), annot = True) # Creates a heatmap to visualize the correlation matrix of the DataFrame with annotations
plt.rcParams['figure.gigsize'] = (20, 7) # Sets the size of the heatmap figure
plt.show() # Displays the heatmap plot which is a color-coded matrix showing correlations between numerical columns

df.groupby('Continent').mean() # Groups the DataFrame by 'Continent' and calculates the mean of each column

df.groupby('Continent').sum() # Groups the DataFrame by 'Continent' and calculates the sum of each column

df.groupby('Continent').count() # Groups the DataFrame by 'Continent' and counts the number of rows in each group

df2 = df.groupby('Continent').mean().sort_values(by="2022 Population", ascending=False) # Groups the DataFrame by 'Continent', calculates the mean of each column, and sorts by '2022 Population' in descending order

df[df['Continent'].str.contains('Oceania')] # Filters the DataFrame to include only rows where the 'Continent' column contains 'Oceania'

df2.plot() # Plots all numerical columns in df2 against the index (which is 'Continent')
df2.plot(kind = 'bar') # Plots all numerical columns in df2 as bar plots against the index (which is 'Continent')
df2.plot(kind = 'barh', stacked = True) # Plots all numerical columns
df2.plot(kind = 'pie', y = '2022 Population', autopct = '%1.1f%%') # Plots a pie chart for the '2022 Population' column in df2 with percentage display
df2.plot(kind = 'line', marker = 'o') # Plots all numerical columns in df2 as line plots with circle markers against the index (which is 'Continent')
plt.show() # Displays the plots

df3 = df2.transpose() # Transposes df2, swapping rows and columns
df3.plot() # Plots all numerical columns in df3 against the index (which is now the original columns of df2)

df.columns # Displays the column names of the DataFrame

df.groupby('Continent')[df.columns[5:13]].mean().sort_values(by="2022 Population", ascending=False) # Groups the DataFrame by the 'Continent' column and calculates the mean of the numerical columns from index 5 to 12 (inclusive) for each continent, then sorts the resulting DataFrame by the '2022 Population' column in descending order

df.boxplot(figsize=(20, 10)) # Creates box plots for all numerical columns in the DataFrame with specified figure size
plt.show() # Displays the box plot

df.dtypes # Displays the data types of each column in the DataFrame

df.select_dtypes(include='number') # Selects and displays only the numerical columns from the DataFrame
df.select_dtypes(include='object') # Selects and displays only the object (string) columns from the DataFrame


