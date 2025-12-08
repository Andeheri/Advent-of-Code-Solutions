
import random
import numpy as np


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
    print(f"random select called with A={A}, p={p} and r={r}, rest_A={rest_A}")
    if p >= r:
        return rest_A + [A[p]]  # Base case if i == 0
    A, q = randomized_partition(A, p, r)  # Partition the list randomly
    print(f"After partition A={A} and q={q}")
    k = q - p + 1 + len(rest_A)  # Number of elements on the low side of the pivot including pivot
    print(f"k={k} and i={i}")
    if k == i:  # If we happen to have chosen a pivot that is in the place of the ith order statistic
        return rest_A + A[p:q + 1]
    elif i < k:  # We're on the right track
        return random_select_all(A, p, q - 1, i, rest_A)
    else:  # i > k
        return random_select_all(A, q + 1, r, i, rest_A + A[p:q + 1])


A = [5, 1, 3, 7, 4]  # Partition should return [1, 3, 4, x, x], 2
A = [(i, val) for i, val in enumerate(A)]
print(A)
i = 4
print(A)
order_statistics = random_select_all(A, 0, len(A) - 1, i)
print(order_statistics)