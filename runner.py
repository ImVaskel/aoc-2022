import argparse
import datetime
from importlib import import_module
import pathlib

from days.utils import get_day_input_from_aoc, time_and_print_result

if __name__ == "__main__":
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5), "EST"))
    parser = argparse.ArgumentParser(description="Run AOC solutions.")
    parser.add_argument(
        "day",
        type=int,
        help="The day to run (default today).",
        default=now.day,
    )
    day: int = parser.parse_args().day

    path = pathlib.Path(f"data/day_{day}.txt")
    if not path.exists():
        print("input data not found, fetching and writing to file.")
        get_day_input_from_aoc(day)

    mod = import_module(f"days.day_{day}")
    for part in ("part_one", "part_two"):
        if not hasattr(mod, part):
            print(f"could not find {part} in day {day}, skipping.")
            continue

        time_and_print_result(part.split("_")[1].title(), getattr(mod, part))
