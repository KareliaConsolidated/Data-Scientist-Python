# SAS and Stata Files
# SAS : Statistical Analysis System
# Stata: "Statistics" + "Data"
# SAS: Business Analytics and Biostatistics
# Stata: Academic Social Sciences Research
# Import sas7bdat package
# conda install -c anaconda sas7bdat
import matplotlib.pyplot as plt
import pandas as pd
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('../Dataset/Importing Data From Dataset/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

# Importing Stata Files
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('../Dataset/Importing Data From Dataset/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
