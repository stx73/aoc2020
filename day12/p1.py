from typing import List, Tuple

CARDINALS = ["N", "E", "S", "W"]
ACTIONS_MAP = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def rotate(amount: int, facing: str) -> str:
    index = (CARDINALS.index(facing) + amount // 90) % 4
    return CARDINALS[index]


def move(amount: int, direction: str, x: int, y: int) -> Tuple[int, int]:
    xx, yy = ACTIONS_MAP[direction]
    x += amount * xx
    y += amount * yy
    return x, y


def Manhattan_dist(actions: List[str]) -> int:
    facing = "E"
    x, y = 0, 0

    for line in actions:
        action, amount = line[0], int(line[1:])

        if action == "R":
            facing = rotate(amount, facing)
        elif action == "L":
            facing = rotate(-amount, facing)
        elif action == "F":
            x, y = move(amount, facing, x, y)
        else:
            x, y = move(amount, action, x, y)

    return abs(x) + abs(y)


def main() -> int:
    with open("input", "r") as input_file:
        actions = [line.strip() for line in input_file.readlines()]

    return Manhattan_dist(actions)


if __name__ == "__main__":
    print(main())
