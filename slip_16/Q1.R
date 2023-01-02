# Write a R program to create a simple bar plot of given data
# Year Export Import
# 2001   26   35
# 2002   32   40
# 2003   35   50

# Create the input vectors.
colors = c("green", "orange")
year <- c(2001, 2002, 2003)
regions <- c("import", "Export")
# Create the matrix of the values.
Values <- matrix(c(26, 32, 35, 35, 40, 50), nrow = 2, ncol = 3, byrow = TRUE)
# Create the bar chart
barplot(Values, main = "import/export", names.arg = year, xlab = "year", ylab = "import/export", col = colors)
# Add the legend to the chart
legend("topleft", regions, cex = 1.3, fill = colors)