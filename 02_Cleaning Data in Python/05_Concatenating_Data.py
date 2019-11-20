# Combining Data
# Data may not always come in 1 Huge File
# 5 Million row dataset may be broken into 5 separate datasets
# Easier to store and share
# May have new data for each day
# concatenated = pd.concat([weather_p1, weather_p2])
# Reset Indexing by pd.concat([weather_p1, weather_p2], ignore_index=True)
# Concatenate uber1, uber2, and uber3: row_concat
import pandas as pd
# row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
# print(row_concat.shape)

# Print the head of row_concat
# print(row_concat.head())

# Combining columns of data
# Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default, axis=0, is for a row-wise concatenation.
# You'll return to the Ebola dataset you worked with briefly in the last chapter. It has been pre-loaded into a DataFrame called ebola_melt. In this DataFrame, the status and country of a patient is contained in a single column. This column has been parsed into a new DataFrame, status_country, where there are separate columns for status and country.
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
# ebola_tidy = pd.concat([ebola_melt,status_country], axis = 1)

# Print the shape of ebola_tidy
# print(ebola_tidy.shape)

# Print the head of ebola_tidy
# print(ebola_tidy.head())

# Concatenating Many Files
# Leverage Python's features with data cleaning in  pandas
# In order to concatenate DataFrames:
	# They must be in a list
	# Can individually load if there are a few datasets
	# But what if there are thousands
	# Solution: glob() function to find files based on a pattern

# Globbing
	# Pattern Matching for File Names
	# Wildcards: * and ?
		# Any CSV Files: *.csv
		# Any Single Character" file_?.csv
	# Returns a list of file names
	# Can use this list to load into separate DataFrames
# THE PLAN
# Load Files from globbing into pandas
# Add the DataFrames into a List!
# Concatenate Multiple Datasets at Once
# Find and Concatenate
import glob
csv_files = glob.glob('*.csv')
print(csv_files)

# Finding files that match a pattern
# You're now going to practice using the glob module to find all csv files in the workspace. In the next exercise, you'll programmatically load them into DataFrames.
# As Dan showed you in the video, the glob module has a function called glob that takes a pattern and returns a list of the files in the working directory that match that pattern.
# For example, if you know the pattern is part_ single digit number .csv, you can write the pattern as 'part_?.csv' (which would match part_1.csv, part_2.csv, part_3.csv, etc.)
# Similarly, you can find all .csv files with '*.csv', or all parts with 'part_*'. The ? wildcard represents any 1 character, and the * wildcard represents any number of characters.

# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())

# The next step is to iterate through this list of filenames, load it into a DataFrame, and add it to a list of DataFrames you can then concatenate together.

# Iterating and concatenating all matches
# Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.

# You'll start with an empty list called frames. Your job is to use a for loop to:

# iterate through each of the filenames
# read each filename into a DataFrame, and then
# append it to the frames list.
# You can then concatenate this list of DataFrames using pd.concat(). Go for it!

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())
