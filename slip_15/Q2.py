'''
Write a Python program build 
Decision Tree Classifier for shows.csv 
from pandas and predict class label for
show starring a 40 years old American comedian, 
with 10 years of experience, and a comedy ranking of 7? 
Create a csv file as shown in 
https://www.w3schools.com/python/python_ml_decision_tree.asp
'''
# Import the necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the data set
df = pd.read_csv('shows.csv')

# Extract the input and output data
X = df[['Age', 'Experience', 'Ranking']]
y = df['Success']

# Create the decision tree classifier
model = DecisionTreeClassifier()

# Train the model on the data
model.fit(X, y)

# Predict the class label for a new data point
new_data = [[40, 10, 7]]
prediction = model.predict(new_data)

# Print the prediction
print(prediction)
