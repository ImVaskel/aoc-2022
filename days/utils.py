def get_day_input(day: str) -> str:
    with open(f"data/day_{day}.txt") as fp:
        return fp.read()
