# coding=utf-8
"""Advent of Code 2016, Day 4, Part 1"""

import operator

with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

sector_sum = 0
for line in data:
    letter_counts = {}
    name = "".join(line.split("-")[:-1])
    sector_id = int(line.split("-")[-1].split("[")[0])
    provided_checksum = line.split("-")[-1].split("[")[1][:-1]
    for letter in name:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    sort_alpha = sorted(letter_counts.items(), key=operator.itemgetter(0))
    sort_numeric = sorted(sort_alpha, key=operator.itemgetter(1), reverse=True)
    derived_checksum = "".join([x[0] for x in sort_numeric[:5]])
    if derived_checksum == provided_checksum:
        sector_sum += sector_id

print(sector_sum)

