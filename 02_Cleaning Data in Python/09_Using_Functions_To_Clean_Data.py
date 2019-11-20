import re
from numpy import NaN

pattern = re.compile('^\$\d*\.\d{2}$')

def diff_money(row, pattern):
	icost = row['Initial Cost']
	tef = row['Total Est. Fee']

	if bool(pattern.match(icost)) and bool(pattern.match(tef)):
		icost = icost.replace('$','')
		tef = tef.replace('$','')

		icost = float(icost)
		tef = float(tef)

		return icost - tef
	else:
		return(NaN)

df_subset['diff'] = df_subset.apply(diff_money, axis=1, pattern = pattern)

# Custom functions to clean data
# You'll now practice writing functions to clean data.
# The tips dataset has been pre-loaded into a DataFrame called tips. It has a 'sex' column that contains the values 'Male' or 'Female'. Your job is to write a function that will recode 'Female' to 0, 'Male' to 1, and return np.nan for all entries of 'sex' that are neither 'Female' nor 'Male'.
# Recoding variables like this is a common data cleaning task. Functions provide a mechanism for you to abstract away complex bits of code as well as reuse code. This makes your code more readable and less error prone.
# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())

# Lambda functions

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())
