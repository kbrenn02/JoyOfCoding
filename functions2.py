#Function practice part 2
#Kevin Brennan

#pyramid function
def pyramid(char, rows):
    for i in range(1,rows+1):
        print(char*i)

# def_main():
    # pyramid("+", 10)
    # pyramid("x", 5)
    # pyramid("!", 3)

#absolute difference
def absolute_difference(num1, num2):
    return abs(num1-num2)

# def_main():
    # print(absolute_difference(5, 10))
    # print(absolute_difference(10, 5))
    # print(absolute_difference(-200, 200))

#is even function. Return true or false depending on if it's even
def is_even(num):
    return num%2 == 0

# def_main():
    # print(is_even(2))
    # print(is_even(104))
    # print(is_even(15))

#calculate the total of a meal, taking in meal total, state tax rate, and tip percentage as a decimal
def calc_total(meal, tax_rate, tip_rate):
    total = meal + (tax_rate*meal) + (tip_rate*meal)
    return total

# def_main()
    # print(calc_total(53.48, .07, .18))

#"hey" function that squares a number
def hey(num):
    return num**2

# def_main():
    # print(hey(5))
    # print(hey(0))
    # print(hey(-3))

#"there" function that returns 2 to the num power
def there(n):
    if n >= 0:
        return 2**n
    else:
        return 0

# def_main():
    # print(there(5))
    # print(there(0))
    # print(there(3))
    # print(there(-2))
    # print(there(-6))

#"are_we" function takes a number and a phrase and prints it n times
def are_we(num, phrase):
    together = "Are we " + phrase + " yet? "
    print(together*num)

# def main():
    # are_we(2, "there")
    # are_we(3, "50")
    # are_we(1, "")
    # are_we(0, "hey")

main()