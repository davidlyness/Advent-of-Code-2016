# coding=utf-8
"""Advent of Code 2016, Day 7, Part 2"""


def get_abas(seq):
    """
    Calculates the candidate ABAs present in a sequence.
    :param seq: the sequence to check
    :return: the collection of ABAs present in the sequence
    """
    abas = []
    for i in range(len(seq) - 2):
        if seq[i] == seq[i+2] and seq[i] != seq[i+1]:
            abas.append(seq[i:i+3])
    return abas


with open("input.txt") as f:
    data = f.read().rstrip("\n").split()

num_ssl_support = 0
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
    abas = []
    for seq in supernet_sequences:
        abas += get_abas(seq)
    if any(aba[1] + aba[0] + aba[1] in seq for seq in hypernet_sequences for aba in abas):
        num_ssl_support += 1

print(num_ssl_support)
