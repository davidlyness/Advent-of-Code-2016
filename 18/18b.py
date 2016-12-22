# coding=utf-8
"""Advent of Code 2016, Day 18, Part 2"""


def calculate_tile_status(a, b, c):
    """

    :param a: first parameter (back left)
    :param b: second parameter (back center)
    :param c: third parameter (back right)
    :return: '^' character if the tile is a trap; '.' character otherwise
    """
    if a == "^" and b == "^" and c == ".":
        return "^"
    elif a == "." and b == "^" and c == "^":
        return "^"
    elif a == "^" and b == "." and c == ".":
        return "^"
    elif a == "." and b == "." and c == "^":
        return "^"
    else:
        return "."


with open("input.txt") as f:
    puzzle_input = list(f.read().rstrip("\n"))

room_width = len(puzzle_input)
room_length = 400000
tiles = [puzzle_input]

for j in range(room_length - 1):
    row = []
    for i in range(room_width):
        if i == 0:
            left = "."
        else:
            left = tiles[j][i-1]
        center = tiles[j][i]
        if i == room_width - 1:
            right = "."
        else:
            right = tiles[j][i+1]
        row.append(calculate_tile_status(left, center, right))
    tiles.append(row)

print(sum([row.count(".") for row in tiles]))
