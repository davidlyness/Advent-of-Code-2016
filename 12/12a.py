# coding=utf-8
"""Advent of Code 2016, Day 12, Part 1"""


with open("input.txt") as f:
    instructions = [x.split(" ") for x in f.read().rstrip("\n").split("\n")]

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}

i = 0
num_instructions = len(instructions)
while i < num_instructions:
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

print(registers['a'])
