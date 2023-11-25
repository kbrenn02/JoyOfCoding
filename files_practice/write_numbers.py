PROMPT = "Enter the next line in the file (entering 0 will exit the program0): "

# outfilename = input("What is the name you want for the output file? ") #first time running the program
#I named the output numbers.txt

userinput = ""
dataFile = open("numbers.txt", "w")

while userinput != "0":
    userinput = input(PROMPT)
    if userinput != "0":
        print(userinput, file=dataFile)

dataFile.close()

dataFile2 = open("numbers.txt")
for line in dataFile2:
    print(line.rstrip())