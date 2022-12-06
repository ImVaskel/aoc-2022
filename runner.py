#!/usr/bin/env python3

import argparse
import datetime
import pathlib
import time
import traceback
from importlib import import_module
from typing import Any, Callable

import requests

RESET = "\u001b[0m"
BLUE = "\u001b[34m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
CYAN = "\u001b[36m"


PATH = pathlib.Path(__file__).parent / "token.txt"
if PATH.exists():
    with open(PATH, "r") as fp:
        SESSION_TOKEN = fp.read()
else:
    print(
        f"{RED} warning: no `token.txt` file detected in the root directory, you will be unable to get data from aoc's website."
    )


def get_day_input_from_aoc(day: int) -> None:
    file = pathlib.Path(__file__).parent / "data" / f"day_{day}.txt"
    with requests.get(
        f"https://adventofcode.com/2022/day/{day}/input",
        cookies={"session": SESSION_TOKEN},
    ) as res:
        with open(file, "w") as fp:
            fp.write(res.text)


def time_and_print_result(part: str, callable: Callable[..., Any]):
    start = time.perf_counter()

    try:
        result = callable()
    except Exception as exc:
        traceback_text = "".join(
            traceback.format_exception(type(exc), exc, exc.__traceback__, 4)
        )
        print(f"{RED}ERROR {BLUE}Part {part}: {RESET}\n{traceback_text}")
        return

    end = time.perf_counter()
    took = (end - start) * 1000

    print(f"{BLUE}Part {part}: {GREEN}{result}{RESET} [took {CYAN}{took:.2f}ms{RESET}]")


if __name__ == "__main__":
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5), "EST"))
    parser = argparse.ArgumentParser(description="Run AOC solutions.")
    parser.add_argument(
        "day",
        type=int,
        help="The day to run (default today).",
        default=now.day,
    )
    parser.add_argument(
        "--alt",
        "-a",
        action="store_true",
        help="Run the alternate answer, this just converts to `day_x_alt.py`.",
    )
    args = parser.parse_args()
    day: int = args.day
    alt = args.alt

    path = pathlib.Path(f"data/day_{day}.txt")
    if not path.exists():
        print("input data not found, fetching and writing to file.")
        get_day_input_from_aoc(day)

    module = f"days.day_{day}{'_alt' if alt else ''}"

    mod = import_module(module)
    for part in ("part_one", "part_two"):
        if not hasattr(mod, part):
            print(f"could not find {part} in day {day}, skipping.")
            continue

        time_and_print_result(part.split("_")[1].title(), getattr(mod, part))
