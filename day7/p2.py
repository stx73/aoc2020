from typing import List, Tuple, Dict
import re
from functools import lru_cache


Bag = str
BagRules = Dict[Bag, Dict[Bag, int]]


def parse_bag_rule(line: str) -> Tuple[Bag, Dict[Bag, int]]:
    line = re.sub(" bags?|[.]", "", line)
    outer, inner = line.split(" contain ")
    return outer, dict(map(parse_inner, inner.split(", ")))


def parse_inner(text: str) -> Tuple[Bag, int]:
    n, bag = text.split(maxsplit=1)
    return bag, 0 if n == "no" else int(n)


sections: List[str] = []
rules: Dict[Bag, Dict[Bag, int]] = {}
with open("input") as input_file:
    sections += input_file.read().rstrip().split("\n")
    rules = dict(map(parse_bag_rule, sections))


def num_contained_in(
    rules: Dict[Bag, Dict[Bag, int]], target: str = "shiny gold"
) -> int:
    return sum(
        n + n * num_contained_in(rules, inner)
        for inner, n in rules[target].items()
        if n > 0
    )


print(num_contained_in(rules))
