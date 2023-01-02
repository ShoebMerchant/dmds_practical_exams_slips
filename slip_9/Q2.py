'''
Write a Python program to build an SVM model to Cancer dataset. The dataset is
available in the scikit-learn library. Check the accuracyof model with precision and
recall
'''
# Import the necessary libraries
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score

# Load the cancer data set
cancer = datasets.load_breast_cancer()

# Extract the input and output data
X = cancer.data
y = cancer.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Create the SVM model
model = SVC(kernel='linear')

# Train the model on the training data
model.fit(X_train, y_train)

# Test the model on the test data
y_pred = model.predict(X_test)

# Calculate the precision and recall
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(precision, recall)
