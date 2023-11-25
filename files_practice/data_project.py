# Data analysis by reading a csv
# by Kevin Brennan

# read the csv and print the mean, median, and standard deviation for Spring and Fall 2016
# write at least 2 functions

import numpy as np

def semester_grade_list(semester):
    dataFile = open("sample_grades.csv")

    semester_list = []
    time = semester.title()

    for line in dataFile:
        if time in line:
            semester_list.append(int("".join(line.split(",")[2:])))

    dataFile.close()

    return sorted(semester_list)

def median(list):
    res = sorted(list)
    lenList = len(list)
    index = (lenList - 1) // 2
    if (lenList % 2):
        return res[index]
    else:
        return (res[index] + res[index + 1]) / 2

def stats_output(list):
    print("Mean:       ", round(sum(list) / len(list), 2))
    print("Median:     ", median(list))
    print("STD:        ", round(np.std(list), 2))

def main():
    fall_grades = semester_grade_list("fall")
    spring_grades = semester_grade_list("spring")

    print("Fall 2016")
    stats_output(fall_grades)
    print("Spring 2016")
    stats_output(spring_grades)

main()




