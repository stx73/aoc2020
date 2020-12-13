from p1 import check


def main() -> int:
    with open("input", "r") as input_file:
        n = [int(line.strip()) for line in input_file.readlines()]

    invalid = check(n)

    while True:
        n2 = n.copy()
        candidates = []
        while True:
            first, n2 = n2[0], n2[1:]
            candidates.append(first)
            s = sum(candidates)
            if s == invalid:
                return min(candidates) + max(candidates)
            elif s > invalid:
                break
        n = n[1:]
    return 0


if __name__ == "__main__":
    print(main())
