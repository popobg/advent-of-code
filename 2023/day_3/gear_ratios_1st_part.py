#! /usr/bin/env python3

"""We are searching for the part numbers of the engine schematics.
Part numbers are numbers that are adjacent to a symbol, even diagonally.
Finally, add up all this numbers."""

# stocker les données du fichier dans une variable "data" et stocker les données 3 lignes par 3 lignes.
# un chiffre peut être adjacent à un symbole si son index / son index -1/+1 dans sa ligne et dans la ligne précédente / suivante correspond à l'index d'un symbole.
# il faut prendre le nombre dans sa globalité (on ne prend pas "2", suivi de "2", suivi de "4" séparement, mais "224" avec l'index de début = celui de 2 et l'index de fin = celui de 4).

# FUNCTIONS

def is_symbol(e):
    """check if the char is different from "." """
    return True if e != "." else False

def get_beg_ind(ind):
    return (ind - 1) if ind > 0 else ind

def get_end_ind(ind, length):
    return (ind + 1) if ind < length else ind

def is_special_char(char, ec):
    if char not in ec:
        return True

def search_adjacent_symbol(data: list, n_line: int, beg_ind: int, end_ind: int, x = 1) -> bool:
    """search for symbol in an adjacent position of the number"""
    excluded_char = "0123456789."
    if is_special_char(data[n_line][beg_ind], excluded_char):
        return True

    if is_special_char(data[n_line][end_ind], excluded_char):
        return True

    if n_line != 0:
        for char in data[n_line - 1][(beg_ind):(end_ind + x)]:
            if char not in excluded_char:
                return True

    if n_line != (len(data) - 1):
        for char in data[n_line + 1][(beg_ind):(end_ind + x)]:
            if char not in excluded_char:
                return True

    return False

def calculate_sum(sum: int, number: int) -> int:
    sum += number
    return sum

def reset():
    index = []
    number = []
    return index, number

# GLOBAL VAR

part_numbers_sum = 0

# MAIN

with open("engine_schematics.txt", "r", encoding= "utf-8") as f:
    data = f.read()

# split the string into a list of strings line by line
data = data.split("\n")
# remove the last blank line
if data[-1] == "":
    data = data[:-1]

index, number = reset()

# parse each line for digit
for number_line, line in enumerate(data):
    # check if the last char of the precedent line was a digit (number is not empty)
    # check if it is a part number
    if len(number) > 0:
        beg_ind = get_beg_ind(index[0])
        end_ind = get_end_ind(index[-1], (len(data[number_line - 1]) - 1))
        if search_adjacent_symbol(data, (number_line - 1), beg_ind, end_ind, x = 0):
            part_number = int("".join(number))
            part_numbers_sum = calculate_sum(part_numbers_sum, part_number)
            index, number = reset()

    # parse each character of the line
    for n, element in enumerate(line):
        if element.isdigit():
            index.append(n)
            number.append(element)
        # check if the current character is not a digit AND there was a digit earlier
        # on the line (if so the number list is not empty)

        elif not element.isdigit() and len(number) > 0:
            if is_symbol(element):
                part_number = int("".join(number))
                part_numbers_sum = calculate_sum(part_numbers_sum, part_number)
            else:
                beg_ind = get_beg_ind(index[0])
                end_ind = get_end_ind(index[-1], (len(line) - 1))
                if search_adjacent_symbol(data, number_line, beg_ind, end_ind):
                    part_number = int("".join(number))
                    part_numbers_sum = calculate_sum(part_numbers_sum, part_number)
            index, number = reset()

# if the last char of the doc was a digit
if len(number) > 0:
        beg_ind = get_beg_ind(index[0])
        end_ind = get_end_ind(index[-1], (len(line) - 1))
        if search_adjacent_symbol(data, number_line, beg_ind, end_ind, x = 0):
            part_number = "".join(number)
            part_numbers_sum = calculate_sum(part_numbers_sum, int(part_number))

print(part_numbers_sum)