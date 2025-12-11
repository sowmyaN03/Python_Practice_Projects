import pandas as pd
df = pd.read_csv(r"D:/Downloads/csv files/Flavors.csv")

group_by_frame = df.groupby('Base Flavor')

group_by_frame.mean() # Calculates the mean of each numeric column for each group in 'Base Flavor'
df.groupby('Base Flavor').mean() # Alternative way to calculate the mean of each numeric column for each group in 'Base Flavor'

df.groupby('Base Flavor').count()  # Counts the number of non-null entries for each column in each group in 'Base Flavor'
df.groupby('Base Flavor').min() # Finds the minimum value for each numeric column for each group in 'Base Flavor'
df.groupby('Base Flavor').max() # Finds the maximum value for each numeric column for each

group_by_frame.sum()  # Calculates the sum of each numeric column for each group in 'Base Flavor'
group_by_frame.size()  # Returns the size of each group in 'Base Flavor'

# Aggregating Data

df.groupby('Base Flavor').agg({'Flavour Rating' : ['mean', 'max', 'count', 'sum']}) # Calculates the mean, max, min, and sum of 'Flavour Rating' and the mean, max, count, and sum of 'Sweetness Level' for each group in 'Base Flavor'

df.groupby('Base Flavor').agg({'Flavour Rating' : ['mean', 'max', 'count', 'sum'], 'Texture Rating' : ['mean', 'max', 'count', 'sum']}) # Calculates the mean, max, count, and sum of 'Flavour Rating' and the mean, max, count, and sum of 'Texture Rating' for each group in 'Base Flavor'

df.groupby(['Base Flavor', 'Liked']).mean() # Calculates the mean of each numeric column for each group in 'Base Flavor' and 'Liked'

df.groupby(['Base Flavor', 'Liked']).agg({'Flavour Rating' : ['mean', 'max', 'count', 'sum'], 'Texture Rating' : ['mean', 'max', 'count', 'sum']}) # Calculates the mean, max, count, and sum of 'Flavour Rating' and the mean, max, count, and sum of 'Texture Rating' for each group in 'Base Flavor' and 'Liked'

df.groupby('Base Flavor').describe() # Calculates the mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum of each numeric column for each group in 'Base Flavor'

