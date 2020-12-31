from typing import Tuple, Dict
from functools import reduce


def move(circle: Dict[int, int], current: int) -> Tuple[Dict[int, int], int]:
    picked = [0] * 3
    next = circle[current]
    for n in range(3):
        picked[n] = next
        next = circle[next]
    circle[current] = next

    while True:
        current = current - 1 if current - 1 >= MIN else MAX
        if current not in picked:
            break

    tmp = circle[current]
    circle[current] = picked[0]
    circle[picked[2]] = tmp

    return circle, next


cups = list(map(int, "368195742"))
MIN, MAX = min(cups), 1000000
cups += [n for n in range(max(cups) + 1, MAX + 1)]


circle = {}
for n in range(len(cups)):
    if n == len(cups) - 1:
        circle[cups[n]] = cups[0]
    else:
        circle[cups[n]] = cups[n + 1]


circle, current = reduce(lambda x, y: move(*x), range(10000000), (circle, cups[0]))
print(circle[1] * circle[circle[1]])
