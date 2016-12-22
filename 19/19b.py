# coding=utf-8
"""Advent of Code 2016, Day 19, Part 2"""

with open("input.txt") as f:
    num_elves = int(f.read().rstrip("\n"))

"""
Coding the actual interactions are fiddly and boring. Instead, inferring from small-N simulations:
1) If the number of elves (N) is a power of 3, the final elf will win.
2) Otherwise:
    a) Find the largest power of 3 which is less than the number of elves (F).
    b) If N - 2F <= 0, answer = N - F.
    c) If N - 2F > 0, answer = N - F + (N - 2F) = 2N - 3F.
"""

floor = 1
while 3 * floor <= num_elves:
    floor *= 3
if num_elves == floor:
    print(num_elves)
else:
    print(num_elves - floor + max(num_elves - 2 * floor, 0))
