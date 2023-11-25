#Strings and Lists in functions
#Kevin Brennan

# 1. Write a program that creates a list of 20 numbers.txt input by the user and prints
# the average (mean) of the list.
from statistics import mean

my_list = []
def avg_input():
    for i in range(20):
        my_list.append(float(input("Please input a number: ")))
    average = mean(my_list)
    return average

#2 Write a function mangle that takes a string as a parameter and returns the string after
# performing the following operations:
# i. Converting the string to all upper case letters
# ii. Removing the third character
# iii. Removing the third to last character
# Test that your function works.

def mangle(string):
    new_string = string.upper()
    final = new_string[:2] + new_string[3:-3] + new_string[-2:]
    return final

#3. Write a function, count_e, that takes a list of strings as a parameter and
# returns the total number of upper and lower case e’s (“E” and “e”) in all the
# strings in the list. Test that your function works with multiple examples.

def count_e(list):
    e_counter = 0
    for i in list:
        for j in i:
            if j.count("e"):
                e_counter += 1
            elif j.count("E"):
                e_counter += 1
    return e_counter

#4 Write a function, count_vowels, that takes a list of strings as a parameter
# and returns the total number of upper and lower case vowels (A, E, I, O, U) in all
# the strings in the list.

def count_vowels(list):
    vowel_counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in list:
        for letter in vowels:
            vowel_counter += i.lower().count(letter)
    return vowel_counter

def main():
    # average = avg_input()
    # print(average)
    # final = mangle("Hellothere")
    # print(final)
    # es = count_e(["hi", "hello", "EEK!", "wowieeee"])
    # print(es)
    es = count_vowels(["hi", "hello", "Karate!"])
    print(es)


main()