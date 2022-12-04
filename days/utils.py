import sys
import time
import traceback
from pathlib import Path
from typing import Any, Callable

import requests

RESET = "\u001b[0m"
BLUE = "\u001b[34m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
CYAN = "\u001b[36m"


PATH = Path(__file__).parent.parent / "token.txt"
if PATH.exists():
    with open(PATH, "r") as fp:
        SESSION_TOKEN = fp.read()
else:
    print(
        f"{RED} warning: no `token.txt` file detected in the root directory, you will be unable to get data from aoc's website."
    )


def get_day_input_from_aoc(day: int) -> None:
    file = Path(__file__).parent.parent / "data" / f"day_{day}.txt"
    with requests.get(
        f"https://adventofcode.com/2022/day/{day}/input",
        cookies={"session": SESSION_TOKEN},
    ) as res:
        with open(file, "w") as fp:
            fp.write(res.text)


def get_day_input(day: int) -> str:
    with open(f"data/day_{day}.txt", "r") as fp:
        return fp.read()


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


# Call this script with (int)day
if __name__ == "__main__":
    args = sys.argv[1:]
    get_day_input_from_aoc(args[0])
