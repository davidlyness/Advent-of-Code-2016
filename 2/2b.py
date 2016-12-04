# coding=utf-8
"""Advent of Code 2016, Day 2, Part 2"""


def move(grid, position, direction):
    """
    Calculates the new position on the button pad.
    :param grid: the source grid to use
    :param position: the starting position
    :param direction: the direction in which to move
    :return: the new position after movement
    """
    if direction == "U":
        new_position = position[0] - 1, position[1]
    elif direction == "R":
        new_position = position[0], position[1] + 1
    elif direction == "D":
        new_position = position[0] + 1, position[1]
    else:
        new_position = position[0], position[1] - 1

    # Verify that we haven't gone out-of-bounds on the grid
    if new_position[0] < 0 or new_position[0] > 4:
        new_position = position[0], new_position[1]
    if new_position[1] < 0 or new_position[1] > 4:
        new_position = new_position[0], position[1]

    # Verify that the position on the grid isn't a blank space
    if grid[new_position[0]][new_position[1]] != 0:
        return new_position
    else:
        return position

code = ""
button_grid = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 10, 11, 12, 0],
    [0, 0, 13, 0, 0]
]
current_position = (2, 0)
with open("input.txt") as f:
    data = f.read().split()

for line in data:
    for movement in line:
        current_position = move(button_grid, current_position, movement)
    current_button = button_grid[current_position[0]][current_position[1]]
    code += str(hex(current_button).split('x')[1]).upper()
print(code)
