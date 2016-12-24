# coding=utf-8
"""Advent of Code 2016, Day 24, Part 1"""

import itertools
import networkx


with open("input.txt") as f:
    puzzle_map = f.read().rstrip("\n")

puzzle_rows = puzzle_map.split()
num_rows = len(puzzle_rows)
num_cols = len(puzzle_rows[0])
num_nodes = 0
coordinates = {}

graph = networkx.generators.classic.grid_2d_graph(num_rows, num_cols)
for i in range(num_rows):
    for j in range(num_cols):
        if puzzle_rows[i][j] == "#":
            graph.remove_node((i, j))
        if puzzle_rows[i][j].isdigit():
            coordinates[int(puzzle_rows[i][j])] = (i, j)
            num_nodes += 1

distances = {}
for i in range(num_nodes):
    for j in range(num_nodes):
        distances[i, j] = networkx.shortest_path_length(graph, coordinates[i], coordinates[j])
        distances[j, i] = distances[i, j]

shortest_path_found = float("inf")
for candidate_path in itertools.permutations(range(1, num_nodes)):
    path_list = [0] + list(candidate_path)
    candidate_path_length = sum([distances[path_list[i + 1], path_list[i]] for i in range(len(path_list) - 1)])
    shortest_path_found = min(candidate_path_length, shortest_path_found)

print(shortest_path_found)
