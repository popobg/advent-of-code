#! /usr/bin/env python3

"""Starting from a list of random cube draws, we are searching which games are possible if there were only 12 red cubes, 13 green cubes and 14 blue cubes in the bag from which the cubes were taken. Finally, calculate the sum of the IDs of those games."""

# FUNCTIONS

def clean_split(string: str, separator = " "):
    """strip then split by the separator a string"""
    return string.strip().split(separator)

def isolate_draws(line: str):
    """return a list of the game's draws without the key "game number:" at the beginning"""
    line = clean_split(line, ":")
    string_of_draws = line[1]
    return clean_split(string_of_draws, ";")

def cube_tuple(element: list):
    """return a tuple (number: int, color: str)"""
    for m, e in enumerate(element):
        if e.isdigit():
            element[m] = int(e)
        else:
            continue
    return tuple(element)

def compare_number_cubes(number_game: tuple, number_max: list, var: bool):
    """compare the number of cubes drawn against the maximum value possible"""
    for max_cube in number_max:
        if number_game[1] == max_cube[1]:
            if number_game > max_cube:
                var = False
    return var

def determine_possible_game(var: bool, sum: int, number: int):
    """add the game's number to sum if the game is possible"""
    if var:
        sum += number
    return sum

# MAIN

f = open("cubes_draws.txt", "r", encoding = "utf-8")

# create the variable that will contain the sum
possible_games_sum = 0
number_cubes = [(12, "red"), (13, "green"), (14, "blue")]

for line_number, line in enumerate(f):
    draws_list = isolate_draws(line)

    possible_draw = True
    for i, cubes in enumerate(draws_list):
        if possible_draw:
            cubes = clean_split(cubes, ",")

            for n, element in enumerate(cubes):
                element = clean_split(element)
                element = cube_tuple(element)
                possible_draw = compare_number_cubes(element, number_cubes, possible_draw)
                cubes[n] = element

            draws_list[i] = cubes
        else:
            break

    possible_games_sum = determine_possible_game(possible_draw, possible_games_sum, (line_number + 1))

print(possible_games_sum)
f.close()