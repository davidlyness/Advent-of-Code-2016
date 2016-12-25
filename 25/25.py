# coding=utf-8
"""Advent of Code 2016, Day 25"""


with open("input.txt") as f:
    instructions = [x.split(" ") for x in f.read().rstrip("\n").split("\n")]


def get_clock_output(a_value):
    """
    Determines the clock output given a specific initial register value.
    :param a_value: initial value for register a
    :return: clock output, truncated to a maximum length of 50
    """
    registers = {
        "a": a_value,
        "b": 0,
        "c": 0,
        "d": 0
    }
    c = []
    i = 0
    while not c or not ((len(c) % 2 == 1 and c[-1] == 1) or (len(c) % 2 == 0 and c[-1] == 0)) and len(c) < 50:
        instruction = instructions[i]
        if instruction[0] == "cpy":
            try:
                value = int(instruction[1])
            except ValueError:
                value = registers[instruction[1]]
            registers[instruction[2]] = value
            i += 1
        elif instruction[0] == "inc":
            registers[instruction[1]] += 1
            i += 1
        elif instruction[0] == "dec":
            registers[instruction[1]] -= 1
            i += 1
        elif instruction[0] == "jnz":
            try:
                value = int(instruction[1])
            except ValueError:
                value = registers[instruction[1]]
            if value != 0:
                i += int(instruction[2])
            else:
                i += 1
        elif instruction[0] == "out":
            try:
                value = int(instruction[1])
            except ValueError:
                value = registers[instruction[1]]
            c.append(value)
            i += 1
    return c

correct_clock_signal = None
candidate_register_value = 1
while not correct_clock_signal:
    if len(get_clock_output(candidate_register_value)) == 50:
        correct_clock_signal = candidate_register_value
    candidate_register_value += 1

print(correct_clock_signal)
