from typing import List
from typing import Set, Tuple


def run(instructions: List[str]) -> Tuple[int, int]:
    acc = 0
    n = 0
    seen: Set[int] = set()
    while n not in seen:
        seen.add(n)
        try:
            op, arg = instructions[n].split()
        except IndexError:
            break
        if op == "nop":
            n += 1
        elif op == "acc":
            acc += int(arg)
            n += 1
        else:  # jmp
            n += int(arg)
    else:
        return (1, acc)
    return (0, acc)


def main() -> int:
    with open("input", "r") as input_file:
        instructions = [line.strip() for line in input_file.readlines()]

    return run(instructions)[1]


if __name__ == "__main__":
    print(main())
