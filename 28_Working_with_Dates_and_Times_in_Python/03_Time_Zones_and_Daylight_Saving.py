############### Exercise ################
# Creating timezone aware datetimes
# In this exercise, you will practice setting timezones manually.

############# Instructions ##############
# Import timezone.
# Set the tzinfo to UTC, without using timedelta.
# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())

############# Instructions ##############
# Set pst to be a timezone set for UTC-8.
# Set dt's timezone to be pst.
# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

############# Instructions ##############
# Set tz to be a timezone set for UTC+11.
# Set dt's timezone to be tz.
# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())
# Did you know that Russia and France are tied for the most number of time zones, with 12 each? The French mainland only has one timezone, but because France has so many overseas dependencies they really add up!

############### Exercise ################
# Setting timezones
# Now that you have the hang of setting timezones one at a time, let's look at setting them for the first ten trips that W20529 took.

# timezone and timedelta have already been imported. Make the change using .replace()

############# Instructions ##############
# Create edt, a timezone object whose UTC offset is -4 hours.
# Within the for loop:
# Set the tzinfo for trip['start'].
# Set the tzinfo for trip['end'].

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = edt)
  trip['end'] = trip['end'].replace(tzinfo = edt)
#  Did you know that despite being over 2,500 miles (4,200 km) wide (about as wide as the continential United States or the European Union) China has only one official timezone? There's a second, unofficial timezone, too. It is used by much of the Uyghurs population in the Xinjiang province in the far west of China.

############### Exercise ################
# What time did the bike leave in UTC?
# Having set the timezone for the first ten rides that W20529 took, let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.
############# Instructions ##############
# Within the for loop, set dt to be the trip['start'] but moved to UTC. Use timezone.utc as a convenient shortcut for UTC.

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start and set it to UTC
  dt = trip['start'].astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())

############### Exercise ################
# Putting the bike trips into the right time zone
# Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.

############# Instructions ##############  
# Import tz from dateutil.
# Assign et to be the timezone 'America/New_York'.
# Within the for loop, set start and end to have et as their timezone (use .replace()).
# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=et)
  trip['end'] = trip['end'].replace(tzinfo=et)

# Time zone rules actually change quite frequently. IANA time zone data gets updated every 3-4 months, as different jurisdictions make changes to their laws about time or as more historical information about timezones are uncovered. tz is smart enough to use the date in your datetime to determine which rules to use historically.  

############### Exercise ################
# What time did the bike leave? (Global edition)
# When you need to move a datetime from one timezone into another, use .astimezone() and tz. Often you will be moving things into UTC, but for fun let's try moving things from 'America/New_York' into a few different time zones.

############# Instructions ##############  
# Set uk to be the timezone for the UK: 'Europe/London'.
# Change local to be in the uk timezone and assign it to notlocal.
# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())
############# Instructions ##############  
# Set ist to be the timezone for India: 'Asia/Kolkata'.
# Change local to be in the ist timezone and assign it to notlocal.
# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())
############# Instructions ##############  
# Set sm to be the timezone for Samoa: 'Pacific/Apia'.
# Change local to be in the sm timezone and assign it to notlocal.
# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

############### Exercise ################
# How many hours elapsed around daylight saving?
# Since our bike data takes place in the fall, you'll have to do something else to learn about the start of daylight savings time.

# Let's look at March 12, 2017, in the Eastern United States, when Daylight Saving kicked in at 2 AM.

# If you create a datetime for midnight that night, and add 6 hours to it, how much time will have elapsed?

############# Instructions ##############  
# You already have a datetime called start, set for March 12, 2017 at midnight, set to the timezone 'America/New_York'.

# Add six hours to start and assign it to end. Look at the UTC offset for the two results.
