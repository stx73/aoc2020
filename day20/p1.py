from typing import List, Set, Callable, Optional, Iterator
import math


class Tile:
    def __init__(self, tile: List[str], tile_id: int = 0):
        self.tile = tile
        self.id = tile_id
        self.edge_len = len(tile)

    def right_edge(self) -> str:
        return "".join(t[-1] for t in self.tile)

    def left_edge(self) -> str:
        return "".join(t[0] for t in self.tile)

    def top_edge(self) -> str:
        return self.tile[0]

    def bottom_edge(self) -> str:
        return self.tile[-1]

    def rotate_right(self) -> None:
        rotated = []
        for ix in range(self.edge_len):
            rotated.append(
                "".join(
                    [
                        self.tile[self.edge_len - jx - 1][ix]
                        for jx in range(self.edge_len)
                    ]
                )
            )
        self.tile = rotated

    def flip(self) -> None:
        flipped = []
        for t in self.tile[::-1]:
            flipped.append(t)
        self.tile = flipped


def check(order: List[Tile], tile: Tile, edge_size: int) -> bool:
    return (
        False
        if (
            (len(order) + 1) % edge_size != 1
            and tile.left_edge() != order[len(order) - 1].right_edge()
        )
        or (
            len(order) >= edge_size
            and tile.top_edge() != order[len(order) - edge_size].bottom_edge()
        )
        else True
    )


reassemble: List[Callable[[Tile], Optional[Tile]]] = [
    lambda tile: tile,
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.flip(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
]


def recursion(
    order: List[Tile], visited: Set[Tile], tiles: List[Tile], edge_size: int
) -> List[Tile]:
    if len(order) == len(tiles):
        return order

    result = []
    for tile in tiles:
        if tile not in visited:
            for r in reassemble:
                r(tile)
                if check(order, tile, edge_size):
                    result = recursion(
                        order + [tile], visited.union({tile}), tiles, edge_size
                    )
                    if result:
                        return result
    return result


def part1(tiles: List[Tile]) -> int:
    size = len(tiles)
    edge_size = int(math.sqrt(size))
    order = recursion([], set(), tiles, edge_size)

    upper_left = 0
    upper_right = edge_size - 1
    bottom_left = size - edge_size
    bottom_right = size - 1

    return (
        order[upper_left].id
        * order[upper_right].id
        * order[bottom_left].id
        * order[bottom_right].id
    )


def extract_data(lines: List[str]) -> Iterator[Tile]:
    tile: List[str] = []
    for line in lines + [""]:
        if "Tile" in line:
            tile_id = int(line.split()[1].strip(":"))
        elif line:
            tile += [line]
        elif tile:
            yield Tile(tile, tile_id)
            tile = []


with open("input") as input_file:
    lines = [line for line in input_file.read().splitlines()]

    print(part1(list(extract_data(lines))))
