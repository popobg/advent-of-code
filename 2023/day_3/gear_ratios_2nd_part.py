#! /usr/bin/env python3

"""We are searching for the part numbers of the engine schematics.
A gear is now only the symbol "*", and must be adjacent to exactly two numbers (not less, not more) to have part numbers.
We then multiply this two numbers together, and add up all this products."""

# On ne recherche plus du point de vue des chiffres mais de celui du symbole gear "*".

# FUNCTIONS

def get_beg_ind(ind: int) -> int:
    """return the index before the symbol if the symbol is not at 0"""
    return (ind - 1) if ind > 0 else ind

def get_end_ind(ind: int, length: int) -> int:
    """return the index after the symbol if the symbol is not at the end of the line"""
    return (ind + 1) if ind < length else ind

def get_pos(data: list, n_line: int, ind: int) -> int:
    """get the index of the complete number"""
    a = data[n_line][ind]
    while data[n_line][ind].isdigit() and ind >= 0:
        ind -= 1
    if ind < 0:
        return 0
    else:
        return ind + 1

def get_bound(ind: int) -> int:
    """return the previous index if index is different from 0"""
    if ind == 0:
            new_beg = None
    else:
        new_beg = ind - 1
    return new_beg

def check_other_line(data: list, n: int, beg_ind: int, end_ind: int, coords_numbers: set) -> set:
    """return the index of the complete number"""
    index = end_ind
    new_beg = get_bound(beg_ind)
    c = data[n][end_ind:new_beg:-1]

    for char in data[n][end_ind:new_beg:-1]:
        if char.isdigit():
            x = get_pos(data, n, index)
            coords_numbers.add((n, x))
        index -= 1

    return coords_numbers

def search_coords_numbers(data: list, n_line: int, beg_ind: int, end_ind: int) -> set:
    """return the coordinates of the numbers near the gear (line, index)"""
    coords_numbers = set()

    if data[n_line][beg_ind].isdigit():
        x = get_pos(data, n_line, beg_ind)
        coords_numbers.add((n_line, x))

    if data[n_line][end_ind].isdigit():
        coords_numbers.add((n_line, end_ind))

    if n_line != 0:
        coords_numbers = check_other_line(data, (n_line - 1), beg_ind, end_ind, coords_numbers)

    if n_line != (len(data) - 1):
        coords_numbers = check_other_line(data, (n_line + 1), beg_ind, end_ind, coords_numbers)

    return coords_numbers

def search_numbers(data: list, n_line: int, beg_ind: int, end_ind: int) -> list:
    """return a list of the numbers adjacent to the gear"""
    coords_number = search_coords_numbers(data, n_line, beg_ind, end_ind)
    numbers = []

    for line, index in coords_number:
        s = ""
        ind = index

        while ind <= (len(data[line]) - 1) and data[line][ind].isdigit():
            a = data[line][ind]
            s += data[line][ind]
            ind += 1
        numbers.append(s)

    return numbers

def is_part_number(numbers: list) -> bool:
    """return True whether there is exactly 2 numbers adjacent to the gear
    otherwise, return False"""
    if len(numbers) == 2:
        return True
    return False

def multiply_part_numbers(numbers: list) -> int:
    """return the product of the two numbers of the list"""
    return int(numbers[0]) * int(numbers[1])

def calculate_sum(sum: int, numbers: list) -> int:
    """return the sum of the product of the two numbers adjacent to the gear"""
    prod = multiply_part_numbers(numbers)
    sum += prod
    return sum

# MAIN
gear_ratios_sum = 0

with open("test.txt", "r", encoding= "utf-8") as f:
    data = f.read()

# split the string into a list of strings line by line
data = data.split("\n")
# remove the last blank line
if data[-1] == "":
    data = data[:-1]

for n, line in enumerate(data):
    for i, char in enumerate(line):
        if char != "*":
            continue
        # reprends la fonction search_coords() pour voir ce que doivent être beg_ind et end_ind et écrire leurs fonctions
        beg_ind = get_beg_ind(i)
        end_ind = get_end_ind(i, (len(line) - 1))
        adjacent_numbers = search_numbers(data, n, beg_ind, end_ind)
        if is_part_number(adjacent_numbers):
            gear_ratios_sum = calculate_sum(gear_ratios_sum, adjacent_numbers)

print(gear_ratios_sum)