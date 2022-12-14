from typing import Dict, List, Tuple

FILE_NAME: str = "day_2/input.txt"

rounds: List[Tuple[str, str]] = []

def parse_data(file_name: str):
  with open(file_name) as f:
    for line in f:
      game_round = line.strip("\n").split(" ")
      rounds.append(game_round)

# part 1
score_map: Dict[str, int] = {
  "X": 1,
  "Y": 2,
  "Z": 3,
}

win_condition: Dict[str, str] = {
  "X": "C",
  "Y": "A",
  "Z": "B",
}

draw_condition: Dict[str, str] = {
  "X": "A",
  "Y": "B",
  "Z": "C",
}

WIN = 6
DRAW = 3

def calc_score_part1(rounds: List[Tuple[str, str]]) -> int:
  score = 0
  for r in rounds:
    opp = r[0]
    you = r[1]
    if draw_condition[you] == opp:
      score += DRAW
    elif win_condition[you] == opp:
      score += WIN
    score += score_map[you]
  return score

parse_data(FILE_NAME)

score = calc_score_part1(rounds)
print(score)

# part 2
win_condition = ""

