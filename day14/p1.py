from typing import Dict, Iterator
import re


def write_to_mem(mem: Dict[int, int], mask: str, addr: int, val: int) -> None:
    bin_str = "".join(apply_mask(mask, f"{val:0>36b}"))
    mem[addr] = int(bin_str, 2)


def apply_mask(mask: str, val: str) -> Iterator[str]:
    for v, m in zip(val, mask):
        yield v if m == "X" else m


def main() -> int:
    with open("input", "r") as input_file:
        lines = [line.strip().split(" = ") for line in input_file.readlines()]

    mem: Dict[int, int] = {}
    for var, val in lines:
        if var == "mask":
            mask = val
            continue
        m = re.match(r"mem\[(\d+)\]", var)
        if m:
            write_to_mem(mem, mask, int(m.groups()[0]), int(val))

    return sum(mem.values())


if __name__ == "__main__":
    print(main())
