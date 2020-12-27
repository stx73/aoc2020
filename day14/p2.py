from typing import Dict, Iterator
import re


def decode(mem: Dict[int, int], mask: str, addr: int, val: int) -> None:
    bin_addr = "".join(apply_mask(mask, f"{addr:0>36b}"))
    write_to_mem(mem, mask, bin_addr, val)


def write_to_mem(mem: Dict[int, int], mask: str, bin_addr: str, val: int) -> None:
    if "X" not in bin_addr:
        mem[int(bin_addr, 2)] = val
    else:
        x = bin_addr.index("X")
        write_to_mem(mem, mask, bin_addr[:x] + "0" + bin_addr[x + 1 :], val)
        write_to_mem(mem, mask, bin_addr[:x] + "1" + bin_addr[x + 1 :], val)


def apply_mask(mask: str, val: str) -> Iterator[str]:
    for v, m in zip(val, mask):
        yield v if m == "0" else m


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
            decode(mem, mask, int(m.groups()[0]), int(val))

    return sum(mem.values())


if __name__ == "__main__":
    print(main())
