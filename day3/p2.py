from typing import List


Picture = List[str]
picture: Picture = []
with open("input") as input_file:
    picture = input_file.read().rstrip().split()


def t(dx: int, dy: int) -> int:
    return sum(
        1 for y, row in enumerate(picture[::dy]) if row[(dx * y) % len(row)] == "#"
    )


print(t(1, 1) * t(3, 1) * t(5, 1) * t(7, 1) * t(1, 2))
