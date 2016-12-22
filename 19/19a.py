# coding=utf-8
"""Advent of Code 2016, Day 19, Part 1"""

with open("input.txt") as f:
    num_elves = int(f.read().rstrip("\n"))

neighbours = {}
for elf_num in range(1, num_elves + 1):
    if elf_num == num_elves:
        neighbours[elf_num] = 1
    else:
        neighbours[elf_num] = elf_num + 1

current_elf = 1
while neighbours[current_elf] != current_elf:
    neighbours[current_elf] = neighbours[neighbours[current_elf]]  # Neighbour of stealee becomes neighbour of stealer
    current_elf = neighbours[current_elf]

print(current_elf)
