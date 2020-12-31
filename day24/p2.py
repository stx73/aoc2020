from collections import Counter
from typing import Tuple


def parse(s: str) -> Tuple[int, int]:
    q, r = 0, 0
    while s.strip():
        if s[0] == "w":
            q, s = q - 1, s[1:]
        elif s[0] == "e":
            q, s = q + 1, s[1:]
        elif s[0:2] == "se":
            r, s = r + 1, s[2:]
        elif s[0:2] == "nw":
            r, s = r - 1, s[2:]
        elif s[0:2] == "sw":
            q, r, s = q - 1, r + 1, s[2:]
        elif s[0:2] == "ne":
            q, r, s = q + 1, r - 1, s[2:]
    return q, r


with open("input", "r") as input_file:
    tiles = [line for line in input_file.readlines()]

cnt = Counter(map(parse, tiles))

maximum = max(max(abs(q), abs(r)) for q, r in cnt.keys())
black, new = {k for k, v in cnt.items() if v % 2 == 1}, set()

for round in range(100):
    for q in range(-(round + 1) - maximum, maximum + (round + 1) + 1):
        for r in range(-(round + 1) - maximum, maximum + (round + 1) + 1):
            adj = sum(
                1
                for dq, dr in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1)]
                if (q + dq, r + dr) in black
            )

            if (q, r) in black and 1 <= adj <= 2 or (q, r) not in black and adj == 2:
                new.add((q, r))
    black, new = new, set()
print(len(black))
