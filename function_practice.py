#function practice
#Kevin

#Add function
def add(x, y):
    return x + y

#multiple function
def multiply(x, y):
    return x * y

def main():
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another, different number: "))
    print("The sum of your two numbers.txt is", add(num1, num2))
    print("The product of your two numbers.txt is", multiply(num1, num2))

main()