
'''
Consider following dataset
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'] 
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'] 
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No'].
Use Naïve Bayes algorithm to predict 
[0: Overcast, 2: Mild] tuple belongs 
to which class whether to play the sports or not.
'''
from collections import Counter

weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast',
           'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']
temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
        'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
        'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']


# Count the number of times each class appears in the play list
class_counts = Counter(play)

# Calculate the probability of each class
probabilities = {}
for cls, count in class_counts.items():
    probabilities[cls] = count / len(play)

# Calculate the probability of each feature value given each class
feature_probabilities = {
    'Overcast': {},
    'Mild': {}
}
for cls in class_counts.keys():
    # Calculate the probability of Overcast given this class
    feature_probabilities['Overcast'][cls] = weather.count(
        'Overcast') / class_counts[cls]
    # Calculate the probability of Mild given this class
    feature_probabilities['Mild'][cls] = temp.count('Mild') / class_counts[cls]

# Calculate the probability that the tuple belongs to each class
tuple_probabilities = {}
for cls in class_counts.keys():
    # Start with the probability of the class
    p = probabilities[cls]
    # Multiply by the probability of Overcast given this class
    p *= feature_probabilities['Overcast'][cls]
    # Multiply by the probability of Mild given this class
    p *= feature_probabilities['Mild'][cls]
    # Store the result in a dictionary
    tuple_probabilities[cls] = p

# Print the results
print(tuple_probabilities)
