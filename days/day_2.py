from utils import get_day_input, time_and_print_result

data = get_day_input(2)

ties= {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins = {
    "A": "Y", # them rock, me paper
    "B": "Z", # them paper, me scissors
    "C": "X" # them scissors, me rock
}

loss = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

scores = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissors
}

def part_one():
    score = 0
    for line in data.split("\n"):
        them, me = line.split(" ")
        if ties.get(them) == me:
            score += 3 # draw
        elif wins.get(them) == me:
            score += 6 # we won
        score += scores[me]

    return score

def part_two():
    score = 0
    for line in data.split("\n"):
        them, end = line.split(" ")
        match end:
            case "X":
                me = loss[them]
            case "Y":
                me = ties[them]
                score += 3
            case "Z":
                me = wins[them]
                score += 6
        score += scores.get(me)
    return score

time_and_print_result("1", part_one)
time_and_print_result("2", part_two)