# coding=utf-8
"""Advent of Code 2016, Day 8"""


def print_screen(grid):
    """
    Output the grid
    :param grid: source grid
    """
    for row in grid:
        print("".join(row))


def add_rect(grid, rect):
    """
    Push a rectangle to the upper-left corner of the grid.
    :param grid: source grid
    :param rect: dimensions of rectangle to add
    :return: updated grid
    """
    coordinates = [int(x) for x in rect.split("x")]
    for j in range(coordinates[1]):
        for i in range(coordinates[0]):
            grid[j][i] = "#"
    return grid


def rotate_screen(grid, details):
    """
    Rotate the grid by the specified parameters.
    :param grid: source grid
    :param details: details of the rotation transformation
    :return: updated grid
    """
    transformation_type = details[1]
    location = int(details[2].split("=")[1])
    amount = int(details[4])
    num_rows = len(grid)
    num_columns = len(grid[0])
    if transformation_type == "row":
        grid[location] = [grid[location][(i - amount) % num_columns] for i in range(num_columns)]
    else:
        current_values = [grid[j][location] for j in range(6)]
        for j in range(num_rows):
            grid[(j + amount) % num_rows][location] = current_values[j]
    return grid


def count_lights(grid):
    """
    Count the number of "on" lights in the grid
    :param grid: source grid
    :return: number of "on" lights
    """
    lights = 0
    for row in grid:
        for char in row:
            if char == "#":
                lights += 1
    return lights


with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

screen = [[" " for y in range(50)] for x in range(6)]

for line in data:
    instruction = line.split()
    if instruction[0] == "rect":
        add_rect(screen, instruction[1])
    else:
        rotate_screen(screen, instruction)

print(count_lights(screen))  # Part 1
print_screen(screen)  # Part 2
