'''
Consider the student data set. It can be downloaded 
from: https://drive.google.com/file/d/1oakZCv7g3mlmCSdv9J8kdSaqO5_6dIOw/view 
Write a program in python to apply simple linear regression 
and find out mean absolute error, 
mean squared error and root mean squared error.
'''
from math import sqrt
# To use sklearn install scikit-learn with command
# pip install scikit-learn
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the data into a Pandas DataFrame
df = pd.read_csv("student_scores.csv")

'''
Next, you will need to split the data into training and testing sets. 
You can do this using the train_test_split 
function from the sklearn.model_selection module:
'''
# Split the data into training and testing sets
X = df[["Hours"]]
y = df[["Scores"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

'''
Once you have the training and testing sets, 
you can fit a simple linear regression model 
to the training data using the LinearRegression class 
from the sklearn.linear_model module:
'''
# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# You can then use the trained model to make predictions on the test data:
y_pred = model.predict(X_test)

'''
To compute the mean absolute error, 
mean squared error, and root mean squared error, 
you can use the mean_absolute_error, mean_squared_error, 
and sqrt functions from the sklearn.metrics module:
'''
# Compute the mean absolute error
mae = mean_absolute_error(y_test, y_pred)
print(mae)

# Compute the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(mse)

# Compute the root mean squared error
rmse = sqrt(mse)
print(rmse)
