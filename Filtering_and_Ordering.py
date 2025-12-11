import pandas as pd

df = pd.read_csv(r"D:/Downloads/csv files/Sales.csv")
df[df['Sales'] <= 10000] # Filters the DataFrame to include only rows where the 'Sales' column is less than or equal to 10,000



# Filtering Data

specific_countries = ['India', 'Brazil','Bangladesh']
df[df['Country'].isin(specific_countries)]  # Filters the DataFrame to include only rows where the 'Country' column is in the specific_countries list

df[df['Country'].str.contains('United')]  # Filters the DataFrame to include only rows where the 'Country' column contains the substring 'United'

df2 = df.set_index('Country')  # Sets the 'Country' column as the index of the DataFrame
df2.filter(items=['India', 'Brazil'])  # Filters the DataFrame to include only the 'India' and 'Brazil' rows based on the index

df2.filter(items = ['India', 'Brazil'], axis = 0)  # Filters the DataFrame to include only the 'India' and 'Brazil' rows based on the index (axis=0)
df2.filter(like = 'United', axis = 0)  # Filters the DataFrame to include only rows where the index contains the substring 'United' (axis=0)

df2.loc['United States']  # Accesses the row with index 'United States'
df2.iloc[3]  # Accesses the row with index 3 (0-based index)



# Ordering Data

df[df['sales'] <= 10000].sort_values(by = ['Sales', 'Country'], ascending = False) # Filters the DataFrame to include only rows where the 'Sales' column is less than or equal to 10,000 and sorts the resulting DataFrame by 'Sales' and 'Country' in descending order

df[df['sales'] <= 10000].sort_values(by = ['Sales', 'Country'], ascending = [False, True]) # Filters the DataFrame to include only rows where the 'Sales' column is less than or equal to 10,000 and sorts the resulting DataFrame by 'Sales' in descending order and 'Country' in ascending order