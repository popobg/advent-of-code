#! /usr/bin/env python3

"""Starting from a list of random cube draws, we are searching which games are possible if there were only 12 red cubes, 13 green cubes and 14 blue cubes in the bag from which the cubes were taken. Finally, calculate the sum of the IDs of those games."""

# first challenge : organize the data of the file cubes_draws into sets.

with open("cubes_draws.txt", "r", encoding = "utf-8") as f:
    games = []
    ID_good_games = []
    number_cubes = [(12, "red"), (13, "green"), (14, "blue")]
    for line_number, line in enumerate(f):
        line = line.strip().split(":")
        line = line[1]
        draws_list = line.strip().split(";")
        possible_draw = True
        for i, couples in enumerate(draws_list):
            couples = couples.strip().split(",")
            for n, element in enumerate(couples):
                element = element.strip().split(" ")
                for m, e in enumerate(element):
                    try:
                        int(e)
                        element[m] = int(e)
                    except:
                        continue
                for max_cube in number_cubes:
                    if element[1] == max_cube[1]:
                        if tuple(element) > max_cube:
                        # il faudrait dans cette situation break le for line_number global car on sait qu'on ne l'écrira pas dans games --> comment faire ?
                            possible_draw = False
                couples[n] = tuple(element)
            draws_list[i] = couples
        if possible_draw:
            ID_good_games.append(line_number + 1)

print(ID_good_games)

games = 0
for number in ID_good_games:
    games += number

print(games)