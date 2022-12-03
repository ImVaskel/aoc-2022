import time
from typing import Any, Callable


def get_day_input(day: str) -> str:
    with open(f"data/day_{day}.txt", "r") as fp:
        return fp.read()

def time_and_print_result(part: str, callable: Callable[..., Any]):
    start = time.perf_counter()
    result = callable()
    end = time.perf_counter()
    took = (end - start) * 1000
    print(f"Part {part}: {result} [took {took} ms]")