from typing import Iterator, List, Callable
import copy


def get_adjacent(
    seat_layout: List[List[str]], x: int, y: int, W: int, H: int
) -> Iterator[str]:
    for yy in range(max(0, y - 1), min(H, y + 2)):
        for xx in range(max(0, x - 1), min(W, x + 2)):
            if xx == x and yy == y:
                continue
            yield seat_layout[yy][xx]


def find_occupied_seats(seat_layout: List[List[str]]) -> int:
    W, H = len(seat_layout[0]), len(seat_layout)

    becomes_occupied: Callable[[int, int], bool] = lambda x, y: "#" not in get_adjacent(
        seat_layout, x, y, W, H
    )
    becomes_empty: Callable[[int, int], bool] = (
        lambda x, y: list(get_adjacent(seat_layout, x, y, W, H)).count("#") >= 4
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
