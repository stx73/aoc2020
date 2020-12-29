import re
from typing import List


rule_re = re.compile(r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")


class Rule:
    def __init__(self, rule: str) -> None:
        m = re.findall(rule_re, rule)[0]
        self.name = m[0]
        self.valid_ranges = [
            range(int(m[1]), int(m[2]) + 1),
            range(int(m[3]), int(m[4]) + 1),
        ]

    def match(self, val: int) -> bool:
        return any([val in r for r in self.valid_ranges])


def is_ticket_valid(ticket: List[int]) -> bool:
    for val in ticket:
        if not any(rule.match(int(val)) for rule in rules):
            return False
    else:
        return True


sections = open("input").read().split("\n\n")

rules = list(map(Rule, sections[0].split("\n")))
my_ticket = list(map(int, sections[1].split("\n")[1].split(",")))
tickets = list(
    filter(
        is_ticket_valid,
        [
            list(map(int, ticket.split(",")))
            for ticket in sections[2].strip().split("\n")[1:]
        ],
    )
)

candidates = {}
for rule in rules:
    candidates[rule.name] = [False] * len(rules)
    for idx in range(len(rules)):
        valid = True
        for ticket in tickets:
            if not rule.match(ticket[idx]):
                valid = False
                break
        candidates[rule.name][idx] = valid

found = {}
while True:
    for rule_name, occurency in candidates.items():
        if occurency.count(True) == 1:
            del candidates[rule_name]
            found[rule_name] = occurency.index(True)

            for rule_name in candidates:
                candidates[rule_name][occurency.index(True)] = False

            break
    else:
        break

product = 1
for rule_name in found:
    m = re.match(r"^departure", rule_name)
    if m:
        product *= my_ticket[found[rule_name]]
print(product)
