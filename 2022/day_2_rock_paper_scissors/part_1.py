

csv_path = "2022\day_2_rock_paper_scissors\input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)


class Move:
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

# result = result_matrix[your move][opponents move] (-1: Lose, 0: Tie, 1: Win)
result_matrix = [[0, -1, 1],
                 [1, 0, -1],
                 [-1, 1, 0]]


