import re


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


def is_valid_any_field(val: str) -> bool:
    for rule in rules:
        if rule.match(int(val)):
            return True
    else:
        return False


sections = open("input").read().split("\n\n")

rules = list(map(Rule, sections[0].split("\n")))
tickets = sections[2].strip().split("\n")[1:]

error_rate = 0
for ticket in tickets:
    for val in ticket.split(","):
        if not any(rule.match(int(val)) for rule in rules):
            error_rate += int(val)
print(error_rate)
