# coding=utf-8
"""Advent of Code 2016, Day 13, Part 1"""


def get_next_positions(position, state):
    """
    Get all valid next positions by moving up, down, left or right from the current position.
    :param position: current position
    :param state: current puzzle state
    :return: list of valid next positions
    """
    candidate_positions = []
    x = position[0]
    y = position[1]
    if x > 0:
        candidate_positions.append((x-1, y))
    if y > 0:
        candidate_positions.append((x, y - 1))
    candidate_positions.append((x+1, y))
    candidate_positions.append((x, y+1))
    return [pos for pos in candidate_positions if state[pos[1]][pos[0]] == "." and pos not in seen_positions]


def calculate_state(x, y, offset):
    """
    Determines whether the current position is an open space or a wall.
    :param x: x-coordinate to consider
    :param y: y-coordinate to consider
    :param offset: custom offset
    :return: "." if the position is an open space; "#" otherwise
    """
    value = x*x + 3*x + 2*x*y + y + y*y + offset
    if bin(value).count("1") % 2 == 0:
        return "."
    else:
        return "#"


puzzle_input = 1364
start_position = (1, 1)
goal_position = (31, 39)
seen_positions = []
min_steps = None

current_state = [[calculate_state(x, y, puzzle_input) for x in range(100)] for y in range(100)]
config_queue = [(start_position, 0)]

while not min_steps:
    current_position, current_steps = config_queue.pop(0)
    if current_position == goal_position:
        min_steps = current_steps
    else:
        seen_positions.append(current_position)
        for next_position in get_next_positions(current_position, current_state):
            config_queue.append((next_position, current_steps + 1))

print(min_steps)
