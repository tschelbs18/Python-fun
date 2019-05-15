# DataFrame Manipulations Refresh: DataFrames and Series
import pandas as pd
import numpy as np

##### MAKING DATAFRAMES #####

# From a Dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
# Format is key = column name, value = list of values in column ordered to match the same record
brics = pd.DataFrame(dict)
print(brics)

# From a CSV
csv_df = pd.read_csv(path)

'''
Can also use any of the following:
    -read_csv(filename) (CSV file)
    -read_table(filename) (delimited text file, like TSV)
    -read_excel(filename) (Excel file)
    -read_sql(query, connection_object) (reads from a SQL table or DB)
    -read_json(json_string) (read from a JSON string, URL, or file)
    -read_html(url) (parses an HTML URL, string or files, and extracts tables to a list of DF's)
    -read_clipboard() Takes the contents of your clipboard and passes to read_table
'''


##### ADDING TO DATAFRAMES #####






##### MANIPULATING DATAFRAMES #####

# Setting the Index
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Set Index to be Column 0 of DF, which could be anything
cars = pd.read_csv('cars.csv', index_col = 0)

# Renaming Columns
df.columns = ['a','b','c']

### DATA CLEANING ###
pd.isnull() # Checks for null values, returns Boolean Array
pd.notnull() # Opposite of isnull()



##### QUERYING DATAFRAMES #####

df.head(n) # View first N rows
df.tail(n) # View last n rows
df.shape # Number of rows and columns
df.info() # Index, Datatype, and Memory info
df.describe() # Summary Stats for numerical columns
s.value_counts(dropna=False) # View unique values and counts for a Series
df.apply(pd.Series.value_counts) # Unique values and counts for all columns


# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out observation for Japan, 2 means row 2, which is japan
# iloc is index based
print(cars.iloc[2]) # This pulls all cols from specified row
print(cars.iloc[2,2]) # This pulls from row and column
print(cars.iloc[:,2]) # This pulls all rows from specified column

# Print out observations for Australia and Egypt
# loc is label based
print(cars.loc[['AUS', 'EG']]) #AUS and EG are indexes so all columns from specified rows, same as print(cars.loc[['AUS', 'EG'],:])
print(cars.loc[['AUS', 'EG'],['cars_per_cap','drives_right']]) # This pulls from row and column
print(cars.loc[:,['cars_per_cap','drives_right']]) # This pulls from all rows for specified columns


##### EXPORTING DATAFRAMES TO FILES #####

'''
to_csv(filename) - Saves a CSV file
to_excel(filename) - Saves an Excel file
to_sql(table_name, connection_object) - Writes to a SQL table
to_json(filename) - Writes to a file in JSON
'''
