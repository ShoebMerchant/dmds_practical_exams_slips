'''
Write a Python program build Decision Tree Classifier 
using Scikit- learn package for diabetes data set 
download database from 
https://www.kaggle.com/uciml/pima-indians-diabetes-database

'''

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Split the dataset into features and labels
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create the decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Test the classifier on the testing data
accuracy = clf.score(X_test, y_test)

# Print the accuracy
print(f'Accuracy: {accuracy:.2f}')
