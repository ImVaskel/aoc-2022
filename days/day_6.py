from .common import get_day_input

data = get_day_input(6)


def part_one():
    for i in range(0, len(data) - 4):
        chars = data[i : i + 4]
        if len(set(chars)) == 4:  # we know we should have 4 characters total
            return i + 4

    raise Exception("this should not be possible.")


def part_two():
    for i in range(0, len(data) - 14):
        chars = data[i : i + 14]
        if len(set(chars)) == 14:  # we know we should have 14 characters total
            return i + 14

    raise Exception("this should not be possible.")
