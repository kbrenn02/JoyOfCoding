# Count lines in files
# Kevin Brennan

def count_file_lines(file_name):
    line_count = 0
    word_count = 0
    dataFile = open(file_name)  # read a file

    for line in dataFile: #this loop gets me the count of the lines in 1 file
        line_count+=1
        for word in line.split(" "):
            word_count += 1

    line_count = str(line_count)
    word_count = str(word_count)

    dataFile2 = open("count_output.txt", "a")
    dataFile2.write(file_name + ": " + line_count + " lines, " + word_count + "words \n")

    dataFile2.close()
    dataFile.close()

def main():
    list = ["add.txt", "input.txt", "numbers.txt"]

    total_words = 0
    total_lines = 0

    for item in list:

        line_count = 0
        word_count = 0
        dataFile = open(item)  # read a file

        for line in dataFile:  # this loop gets me the count of the lines in 1 file
            line_count += 1
            total_lines += 1
            for word in line.split(" "):
                word_count += 1
                total_words += 1

        line_count = str(line_count)
        word_count = str(word_count)

        dataFile2 = open("count_output.txt", "a")
        dataFile2.write(item + ": " + line_count + " lines, " + word_count + " words \n")
        dataFile.close()

    total_lines = str(total_lines)
    total_words = str(total_words)
    dataFile2 = open("count_output.txt", "a")
    dataFile2.write("TOTAL: " + total_lines + " lines, " + total_words + " words \n")
    dataFile2.close()


    dataFile = open("count_output.txt")
    for line in dataFile:
        print(line.rstrip())
    dataFile.close()

main()

