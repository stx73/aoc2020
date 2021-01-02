with open("input") as input_file:
    nums = {int(line.strip()) for line in input_file.readlines()}

print(next(x * y for x in nums for y in nums & {2020 - x} if x != y))
