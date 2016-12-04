# coding=utf-8
"""Advent of Code 2016, Day 2, Part 1"""


def move(position, direction):
    """
    Calculates the new position on the button pad.
    :param position: the starting position
    :param direction: the direction in which to move
    :return: the new position after movement
    """
    if direction == "U":
        if position < 4:
            return position
        else:
            return position - 3
    if direction == "R":
        if position % 3 == 0:
            return position
        else:
            return position + 1
    if direction == "D":
        if position > 6:
            return position
        else:
            return position + 3
    if direction == "L":
        if position % 3 == 1:
            return position
        else:
            return position - 1

code = ""
current_position = 5
with open("input.txt") as f:
    data = f.read().split()

for line in data:
    for movement in line:
        current_position = move(current_position, movement)
    code += str(current_position)
print(code)
