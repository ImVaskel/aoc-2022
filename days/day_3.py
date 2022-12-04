import string
from .utils import get_day_input


data = get_day_input(3)
weights = string.ascii_letters


def part_one():
    sum = 0
    for line in data.split("\n"):
        length = len(line)
        one, two = line[: length // 2], line[length // 2 :]
        for char in one:
            if char in two:
                found = char
                break
        else:
            raise Exception("how?")
        sum += weights.index(found) + 1

    return sum


def part_two():
    lines = data.split("\n")
    groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    sum = 0
    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                found = char
                break
        else:
            raise Exception("how once again?")
        sum += weights.index(found) + 1

    return sum
