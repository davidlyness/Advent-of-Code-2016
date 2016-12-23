# coding=utf-8
"""Advent of Code 2016, Day 20, Part 1"""


with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split()
items = [x.split("-") for x in puzzle_input]
blacklists = [(int(x[0]), int(x[1])) for x in items]

max_value = 4294967295
candidate_ip = 0
lowest_ip = None

while not lowest_ip and candidate_ip <= max_value:
    min_blacklist_range = min(blacklists, key=lambda x: x[0])
    ranges = [x for x in blacklists if x[0] < min_blacklist_range[1]]
    start_range = min_blacklist_range[0]
    end_range = max(ranges, key=lambda x: x[1])[1]
    if candidate_ip < start_range:
        lowest_ip = candidate_ip
    else:
        candidate_ip = end_range + 1
    [blacklists.remove(x) for x in ranges]

print(lowest_ip)
