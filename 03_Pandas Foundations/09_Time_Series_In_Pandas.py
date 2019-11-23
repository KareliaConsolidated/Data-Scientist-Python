# Using Pandas to Read datetime objects
# read_csv() function
	# Can read strings into datetime objects
	# Need to specify 'parse_dates = True'
# ISO 8601 Format
	# yyyy-mm-dd hh:mm:ss
import pandas as pd

sales = pd.read_csv('../Dataset/Pandas Foundations/sales-feb-2015.csv', parse_dates = True, index_col = 'Date')
print(sales.head())
print(sales.info())
print(sales.loc['2015-2-5'])

# Partial Datetime String Selection
# Alternative Formats:
	# sales.loc['February 5,2015']
	# sales.loc['2015-Feb-5']
# Whole month: sales.loc['2015-2']
# Whole Year : sales.loc['2015']
print('############### Selecting Whole Month ###################')
print(sales.loc['2015-2'])

# Slicing Using Dates/Times Strings
print('############### Slicing Using Dates/Times Strings ###################')
print(sales.loc['2015-02-16':'2015-02-20'])

# Converting String to Datetime Objects
evening_2_11 = pd.to_datetime(['2015-02-11 20:00:00','2015-02-11 21:00:00', '2015-02-11 22:00:00', '2015-02-11 23:00:00'])
print(evening_2_11)
# DatetimeIndex(['2015-02-11 20:00:00', '2015-02-11 21:00:00','2015-02-11 22:00:00', '2015-02-11 23:00:00'],dtype='datetime64[ns]', freq=None) 

# Reindexing DataFrame
print(sales.reindex(evening_2_11))

# Filling Missing Values
sales.reindex(evening_2_11, method='ffill') # Forward Fill

sales.reindex(evening_2_11, method='bfill') # Backward Fill