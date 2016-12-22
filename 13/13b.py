# coding=utf-8
"""Advent of Code 2016, Day 13, Part 2"""


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
seen_positions = set()
max_steps = 50

current_state = [[calculate_state(x, y, puzzle_input) for x in range(100)] for y in range(100)]
position_queue = [(start_position, 0)]

step_count = 0
while position_queue:
    current_position, current_steps = position_queue.pop(0)
    seen_positions.add(current_position)
    if current_steps < max_steps:
        for next_position in get_next_positions(current_position, current_state):
            position_queue.append((next_position, current_steps + 1))

print(len(seen_positions))
