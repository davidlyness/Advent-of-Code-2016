# coding=utf-8
"""Advent of Code 2016, Day 21, Part 1"""


def scramble(password_string):
    """
    Scramble a provided password.
    :param password_string: string to scramble
    :return: scrambled version of provided password
    """
    password = list(password_string)
    for instruction in instructions:
        words = instruction.split()
        operation = " ".join(words[:2])
        if operation == "swap position":
            position1, position2 = int(words[2]), int(words[5])
            password[position1], password[position2] = password[position2], password[position1]
        elif operation == "swap letter":
            letter1, letter2 = words[2], words[5]
            position1, position2 = password.index(letter1), password.index(letter2)
            password[position1], password[position2] = letter2, letter1
        elif operation == "rotate left":
            amount = int(words[2]) % len(password)
            password = password[amount:] + password[:amount]
        elif operation == "rotate right":
            amount = int(words[2]) % len(password)
            password = password[-amount:] + password[:-amount]
        elif operation == "rotate based":
            letter_index = password.index(words[6])
            if letter_index >= 4:
                amount = letter_index + 2
            else:
                amount = letter_index + 1
            amount %= len(password)
            password = password[-amount:] + password[:-amount]
        elif operation == "reverse positions":
            start, end = int(words[2]), int(words[4]) + 1
            password[start:end] = reversed(password[start:end])
        elif operation == "move position":
            position1, position2 = int(words[2]), int(words[5])
            letter = password[position1]
            password.pop(position1)
            password.insert(position2, letter)
    return "".join(password)


with open("input.txt") as f:
    instructions = f.read().rstrip("\n").split("\n")

print(scramble("abcdefgh"))
