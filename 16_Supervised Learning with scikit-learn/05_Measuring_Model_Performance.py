# In order to measure performance, we need to find accuracy is a equal to commonly-used metric
# The accuracy of a classifier is defined as the number of correct predictions divided by the total number of data-points.
# Which data should be used to compute accuracy?
# What we are interesting in is, How well will the model perform on new data ?
# Could compute accuracy on data used to fit classifier
# NOT indicative of ability to generalize
# Split data into Training and Test Set
# You train or fit the classifier on the Training Set
# Then you make predictions on the labeled test set and compare these predictions with the known labels.
# Compare predictions with the known labels

# TRAIN/ TEST SPLIT
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# import pandas as pd
# import numpy as np

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=21,stratify=y)
# The test_size keyword argument specifies what proportion of the original data is used for the test set.
# The random state kwarg sets a seed for the random number generator that splits the data into train and test.
# Setting the seed with same argument later will allow you to reproduce the exact split downstream.
# By Default 75% Training Data and 25% Test Data
# It is also best practice to perform your split so that the split reflects the labels on your data. That is, you want the labels to be distributed in train and test sets as they are in the original dataset. To achieve this, we use the keyword argument stratify equals y, where y the list of array containing the labels.

# knn = KNeighborsClassifier(n_neighbors=8)
# knn.fit(X_train, y_train)
# y_pred  = knn.predict(X_test)
# print(f"Test set predictions: {y_pred}")
# knn.score(X_test, y_test) # 95%

# Model Complexity
# Larger k = smoother decision boundary = less complex model
# Smaller k = more complex model = can lead to overfitting
# <- Overfitting k Underfitting ->

# The digits recognition dataset
# Up until now, you have been performing binary classification, since the target variable had two possible outcomes. Hugo, however, got to perform multi-class classification in the videos, where the target variable could take on three possible outcomes. Why does he get to have all the fun?! In the following exercises, you'll be working with the MNIST digits recognition dataset, which has 10 classes, the digits 0 through 9! A reduced version of the MNIST dataset is one of scikit-learn's included datasets, and that is the one we will use in this exercise.

# Each sample in this scikit-learn dataset is an 8x8 image representing a handwritten digit. Each pixel is represented by an integer in the range 0 to 16, indicating varying levels of black. Recall that scikit-learn's built-in datasets are of type Bunch, which are dictionary-like objects. Helpfully for the MNIST dataset, scikit-learn provides an 'images' key in addition to the 'data' and 'target' keys that you have seen with the Iris data. Because it is a 2D array of the images corresponding to each sample, this 'images' key is useful for visualizing the images, as you'll see in this exercise (for more on plotting 2D arrays, see Chapter 2 of DataCamp's course on Data Visualization with Python). On the other hand, the 'data' key contains the feature array - that is, the images as a flattened array of 64 pixels.

# Notice that you can access the keys of these Bunch objects in two different ways: By using the . notation, as in digits.images, or the [] notation, as in digits['images'].

# For more on the MNIST data, check out this exercise in Part 1 of DataCamp's Importing Data in Python course. There, the full version of the MNIST dataset is used, in which the images are 28x28. It is a famous dataset in machine learning and computer vision, and frequently used as a benchmark to evaluate the performance of a new model.

from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys()) # dict_keys(['data', 'target', 'target_names', 'images', 'DESCR'])
print(digits.DESCR)

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
#It looks like the image in question corresponds to the digit '5'. Now, can you build a classifier that can make this prediction not only for this image, but for all the other ones in the dataset?

# Train/Test Split + Fit/Predict/Accuracy
# Now that you have learned about the importance of splitting your data into training and test sets, it's time to practice doing this on the digits dataset! After creating arrays for the features and target variable, you will split them into training and test sets, fit a k-NN classifier to the training data, and then compute its accuracy using the .score() method.

# Import Modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits.data
y = digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42,stratify=y)
# Create a k-NN Classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the Data
print(knn.predict(X_test))
# [5 2 8 1 7 2 6 2 6 5 0 5 9 3 4 4 2 4 9 9 6 3 8 1 2 5 6 0 3 4 6 7 2 6 6 6 8
# 5 0 9 1 7 9 6 5 7 5 2 7 5 0 1 5 5 3 2 4 0 0 2 7 5 6 1 3 7 6 5 7 0 9 0 3 8
# 2 5 7 2 3 5 9 3 2 7 9 6 8 1 0 1 2 9 4 4 1 2 7 8 4 2 6 8 3 7 3 9 6 1 1 0 9
# 2 1 6 3 4 8 7 1 0 0 4 6 5 8 2 8 1 3 0 0 8 6 4 3 9 3 3 3 3 0 7 0 0 1 9 5 8
# 1 5 0 6 6 6 6 1 7 7 6 7 7 8 7 3 6 5 9 0 3 8 0 9 8 1 9 5 9 5 8 9 9 7 9 1 9
# 5 4 7 3 0 4 9 7 7 5 6 5 8 3 4 5 4 9 2 5 5 2 1 3 8 8 9 3 6 1 0 1 4 0 5 5 6
# 6 7 4 3 8 4 1 0 7 9 2 8 4 8 4 2 4 0 0 0 2 6 7 0 4 5 2 2 9 0 4 6 8 2 3 9 2
# 3 0 6 8 7 1 4 4 1 1 6 3 8 1 2 5 7 8 3 2 0 3 4 1 9 9 9 6 3 7 1 6 9 4 7 1 8
# 1 3 0 5 3 4 1 9 3 5 4 7 4 1 5 1 5 0 9 8 4 2 3 8 4 1 2 0 1 1 4 4 5 7 5 0 3
# 2 2 4 2 7 7 8 7 6 3 1 1 5 8 8 8 6 7 2 7 8 9 4 2 0 3 4]

# Print the accuracy
print(knn.score(X_test, y_test)) # 0.983333333
 # Incredibly, this out of the box k-NN classifier with 7 neighbors has learned from the training data and predicted the labels of the images in the test set with 98% accuracy, and it did so in less than a second! This is one illustration of how incredibly useful machine learning techniques can be.

# Overfitting and underfitting
# Remember the model complexity curve that Hugo showed in the video? You will now construct such a curve for the digits dataset! In this exercise, you will compute and plot the training and testing accuracy scores for a variety of different neighbor values. By observing how the accuracy scores differ for the training and testing sets with different values of k, you will develop your intuition for overfitting and underfitting.

# The training and testing sets are available to you in the workspace as X_train, X_test, y_train, y_test. In addition, KNeighborsClassifier has been imported from sklearn.neighbors.
# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
# It looks like the test accuracy is highest when using 3 and 5 neighbors. Using 8 neighbors or more seems to result in a simple model that underfits the data.

