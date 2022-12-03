from utils import get_day_input

data = get_day_input("one")

# Part One
print("Part 1: ", max(
    sum(map(int, entry.split("\n"))) for entry in data.split("\n\n")
))

# Part 2
print("Part 2: ", sum(sorted(
    [sum(map(int, entry.split("\n"))) for entry in data.split("\n\n")]
, reverse=True)[:3]))
