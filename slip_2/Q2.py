'''
Consider the following observations/data. 
And apply simple linear regression and find out estimated coefficients b0 and b1.
(use numpy package) 
x = [0,1,2,3,4,5,6,7,8,9,11,13] 
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12,16, 18]
'''
import numpy as np

'''
Next, you can use the polyfit function from numpy to fit a 
linear regression model to the data and compute the coefficients. 
The polyfit function takes in the following arguments:
np.polyfit(x, y, deg)
Where x is the list of independent variables, 
y is the list of dependent variables, and deg is the degree of the polynomial to fit. 
In this case, since we are performing simple linear regression, deg should be set to 1.
'''
# Fit the linear regression model and compute the coefficients
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18]
'''
The polyfit function will return an array of coefficients,
where the first element is the intercept term (b0) and the second element is the slope (b1). 
You can access these values by indexing the array as follows:
'''
b0, b1 = np.polyfit(x, y, deg=1)
print(b0, b1)

# * Solution ends here

'''
You can then use the estimated coefficients to predict the dependent variable 
for new values of the independent variable. 
For example, you can use the following code to predict y for a new value of x=10:
'''
# Predict y for a new value of x
x_new = 10
y_pred = b0 + b1 * x_new

print(f"Predicted y value: {y_pred}")
