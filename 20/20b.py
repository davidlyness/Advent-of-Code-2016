# coding=utf-8
"""Advent of Code 2016, Day 20, Part 2"""


with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split()
items = [x.split("-") for x in puzzle_input]
blacklists = [(int(x[0]), int(x[1])) for x in items]

max_value = 4294967295
full_blacklists = []
num_allowed_ips = 0

while blacklists:
    ranges = [min(blacklists, key=lambda x: x[0])]
    start_range = ranges[0][0]
    overlapping_ranges = True  # Sentinel value to ensure at least one loop iteration below; this is ugly. :(
    while overlapping_ranges:
        overlapping_ranges = [x for x in blacklists for r in ranges if x[0] < r[1]]
        ranges += overlapping_ranges
        [blacklists.remove(x) for x in set(overlapping_ranges)]
    end_range = max(ranges, key=lambda x: x[1])[1]
    full_blacklists.append((start_range, end_range))

num_allowed_ips += max(full_blacklists[0][0], 0)
for i in range(1, len(full_blacklists)):
    num_allowed_ips += max(full_blacklists[i][0] - full_blacklists[i-1][1] - 1, 0)
num_allowed_ips += max(max_value - full_blacklists[len(full_blacklists)-1][1], 0)

print(num_allowed_ips)
