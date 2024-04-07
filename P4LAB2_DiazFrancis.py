#Francis Diaz
#04/07/2024
#P4LAB2
#Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

#Create variables for user interger input
var_one = int(input())
var_two = int(input())

#Create while loop where var_one displays input plus increments of 5 until = to var_two
if var_one > var_two:
    print("Second integer can't be less than the first.")
else:
    while var_one <= var_two:
        print(var_one, end=' ')
        var_one += 5
    print()
