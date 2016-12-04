# coding=utf-8
"""Advent of Code 2016, Day 3, Part 2"""

with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

i = 0
triplets = []
while i < len(data):
    line1 = [int(x) for x in data[i].split()]
    line2 = [int(x) for x in data[i + 1].split()]
    line3 = [int(x) for x in data[i + 2].split()]
    for j in range(3):
        triplets.append((line1[j], line2[j], line3[j]))
    i += 3

num_possible_triangles = 0
for a, b, c in triplets:
    if a < b + c and b < a + c and c < a + b:
        num_possible_triangles += 1
print(num_possible_triangles)
