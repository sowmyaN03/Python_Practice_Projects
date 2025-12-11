#Web Scrapping with BeautifulSoup and Requests
from bs4 import BeautifulSoup
import requests
url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup.prettify())

#Find and Find_All
soup.find_all('p', class_ = 'lead')  # Finds all paragraph tags
soup.find('p', class_ = 'lead').text # Finds the first paragraph tag with class 'lead'
soup.find('h1')     # Finds the first h1 tag

soup.find_all('th')  # Finds all table header tags
soup.find('th').text.strip() # Finds the first table header tag and strips whitespace




#Scraping Data from a Real Website + Pandas

url1 = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.text, 'html')
print(soup1.prettify())

soup1.find_all('table')[1] # Finds the second table tag
soup1.find_all('table', class_ = "wikitable sortable")[1]  # Finds the second table tag with class 'wikitable sortable'
table = soup1.find_all('table')[1]
print(table.prettify()) # prettify makes the html more readable

world_titles = soup1.find_all('th')  # Finds all table header tags
soup1.find_all('th')[0].text.strip() # Finds the first table header

world_table_titles = [title.text.stripe() for title in world_titles] # List comprehension to get all table header titles and strip whitespace
print(world_table_titles)

import pandas as pd
df = pd.DataFrame(columns = world_table_titles) # Create a DataFrame from the list of table header titles
column_data = table.find_all('tr') 

for row in column_data[1:]:
    row_data = row.find_all('td') # Finds all table data tags in each row:
    individual_row_data = [data.text.strip() for data in row_data]    

    length = len(df)  # Get the current length of the DataFrame
    df.loc[length] = individual_row_data  # Add the row data to the DataFrame

