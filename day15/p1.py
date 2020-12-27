def main() -> int:
    with open("input", "r") as input_file:
        numbers = list(map(int, input_file.readline().strip().split(",")))

    STOP = 2020
    while len(numbers) < STOP:
        last_number = numbers[-1]
        next_number = (
            numbers[:-1][::-1].index(last_number) + 1
            if last_number in numbers[:-1]
            else 0
        )
        numbers += [next_number]

    return numbers[-1]


if __name__ == "__main__":
    print(main())
