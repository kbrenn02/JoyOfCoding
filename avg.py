# Average of 10 input numbers.txt
# Kevin Brennan

all_nums = []

print("Please provide 10 numbers.txt you want me to find the average of.")
for i in range(10):
    all_nums.append(float(input("Num: ")))

print(all_nums)

sum = 0

for num in all_nums:
    sum += num

print("The average of your inputs is:", sum/10)