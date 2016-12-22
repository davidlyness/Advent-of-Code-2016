# coding=utf-8
"""Advent of Code 2016, Day 16"""


def expand_data(data, length):
    """
    Expands data using modified dragon curve algorithm.
    :param data: input data
    :param length: required length of output
    :return: binary string of required length
    """
    while len(data) < length:
        a = data
        b = a[::-1].replace("0", "X").replace("1", "0").replace("X", "1")
        data = a + "0" + b
    return data[:length]


def generate_checksum(data):
    """
    Generates a checksum for the provided data
    :param data: input data
    :return: checksum string
    """
    checksum = None
    while not checksum or len(checksum) % 2 == 0:
        checksum = ""
        for i in range(0, len(data) - 1, 2):
            if data[i] == data[i+1]:
                checksum += "1"
            else:
                checksum += "0"
        data = checksum
    return checksum

print("Part 1: " + generate_checksum(expand_data("10011111011011001", 272)))
print("Part 2: " + generate_checksum(expand_data("10011111011011001", 35651584)))
