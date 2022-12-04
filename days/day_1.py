from utils import get_day_input, time_and_print_result

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


time_and_print_result("1", part_one)
time_and_print_result("2", part_two)
