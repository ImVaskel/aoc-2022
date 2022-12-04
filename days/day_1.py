from .utils import get_day_input

data = get_day_input(1)

# Part One
def part_one():
    return max(sum(map(int, entry.split("\n"))) for entry in data.split("\n\n"))


# Part 2
def part_two():
    return sum(
        sorted(
            [sum(map(int, entry.split("\n"))) for entry in data.split("\n\n")],
            reverse=True,
        )[:3]
    )
