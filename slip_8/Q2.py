'''
Write a python program to implement 
k-means algorithm to build prediction model 
(Use Credit Card Dataset CC GENERAL.csv 
Download from kaggle.com)
'''
# Import the necessary libraries
import pandas as pd
from sklearn.cluster import KMeans

# Load the credit card data set
df = pd.read_csv('GENERAL.csv')

# Extract the input data
X = df.drop('TENURE', axis=1)

# Create the k-means model
model = KMeans(n_clusters=4)

# Fit the model to the data
model.fit(X)

# Predict the clusters for each data point
y_pred = model.predict(X)

# Print the cluster assignments
print(y_pred)
