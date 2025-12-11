import pandas as pd
df1 = pd.read_csv(r"D:/Downloads/csv files/LOTR.csv")

df2 = pd.read_csv(r"D:/Downloads/csv files/LOTR2.csv")

#Merging DataFrames

df1.merge(df2) # Merges df1 and df2 based on common columns

df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName']) # Performs an inner join on df1 and df2 based on 'FellowshipID' and 'FirstName' columns

df1.merge(df2, how = 'outer') # Performs an outer join on df1 and df2, keeping all rows from both DataFrames

df1.merge(df2, how = 'left') # Performs a left join on df1 and df2, keeping all rows from df1

df1.merge(df2, how = 'right') # Performs a right join on df1 and df2, keeping all rows from df2

df1.merge(df2, how = 'cross') # Performs a cross join on df1 and df2, creating a Cartesian product of both DataFrames

df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_left', rsuffix = '_right') # Joins df1 and df2 based on 'FellowshipID' with outer join, adding suffixes to overlapping column names

df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_left', rsuffix = '_Right', how = 'outer') # Sets 'FellowshipID' as index for both DataFrames and joins them with outer join, adding suffixes to overlapping column names


# Concatenating DataFrames

pd.concat([df1, df2]) # Concatenates df1 and df2 vertically (stacking rows)
pd.concat([df1, df2], axis = 1) # Concatenates df1 and df2 horizontally (adding columns)
pd.concat([df1, df2], join = 'inner', axis = 1) # Concatenates df1 and df2 horizontally, keeping only common columns
pd.concat([df1, df2], join = 'outer', axis = 1) # Concatenates df1 and df2 horizontally, keeping all columns from both DataFrames
pd.concat([df1, df2], ignore_index = True) # Concatenates df1 and df2 vertically, resetting the index


# Appending DataFrames
df1.append(df2) # Appends df2 to the end of df1