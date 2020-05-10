############### Exercise ################
# Loading a csv file in Pandas
# The capital_onebike.csv file covers the October, November and December rides of the Capital Bikeshare bike W20529.

# Here are the first two columns:

# Start date	End date	...
# 2017-10-01 15:23:25	2017-10-01 15:26:26	...
# 2017-10-01 15:42:57	2017-10-01 17:49:59	...

############# Instructions ############## 
# Import Pandas.
# Complete the call to read_csv() so that it correctly parses the date columns Start date and End date.
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])

############### Exercise ################
# Making timedelta columns
# Earlier in this course, you wrote a loop to subtract datetime objects and determine how long our sample bike had been out of the docks. Now you'll do the same thing with Pandas.

# rides has already been loaded for you.

############# Instructions ############## 
# Subtract the Start date column from the End date column to get a Series of timedeltas; assign the result to ride_durations.
# Convert ride_durations into seconds and assign the result to the 'Duration' column of rides.

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())

############### Exercise ################
# How many joyrides?
# Suppose you have a theory that some people take long bike rides before putting their bike back in the same dock. Let's call these rides "joyrides".

# You only have data on one bike, so while you can't draw any bigger conclusions, it's certainly worth a look.

# Are there many joyrides? How long were they in our data set? Use the median instead of the mean, because we know there are some very long trips in our data set that might skew the answer, and the median is less sensitive to outliers.

############# Instructions ############## 
# Create a Pandas Series which is True when Start station and End station are the same, and assign the result to joyrides.
# Calculate the median duration of all rides.
# Calculate the median duration of joyrides.

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"\
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"\
      .format(rides[joyrides]['Duration'].median()))

############### Exercise ################
# It's getting cold outside, W20529
# Washington, D.C. has mild weather overall, but the average high temperature in October (68ºF / 20ºC) is certainly higher than the average high temperature in December (47ºF / 8ºC). People also travel more in December, and they work fewer days so they commute less.

# How might the weather or the season have affected the length of bike trips?
############# Instructions ############## 
# Resample rides to the daily level, based on the Start date column.
# Plot the .size() of each result.
# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to daily, take the size, plot the results
rides.resample('D', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 15])

# Show the results
plt.show()
############# Instructions ############## 
# Since the daily time series is so noisy for this one bike, change the resampling to be monthly.

# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])

# Show the results
plt.show()

############### Exercise ################
# Members vs casual riders over time
# Riders can either be "Members", meaning they pay yearly for the ability to take a bike at any time, or "Casual", meaning they pay at the kiosk attached to the bike dock.

# Do members and casual riders drop off at the same rate over October to December, or does one drop off faster than the other?

# As before, rides has been loaded for you. You're going to use the Pandas method .value_counts(), which returns the number of instances of each value in a Series. In this case, the counts of "Member" or "Casual".

############# Instructions ############## 
# Set monthly_rides to be a resampled version of rides, by month, based on start date.
# Use the method .value_counts() to find out how many Member and Casual rides there were, and divide them by the total number of rides per month.
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on = 'Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

############### Exercise ################
# Combining groupby() and resample()
# A very powerful method in Pandas is .groupby(). Whereas .resample() groups rows by some time or date information, .groupby() groups rows based on the values in one or more columns. For example, rides.groupby('Member type').size() would tell us how many rides there were by member type in our entire DataFrame.

# .resample() can be called after .groupby(). For example, how long was the median ride by month, and by Membership type?

############# Instructions ############## 
# Complete the .groupby() call to group by 'Member type', and the .resample() call to resample according to 'Start date', by month.
# Print the median Duration for each group.
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())

############### Exercise ################
# Timezones in Pandas
# Earlier in this course, you assigned a timezone to each datetime in a list. Now with Pandas you can do that with a single method call.

# (Note that, just as before, your data set actually includes some ambiguous datetimes on account of daylight saving; for now, we'll tell Pandas to not even try on those ones. Figuring them out would require more work.)
############# Instructions ############## 
# Make the Start date column timezone aware by localizing it to 'America/New_York' while ignoring any ambiguous datetimes.
# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])
############# Instructions ############## 
# Now switch the Start date column to the timezone 'Europe/London' using the .dt.tz_convert() method.
# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])

############### Exercise ################
# How long per weekday?
# Pandas has a number of datetime-related attributes within the .dt accessor. Many of them are ones you've encountered before, like .dt.month. Others are convenient and save time compared to standard Python, like .dt.weekday_name.
# ############# Instructions ############## 
# Add a new column to rides called 'Ride start weekday', which is the weekday of the Start date.
# Print the median ride duration for each weekday.

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())


############### Exercise ################
# How long between rides?
# For your final exercise, let's take advantage of Pandas indexing to do something interesting. How much time elapsed between rides?

# ############# Instructions ############## 
# Calculate the difference in the Start date of the current row and the End date of the previous row and assign it to rides['Time since'].
# Convert rides['Time since'] to seconds to make it easier to work with.
# Resample rides to be in monthly buckets according to the Start date.
# Divide the average by (60*60) to get the number of hours on average that W20529 waited in the dock before being picked up again.

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on = 'Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))