#! /usr/bin/env python3

"""Starting from a list of random cube draws, we are searching for the fewest number of cubes of each color that could have been in the bag to make the game possible. For each game (line in the cubes_draws file), multiply this set of cubes to obtain the "power" of the game. Finally, calculate the sum of all the powers."""

# FUNCTIONS

def clean_split(string: str, separator = " ") -> list:
    """strip then split by the separator a string"""
    return string.strip().split(separator)

def isolate_draws(line: str) -> list:
    """return a list of the game's draws without the key "game number:" at the beginning"""
    line = clean_split(line, ":")
    string_of_draws = line[1]
    return clean_split(string_of_draws, ";")

def cube_tuple(element: list) -> tuple:
    """return a tuple (number: int, color: str)"""
    for m, e in enumerate(element):
        if e.isdigit():
            element[m] = int(e)
        else:
            continue
    return tuple(element)

def compare_number_cubes(number_game: tuple, number_max: list) -> list:
    """compare the number of cubes drawn against the current maximum of cube of that color already drawn"""
    for max_cube in number_max:
        if number_game[1] == max_cube[1]:
            if number_game[0] > max_cube[0]:
                max_cube[0] = number_game[0]
    return number_max

def calculate_power(number_max: list) -> int:
    """multiply the minimum cubes of each color together"""
    game_power = 1
    for cubes in number_max:
        game_power *= cubes[0]
    return game_power

def calculate_power_sum(sum: int, number_max: list) -> int:
    """add the game's power to the powers sum"""
    game_power = calculate_power(number_max)
    sum += game_power
    return sum

# MAIN

f = open("cubes_draws.txt", "r", encoding = "utf-8")

# create the variable that will contain the sum
powers_sum = 0

for line_number, line in enumerate(f):
    max_cubes = [[0, "red"], [0, "green"], [0, "blue"]]
    draws_list = isolate_draws(line)

    for i, cubes in enumerate(draws_list):
        cubes = clean_split(cubes, ",")

        for n, element in enumerate(cubes):
            element = clean_split(element)
            element = cube_tuple(element)
            max_cubes = compare_number_cubes(element, max_cubes)
            cubes[n] = element

        draws_list[i] = cubes

    powers_sum = calculate_power_sum(powers_sum, max_cubes)

print(powers_sum)

f.close()