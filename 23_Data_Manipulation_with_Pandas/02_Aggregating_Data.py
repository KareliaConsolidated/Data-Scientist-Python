# Exercise
# Mean and median
# Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. For example, mean, median, minimum, maximum, and standard deviation are summary statistics. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.

# sales is available and pandas is loaded as pd.

# Instructions
# Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
# Print information about the columns in sales.
# Print the mean of the weekly_sales column.
# Print the median of the weekly_sales column.

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())
# The mean weekly sales is almost double the median weekly sales! This can tell you that there are a few very high sales weeks that are making the mean so much higher than the median.

# Exercise
# Summarizing dates
# Summary statistics can also be calculated on date columns which have values with the data type datetime64. Some summary statistics — like mean — don't make a ton of sense on dates, but others are super helpful, for example minimum and maximum, which allow you to see what time range your data covers.
# sales is available and pandas is loaded as pd.

# Instructions
# Print the maximum of the date column.
# Print the minimum of the date column.

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())
# Super summarizing! Taking the minimum and maximum of a column of dates is handy for figuring out what time period your data covers. In this case, there's data from February of 2010 to October of 2012.

# Exercise
# Efficient summaries
# While pandas and NumPy have tons of functions, sometimes you may need a different function to summarize your data.

# The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making your aggregations super efficient.

# In the custom function for this exercise, "IQR" is short for inter-quartile range, which is the 75th percentile minus the 25th percentile. It's an alternative to standard deviation that is helpful if your data contains outliers.

# sales is available and pandas is loaded as pd.

# Instructions
# Use the custom iqr function defined for you along with .agg() to print the IQR of the temperature_c column of sales.

# Update the column selection to use the custom iqr function with .agg() to print the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.

# Update the aggregation functions called by .agg(): include iqr and np.median in that order.

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c","fuel_price_usd_per_l","unemployment"]].agg(iqr))

# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# Excellent efficiency! The .agg() method makes it easy to compute multiple statistics on multiple columns, all in just one line of code.

# Exercise
# Cumulative statistics
# Cumulative statistics can also be helpful in tracking summary statistics over time. In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow you to identify what the total sales were so far as well as what the highest weekly sales were so far.

# A DataFrame called sales_1_1 has been created for you, which contains the sales data for department 1 of store 1. pandas is loaded as pd.

# Instructions
# Sort the rows of sales_1_1 by the date column in ascending order.
# Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
# Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# Exercise

# Dropping duplicates
# Removing duplicates is an essential skill to get accurate counts, because often you don't want to count the same thing multiple times. In this exercise, you'll create some new DataFrames using unique values from sales.

# sales is available and pandas is imported as pd.

# # Instructions
# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
# Subset the rows that are holiday weeks, and drop the duplicate dates, saving as holiday_dates.
# Select the date column of holiday_dates, and print.
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(['store','department'])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates('date')

# Print date col of holiday_dates
print(holiday_dates['date'])

# Dazzling duplicate dropping! The holiday weeks correspond to the Superbowl in February, Labor Day in September, Thanksgiving in November, and Christmas in December. Now that the duplicates are removed, it's time to do some counting.

# # Exercise
# Counting categorical variables
# Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, you'll count the number of each type of store and the number of each department number.

# The stores and departments DataFrames you created in the last exercise are available and pandas is imported as pd.

# Instructions
# Count the number of stores of each store type.
# Count the proportion of stores of each store type.
# Count the number of different department numbers, sorting the counts in descending order.
# Count the proportion of different department numbers, sorting the proportions in descending order.
