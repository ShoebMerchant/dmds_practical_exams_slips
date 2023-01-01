'''
Write a python program to implement 
hierarchical Agglomerative clustering algorithm.
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Load the dataset
df = pd.read_csv('customers.csv')

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Create the AgglomerativeClustering model
model = AgglomerativeClustering(
    n_clusters=3, linkage='ward')

# Fit the model to the data
model.fit(X)

print(model)
