# coding=utf-8
"""Advent of Code 2016, Day 23, Part 2"""


with open("input.txt") as f:
    instructions = [x.split(" ") for x in f.read().rstrip("\n").split("\n")]

registers = {
    "a": 12,
    "b": 0,
    "c": 0,
    "d": 0
}

i = 0
num_instructions = len(instructions)
while i < num_instructions:
    instruction = instructions[i]
    if i == 4:  # Loop optimisation: the following 6 lines just set a = b * d, so short-circuit the individual ops.
        registers['a'] = registers['b'] * registers['d']
        i += 6
    else:
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
            try:
                amount = int(instruction[2])
            except ValueError:
                amount = registers[instruction[2]]
            if value != 0:
                i += amount
            else:
                i += 1
        elif instruction[0] == "tgl":
            try:
                value = int(instruction[1])
            except ValueError:
                value = registers[instruction[1]]
            target_index = i + value
            if target_index < len(instructions):
                target_instruction = instructions[i + value]
                if target_instruction[0] == "inc":
                    target_instruction[0] = "dec"
                elif target_instruction[0] in ["dec", "tgl"]:
                    target_instruction[0] = "inc"
                elif target_instruction[0] == "jnz":
                    target_instruction[0] = "cpy"
                elif target_instruction[0] == "cpy":
                    target_instruction[0] = "jnz"
            i += 1

print(registers['a'])
