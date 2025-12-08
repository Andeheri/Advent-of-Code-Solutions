
import numpy as np
import random

csv_path = "2025\day_8_playground\input.csv"
delimiter = "\n"

with open(csv_path, "r") as file:
    lines = file.read().strip().split(delimiter)

positions = [np.array([int(coordinate) for coordinate in line.split(',')]) for line in lines]

distances = []
for i, pos1 in enumerate(positions[:-1]):
    for j, pos2 in enumerate(positions[i + 1:], start = i + 1):
        distances.append(((i, j), np.sum((pos1 - pos2)**2)))


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


i = 1000
shortest_pairs = random_select_all(distances, 0, len(distances) - 1, i)

print(shortest_pairs)
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

for i, group in enumerate(groups):
    print(f"Group {i}")
    for index in group:
        print(positions[index])
    print()

size_groups = sorted(len(group) for group in groups)
print(f"Group sizes: {size_groups}")
print(f"Result = {size_groups[-1] * size_groups[-2] * size_groups[-3]}")

