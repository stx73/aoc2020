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

print(sum(value % 2 for value in Counter(map(parse, tiles)).values()))
