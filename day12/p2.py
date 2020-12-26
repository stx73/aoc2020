from typing import List, Tuple

ACTIONS_MAP = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def rotate_waypoint(amount: int, x: int, y: int, X: int, Y: int) -> Tuple[int, int]:
    dx, dy = X - x, Y - y
    for i in range(amount // 90):
        tmp = dx
        dx = -dy
        dy = tmp
    X = x + dx
    Y = y + dy
    return X, Y


def move_ship(amount: int, x: int, y: int, X: int, Y: int) -> Tuple[int, int, int, int]:
    dx, dy = X - x, Y - y
    x += dx * amount
    y += dy * amount
    X = x + dx
    Y = y + dy
    return x, y, X, Y


def move_waypoint(amount: int, action: str, X: int, Y: int) -> Tuple[int, int]:
    xx, yy = ACTIONS_MAP[action]
    X += amount * xx
    Y += amount * yy
    return X, Y


def Manhattan_dist(actions: List[str]) -> int:
    x, y = 0, 0
    X, Y = 10, -1

    for line in actions:
        action, amount = line[0], int(line[1:])

        if action == "R":
            X, Y = rotate_waypoint(amount, x, y, X, Y)
        elif action == "L":
            X, Y = rotate_waypoint(360 - amount, x, y, X, Y)
        elif action == "F":
            x, y, X, Y = move_ship(amount, x, y, X, Y)
        else:
            X, Y = move_waypoint(amount, action, X, Y)

    return abs(x) + abs(y)


def main() -> int:
    with open("input", "r") as input_file:
        actions = [line.strip() for line in input_file.readlines()]

    return Manhattan_dist(actions)


if __name__ == "__main__":
    print(main())
