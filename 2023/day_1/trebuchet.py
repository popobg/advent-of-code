#! /usr/bin/env python3

"""We are searching for the sum of all the calibration values.
The list has been messed up and the calibration values are the first and the last digit for each line. Be careful, the numbers can be spelled out with letters."""

# FUNCTIONS

def catching_number(line: str, calibration_line: list, x: int):
    """catch the first or the last number of the string whether x = 1 or x = -1.
    Detect spelled out number too."""
    new_line = ""
    for i in line[::x]:
        try:
            int(i)
            calibration_line.append(i)
            return calibration_line
        except:
            new_line += i
            if len(new_line) >= 3:
                for n in spelled_numbers.keys():
                    if n in new_line[::x]:
                        calibration_line.append(str(spelled_numbers[n]))
                        return calibration_line

def calculate_sum(sum, line_values):
    """add the calibration value of the line to the sum"""
    sum += line_values
    return sum

# GLOBAL VARIABLES

spelled_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

calibration_sum = 0

# MAIN

f = open("calibration_doc.txt", "r", encoding= "utf-8")

for line in f:
    line = line.strip()
    calibration_line = []

    # searching for the first digit of the string
    calibration_line = catching_number(line, calibration_line, 1)

    # searching for the last digit of the string
    calibration_line = catching_number(line, calibration_line, -1)

    calibration_line = int("".join(calibration_line))
    calibration_sum = calculate_sum(calibration_sum, calibration_line)

print(calibration_sum)

f.close()