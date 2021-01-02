from itertools import combinations


with open("input") as input_file:
    nums = {int(line.strip()) for line in input_file.readlines()}

print(
    next(
        x * y * z
        for x, y in combinations(nums, 2)
        for z in nums & {2020 - x - y}
        if x != z != y
    )
)
