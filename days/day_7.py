from collections import defaultdict

from .common import get_day_input

data = get_day_input(7)

MAX_LENGTH = 100000


def parse_folders():
    folders = defaultdict[str, list[int]](list)
    cmds = data.split("$ ")[1:]  # all commands are `$ cmd <arg>`

    dir: list[str] = []
    for entry in cmds:
        split = entry.splitlines()
        cmd = split.pop(0)
        if cmd == "ls":  # listing directories does not involve parsing anything out
            for line in split:
                if not line.startswith(
                    "dir"
                ):  # we can just ignore any directories found, since we don't need any knowledge of the tree
                    size, _ = line.split(" ")
                    size = int(size)
                    for i in range(len(dir) + 1):
                        folders["/".join(dir[:i])].append(size)
                else:
                    _, name = line.split(" ")
        else:  # we have a cd
            _, arg = cmd.split(" ")
            if arg == "..":
                dir = dir[:-1]
            else:
                if arg == "/":  # just go ahead and reset the list
                    dir.clear()
                else:
                    dir.append(arg)

    return folders


def part_one():
    folders = parse_folders()

    return sum(sum(l) for l in folders.values() if sum(l) <= MAX_LENGTH)


def part_two():
    totals = {n: sum(l) for n, l in parse_folders().items()}
    free = 70_000_000 - totals['']

    return next(n for i, n in sorted(totals.items(), key=lambda i: i[1]) if 30_000_000 - free <= n )
