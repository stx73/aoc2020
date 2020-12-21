from p1 import find_distribution
from itertools import groupby
from functools import reduce
import operator


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


def main() -> int:
    with open("input", "r") as input_file:
        joltage_ratings = sorted(int(line.strip()) for line in input_file.readlines())

    jolts = find_distribution(joltage_ratings)
    jolt_groups = [
        (key, len(list(group))) for key, group in groupby(jolts, key=lambda x: x != 3)
    ]
    return reduce(operator.mul, (fib(v + 2) - 1 for k, v in jolt_groups if k))


if __name__ == "__main__":
    print(main())
