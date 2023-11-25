#while loop practice
#Kevin Brennan

#1
# i = 1
# while i < 6:
#     print(i)
#     i += 1

#2
# i = 2
# while i < 12:
#     print(i)
#     i+=3

#3
# i = -10
# while i <= 0:
#     print(i, end=" ")
#     i+=2

#4
# i = 0
# while i < 4:
#     print("****")
#     i+=1

#5
# string = "CSCI 150"
# i=0
# while i < len(string):
#     print(string[i])
#     i+=1

#6
# user = ""
# list = []
# while user != "0":
#     user = input("Please input a number: ")
#     list.append(float(user))
# print(sum(list))
# print(sum(list)/(len(list)-1))


def average_neg_evens(list):
    i = 0
    negs = 0
    num_negs = 0
    while i < len(list):
        if list[i] < 0 and list[i] % 2 == 0:
            negs += list[i]
            num_negs += 1
        i += 1
    return negs / num_negs

def count_letter(list, letter):
    i = 0
    count = 0
    letter = letter.lower()
    while i < len(list):
        count += list[i].lower().count(letter)
        i+=1
    return count


def main():
    list = ["HELLO", "goodbye", "1234 Oooh!", "jolly good", "potato potatohoo"]
    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
    print(count_letter(list, "o"))

main()