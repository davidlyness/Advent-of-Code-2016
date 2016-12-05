# coding=utf-8
"""Advent of Code 2016, Day 5, Part 2"""

import hashlib

with open("input.txt") as f:
    door_id = f.read().rstrip("\n")

index = 0
password = [None] * 8
while any(x is None for x in password):
    candidate_string = door_id + str(index)
    hashed_string = hashlib.md5(candidate_string.encode()).hexdigest()
    try:
        position = int(hashed_string[5])
    except ValueError:
        position = None
    if hashed_string[:5] == "00000" and position in range(8):
        if password[position] is None:
            password[position] = hashed_string[6]
            print("Position " + hashed_string[5] + " is " + hashed_string[6])
    index += 1

print("".join(password))
