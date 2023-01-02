'''
Write a python program to implement multiple 
Linear Regression model for a car dataset.
Dataset can be downloaded from: 
https://www.w3schools.com/python/python_ml_multiple_regression.asp
'''

'''
Write a python program to implement 
multiple Linear Regression model for a car dataset. 
Dataset can be downloaded 
from: https://www.w3schools.com/python/python_ml_multiple_regression.asp
'''

# Import the necessary libraries

# Load the car data set
import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv('cars.csv')

# Extract the input and output data
X = df[['mpg', 'cyl', 'disp', 'hp']]
y = df['carb']

# Create the linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(X, y)

# Predict on a new data point
new_data = [[3.5, 6, 10, 8]]
prediction = model.predict(new_data)

# Print the prediction
print(prediction)
