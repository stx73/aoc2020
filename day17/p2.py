from typing import DefaultDict, Tuple, Set
from itertools import product
from collections import defaultdict

NUM_CYCLES = 6


active: Set[Tuple[int, ...]] = set()
with open("input", "r") as input_file:
    for y, line in enumerate(input_file.readlines()):
        for x, activity in enumerate(line.strip()):
            if activity == "#":
                active.add((x, y) + 2 * (0,))

for cycle in range(NUM_CYCLES):
    neighbours: DefaultDict[Tuple[int, ...], int] = defaultdict(int)
    for coord in active:
        for d in product([-1, 0, 1], repeat=4):
            if d != (0, 0, 0, 0):
                neighbours[tuple([i + di for i, di in zip(coord, d)])] += 1

    newactive = set()
    for neigh_pos, neighbour_count in neighbours.items():
        if (
            neigh_pos in active
            and (neighbour_count == 2 or neighbour_count == 3)
            or neigh_pos not in active
            and neighbour_count == 3
        ):
            newactive.add(neigh_pos)

    active = newactive

print(len(active))
