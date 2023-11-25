dataFile = open("input.txt")
dataFile2 = open("add.txt")
dataFile3 = open("output.txt")
for line in dataFile3:
    print(line.rstrip())

#Output a file with dashes in front
dataFile3 = open("output.txt", "w")
list = ["a", "b", "c", "d", "e"]
for line in dataFile:
    print("-" + line, file=dataFile3)
for item in list:
    dataFile3.write(item)
    dataFile3.write("\n and another item \n")

dataFile3.close()