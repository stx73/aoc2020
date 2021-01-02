from typing import List
import re
from collections import namedtuple


Policy = namedtuple("Policy", ["a", "b", "L", "pw"])
policies: List[Policy] = []
with open("input") as input_file:
    for line in input_file.readlines():
        policies += [Policy(*re.findall(r"[^-:\s]+", line.strip()))]

print(
    sum(
        1
        for policy in policies
        if int(policy.a) <= policy.pw.count(policy.L) <= int(policy.b)
    )
)
