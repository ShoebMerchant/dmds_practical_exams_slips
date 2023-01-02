'''Write a Python Programme to read the dataset(“Iris.csv”). dataset download from
(https: // archive.ics.uci.edu/ml/datasets/iris) and apply Apriori algorithm.
'''

# Import the necessary libraries
import pandas as pd
from apyori import apriori

# Load the Iris data set
df = pd.read_csv('iris.csv')

# Extract the input data as a list of lists
data = df.values.tolist()

# Run the Apriori algorithm
association_rules = apriori(data, min_support=0.5, min_confidence=0.5)

# Print the association rules
for item in association_rules:
    pair = item[0]
    items = [x for x in pair]
    print("Rule:", items[0], "->", items[1])
    print("Support:", item[1])
    print("Confidence:", item[2][0][2])
    print("Lift:", item[2][0][3])
    print("=====================================")
