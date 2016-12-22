# coding=utf-8
"""Advent of Code 2016, Day 17, Part 2"""

import hashlib


def get_next_positions(position, path):
    """
    Get all valid next positions by moving up, down, left or right from the current position.
    :param position: current position
    :param path: the prior path already taken
    :return: list of tuples of (valid next position, associated direction)
    """
    open_whitelist = ["b", "c", "d", "e", "f"]
    candidate_states = []
    up, down, left, right = hashlib.md5(path.encode()).hexdigest()[:4]
    if up in open_whitelist and position[0] > 0:
        candidate_states.append(((position[0] - 1, position[1]), "U"))
    if down in open_whitelist and position[0] < 3:
        candidate_states.append(((position[0] + 1, position[1]), "D"))
    if left in open_whitelist and position[1] > 0:
        candidate_states.append(((position[0], position[1] - 1), "L"))
    if right in open_whitelist and position[1] < 3:
        candidate_states.append(((position[0], position[1] + 1), "R"))
    return candidate_states

with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n")

start_position = (0, 0)
goal_position = (3, 3)
winning_paths = []
config_queue = [(start_position, puzzle_input)]

while config_queue:
    current_position, current_path = config_queue.pop(0)
    if current_position == goal_position:
        winning_paths.append(current_path[len(puzzle_input):])
    else:
        for next_position, direction in get_next_positions(current_position, current_path):
            config_queue.append((next_position, current_path + direction))

print(len(max(winning_paths, key=len)))
