################ Exercise ################
# Uniform currencies
# In this exercise and throughout this chapter, you will be working with a retail banking dataset stored in the banking DataFrame. The dataset contains data on the amount of money stored in accounts, their currency, amount invested, account opening date and last transaction date that were consolidated from American and European branches.

# You are tasked with understanding the average account size and how investments vary by the size of account, however in order to produce this analysis accurately, you first need to unify the currency amount into dollars. The pandas package has been imported as pd, and the banking DataFrame is in your environment.

############ Instructions ################
# Find the rows of acct_cur in banking that are equal to 'euro' and store them in acct_eu.
# Find all the rows of acct_amount in banking that fit the acct_eu condition, and convert them to USD by multiplying them with 1.1.
# Find all the rows of acct_cur in banking that fit the acct_eu condition, set them to 'dollar'.

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Print unique values of acct_cur
assert banking['acct_cur'].unique() == 'dollar'

################ Exercise ################
# Uniform dates
# After having unified the currencies of your different account amounts, you want to add a temporal dimension to your analysis and see how customers have been investing their money given the size of their account over each year. The account_opened column represents when customers opened their accounts and is a good proxy for segmenting customer activity and investment over time.

# However, since this data was consolidated from multiple sources, you need to make sure that all dates are of the same format. You will do so by converting this column into a datetime object, while making sure that the format is inferred and potentially incorrect formats are set to missing. The banking DataFrame is in your environment and pandas was imported as pd.

############ Instructions ################
# Print the header of account_opened from the banking DataFrame and take a look at the different results.
# Print the header of account_opened
print(banking['account_opened'].head())

############ Instructions ################
# Question
# Take a look at the output. You tried converting the values to datetime using the default to_datetime() function without changing any argument, however received the following error:

# ValueError: month must be in 1..12
# Why do you think that is?

# Possible Answers
# The to_datetime() function needs to be explicitly told which date format each row is in.
# The to_datetime() function can only be applied on YY-mm-dd date formats.
# -> The 21-14-17 entry is erroneous and leads to an error.

############ Instructions ################
# Convert the account_opened column to datetime, while making sure the date format is inferred and that erroneous formats that raise error return a missing value.
# Print the header of account_opened
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

############ Instructions ################
# Extract the year from the amended account_opened column and assign it to the acct_year column.
# Print the newly created acct_year column.

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])

################ Exercise ################
# How's our data integrity?
# New data has been merged into the banking DataFrame that contains details on how investments in the inv_amount column are allocated across four different funds A, B, C and D.

# Furthermore, the age and birthdays of customers are now stored in the age and birth_date columns respectively.

# You want to understand how customers of different age groups invest. However, you want to first make sure the data you're analyzing is correct. You will do so by cross field checking values of inv_amount and age against the amount invested in different funds and customers' birthdays. Both pandas and datetime have been imported as pd and dt respectively.

############ Instructions ################
# Find the rows where the sum of all rows of the fund_columns in banking are equal to the inv_amount column.
# Store the values of banking with consistent inv_amount in consistent_inv, and those with inconsistent ones in inconsistent_inv.
# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

############ Instructions ################
# Store today's date into today, and manually calculate customers' ages and store them in ages_manual.
# Find all rows of banking where the age column is equal to ages_manual and then filter banking into consistent_ages and inconsistent_ages.

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])
# There are only 8 and 4 rows affected by inconsistent inv_amount and age values respectively. In this case, it's best to investigate the underlying data sources before deciding on a course of action!

################ Exercise ################
# Missing investors
# Dealing with missing data is one of the most common tasks in data science. There are a variety of types of missingness, as well as a variety of types of solutions to missing data.

# You just received a new version of the banking DataFrame containing data on the amount held and invested for new and existing customers. However, there are rows with missing inv_amount values.

# You know for a fact that most customers below 25 do not have investment accounts yet, and suspect it could be driving the missingness. The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt respectively. The banking DataFrame is in your environment.

############ Instructions ################
# Print the number of missing values by column in the banking DataFrame.
# Plot and show the missingness matrix of banking with the msno.matrix() function.
# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()
############ Instructions ################
# Isolate the values of banking missing values of inv_amount into missing_investors and with non-missing inv_amount values into investors.
# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

############ Instructions ################
# Question
# Now that you've isolated banking into investors and missing_investors, use the .describe() method on both of these DataFrames in the console to understand whether there are structural differences between them. What do you think is going on?

# Possible Answers
# The data is missing completely at random and there are no drivers behind the missingness.
#-> The inv_amount is missing only for young customers, since the average age in missing_investors is 22 and the maximum age is 25.
# The inv_amount is missing only for old customers, since the average age in missing_investors is 42 and the maximum age is 59.

############ Instructions ################
# Sort the banking DataFrame by the age column and plot the missingness matrix of banking_sorted.
# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values('age')
msno.matrix(banking_sorted)
plt.show()

################ Exercise ################
# Follow the money
# In this exercise, you're working with another version of the banking DataFrame that contains missing values for both the cust_id column and the acct_amount column.

# You want to produce analysis on how many unique customers the bank has, the average amount held by customers and more. You know that rows with missing cust_id don't really help you, and that on average acct_amount is usually 5 times the amount of inv_amount.

# In this exercise, you will drop rows of banking with missing cust_ids, and impute missing values of acct_amount with some domain knowledge.

############ Instructions ################
# Use .dropna() to drop missing values of the cust_id column in banking and store the results in banking_fullid.
# Compute the estimated acct_amount of banking_fullid knowing that acct_amount is usually inv_amount * 5 and assign the results to acct_imp.
# Impute the missing values of acct_amount in banking_fullid with the newly created acct_imp using .fillna().

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())