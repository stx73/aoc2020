from typing import List


sections: List[str] = []
ID = int
seats: List[ID] = []
with open("input") as input_file:
    sections += input_file.read().rstrip().split()
    seats = list(
        map(
            lambda seat: ID(seat.translate(str.maketrans("FLBR", "0011")), base=2),
            sections,
        )
    )

print(max(seats))
