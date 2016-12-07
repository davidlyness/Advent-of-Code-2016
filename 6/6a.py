# coding=utf-8
"""Advent of Code 2016, Day 6, Part 1"""

with open("input.txt") as f:
    data = f.read().rstrip("\n").split()

message = ""
message_length = len(data[0])

for i in range(message_length):
    frequencies = {}
    for transmission in data:
        if transmission[i] not in frequencies:
            frequencies[transmission[i]] = 0
        frequencies[transmission[i]] += 1
    message += max(frequencies.keys(), key=(lambda k: frequencies[k]))

print(message)