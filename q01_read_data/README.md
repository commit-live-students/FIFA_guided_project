# Read a CSV file into a DataFrame
What's the use of data and pandas if we can't even import the data?
This assignment aims to help you get comfortable importing data stored in one of the most used 
formats: `.csv`

## Write a function `q01_read_data` that

- Returns a Pandas DataFrame when given a path to a CSV file
- Limits and takes in only selected no.of columns to work upon which are given as follows -
'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Preferred Positions',
                       'Wage.


### Parameters
- path: path of the file to be loaded

### Returns
- DataFrame with Data from the CSV file. `dtype: DataFrame`
