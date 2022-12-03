import string
from utils import get_day_input


data = get_day_input("three")
weights = string.ascii_letters

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

print("Part 1: ", sum)

data = data.split("\n")
groups = [data[i : i + 3] for i in range(0, len(data), 3)]
sum = 0
for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            found = char
            break
    else:
        raise Exception("how once again?")
    sum += weights.index(found) + 1


print("Part 2: ", sum)
