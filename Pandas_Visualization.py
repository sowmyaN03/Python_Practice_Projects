import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:/Downloads/csv files/Ice cream ratings.csv")

df = df.set_index('Date') # Sets the 'Date' column as the index of the DataFrame

df.plot() # Plots all numerical columns in the DataFrame against the index
df.plot(kind = 'line') # Plots all numerical columns in the DataFrame as line plots against the index
df.plot(kind = 'line', subplots = True) # Plots each numerical column in the DataFrame as separate line plots against the index
df.plot(kind = 'line', title = 'Ice Cream Rating', xlabel = 'Daily Ratings', ylabel = 'Scores') # Plots all numerical columns in the DataFrame as line plots with title and axis labels
print(plt.style.available) # Prints the list of available matplotlib styles
plt.style.use('seaborn-dark') # Sets the matplotlib style to 'seaborn-dark'


df.plot(kind = 'bar') # Plots all numerical columns in the DataFrame as bar plots against the index
df.plot(kind = 'bar', stacked = True) # Plots all numerical columns in the DataFrame as stacked bar plots against the index
df['Flover Rating'.plot(kind = 'bar', stacked = True)] #Plots the 'Flover Rating' column as a stacked bar plot

df['Flover Rating'.plot(kind = 'bar', color = 'red')] #Plots the 'Flover Rating' column as a bar plot with red color

df.plot.barh(stacked = True) # Plots all numerical columns in the DataFrame as stacked horizontal bar plots against the index

df.plot.scatter(x = 'Flover Rating', y = 'Texture Rating') # Plots a scatter plot with 'Flover Rating' on the x-axis and 'Texture Rating' on the y-axis
df.plot.scatter(x = 'Flover Rating', y = 'Texture Rating', c = 'Sweetness Level', cmap = 'viridis', colorbar = True) # Plots a scatter plot with 'Flover Rating' on the x-axis, 'Texture Rating' on the y-axis, and colors the points based on 'Sweetness Level' using the 'viridis' colormap
df.plot.scatter(x = 'Flover Rating', y = 'Texture Rating', s = 500, c = 'purple') # Plots a scatter plot with 'Flover Rating' on the x-axis, 'Texture Rating' on the y-axis, with point size 500 and purple color


df.plot.hist() # Plots histograms for all numerical columns in the DataFrame
df.plot.hist(bins = 20) # Plots histograms for all numerical columns in the DataFrame with 20 bins


df.plot.box() # Plots box plots for all numerical columns in the DataFrame
df.boxplot() # Plots box plots for all numerical columns in the DataFrame

df.plot.area() # Plots area plots for all numerical columns in the DataFrame
df.plot.area(figsize = (10, 5)) # Plots area plots for all numerical columns in the DataFrame with specified figure size
df.plot.area(stacked = False) # Plots unstacked area plots for all numerical columns in the DataFrame

df.plot.pie(y = 'Flavour Rating', figsize = (10, 5)) # Plots pie chart for 'Flavour Rating' column in the DataFrame with specified figure size
df.plot.pie(y = 'Flavour Rating', figsize = (10, 5), autopct = '%1.1f%%', colors = ['lightblue', 'lightgreen', 'lightcoral', 'gold', 'cyan']) # Plots pie chart for 'Flavour Rating' column in the DataFrame with specified figure size, percentage display, and custom colors

