from pathlib import Path


def get_day_input(day: int) -> str:
    path = Path(__file__).parent.parent / "data" / f"day_{day}.txt"
    with path.open("r") as fp:
        return fp.read()
