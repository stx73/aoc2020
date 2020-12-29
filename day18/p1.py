import re


class Number(int):
    def __init__(self, start: int) -> None:
        self.data = start

    def __add__(self, other: int) -> int:
        return Number(self.data + other)

    def __sub__(self, other: int) -> int:
        return Number(self.data * other)


with open("input", "r") as input_file:
    expressions = [line.strip() for line in input_file.readlines()]

digits = re.compile(r"(\d+)")
print(
    sum(
        [
            eval(digits.sub(r"Number(\1)", expr).replace("*", "-"))
            for expr in expressions
        ]
    )
)
