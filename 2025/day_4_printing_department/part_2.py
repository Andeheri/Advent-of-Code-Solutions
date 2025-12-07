
import numpy as np

csv_path = "day_4_printing_department/input.csv"
delimiter = "\n"

with open(csv_path, 'r') as file:
    lines = file.read().strip().split(delimiter)

# Convert symbols to 1's and 0's
symbol = '@'
new_lines = []
for line in lines:
    new_line = []
    for char in line:
        new_line.append(1 if char == symbol else 0)
    new_lines.append(new_line)
lines = np.array(new_lines)

# Convert data to matrix
num_columns = len(lines[0])
num_rows = len(lines)

# Data is padded with zeros
data = np.zeros((num_rows + 2, num_columns + 2))

data[1:-1,1:-1] = lines  # Lines are surrounded by zeros

kernel = np.array([[1, 1, 1], 
                   [1, 0, 1],
                   [1, 1, 1]])
total_number_rolls = 0
iteration_number = 0
while True:
    iteration_number += 1
    print(f"Iteration {iteration_number}")
    removed_rolls = 0
    for x in range(num_columns):
        for y in range(num_rows):
            if data[y + 1, x + 1]:
                patch_data = data[y:y + 3, x:x + 3]
                if np.sum(patch_data * kernel) < 4:
                    removed_rolls += 1
                    data[y + 1, x + 1] = 0
    if removed_rolls == 0:
        break
    total_number_rolls += removed_rolls

print(f"The number of accesible rolls are: {total_number_rolls}")