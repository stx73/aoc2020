from typing import List
from functools import reduce


def move(cups: List[int]) -> List[int]:
    current, picked = cups[0], cups[1:4]
    remain = cups[4:] + [current]

    while True:
        current = current - 1 if current - 1 >= min(cups) else max(cups)
        if current in remain:
            break

    dest = remain.index(current)
    cups = remain[: dest + 1] + picked + remain[dest + 1 :]
    return cups


cups = list(map(int, "368195742"))
cups = reduce(lambda x, y: move(x), range(100), cups)

print(
    "".join(
        map(
            str,
            (cups[cups.index(1) + 1 :] if cups[-1] != 1 else [])
            + cups[: cups.index(1)],
        )
    )
)
