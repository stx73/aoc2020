from typing import List


sections: List[str] = []
Group = List[str]
groups: List[Group] = []
with open("input") as input_file:
    sections += input_file.read().rstrip().split("\n\n")
    groups = list(map(lambda text: text.splitlines(), sections))

print(sum(len(set.intersection(*map(lambda x: set(x), group))) for group in groups))
