from typing import List
from p1 import run


def try_run(instructions: List[str]) -> int:
    op_map = {"nop": "jmp", "jmp": "nop"}
    for n, instr in enumerate(instructions):
        op, arg = instr.split()
        if op in op_map:
            temp_instructions = instructions.copy()
            temp_instructions[n] = f"{op_map[op]} {arg}"
            acc = run(temp_instructions)
            if acc[0] == 0:
                break
    return acc[1]


def main() -> int:
    with open("input", "r") as input_file:
        instructions = [line.strip() for line in input_file.readlines()]

    return try_run(instructions)


if __name__ == "__main__":
    print(main())
