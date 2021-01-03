from typing import List


Picture = List[str]
picture: Picture = []
with open("input") as input_file:
    picture = input_file.read().rstrip().split()

print(sum(1 for y, row in enumerate(picture) if row[(3 * y) % len(row)] == "#"))
