def main() -> int:
    with open("input", "r") as input_file:
        _ = input_file.readline()
        fields = input_file.readline().strip().split(",")

    ids = {n: int(id) for n, id in enumerate(fields) if id != "x"}
    n = 0
    s = 1
    for m, bus_id in ids.items():
        while (n + m) % bus_id:
            n += s
        s *= bus_id
    return n


if __name__ == "__main__":
    print(main())
