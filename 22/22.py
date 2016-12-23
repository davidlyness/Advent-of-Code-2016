# coding=utf-8
"""Advent of Code 2016, Day 22"""

import itertools
import re

"""
Part 2 can be solved by hand when you realise it reduces to a simple version of https://en.wikipedia.org/wiki/15_puzzle
"""

with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split("\n")

nodes = {}
for line in puzzle_input[2:]:
    match = re.search("/dev/grid/node-(x\d+-y\d+).* \d+T.* (\d+)T.* (\d+)T.* \d+%.*", line)
    node_dict = {
        "used": int(match.group(2)),
        "avail": int(match.group(3))
    }
    nodes[match.group(1)] = node_dict

num_viable_pairs = 0
for nodeA, nodeB in itertools.product(nodes, repeat=2):
    if nodeA != nodeB and nodes[nodeA]['used'] != 0 and nodes[nodeA]['used'] <= nodes[nodeB]['avail']:
        num_viable_pairs += 1
print(num_viable_pairs)
