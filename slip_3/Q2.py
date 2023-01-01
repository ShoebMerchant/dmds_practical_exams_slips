'''
Consider the following observations/data. 
And apply simple linear regression and find out estimated coefficients b0 and b1.
( use numpy package)
x=[0,1,2,3,4,5,6,7,8,9,11,13]
y = ([1, 3, 2, 5, 7, 8, 8, 9, 10, 12,16, 18]
'''
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18]

b0, b1 = np.polyfit(x, y, deg=1)
print(b0, b1)
