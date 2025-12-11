import pandas as pd
df = pd.read_csv(r"D:/Downloads/csv files/Sales.csv")
#pd.read_csv(r"D:/Downloads/csv files/Sales", header = None, names = ['Country', 'Region']) # Reads a CSV file without headers and assigns column names 'Country' and 'Region'
df1 = pd.read_csv(r"D:/Downloads/csv files/Sales.txt") # Reads a TXT file as a CSV file

df2 = pd.read_csv(r"D:/Downloads/csv files/Sales.csv", sep = ';') # Reads a CSV file with a semicolon separator
df3 = pd.read_excel(r"D:/Downloads/csv files/Sales.xlsx") # Reads an Excel file 
df4 = pd.read_excel(r"D:/Downloads/csv files/Sales.xlsx", sheet_name = 'Sheet1') # Reads a specific sheet from an Excel file. the sheet name is used to specify the sheet to read.

# Display settings
pd.set_option('display.max_rows', 235) # Sets the option to display a maximum of 235 rows when printing a DataFrame
pd.set_option('display.max_columns', 40) # Sets the option to display a maximum of 40 columns when printing a DataFrame


df4.info()  # Displays information about the DataFrame, including the number of non-null entries and data types of each column
df4.shape  # Returns the shape of the DataFrame as a tuple (number of rows, number of columns)
df4.head(10)  # Displays the first 10 rows of the DataFrame
df4.tail(10)  # Displays the last 10 rows of the DataFrame

df4['Country']  # Accesses the 'Country' column of the DataFrame


df4.loc[224, ['Country', 'Region']]  # Accesses the 'Country' and 'Region' columns for the row with index 224 in df2
df4.iloc[224] # Accesses the row with index 224 using integer-location based indexing
