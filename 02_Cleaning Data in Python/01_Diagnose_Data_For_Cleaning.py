# Cleaning Data
# Prepare Data for Analysis
# Data almost never comes in clean
# Diagnose your data for problems

# Common Data Problems
# Inconsistent Column Names
# Missing Data
# Outliers
# Duplicate Rows
# Untidy
# Need to process columns
# Column types can signal unexpected data values
# Useful functions and attributes: df.columns, df.shape, df.info(), df.describe() # Will Return Column of Numeric Type, df.column_name.value_counts(dropna=False).head()
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('../Dataset/Cleaning Data in Python/dob_job_application_filings_subset.csv.txt')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Further diagnosis
# In the previous exercise, you identified some potentially unclean or missing data. Now, you'll continue to diagnose your data with the very useful .info() method.
# The .info() method provides important information about a DataFrame, such as the number of rows, number of columns, number of non-missing values in each column, and the data type stored in each column. This is the kind of information that will allow you to confirm whether the 'Initial Cost' and 'Total Est. Fee' columns are numeric or strings. From the results, you'll also be able to see whether or not all columns have complete data in them.
# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())

# Excellent! Notice that the columns 'Initial Cost' and 'Total Est. Fee' are of type object. The currency sign in the beginning of each value in these columns needs to be removed, and the columns need to be converted to numeric. In the full DataFrame, note that there are a lot of missing values. You saw in the previous exercise that there are also a lot of 0 values. Given the amount of data that is missing in the full dataset, it's highly likely that these 0 values represent missing data.

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

#  Notice how not all values in the 'State' column are NY. This is an interesting find, as this data is supposed to consist of applications filed in NYC. Curiously, all the 'Borough' values are correct. A good start as to why this may be the case would be to find and look at the codebook for this dataset. Also, for the 'Site Fill' column, you may or may not need to recode the NOT APPLICABLE values to NaN in your final analysis.