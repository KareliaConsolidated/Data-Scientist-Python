import pandas as pd

sales = pd.read_csv('../Dataset/Pandas Foundations/sales-feb-2015.csv', parse_dates=True, index_col='Date')
print(sales.head())

# Resampling 
# Statistical methods over different time intervals.
	# mean(), sum(), count() etc.

# Downsampling
	# Reduce Datetime Rows to Slower Frequency (Ex: Daily to Weekly)
# Upsampling 
	# Increase Datetime Rows to Faster Frequency (Ex: Daily to Hourly)

# Aggregating Means
daily_mean = sales.resample("D").mean() # D - Daily
print(daily_mean)
# Verifying
print(daily_mean.loc['2015-2-2']) # 6
print(sales.loc['2015-2-2', 'Units'].mean()) # 6

# Method Chaining
daily_sum = sales.resample('D').sum()
print(daily_sum)

print(sales.resample('D').sum().max()) # Max Number of Unit Sold

# Resampling Strings
print(sales.resample('W').count())

# Resampling Frequencies
# Input			Frequencies 
# 'min','T'	 	minute
# 'H'			hour
# 'D'			day
# 'B'			business day
# 'W'			week
# 'M'			month
# 'Q'			quarter
# 'A'			year

# Multiplying Frequencies # Daily to Weekly
print(sales.loc[:, 'Units'].resample('2W').sum())
# Date
# 2015-02-08    82
# 2015-02-22    79
# 2015-03-08    15

# Upsampling
two_days = sales.loc['2015-2-4':'2015-2-5', 'Units']
print(two_days)
# Date
# 2015-02-05 01:53:06    19
# 2015-02-04 21:52:45    14
# 2015-02-05 22:05:03    10
# 2015-02-04 15:36:29    13
# Name: Units, dtype: int64

# UpSampling and Filling
two_days.resample('4H').ffill()

# Resampling and frequency
# Pandas provides methods for resampling time series data. When downsampling or upsampling, the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.
# For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().
# In this exercise, a data set containing hourly temperature data has been pre-loaded for you. Your job is to resample the data using a variety of aggregation methods to answer a few questions.
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()

# Separating and resampling
# With pandas, you can resample in different ways on different subsets of your data. For example, resampling different months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the last exercise has been pre-loaded.
# Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as df. You will be working with the 'Temperature' column.
# Extract temperature data for August: august
august = df['Temperature']['2010-August']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature']['2010-February']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

# Rolling mean and frequency
# In this exercise, some hourly weather data is pre-loaded for you. You will continue to practice resampling, this time using rolling means.
# Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.
# To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point. The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data.
# Your job is to resample the data using the combination of .rolling() and .mean(). You will work with the same DataFrame df from the previous exercise.

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window = 24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()

# Resample and roll with it
# As of pandas version 0.18.0, the interface for applying rolling transformations to time series has become more consistent and flexible, and feels somewhat like a groupby (If you do not know what a groupby is, don't worry, you will learn about it in the next course!).
# You can now flexibly chain together resampling and rolling operations. In this exercise, the same weather data from the previous exercises has been pre-loaded for you. Your job is to extract one month of data, resample to find the daily high temperatures, and then use a rolling and aggregation operation to smooth the data.
# Extract the August 2010 data: august
august = df['Temperature']['2010-August']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)