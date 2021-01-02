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
        if (policy.L == policy.pw[int(policy.a) - 1])
        ^ (policy.L == policy.pw[int(policy.b) - 1])
    )
)
