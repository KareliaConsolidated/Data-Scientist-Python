############### Exercise ################
# Creating datetimes by hand
# Often you create datetime objects based on outside data. Sometimes though, you want to create a datetime object from scratch.

# You're going to create a few different datetime objects from scratch to get the hang of that process. These come from the bikeshare data set that you'll use throughout the rest of the chapter.

############# Instructions ##############
# Import the datetime class.
# Create a datetime for October 1, 2017 at 15:26:26.
# Print the results in ISO format.
# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())

############# Instructions ##############
# Import the datetime class.
# Create a datetime for December 31, 2017 at 15:19:13.
# Print the results in ISO format.
# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Print the results in ISO 8601 format
print(dt.isoformat())

############# Instructions ##############
# Create a new datetime by replacing the year in dt with 1917 (instead of 2017)
# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print(dt_old)

############### Exercise ################
# Counting events before and after noon
# In this chapter, you will be working with a list of all bike trips for one Capital Bikeshare bike, W20529, from October 1, 2017 to December 31, 2017. This list has been loaded as onebike_datetimes.

# Each element of the list is a dictionary with two entries: start is a datetime object corresponding to the start of a trip (when a bike is removed from the dock) and end is a datetime object corresponding to the end of a trip (when a bike is put back into a dock).

# You can use this data set to understand better how this bike was used. Did more trips start before noon or after noon?

############# Instructions ##############
# Within the for loop, complete the if statement to check if the trip started before noon.
# Within the for loop, increment trip_counts['AM'] if the trip started before noon, and trip_counts['PM'] if it started after noon.
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
  
print(trip_counts)

############### Exercise ################
# Turning strings into datetimes
# When you download data from the Internet, dates and times usually come to you as strings. Often the first step is to turn those strings into datetime objects.

# In this exercise, you will practice this transformation.

# Reference	
# %Y	4 digit year (0000-9999)
# %m	2 digit month (1-12)
# %d	2 digit day (1-31)
# %H	2 digit hour (0-23)
# %M	2 digit minute (0-59)
# %S	2 digit second (0-59)

############# Instructions ##############
# Determine the format needed to convert s to datetime and assign it to fmt.
# Convert the string s to datetime using fmt.
# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD HH:MM:SS format
s = '2017-02-03 00:00:01'

# Write a format string to parse s
fmt = '%Y-%m-%d %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)
############# Instructions ##############
# Determine the format needed to convert s to datetime and assign it to fmt.
# Convert the string s to datetime using fmt.
# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD format
s = '2030-10-15'

# Write a format string to parse s
fmt = '%Y-%m-%d'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)

############# Instructions ##############
# Determine the format needed to convert s to datetime and assign it to fmt.
# Convert the string s to datetime using fmt.
# Import the datetime class
from datetime import datetime

# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'

# Write a format string to parse s
fmt = '%m/%d/%Y %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)

############### Exercise ################
# Parsing pairs of strings as datetimes
# Up until now, you've been working with a pre-processed list of datetimes for W20529's trips. For this exercise, you're going to go one step back in the data cleaning pipeline and work with the strings that the data started as.

# Explore onebike_datetime_strings in the IPython shell to determine the correct format. datetime has already been loaded for you.

# Reference	
# %Y	4 digit year (0000-9999)
# %m	2 digit month (1-12)
# %d	2 digit day (1-31)
# %H	2 digit hour (0-23)
# %M	2 digit minute (0-59)
# %S	2 digit second (0-59)

############# Instructions ##############
# Outside the for loop, fill out the fmt string with the correct parsing format for the data.
# Within the for loop, parse the start and end strings into the trip dictionary with start and end keys and datetime objects for values.
# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)

############### Exercise ################
# Recreating ISO format with strftime()
# In the last chapter, you used strftime() to create strings from date objects. Now that you know about datetime objects, let's practice doing something similar.

# Re-create the .isoformat() method, using .strftime(), and print the first trip start in our data set.

# Reference	
# %Y	4 digit year (0000-9999)
# %m	2 digit month (1-12)
# %d	2 digit day (1-31)
# %H	2 digit hour (0-23)
# %M	2 digit minute (0-59)
# %S	2 digit second (0-59)

############# Instructions ##############

# Complete fmt to match the format of ISO 8601.
# Print first_start with both .isoformat() and .strftime(); they should match.
# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))

############### Exercise ################
# Unix timestamps
# Datetimes are sometimes stored as Unix timestamps: the number of seconds since January 1, 1970. This is especially common with computer infrastructure, like the log files that websites keep when they get visitors.

############# Instructions ##############
# Complete the for loop to loop over timestamps.
# Complete the code to turn each timestamp ts into a datetime.
# Import datetime
from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = []

# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))
  
# Print results
print(dts)

############### Exercise ################
# Turning pairs of datetimes into durations
# When working with timestamps, we often want to know how much time has elapsed between events. Thankfully, we can use datetime arithmetic to ask Python to do the heavy lifting for us so we don't need to worry about day, month, or year boundaries. Let's calculate the number of seconds that the bike was out of the dock for each trip.

# Continuing our work from a previous coding exercise, the bike trip data has been loaded as the list onebike_datetimes. Each element of the list consists of two datetime objects, corresponding to the start and end of a trip, respectively.

############# Instructions ##############
# Within the loop:
# Use arithmetic on the start and end elements to find the length of the trip
# Save the results to trip_duration.
# Calculate trip_length_seconds from trip_duration.

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds()
  
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)

############### Exercise ################
# Average trip time
# W20529 took 291 trips in our data set. How long were the trips on average? We can use the built-in Python functions sum() and len() to make this calculation.

# Based on your last coding exercise, the data has been loaded as onebike_durations. Each entry is a number of seconds that the bike was out of the dock.

############# Instructions ##############  
# Calculate total_elapsed_time across all trips in onebike_durations.
# Calculate number_of_trips for onebike_durations.
# Divide total_elapsed_time by number_of_trips to get the average trip length.

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)
  
# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)
# Great work, and not remotely average! For the average to be a helpful summary of the data, we need for all of our durations to be reasonable numbers, and not a few that are way too big, way too small, or even malformed. For example, if there is anything fishy happening in the data, and our trip ended before it started, we'd have a negative trip length.

############### Exercise ################
# The long and the short of why time is hard
# Out of 291 trips taken by W20529, how long was the longest? How short was the shortest? Does anything look fishy?

# As before, data has been loaded as onebike_durations.

############# Instructions ##############  
# Calculate shortest_trip from onebike_durations.
# Calculate longest_trip from onebike_durations.
# Print the results, turning shortest_trip and longest_trip into strings so they can print.

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")
# For at least one trip, the bike returned before it left. Why could that be? Here's a hint: it happened in early November, around 2AM local time. What happens to clocks around that time each year? By the end of the next chapter, we'll have all the tools we need to deal with this situation!