# Draw a pie chart using R programming for the following datadistribution:
# Digits on Dice 1 2 3 4 5 6
# Frequency of getting each number 7 2 6 3 4 8
# Create data for the graph.
DigitsonDice <- c(1, 2, 3, 4, 5, 6)
Frequency <- c(7, 2, 6, 3, 4, 8)
# Plot the chart.
pie(DigitsonDice, Frequency)