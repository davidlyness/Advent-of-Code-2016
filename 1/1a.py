# coding=utf-8
"""Advent of Code 2016, Day 1, Part 1"""


def turn(direction, action):
    """
    Calculates the new direction to face.
    :param direction: the starting direction
    :param action: whether to turn left (L) or right (R)
    :return: the new direction after turning
    """
    directions = ["north", "east", "south", "west"]
    if action == "L":
        return directions[(directions.index(direction) - 1) % 4]
    else:
        return directions[(directions.index(direction) + 1) % 4]


def move(position, direction):
    """
    Calculates the new position of the sleigh.
    :param position: the starting position
    :param direction: the direction in which to move
    :return: the new position after movement
    """
    if direction == "north":
        return position[0], position[1] + 1
    elif direction == "east":
        return position[0] + 1, position[1]
    elif direction == "south":
        return position[0], position[1] - 1
    elif direction == "west":
        return position[0] - 1, position[1]
    return position


def calculate_distance(instructions):
    """
    Calculates the absolute distance between the starting and ending positions.
    :param instructions: direction and movement instructions
    :return: the number of blocks between the ending position and starting position
    """
    current_direction = "north"
    current_position = (0, 0)
    for instruction in instructions:
        current_direction = turn(current_direction, action=instruction[:1])
        current_distance = int(instruction[1:])
        for _ in range(current_distance):
            current_position = move(current_position, current_direction)
    return abs(current_position[0]) + abs(current_position[1])


with open("input.txt") as f:
    data = f.read().replace("\n", "").split(", ")

print(calculate_distance(data))
