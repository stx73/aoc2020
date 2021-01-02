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

    def remove_edge(self) -> None:
        removed = []
        for ix in range(1, self.edge_len - 1):
            removed.append(
                "".join([self.tile[ix][jx] for jx in range(1, self.edge_len - 1)])
            )
        self.tile = removed


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


def form_pic(order: List[Tile]) -> Tile:
    tile_edge_len = order[0].edge_len - 2
    num_of_tile_in_each_edge = int(math.sqrt(len(order)))

    pic_edge_len = tile_edge_len * num_of_tile_in_each_edge
    pic = ["" for _ in range(pic_edge_len)]

    for ix, tile in enumerate(order):
        tile.remove_edge()
        for jx, t in enumerate(tile.tile):
            pic[(ix // num_of_tile_in_each_edge) * tile_edge_len + jx] += t

    return Tile(pic)


def search(target: List[str], pic: Tile) -> int:
    target_row_len = len(target)
    target_column_len = len(target[0])
    pic_row_len = len(pic.tile)
    pic_column_len = len(pic.tile[0])

    count = 0
    for ix in range(pic_row_len - target_row_len + 1):
        for jx in range(pic_column_len - target_column_len + 1):
            valid = True
            for kx in range(target_row_len):
                for lx in range(target_column_len):
                    if (target[kx][lx] != " ") and target[kx][lx] != pic.tile[ix + kx][
                        jx + lx
                    ]:
                        valid = False
                        break
                if valid == False:
                    break
            if valid:
                count += 1

    return count


def search_pic(target: List[str], pic: Tile) -> int:
    for r in reassemble:
        r(pic)
        count = search(target, pic)
        if count:
            return count

    return 0


def part2(tiles: List[Tile]) -> int:
    order = recursion([], set(), tiles, int(math.sqrt(len(tiles))))
    pic = form_pic(order)
    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    return search_pic(["#"], pic) - search_pic(sea_monster, pic) * 15


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

    print(part2(list(extract_data(lines))))
