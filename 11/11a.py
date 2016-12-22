# coding=utf-8
"""Advent of Code 2016, Day 11, Part 1"""

import itertools


def is_valid_state(state):
    """
    Determines whether the provided state is a survivable one.
    :param state: specified state
    :return: True if the provided state is valid; False otherwise
    """
    for floor in state:
        for item in floor:
            if item[-1] == "M":
                microchip = item[:-1]
                generators = [generator[:-1] for generator in floor if generator[-1] == "G"]
                if microchip not in generators and len(generators) > 0:
                    return False
    return True


class RTF(object):
    """
    Represents the configuration of Radioisotope Thermoelectric Generators (RTGs).
    """

    def __init__(self, floor, state=None):

        self.current_floor = floor
        if state:
            self.current_state = state
        else:
            with open("part1.txt") as f:
                data = f.read().rstrip("\n").split("\n")
            self.current_state = [[] for _ in range(len(data))]
            for i in range(len(data)):
                words = data[i].split(" contains ")[1][:-1].split(" ")
                for j in range(len(words)):
                    if "generator" in words[j]:
                        self.current_state[i].append(words[j-1] + "G")
                    if "microchip" in words[j]:
                        self.current_state[i].append(words[j-1].split("-")[0] + "M")

    def is_end_state(self):
        """
        Determines whether the current state is an end state.
        :return: True if the current state is an end state; False otherwise.
        """
        return all([len(floor) == 0 for floor in self.current_state[:-1]])

    def get_candidate_next_floors(self):
        """
        Determine the possible next positions of the lift.
        :return: list of the floors on which the lift can end up next tick.
        """
        min_floor = 0
        max_floor = len(self.current_state) - 1
        if min_floor <= self.current_floor < max_floor:
            return [self.current_floor + 1, self.current_floor - 1]
        elif self.current_floor > min_floor:
            return [self.current_floor - 1]
        else:
            return [self.current_floor + 1]

    def get_candidate_next_states(self):
        """
        Determine the possible next states of the RTGs.
        :return: list of the candidate next states.
        """
        candidate_next_states = []
        contents = self.current_state[self.current_floor]
        candidate_floors = self.get_candidate_next_floors()
        final_candidates = []
        num_items = 2
        while final_candidates == [] and num_items > 0:
            candidate_combinations = list(itertools.combinations(contents, num_items))
            for combination in candidate_combinations:
                candidate_state = [list(x) for x in self.current_state]
                [candidate_state[self.current_floor].remove(item) for item in combination]
                for new_floor in candidate_floors:
                    candidate_state_floor = [list(x) for x in candidate_state]
                    for item in combination:
                        candidate_state_floor[new_floor].append(item)
                    candidate_next_states.append([new_floor, candidate_state_floor])
            final_candidates = [[floor, state] for floor, state in candidate_next_states if is_valid_state(state)]
            num_items -= 1
        return final_candidates

seen_states = []
config_queue = [[0, None, 0]]
current_config = None
win = False
max_steps = 0

while not win:
    current_config = config_queue.pop(0)
    if current_config[:-1] not in seen_states:
        seen_states.append(current_config[:-1])
        current_state = RTF(floor=current_config[0], state=current_config[1])
        if current_state.is_end_state():
            win = True
        for next_state in current_state.get_candidate_next_states():
            config_queue.append([next_state[0], next_state[1], current_config[2] + 1])

print(current_config[0])
