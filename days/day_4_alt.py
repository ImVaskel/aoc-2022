import re
from .utils import get_day_input

data = get_day_input(4)

parsed = [[*map(int, re.findall("\d+", line))] for line in data.splitlines()]


def part_one():
    # if one contains the other, the start of the range will be the same or less than the other range's start
    # and the end will be greater than or the same as the end of the other range
    return sum(a <= x and b >= y or x <= a and y >= b for a, b, x, y in parsed)


def part_two():
    return sum(a <= x <= b or x <= a <= y for a, b, x, y in parsed)
