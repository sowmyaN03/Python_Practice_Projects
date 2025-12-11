import pandas as pd
df = pd.read_csv(r"D:/Downloads/csv files/Sales.csv")

df = pd.read_csv(r"D:/Downloads/csv files/Sales.csv", index_col = 'Country')  # Reads the CSV file and sets the 'Country' column as the index

df.reset_index(inplace = True)  # Resets the index of the DataFrame, converting the index back into a regular column

df.set_index('Country', inplace = True)  # Sets the 'Country' column as the index of the DataFrame

df.loc['India']  # Accesses the row with index 'India'
df.iloc[1] # Accesses the row with index 1 (0-based index)
df.loc['India', 'Sales']  # Accesses the 'Sales' column for the row with index 'India'


df.reset_index(inplace = True)  # Resets the index of the DataFrame, converting the index back into a regular column

df.set_index(['Continent', 'Country'], inplace = True)  # Sets a multi-level index using the 'Continent' and 'Country' columns

df.sort_index()  # Sorts the DataFrame based on the multi-level index
df.sort_index(ascending = True)

df.loc['Africa', 'Angola'] # Accesses the row with multi-level index ('Africa', 'Angola')

df.iloc[1] # Accesses the row with index 1 (0-based index)

