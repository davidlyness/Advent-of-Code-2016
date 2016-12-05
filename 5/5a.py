# coding=utf-8
"""Advent of Code 2016, Day 5, Part 1"""

import hashlib

with open("input.txt") as f:
    door_id = f.read().rstrip("\n")

index = 0
password = ""
while len(password) < 8:
    candidate_string = door_id + str(index)
    hashed_string = hashlib.md5(candidate_string.encode()).hexdigest()
    if hashed_string[:5] == "00000":
        password += hashed_string[5]
    index += 1

print(password)
