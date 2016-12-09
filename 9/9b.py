# coding=utf-8
"""Advent of Code 2016, Day 9, Part 2"""

import re

with open("input.txt") as f:
    data = f.read().rstrip("\n")


def get_decompress_length(s):
    """
    Get the length of a decompressed string.
    :param s: string to decompress
    :return: decompressed length of string
    """
    result = 0
    pattern = re.compile("\((\d+)x(\d+)\).*")
    if "(" in s:
        while len(s) > 0:
            match = pattern.match(s)
            if match:
                num_characters = int(match.group(1))
                repeat = int(match.group(2))
                skip_length = 3 + len(match.group(1)) + len(match.group(2))
                result += get_decompress_length(s[skip_length:skip_length + num_characters]) * repeat
                s = s[skip_length + num_characters:]
            else:
                result += 1
                s = s[1:]
        return result
    else:
        return len(s)

print(get_decompress_length(data))
