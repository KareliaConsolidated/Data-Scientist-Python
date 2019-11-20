# String Manipulation
# Much of data cleaning involves string manipulation.
# Most of the world's data is unstructured text.
# Also have to do string manipulation to make datasets consistent with one another.

# String Manipulation Library 
# "re" library for regular expressions.
	# A Formal way of specifying a pattern
	# Sequence of characters
# Pattern Matching
# Example Match
# 17	-	\d* (* represents 0 or more time)
# $17   - 	\$\d* (\$ is escaping $ sign, as it is already has predefined value)
# $17.00 - 	\$\d*\.\d* (. has meaning in regex, . represents matching any one character)
# $17.89 - 	\$\d*\.\d{2} (Exactly 2 Values)
# $17.895 - ^\$\d*\.\d{2}$
import re
pattern = re.compile('\$\d*\.\d{2}')
result = pattern.match('$17.89')
print(bool(result))

# String parsing with regular expressions
# When working with data, it is sometimes necessary to write a regular expression to look for properly entered values. Phone numbers in a dataset is a common field that needs to be checked for validity. Your job in this exercise is to define a regular expression to match US phone numbers that fit the pattern of xxx-xxx-xxxx.
#The regular expression module in python is re. When performing pattern matching on data, since the pattern will be used for a match across multiple rows, it's better to compile the pattern first using re.compile(), and then use the compiled pattern to match values.
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))

# Extracting numerical values from strings
# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches) # ['10', '1']

#==================================================================================#

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='\w*', string='Australia'))
print(pattern3)
