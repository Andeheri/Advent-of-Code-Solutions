
csv_path = "day_5_cafeteria/input.csv"
delimiter = "\n"

# Read csv file
with open(csv_path, 'r') as file:
    data = file.read().strip().split(delimiter)
split_index = data.index("")
ingredient_ID_ranges, available_ingredient_IDs = data[:split_index], data[split_index+1:]

# Convert to appropriate types
ingredient_ID_ranges = [tuple(map(int, item.split("-"))) for item in ingredient_ID_ranges]
available_ingredient_IDs = list(map(int, available_ingredient_IDs))
print(ingredient_ID_ranges, available_ingredient_IDs)

# Sort ID ranges after the first item of the tuple
ingredient_ID_ranges.sort(key=lambda x: x[0])
print(f"\nSorted ingredient ID ranges: \n{len(ingredient_ID_ranges)}\n")

# Merge ranges
temp_ingredient_ID_ranges = []
i = 0
len_ID_ranges = len(ingredient_ID_ranges)
while i < len_ID_ranges:
    ingredient_ID_range = ingredient_ID_ranges[i]
    if i != len_ID_ranges - 1:
        for j in range(i + 1, len_ID_ranges):
            next_ingredient_ID_range = ingredient_ID_ranges[j]
            if next_ingredient_ID_range[0] <= ingredient_ID_range[1] <= next_ingredient_ID_range[1]:
                # Merge ranges
                ingredient_ID_range = (ingredient_ID_range[0], next_ingredient_ID_range[1])
            else:
                j -= 1
                break
        i = j + 1
    else:
        i += 1
    temp_ingredient_ID_ranges.append(ingredient_ID_range)
ingredient_ID_ranges = temp_ingredient_ID_ranges

print(f"Merged ingredient ID ranges: \n{len(ingredient_ID_ranges)}\n") 

num_fresh_ingredients = 0
for ingredient_ID in available_ingredient_IDs:
    for (ingredient_ID_min, ingredient_ID_max) in ingredient_ID_ranges:
        if ingredient_ID_min <= ingredient_ID <= ingredient_ID_max:
            num_fresh_ingredients += 1
            break

print(f"Number of fresh ingredients: {num_fresh_ingredients}")