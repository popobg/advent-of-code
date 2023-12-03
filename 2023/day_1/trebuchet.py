#! /usr/bin/env python3

"""We are searching for the sum of all the calibration values.
The list has been messed up and the calibration values are the first and the last digit for each line. Be careful, the numbers can be spelled out with letters."""

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

with open("calibration_doc.txt", "r") as f :
    calibration_values = []
    for line in f:
        calibration_line = []
        # searching for the first digit of the string
        new_line = ""
        for i in line:
            if len(calibration_line) == 1:
                break
            else:
                try:
                    int(i)
                    calibration_line.append(i)
                    break
                except:
                    new_line += i
                    if len(new_line) >= 3:
                        for n in spelled_numbers.keys():
                            if n in new_line:
                                calibration_line.append(str(spelled_numbers[n]))
                                break
        # searching for the last digit of the string
        new_line = ""
        for i in line[::-1]:
            if len(calibration_line) == 2:
                break
            else:
                try:
                    int(i)
                    calibration_line.append(i)
                    break
                except:
                    new_line += i
                    if len(new_line) >= 3 :
                        for n in spelled_numbers.keys():
                            if n in new_line[::-1]:
                                calibration_line.append(str(spelled_numbers[n]))
                                break
        calibration_values.append("".join(calibration_line))

sum = 0
for i in calibration_values:
    sum += int(i)

print(sum)