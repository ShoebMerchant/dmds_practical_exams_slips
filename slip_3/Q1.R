# Write a R program to reverse a number and also calculate the sum of digits of that number.
num = as.integer(readline(prompt = "Enter a number : "))

rev_num <- function(n) {
    rev = 0
    sum = 0
    while (n>0) {
        rem = n %% 10
        sum = sum + rem
        rev = rev*10 + rem
        n = n %/% 10
    }
    print(paste("Reverse of number : ", rev))
    print(paste("Sum of number : ", sum))
}