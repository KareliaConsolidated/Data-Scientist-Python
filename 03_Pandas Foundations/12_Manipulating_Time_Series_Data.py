# Manipulating Time Series Data
import pandas as pd
sales = pd.read_csv('../Dataset/Pandas Foundations/sales-feb-2015.csv', parse_dates = ['Date'])
print(sales.head())
print('############### Upper Case ###############')
print(sales['Company'].str.upper())
print('############### Contains ###############')
print(sales['Product'].str.contains('ware'))
print('############### Counting Number of Sales for Product Hardware/Software ###############')
print(sales['Product'].str.contains('ware').sum())
print('############### Datetime Methods ###############')
print(sales['Date'].dt.hour)
print('############### Datetime Methods : Convert Between Timezones ###############')
print(sales['Date'].dt.tz_localize('US/Central').dt.tz_convert('US/Eastern'))


population = pd.read_csv('../Dataset/Pandas Foundations/world_population.csv', parse_dates = True, index_col = 'Year')
print(population)
##### Upsample Population #####
print(population.resample('A').first())
##### Interpolate Missing Data #####
print(population.resample('A').first().interpolate('linear'))

# Method chaining and filtering
# We've seen that pandas supports method chaining. This technique can be very powerful when cleaning and filtering data.
# In this exercise, a DataFrame containing flight departure data for a single airline and a single airport for the month of July 2015 has been pre-loaded. Your job is to use .str() filtering and method chaining to generate summary statistics on flight delays each day to Dallas.

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip(' ')

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

# Missing values and interpolation
# One common application of interpolation in data analysis is to fill in missing data.
# In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.
# Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1 - ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())

# Time zones and conversion
# Time zone handling with pandas typically assumes that you are handling the Index of the Series. In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, and not just the Index.
# You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.
# Here we will use a mask to ensure that we only compute on data we actually want. To learn more about Boolean masks, click here!
# Build a Boolean mask to filter for the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')