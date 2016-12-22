# coding=utf-8
"""Advent of Code 2016, Day 15"""


def get_capsule_drop_time():
    """
    Determine when all discs in the sequence line up for the capsule to drop successfully.
    :return: the first time at which the capsule drops successfully
    """
    step_size = 1
    start_time = 1
    num_discs = len(discs)
    while True:
        current_time = start_time
        for i in range(num_discs):
            current_time += 1
            num_disc_positions = discs[i][0]
            disc_start_position = discs[i][1]
            current_disc_position = (disc_start_position + current_time) % num_disc_positions
            if current_disc_position == 0:
                if step_size % num_disc_positions != 0:
                    step_size *= num_disc_positions
                if i == num_discs - 1:
                    return start_time
            else:
                break
        start_time += step_size

discs = []
with open("part1.txt") as f:
    data = f.read().rstrip("\n").split("\n")
for line in data:
    items = line.split()
    discs.append((int(items[3]), int(items[11][:-1])))

print(get_capsule_drop_time())
