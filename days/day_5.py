import re
from itertools import islice
from typing import Iterable, TypeVar

from .common import get_day_input

data = get_day_input(5)

INSTRUCTION_REGEX = re.compile("move (\d+) from (\d+) to (\d+)")

T = TypeVar("T")

# ty aba
def chunks(iterable: Iterable[T], *, n: int):
    it = iter(iterable)
    return iter(lambda: tuple(islice(it, n)), ())


def parse_stacks_and_instructions():
    crates, instructions = data.split("\n\n")
    # get ready for horror
    # tldr: regardless of whether or not there is a box in the area, the length is the same, so we can just parse by that.
    stacks: list[list[str]] = [[] for _ in range(9)]
    for line in crates.split("\n")[:-1]:  # get rid of the boxes numbers
        line_crates = chunks(line, n=4)
        for idx, crate in enumerate(line_crates):
            if crate[1].isalpha():
                stacks[idx] += crate[1]

    return stacks, instructions


def part_one():
    stacks, instructions = parse_stacks_and_instructions()
    for instruction in instructions.split("\n"):
        amt, _from, to = [*map(int, INSTRUCTION_REGEX.findall(instruction)[0])]
        for _ in range(amt):
            crate = stacks[_from - 1].pop(0)
            stacks[to - 1].insert(0, crate)

    tops = "".join(next(x for x in stack if x.isalpha()) for stack in stacks)

    return tops


def part_two():
    stacks, instructions = parse_stacks_and_instructions()

    for instruction in instructions.split("\n"):
        amt, _from, to = [*map(int, INSTRUCTION_REGEX.findall(instruction)[0])]
        crates = [stacks[_from - 1].pop(0) for _ in range(amt)]
        for crate in reversed(crates):
            stacks[to - 1].insert(0, crate)

    tops = "".join(next(x for x in stack if x.isalpha()) for stack in stacks)

    return tops
