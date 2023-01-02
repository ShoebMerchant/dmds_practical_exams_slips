'''
Write a  very simple Python program to read “StudentsPerformance.csv” file. 
Solve following:
    - To display the shape of dataset.
    - To display the top rows of the dataset with their columns.Note: Download
    dataset from following link:
    (https: // www.kaggle.com/spscientist/students-performance-inexams?
select = StudentsPerformance.csv

'''
# Import the necessary libraries
import pandas as pd

# Load the data set
df = pd.read_csv('StudentsPerformance.csv')

# Print the shape of the data set
print("Shape of the data set:", df.shape)

# Print the top rows of the data set with their columns
print(df.head())
