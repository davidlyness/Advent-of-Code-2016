# coding=utf-8
"""Advent of Code 2016, Day 14, Part 2"""

import hashlib


def get_hash(string):
    """
    Calculate the MD5 hash of a given string, repeated 2017 times.
    :param string: the given string
    :return: hexadecimal hash of the string
    """
    for _ in range(2017):
        string = hashlib.md5(string.encode()).hexdigest()
    return string


def get_repeating_sequence(string):
    """
    Determine the first thrice-repeating character within a string.
    :param string: the given string
    :return: the repeating character if it exists; None otherwise
    """
    for position in range(len(string) - 2):
        sequence = string[position:position+3]
        if sequence == string[position] * 3:
            return sequence[0]
    return None

with open("input.txt") as f:
    salt = f.read().rstrip("\n")

hashes = []
key_indexes = []

for i in range(1000):
    hashes.append(get_hash(salt + str(i)))

index = 0
while len(key_indexes) < 64:
    hashes.append(get_hash(salt + str(index+1000)))
    candidate_key = hashes[index]
    candidate_character = get_repeating_sequence(candidate_key)
    if candidate_character:
        extended_sequence = candidate_character * 5
        if any(extended_sequence in hashed_string for hashed_string in hashes[index+1:index+1001]):
            key_indexes.append(index)
    index += 1

print(key_indexes[-1])
