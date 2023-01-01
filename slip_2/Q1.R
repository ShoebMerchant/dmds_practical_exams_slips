number = as.integer(readline(prompt= "Please Enter a number : "))
display_table = function(num) {
    for( i in 1:10){
        print(paste(num, "*", i,"=",num*i))
    }
}
display_table(number)
