
csv_path = "2025\day_7_laboratories\input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

source = 'S'
splitter = '^'

source_index = lines[0].index(source)
num_cols = len(lines[0])
beam_values = [0 for _ in range(num_cols)]
beam_values[source_index] = 1

active_beam_indexes = {source_index}

num_splits = 0
for height, line in enumerate(lines[1:], start = 1):
    if splitter not in line:
        continue
    beams_to_be_removed = set()
    beams_to_be_added = set()
    for i in active_beam_indexes:
        if line[i] == splitter:  # Split beam
            beam_values[i - 1] += beam_values[i]
            beam_values[i + 1] += beam_values[i]
            beam_values[i] = 0
            beams_to_be_removed.add(i)
            beams_to_be_added.add(i - 1)
            beams_to_be_added.add(i + 1)
    active_beam_indexes -= beams_to_be_removed
    active_beam_indexes = active_beam_indexes.union(beams_to_be_added)
print(f"The particle ends up in a total of {sum(beam_values)} timelines.")