# Write a R program to get the first 20 Fibonacci numbers.
Fibonacci <- numeric(20)
Fibonacci[1] < Fibonacci[2] <- 1
for (i in 3:20) {
  Fibonacci[i] <- Fibonacci[i - 2] + Fibonacci[i - 1]
}
print(Fibonacci)