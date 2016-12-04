# coding=utf-8
"""Advent of Code 2016, Day 3, Part 1"""

with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

num_possible_triangles = 0
for line in data:
    a, b, c = [int(x) for x in line.split()]
    if a < b + c and b < a + c and c < a + b:
        num_possible_triangles += 1

print(num_possible_triangles)
