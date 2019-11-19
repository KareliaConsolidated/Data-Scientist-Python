# Import package
import numpy as np
import matplotlib.pyplot as plt
# Assign filename to variable: file
file = '../Dataset/Importing Data From Dataset/mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# Customizing your NumPy import
# What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other than a comma? What if you only wish to import particular columns?

# There are a number of arguments that np.loadtxt() takes that you'll find useful:

# delimiter changes the delimiter that loadtxt() is expecting.
# You can use ',' for comma-delimited.
# You can use '\t' for tab-delimited.
# skiprows allows you to specify how many rows (not indices) you wish to skip
# usecols takes a list of the indices of the columns you wish to keep.
# Import numpy
# import numpy as np

# Assign the filename: file
file = '../Dataset/Importing Data From Dataset/digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)

# Importing different datatypes
# The file seaslug.txt

# has a text header, consisting of strings
# is tab-delimited.
# These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. Read more here.

# Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).

# Alternatively, you can skip the first row as we have seen before, using the skiprows argument.
# Assign filename: file
file = '../Dataset/Importing Data From Dataset/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

File_Path = '../Dataset/Importing Data From Dataset/titanic.csv'
file = np.genfromtxt(File_Path, delimiter=',',names=True,dtype=None)

# Working with mixed datatypes (2)
# Assign the filename: file

# Import file using np.recfromcsv: d
d = np.recfromcsv(File_Path, delimiter=',',names=True,dtype=None)

# Print out first three entries of d
print(d[:3])
