#! /usr/bin/env python3

"""We are searching for the sum of all the calibration values.
The list has been messed up and the calibration values are the first and the last digit for each line.
Example : 1abv2 = 12, a1b2c3d4e5f = 25, treb7uchet = 77"""

with open("calibration_doc.txt", "r") as f :
    calibration_values = []
    for line in f:
        calibration_line = []
        for j in line:
            try :
                int(j)
                calibration_line.append(j)
            except:
                continue
        calibration_line[1:-1] = []
        calibration_values.append("".join(calibration_line))

sum = 0
for i in calibration_values:
    if len(i) == 1:
        i = i + i
    sum += int(i)

print(sum)