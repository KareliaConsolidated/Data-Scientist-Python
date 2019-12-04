# Setting up a pivot table
# Pivot table allows you to see all of your variables as a function of two other variables. In this exercise, you will use the .pivot_table() method to see how the users DataFrame entries appear when presented as functions of the 'weekday' and 'city' columns. That is, with the rows indexed by 'weekday' and the columns indexed by 'city'.
import pandas as pd
users = pd.read_csv('../Dataset/Manipulating DataFrames with Pandas/users.csv')
# Before using the pivot table, print the users DataFrame in the IPython Shell and observe the layout.

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = pd.pivot_table(users, index= 'weekday', columns='city')

# Print by_city_day
print(by_city_day)

# Using other aggregations in pivot tables
# You can also use aggregation functions within a pivot table by specifying the aggfunc parameter. In this exercise, you will practice using the 'count' and len aggregation functions - which produce the same result - on the users DataFrame.

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = pd.pivot_table(users, index='weekday',aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = pd.pivot_table(users, index='weekday', aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))


# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = pd.pivot_table(users, index='weekday', aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Using margins in pivot tables
# Sometimes it's useful to add totals in the margins of a pivot table. You can do this with the argument margins=True. In this exercise, you will practice using margins in a pivot table along with a new aggregation function: sum.

# The users DataFrame, which you are now probably very familiar with, has been pre-loaded for you.

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = pd.pivot_table(users, index='weekday', aggfunc=sum, margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)