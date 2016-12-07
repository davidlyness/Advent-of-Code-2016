# coding=utf-8
"""Advent of Code 2016, Day 7, Part 1"""


def has_abba(seq):
    """
    Determines whether a sequence has an ABBA.
    :param seq: the sequence to check
    :return: True if the sequence contains an ABBA; False otherwise
    """
    for i in range(len(seq) - 3):
        if seq[i] == seq[i+3] and seq[i+1] == seq[i+2] and seq[i] != seq[i+1]:
            return True
    return False

with open("input.txt") as f:
    data = f.read().rstrip("\n").split()

num_tls_support = 0
for ip in data:
    supernet_sequences = []
    hypernet_sequences = []
    current_string = ""
    supernet = True
    for i in range(len(ip)):
        if ip[i] == "[":
            if current_string != "":
                supernet_sequences.append(current_string)
                current_string = ""
            supernet = False
        elif ip[i] == "]":
            if current_string != "":
                hypernet_sequences.append(current_string)
                current_string = ""
            supernet = True
        else:
            current_string += ip[i]
        if i == len(ip) - 1:
            supernet_sequences.append(current_string)
    if any(has_abba(x) for x in supernet_sequences) and not any(has_abba(x) for x in hypernet_sequences):
        num_tls_support += 1

print(num_tls_support)
