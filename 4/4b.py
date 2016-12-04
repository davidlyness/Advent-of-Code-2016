# coding=utf-8
"""Advent of Code 2016, Day 4, Part 2"""

import string


def decrypt_character(c, shift):
    """
    Decrypts a character according to a custom Caesar cipher.
    :param c: character to decrypt
    :param shift: amount of letters (Caesar cipher distance) to shift
    :return: the decrypted character
    """
    if c == "-":
        return " "
    else:
        return list(string.ascii_lowercase)[(ord(c) - ord("a") + shift) % 26]


with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

for line in data:
    name = "-".join(line.split("-")[:-1])
    sector_id = int(line.split("-")[-1].split("[")[0])
    decrypted_string = "".join([decrypt_character(x, sector_id) for x in name])
    if "northpole" in decrypted_string:
        print(sector_id)
