'''
Consider the following observations/data.
And apply simple linear regression and find out
estimated coefficients b1 and b1 Also analyse the performance of the model
(Use sklearn package)
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([7,14,15,18,19,21,26,23])
'''

# Import the necessary libraries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Define the data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Create the linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(x.reshape(-1, 1), y)

# Predict on the test data
predictions = model.predict(x.reshape(-1, 1))

# Calculate the mean squared error and the R^2 score
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

# Print the results
print("Coefficients:", model.coef_, model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
