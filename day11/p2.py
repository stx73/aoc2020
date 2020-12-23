from typing import List, Callable, Tuple
import copy


def move(x: int, y: int, dir: str) -> Tuple[int, int]:
    if dir == "l":
        return (x - 1, y)
    elif dir == "r":
        return (x + 1, y)
    elif dir == "u":
        return (x, y - 1)
    elif dir == "d":
        return (x, y + 1)
    elif dir == "ul":
        return (x - 1, y - 1)
    elif dir == "ur":
        return (x + 1, y - 1)
    elif dir == "dl":
        return (x - 1, y + 1)
    else:  # dir == "dr":
        return (x + 1, y + 1)


def get_in_sight(
    seat_layout: List[List[str]], x: int, y: int, W: int, H: int
) -> List[str]:
    res = []

    for dir in ["l", "r", "u", "d", "ul", "ur", "dl", "dr"]:
        xx, yy = move(x, y, dir)

        while xx >= 0 and xx < W and yy >= 0 and yy < H:
            if seat_layout[yy][xx] != ".":
                res.append(seat_layout[yy][xx])
                break
            else:
                xx, yy = move(xx, yy, dir)

    return res


def find_occupied_seats(seat_layout: List[List[str]]) -> int:
    W, H = len(seat_layout[0]), len(seat_layout)

    becomes_occupied: Callable[[int, int], bool] = lambda x, y: "#" not in get_in_sight(
        seat_layout, x, y, W, H
    )
    becomes_empty: Callable[[int, int], bool] = (
        lambda x, y: list(get_in_sight(seat_layout, x, y, W, H)).count("#") >= 5
    )

    changed = True
    while changed:
        changed = False
        new_seat_layout = copy.deepcopy(seat_layout)

        for y in range(H):
            for x in range(W):
                seat = seat_layout[y][x]
                if seat == "L" and becomes_occupied(x, y):
                    new_seat_layout[y][x] = "#"
                    changed = True
                elif seat == "#" and becomes_empty(x, y):
                    new_seat_layout[y][x] = "L"
                    changed = True

        seat_layout = new_seat_layout

    return sum(row.count("#") for row in seat_layout)


def main() -> int:
    with open("input", "r") as input_file:
        seat_layout = [
            list(line) for line in [line.strip() for line in input_file.readlines()]
        ]

    return find_occupied_seats(seat_layout)


if __name__ == "__main__":
    print(main())
