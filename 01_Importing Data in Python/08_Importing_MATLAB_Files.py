# Importing MATLAB Files
# .mat Files
# SciPy to the Rescue
# scipy.io.loadmat() - read .mat files
# scipy.io.savemat() - write .mat files
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

filename = '../Dataset/Importing Data From Dataset/albeck_gene_expression.mat'
mat = scipy.io.loadmat(filename)
print(type(mat)) # <class 'dict'>
# keys = MATLAB variable names
# values = objects assigned to variables.
print(type(mat['x'])) # <class 'numpy.ndarray'>

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(mat['CYratioCyt'].shape)

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
