# Write a R program to concatenate two given factors.

# Create the first factor
factor1 <- factor(c("A", "B", "C", "D", "E"))

# Create the second factor
factor2 <- factor(c("C", "D", "E", "F", "G"))

# Concatenate the two factors
factor3 <- c(factor1, factor2)

# Print the result
print(factor3)
