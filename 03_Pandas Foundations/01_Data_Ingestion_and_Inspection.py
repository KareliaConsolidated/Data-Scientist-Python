# In this chapter, you will be introduced to pandas DataFrames. You will use pandas to import and inspect a variety of datasets, ranging from population data obtained from the World Bank to monthly stock data obtained via Yahoo Finance. You will also practice building DataFrames from scratch and become familiar with the intrinsic data visualization capabilities of pandas.
# Return Single Column From Dataset Returns Series
# Pandas Series is labelled 1 Dimensional NumPy Array
# Pandas DataFrame is labelled 2 Dimensional Array whose Column are Series

# NumPy and pandas working together
# Pandas depends upon and interoperates with NumPy, the Python library for fast numeric array computations. For example, you can use the DataFrame attribute .values to represent a DataFrame df as a NumPy array. You can also pass pandas data structures to NumPy methods. In this exercise, we have imported pandas as pd and loaded world population data every 10 years since 1960 into the DataFrame df. This dataset was derived from the one used in the previous exercise.

# Your job is to extract the values and store them in an array using the attribute .values. You'll then use those values as input into the NumPy np.log10() method to compute the base 10 logarithm of the population values. Finally, you will pass the entire pandas DataFrame into the same NumPy np.log10() method and compare the results.

# Import numpy
import numpy as np

# Create array of DataFrame values: np_vals
#np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
#np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
#df_log10 = np.log10(df)

# Print original and new data containers
# [print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]

# As a data scientist, you'll frequently interact with NumPy arrays, pandas Series, and pandas DataFrames, and you'll leverage a variety of NumPy and pandas methods to perform your desired computations. Understanding how NumPy and pandas work together will prove to be very useful.

# DataFrames from Dictionaries
import pandas as pd

data = {
	'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
	'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
	'visitors': [139, 237, 236, 456],
	'signups': [7, 12, 3, 5]
}

users = pd.DataFrame(data)

print(users)

#   weekday    city  visitors  signups
# 0     Sun  Austin       139        7
# 1     Sun  Dallas       237       12
# 2     Mon  Austin       236        3
# 3     Mon  Dallas       456        5
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 236, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['cities', 'signups', 'visitors', 'weekdays']
list_cols = [cities, signups, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))
data = dict(zipped)
users = pd.DataFrame(data)
print(users)

# Broadcasting
users['fees'] = 0 # Broadcasts to Entire Column
print(users)

# Broadcasting with a Dictionary
heights = [59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1]
data = {'heights': heights, 'Gender': 'M'}
results = pd.DataFrame(data)
print(results)
results.columns = ['height (in)', 'sex']
results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(results)

# Zip lists to build a DataFrame
# In this exercise, you're going to make a pandas DataFrame of the top three countries to win gold medals since 1896 by first building a dictionary. list_keys contains the column names 'Country' and 'Total'. list_values contains the full names of each country and the number of gold medals awarded. The values have been taken from Wikipedia.

# Your job is to use these lists to construct a list of tuples, use the list of tuples to construct a dictionary, and then use that dictionary to construct a DataFrame. In doing so, you'll make use of the list(), zip(), dict() and pd.DataFrame() functions. Pandas has already been imported as pd.

# Note: The zip() function in Python 3 and above returns a special zip object, which is essentially a generator. To convert this zip object into a list, you'll need to use list(). You can learn more about the zip() function as well as generators in Python Data Science Toolbox (Part 2).
# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

# Labeling your data
# You can use the DataFrame attribute df.columns to view and assign new string labels to columns in a pandas DataFrame.

# In this exercise, we have imported pandas as pd and defined a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia). Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. Your job is to use the df.columns attribute to re-assign descriptive column labels.
# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels

# Building DataFrames with broadcasting
# You can implicitly use 'broadcasting', a feature of NumPy, when creating pandas DataFrames. In this exercise, you're going to create a DataFrame of cities in Pennsylvania that contains the city name in one column and the state name in the second. We have imported the names of 15 cities as the list cities.
# Your job is to construct a DataFrame from the list of cities and the string 'PA'.

# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Read in the file: df1
df1 = pd.read_csv(data_file)

# Create a list of the new column labels: new_labels
new_labels = ['year','population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv(data_file, header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)

# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

#Delimiters, headers, and extensions
# Not all data files are clean and tidy. Pandas provides methods for reading those not-so-perfect data files that you encounter far too often.

# In this exercise, you have monthly stock data for four companies downloaded from Yahoo Finance. The data is stored as one row for each company and each column is the end-of-month closing price. The file name is given to you in the variable file_messy.

# In addition, this file has three aspects that may cause trouble for lesser tools: multiple header lines, comment records (rows) interleaved throughout the data rows, and space delimiters instead of commas.

# Your job is to use pandas to read the data from this problematic file_messy using non-default input options with read_csv() so as to tidy up the mess at read time. Then, write the cleaned up data to a CSV file with the variable file_clean that has been prepared for you, as you might do in a real data workflow.

# You can learn about the option input parameters needed by using help() on the pandas function pd.read_csv().
# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)

# Plotting DataFrames
# Comparing data from several columns can be very illuminating. Pandas makes doing so easy with multi-column DataFrames. By default, calling df.plot() will cause pandas to over-plot all column data, with each column as a single line. In this exercise, we have pre-loaded three columns of data from a weather data set - temperature, dew point, and pressure - but the problem is that pressure has different units of measure. The pressure data, measured in Atmospheres, has a different vertical scaling than that of the other two data columns, which are both measured in degrees Fahrenheit.

# Your job is to plot all columns as a multi-line plot, to see the nature of vertical scaling problem. Then, use a list of column names passed into the DataFrame df[column_list] to limit plotting to just one column, and then just 2 columns of data. When you are finished, you will have created 4 plots. You can cycle through them by clicking on the 'Previous Plot' and 'Next Plot' buttons.

# As in the previous exercise, inspect the DataFrame df in the IPython Shell using the .head() and .info() methods.
# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots = True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()