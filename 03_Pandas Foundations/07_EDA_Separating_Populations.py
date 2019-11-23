import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
iris = pd.read_csv('../Dataset/Pandas Foundations/iris.csv')

print(iris.head())

print(iris['species'].describe())
# count            150
# unique             3
# top       versicolor
# freq              50
# Name: species, dtype: object
# count: # non-null entries
# unique: # distinct values
# top: most frequent category
# Freq: # No Occurences of Top

# To Get the Unique Values
print(iris['species'].unique())

# Filtering by Species
indices = iris['species'] == 'setosa'
setosa = iris.loc[indices,:] # Extract New DataFrame
indices = iris['species'] == 'versicolor'
versicolor = iris.loc[indices,:] # Extract New DataFrame
indices = iris['species'] == 'virginica'
virginica = iris.loc[indices,:] # Extract New DataFrame
# Print
print(setosa.head(2))
print(versicolor.head(2))
print(virginica.head(2))

iris.plot(kind = 'hist', bins = 50, range=(0,8), alpha=0.3)
plt.title('Entire iris data set')
plt.xlabel('[cm]')

setosa.plot(kind = 'hist', bins = 50, range=(0,8), alpha=0.3)
plt.title('Entire setosa data set')
plt.xlabel('[cm]')

versicolor.plot(kind = 'hist', bins = 50, range=(0,8), alpha=0.3)
plt.title('Entire versicolor data set')
plt.xlabel('[cm]')

virginica.plot(kind = 'hist', bins = 50, range=(0,8), alpha=0.3)
plt.title('Entire virginica data set')
plt.xlabel('[cm]')

plt.show()

# Statistical EDA: describe()
describe_all = iris.describe()
describe_setosa = setosa.describe()
describe_versicolor = versicolor.describe()
describe_virginica = virginica.describe()

# Computing Errors
error_setosa = 100 * np.abs(describe_setosa - describe_all)
error_setosa = error_setosa / describe_setosa

error_versicolor = 100 * np.abs(describe_versicolor - describe_all)
error_versicolor = error_versicolor / describe_versicolor

error_virginica = 100 * np.abs(describe_virginica - describe_all)
error_virginica = error_virginica / describe_virginica

print(error_setosa)
print(error_virginica)
print(error_versicolor)