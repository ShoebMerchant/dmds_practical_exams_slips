'''
Write a python program to implement hierarchical clustering algorithm. 
(Download Wholesale customers data dataset from github.com).
'''

# Import the necessary libraries
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Load the wholesale customers data set
df = pd.read_csv('wholesale_customers.csv')

# Extract the input data
X = df.values

# Create the linkage matrix using the ward method
linkage_matrix = linkage(X, method='ward')

# Create the dendrogram plot
dendrogram(linkage_matrix)
plt.show()

# Create the Agglomerative Clustering model
model = AgglomerativeClustering(n_clusters=4)

# Fit the model to the data
model.fit(X)

# Predict the clusters for each data point
y_pred = model.fit_predict(X)

# Print the cluster assignments
print(y_pred)
