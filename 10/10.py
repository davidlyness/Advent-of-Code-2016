# coding=utf-8
"""Advent of Code 2016, Day 10"""


def add_bot_value(bot, num):
    """
    Adds a value to a bot's collection of microchips.
    :param bot: the bot to consider
    :param num: the value to add
    """
    if bot not in bots:
        bots[bot] = []
    bots[bot].append(num)


def pass_value(source, destination, value_type, destination_type):
    """
    Transfer a value from one bot to a new destination.
    :param source: the bot currently holding the value
    :param destination: the bot or output bin that should be holding the value
    :param value_type: the "low" or "high" value from the source bot
    :param destination_type: whether the destination is a bot or an output bin
    """
    if value_type == "low":
        value = min(bots[source])
    else:
        value = max(bots[source])
    if destination_type == "bot":
        add_bot_value(destination, value)
    else:
        outputs[destination] = value


with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")

bots = {}
outputs = {}
part_1_bot_id = None

for line in data:
    if line.split()[0] == "value":
        add_bot_value(int(line.split()[5]), int(line.split()[1]))

instructions = [line for line in data if line.split()[0] == "bot"]

while any(x is not None for x in instructions):
    for i in range(len(instructions)):
        if instructions[i] is not None:
            details = instructions[i].split()
            source_bot = int(details[1])
            if source_bot in bots and len(bots[source_bot]) == 2:
                if 61 in bots[source_bot] and 17 in bots[source_bot]:
                    part_1_bot_id = source_bot
                if details[5] == "bot":
                    pass_value(source_bot, int(details[6]), "low", "bot")
                else:
                    pass_value(source_bot, int(details[6]), "low", "output")
                if details[10] == "bot":
                    pass_value(source_bot, int(details[11]), "high", "bot")
                else:
                    pass_value(source_bot, int(details[11]), "high", "output")
                instructions[i] = None

print(part_1_bot_id)  # Part 1
print(outputs[0] * outputs[1] * outputs[2])  # Part 2
