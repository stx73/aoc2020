import re
from collections import Counter
import typing
from typing import Dict, Set
from itertools import chain


with open("input", "r") as input_file:
    foods = [line.strip() for line in input_file.readlines()]

ingredients_count: typing.Counter[str] = Counter()
allergens: Dict[str, Set[str]] = {}
for food in foods:
    m = re.match(r"(.*) \(contains (.+)\)$", food)
    if m:
        ingredients = m.groups()[0].split(" ")

        ingredients_count.update(ingredients)
        for allergen in m.groups()[1].split(", "):
            if allergen in allergens:
                allergens[allergen].intersection_update(set(ingredients))
            else:
                allergens[allergen] = set(ingredients)

ingredients_without_allergens = set(ingredients_count) - set(chain(*allergens.values()))
print(
    sum(ingredients_count[ingredient] for ingredient in ingredients_without_allergens)
)
