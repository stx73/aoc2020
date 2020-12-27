def main() -> int:
    with open("input", "r") as input_file:
        earliest = int(input_file.readline().strip())
        ids = [int(id) for id in input_file.readline().strip().split(",") if id != "x"]

    res = min((id - (earliest % id), id) for id in ids)
    return res[0] * res[1]


if __name__ == "__main__":
    print(main())
