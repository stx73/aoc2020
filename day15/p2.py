def main() -> int:
    with open("input", "r") as input_file:
        numbers = list(map(int, input_file.readline().strip().split(",")))

    cache = {n: i for i, n in enumerate(numbers[:-1])}

    STOP = 30000000
    while len(numbers) < STOP:
        last_number = numbers[-1]
        next_number = (
            len(numbers) - 1 - cache[last_number] if last_number in cache else 0
        )
        cache[last_number] = len(numbers) - 1
        numbers += [next_number]

    return numbers[-1]


if __name__ == "__main__":
    print(main())
