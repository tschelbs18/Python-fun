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
df.set_index('column_one') # Set index to column one

# Renaming Columns
df.columns = ['a','b','c']
df.rename(columns={'old_name':'new_name'})

### DATA CLEANING ###
pd.isnull() # Checks for null values, returns Boolean Array
pd.notnull() # Opposite of isnull()
df.dropna # Drop all rows with a null value
df.dropna(axis=1) # Drop all columns that contain null values
df.dropna(axis=1,thresh=n) # Drop all rows that have less than n non null values
df.fillna(x) # Replace all null values in the DF with x
s.fillna(s.mean()) # Replace all null values in a series with the mean (mean could be replaced w a different stats module function)
s.astype(float) # Convert the datatype of the series to float
s.replace(1, 'one') # replace all values in the series equal to 1 with "one"
s.replace([1,3],['one','three']) # reaplce all 1s with "one"s and 3s with "three"s

# Filtering and Sorting
df[df[col] > 0.5] # Filters to rows where col is greater than 0.5
df[(df[col] > 0.5) & (df[col] < 0.7)] # Filters to rows where col is between .5 and .7
 
# Applying Functions
df.apply(np.mean) # Apply the function np.mean() across each column
df.apply(np.max,axis=1) # Apply the function np.max() across each row

# Joining or Combining DFs
df1.append(df2) # Adds the rows in df2 to end of df1, columns should be identical
pd.concat([df1,df2],axis=1) # Add the columns in df1 to the end of df 2, rows should be identical
df1.join(df2, on=col1,how='inner') # SQl style join of columns in df1 to df2 where the rows for the named column have identical values

##### QUERYING DATAFRAMES #####

df.head(n) # View first N rows
df.tail(n) # View last n rows
df.shape # Number of rows and columns
df.info() # Index, Datatype, and Memory info
df.describe() # Summary Stats for numerical columns, this also works on groupby objects
s.value_counts(dropna=False) # View unique values and counts for a Series
df.apply(pd.Series.value_counts) # Unique values and counts for all columns

# Summary Statistics
df.mean() # Returns mean of all columns
df.corr() # Returns the correlation between columns in a DF
df.count() # Returns the number of non-null values in each DF column
df.max() # Returns the max value of each column
df.min() # Returns the min value of each column
df.median() # Returns the median value of each column
df.std() # Returns the STD of each column

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

# Sorting a DF
df.sort_values(col1) # Sorts by col1 in ascending order
df.sort_values(col2, ascending=False) # Sorts by col2 in desc order
df.sort_values([col1,col2],ascending=[True,False] # Sort values by col1 asc then col2 desc

# Group By
df.groupby(col1) # Returns a group by object for values from one column
df.groupby([col1,col2]) # Returns the mean of values in col2 grouped by col1 as a groupby object

# Pivot Table
df.pivot_table(index=col1, values=[col2,col3],aggfunc=np.mean) # Create a pivot table that groups by col1 and calcs mean of col2 and col3

##### EXPORTING DATAFRAMES TO FILES #####

'''
to_csv(filename) - Saves a CSV file
to_excel(filename) - Saves an Excel file
to_sql(table_name, connection_object) - Writes to a SQL table
to_json(filename) - Writes to a file in JSON
'''
