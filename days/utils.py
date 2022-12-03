import pathlib
import sys
import time
from typing import Any, Callable

import requests

with open(pathlib.Path(__file__).parent.parent / "token.txt", "r") as fp:
    SESSION_TOKEN = fp.read()

def get_day_input_from_aoc(day: int, name: str) -> None:
    file = pathlib.Path(__file__).parent.parent / "data" / f"day_{name}.txt"
    with requests.get(
        f"https://adventofcode.com/2022/day/{day}/input", cookies={"session": SESSION_TOKEN}
    ) as res:
        with open(file, "w") as fp:
            fp.write(res.text)


def get_day_input(day: str) -> str:
    with open(f"data/day_{day}.txt", "r") as fp:
        return fp.read()


def time_and_print_result(part: str, callable: Callable[..., Any]):
    start = time.perf_counter()
    result = callable()
    end = time.perf_counter()
    took = (end - start) * 1000
    print(f"Part {part}: {result} [took {took:.2f} ms]")

# Call this script with (int)day (string)output
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        raise Exception("args need to be in the form of (day), (name).")
    get_day_input_from_aoc(args[0], args[1])