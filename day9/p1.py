from typing import List


PREAMBLE = 25


def found(n: List[int]) -> bool:
    preamble = n[:PREAMBLE]
    for p in preamble:
        if n[PREAMBLE] - p in preamble:
            return True
    return False


def check(n: List[int]) -> int:
    while True:
        if found(n):
            n = n[1:]
        else:
            break
    return n[PREAMBLE]


def main() -> int:
    with open("input", "r") as input_file:
        n = [int(line.strip()) for line in input_file.readlines()]

    return check(n)


if __name__ == "__main__":
    print(main())
