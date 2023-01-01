# Write a R program to calculate the sum of two matrices of given size.

# Define the matrices to sum
matrix_a <- matrix(c(1, 2, 3, 4, 5, 6), nrow=3, ncol=2)
matrix_b <- matrix(c(7, 8, 9, 10, 11, 12), nrow=3, ncol=2)

# Calculate the sum of the matrices
matrix_sum <- matrix_a + matrix_b

# Print the result to the console
print(matrix_sum)
