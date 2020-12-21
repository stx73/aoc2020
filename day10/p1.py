from typing import List


def find_distribution(joltage_ratings: List[int]) -> List[int]:
    return (
        [joltage_ratings[0]]
        + [b - a for a, b in zip(joltage_ratings, joltage_ratings[1:])]
        + [3]
    )


def main() -> int:
    with open("input", "r") as input_file:
        joltage_ratings = sorted(int(line.strip()) for line in input_file.readlines())

    jolts = find_distribution(joltage_ratings)
    return jolts.count(1) * jolts.count(3)


if __name__ == "__main__":
    print(main())
