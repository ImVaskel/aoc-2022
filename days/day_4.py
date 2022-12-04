from .utils import get_day_input

data = get_day_input(4)


def part_one():
    overlapping = 0
    for pair in data.split("\n"):
        first, second = pair.split(",")  # a-b c-d
        first = first.split("-")
        second = second.split("-")
        first_range = set(range(int(first[0]), int(first[1]) + 1))
        second_range = set(range(int(second[0]), int(second[1]) + 1))

        if len(first_range.intersection(second_range)) in (
            len(first_range),
            len(second_range),
        ):
            overlapping += 1

    return overlapping


def part_two():
    overlapping = 0
    for pair in data.split("\n"):
        first, second = pair.split(",")  # a-b c-d
        first = first.split("-")
        second = second.split("-")
        first_range = set(range(int(first[0]), int(first[1]) + 1))
        second_range = set(range(int(second[0]), int(second[1]) + 1))

        if first_range.intersection(second_range):
            overlapping += 1

    return overlapping
