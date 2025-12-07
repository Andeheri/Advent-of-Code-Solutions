
csv_path = "2025\day_7_laboratories\input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

source = 'S'
splitter = '^'

height = 0
beam_indexes = {lines[0].index(source)}


def find_all_char_indexes(string: str, search_char: str) -> list[int]:
    return {i for i, char in enumerate(string) if char == search_char}

num_splits = 0
for height in range(1, len(lines)):
    try:
        split_indexes = find_all_char_indexes(lines[height], splitter)
        if not split_indexes:
            continue
        beams_to_be_split = beam_indexes.intersection(split_indexes)
        num_splits += len(beams_to_be_split)
        # Split beams
        new_beam_indexes = {j
                    for i in beams_to_be_split
                    for j in (i - 1, i + 1)}
        # Merge with unsplit beams
        beam_indexes -= beams_to_be_split
        beam_indexes = beam_indexes.union(new_beam_indexes)
    except ValueError:
        continue
print(num_splits)