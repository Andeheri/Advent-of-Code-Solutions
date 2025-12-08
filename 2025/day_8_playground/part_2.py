
import numpy as np
import random

csv_path = "2025\day_8_playground\input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

positions = [np.array([int(coordinate) for coordinate in line.split(',')]) for line in lines]

distances = []
min_distances = []
for i, pos1 in enumerate(positions[:-1]):
    min_distance = float('inf')
    for j, pos2 in enumerate(positions[i + 1:], start = i + 1):
        distance = np.sum((pos1 - pos2)**2)
        distances.append(((i, j), distance))
        if distance < min_distance:
            min_distance = distance
    min_distances.append((i, min_distance))
sorted_min_distances = sorted(min_distances, key=lambda x: x[1])


def partition(A: list, p: int, r: int) -> tuple[list, int]:
    x = A[r]  # Uses last element as pivot
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x[1]:
            i += 1
            A[i], A[j] = A[j], A[i]  # Puts element of the low side of pivot
    A[i + 1], A[r] = A[r], A[i + 1]  # Puts pivot to the right of the smaller elements
    return A, i + 1  # Returns list, indexes of elements less than or equal to pivot, and index of the pivot

def randomized_partition(A: list, p: int, r: int) -> tuple[list, list, int]:
    q = random.randint(p, r)  # Pick random pivot
    A[q], A[r] = A[r], A[q]  # Put pivot at the end, so that partition uses it
    return partition(A, p, r)


def random_select_all(A: list, p: int, r: int, i: int, rest_A: list[np.ndarray | None] = []) -> list:
    if p >= r:
        return rest_A + [A[p]]  # Base case if i == 0
    A, q = randomized_partition(A, p, r)  # Partition the list randomly
    k = q - p + 1 + len(rest_A)  # Number of elements on the low side of the pivot including pivot
    if k == i:  # If we happen to have chosen a pivot that is in the place of the ith order statistic
        return rest_A + A[p:q + 1]
    elif i < k:  # We're on the right track
        return random_select_all(A, p, q - 1, i, rest_A)
    else:  # i > k
        return random_select_all(A, q + 1, r, i, rest_A + A[p:q + 1])


i = 5000  # Magic number found by trial and error


shortest_pairs = random_select_all(distances, 0, len(distances) - 1, i)

groups = []
for (i, j), _ in shortest_pairs:
    hit = [g for g in groups if i in g or j in g]

    if not hit:
        # new group
        groups.append({i, j})
    else:
        # merge all hit groups plus i, j
        merged = {i, j}
        for g in hit:
            merged |= g
            groups.remove(g)
        groups.append(merged)

# Get all indices that are in groups
in_groups = set()
for group in groups:
    in_groups |= group

# Get all indices not in groups
not_in_groups = set(range(len(positions))) - in_groups
print(f"Indices in groups: {len(in_groups)}")
print(f"Indices not in groups: {len(not_in_groups)}")

# Find closest pair where one is in groups and one is not
min_distance = float('inf')
closest_pair = None

for idx_in in in_groups:
    for idx_out in not_in_groups:
        distance = np.sum((positions[idx_in] - positions[idx_out])**2)
        if distance < min_distance:
            min_distance = distance
            closest_pair = (idx_in, idx_out)

print(f"Closest pair (in group, not in group): {closest_pair}")
print(f"Distance: {min_distance}")
print(f"Point in group: {positions[closest_pair[0]]}")
print(f"Point not in group: {positions[closest_pair[1]]}")
print()
if len(not_in_groups) == 1:
    print(f"Result: {positions[closest_pair[1]][0] * positions[closest_pair[0]][0]}")


