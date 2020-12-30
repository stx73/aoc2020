import re
from typing import Dict, Set


with open("input", "r") as input_file:
    foods = [line.strip() for line in input_file.readlines()]

allergens: Dict[str, Set[str]] = {}
for food in foods:
    m = re.match(r"(.*) \(contains (.+)\)$", food)
    if m:
        ingredients = m.groups()[0].split(" ")

        for allergen in m.groups()[1].split(", "):
            if allergen in allergens:
                allergens[allergen].intersection_update(set(ingredients))
            else:
                allergens[allergen] = set(ingredients)


while not all([len(v) == 1 for v in allergens.values()]):
    L = sorted(allergens, key=lambda allergen: len(allergens[allergen]))
    for n, allergen in enumerate(L):
        if len(allergens[allergen]) > 1:
            break
        for allergen2 in L[n + 1 :]:
            allergens[allergen2].difference_update(allergens[allergen])

print(",".join([allergens[key].pop() for key in sorted(allergens)]))
