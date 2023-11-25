# Write a program madfun.py that takes a decimal number as input from
# the user and prints out the following:
# a. The absolute value of the number
# b. The number rounded to 0 decimal places
# c. The square root of the rounded number’s absolute value
# Example runs of this program might be:
# > Please enter a number: 8.88
# > 8.88
# > 9.0
# > 3.0
# > Please enter a number: -24.75
# > 24.75
# > -25.0
# > 5.0

import math

#get user input
deci = eval(input("Please provide a decimal number: "))
#absolute value
print(abs(deci))
#float equivalent of the rounded number
print(float(round(deci)))
#square root of the absolute value of the rounded number
print(math.sqrt(round(abs(deci))))

