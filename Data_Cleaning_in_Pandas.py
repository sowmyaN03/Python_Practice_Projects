import pandas as pd
df = pd.read_csv(r"D:/Downloads/csv files/Customer Call List.xlsx")

df = df.drop_duplicates() # Removes duplicate rows from the DataFrame
df.drop(colums = 'Not_Useful_Column', inplace = True) # Drops the specified column from the DataFrame

df["Last_Name"].str.strip() # Removes leading and trailing whitespace from the 'Last_Name' column
df["Last_Name"].str.lstrip() # Removes leading whitespace from the 'Last_Name' column
df["Last_Name"].str.rstrip("_") # Removes trailing whitespace from the 'Last_Name' column
df["Last_Name"].str.lstrip("/", "...") # Removes leading '/' and '...' characters from the 'Last_Name' column
df["Last_Name"] = df["Last_Name"].str.strip("123./") # Removes leading and trailing '1', '2', '3', '.', and '/' characters from the 'Last_Name' column

df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '') # Removes all non-alphanumeric characters from the 'Phone_Number' column

df["Phone_Number"].apply(lambda x: x[0-3] + '-' + x[3:6] + '-' + x[6:10]) # Formats the 'Phone_Number' column to the format 'xxx-xxx-xxxx'. it has to be string to apply this function
df["Phone_Number"] = str(df["Phone_Number"].apply(lambda x: x[0-3] + '-' + x[3:6] + '-' + x[6:10])) # Converts the formatted 'Phone_Number' column to string type

df["Phone_Number"].str.replace('nan---', '') # Removes 'nan---' from the 'Phone_Number' column
df["Phone_Number"].str.replace('Na---', '') # Removes 'Na---' from the 'Phone_Number' column


df["Street Address", "State", "Zip_Code"].str.split(',',2, expand=True) # Splits the 'Street Address', 'State', and 'Zip_Code' columns into separate columns based on the first two commas

df["Paying_Customer"] = df["Paying_Customer"].str.replace('Yes', 'Y') # Replaces 'Yes' with 'Y' in the 'Paying_Customer' column
df["Paying_Customer"] = df["Paying_Customer"].str.replace('No', 'N') # Replaces 'No' with 'N' in the 'Paying_Customer' column
df.str.replace('N/a', '') # Replaces 'N/a' with an empty string in all string columns of the DataFrame

df = df.fillna('') # Fills all NaN values in the DataFrame with an empty string

for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)  # Drops rows where 'Do_Not_Contact' column is 'Y'



df["Do_Not_Contact"].str.replace('', 'N') # Replaces empty strings with 'N' in the 'Do_Not_Contact' column


for x in df.index:
    if df.loc[x,"Phone_Number"] == 'Y':
        df.drop(x, inplace=True)  # Drops rows where 'Phone_Number' column is 'Y'

#Other way to drop null values
df = df.dropna(subset=['Phone_Number']) # Drops rows where 'Phone_Number' column has NaN values

df.reset_index(drop=True, inplace=True) # Resets the index of the DataFrame after dropping rows


