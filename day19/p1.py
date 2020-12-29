from typing import Dict, List
import re

sections = open("input").read().split("\n\n")

rules = dict(
    map(
        lambda line: (
            line.split(": ")[0],
            [item.split() for item in line.split(": ")[1].split("|")],
        ),
        sections[0].split("\n"),
    )
)


messages = sections[1].split("\n")


def make_pattern(rules: Dict[str, List[List[str]]], name: str) -> str:
    return (
        "("
        + "|".join(
            "".join(
                rule[1] if re.match(r'^"[ab]"$', rule) else make_pattern(rules, rule)
                for rule in sub_rules
            )
            for sub_rules in rules[name]
        )
        + ")"
    )


pattern = re.compile(make_pattern(rules, "0"))
print(sum(1 for message in messages if re.fullmatch(pattern, message)))
