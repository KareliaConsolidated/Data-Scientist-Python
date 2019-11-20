# Pivot(): Unmelting Data
# Opposite of Melting
# In Melting, We Turned Columns into Rows
# In Pivoting, We Turn Unique Values into Separate Columns
# Analysis-friendly shape to reporting-friendly shape
# Violates tidy data principle: rows contain observation
import numpy as np
weather.pivot(values='value', index='date', columns='element')
# Throws ValueError, if for same date, there is more than one values for MIN

# Solution : pivot_table()
# Has a Parameter that Specifies How to Deal with Duplicate Values
# Example : Can Aggregate the Duplicate Values by Takeing Their Average
# weather.pivot_table(values = 'value', index='date', columns='element', aggfunc = np.mean)

# Pivot Data
# Pivoting data is the opposite of melting it. Remember the tidy form that the airquality DataFrame was in before you melted it? You'll now begin pivoting it back into that form using the .pivot_table() method!
# While melting takes a set of columns and turns it into a single column, pivoting will create a new column for each unique value in a specified column.
# .pivot_table() has an index parameter which you can use to specify the columns that you don't want pivoted: It is similar to the id_vars parameter of pd.melt(). Two other parameters that you have to specify are columns (the name of the column you want to pivot), and values (the values to be used when the column is pivoted). The melted DataFrame airquality_melt has been pre-loaded for you.
# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Resetting the index of a DataFrame
# After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.
# What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).
# Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow you to group columns or rows by another variable - in this case, by 'Month' as well as 'Day'.
# There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index(). 
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())

# Pivoting duplicate values
# Pivot table the airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Print the head of airquality_pivot before reset_index
print(airquality_pivot.head())

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())

# The default aggregation function used by .pivot_table() is np.mean(). So you could have pivoted the duplicate values in this DataFrame even without explicitly specifying the aggfunc parameter.

# Splitting a column with .str

import pandas as pd
# Dataset consisting of case counts of tuberculosis by country, year, gender, and age group.
tb = pd.read_csv('../Dataset/Cleaning Data in Python/tb.csv.txt')
# In this exercise, you're going to tidy the 'm014' column, which represents males aged 0-14 years of age. In order to parse this value, you need to extract the first letter into a new column for gender, and the rest into a column for age_group. Here, since you can parse values by position, you can take advantage of pandas' vectorized string slicing by using the str attribute of columns of type object.
# Melt tb: tb_melt
tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())

# Notice the new 'gender' and 'age_group' columns you created. It is vital to be able to split columns as needed so you can access the data that is relevant to your question.
# Splitting a column with .split() and .get()
# Another common way multiple variables are stored in columns is with a delimiter. You'll learn how to deal with such cases in this exercise, using a dataset consisting of Ebola cases and death counts by state and country. It has been pre-loaded into a DataFrame as ebola.
# Print the columns of ebola in the IPython Shell using ebola.columns. Notice that the data has column names such as Cases_Guinea and Deaths_Guinea. Here, the underscore _ serves as a delimiter between the first part (cases or deaths), and the second part (country).
# This time, you cannot directly slice the variable by position as in the previous exercise. You now need to use Python's built-in string method called .split(). By default, this method will split a string into parts separated by a space. However, in this case you want it to split by an underscore. You can do this on 'Cases_Guinea', for example, using 'Cases_Guinea'.split('_'), which returns the list ['Cases', 'Guinea'].
# The next challenge is to extract the first element of this list and assign it to a type variable, and the second element of the list to a country variable. You can accomplish this by accessing the str attribute of the column and using the .get() method to retrieve the 0 or 1 index, depending on the part you want.


# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())
