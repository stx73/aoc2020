from typing import List, Dict, Callable
import re


Passport = dict
sections: List[str] = []
passports: List[Dict[str, str]] = []
with open("input") as input_file:
    sections += input_file.read().rstrip().split("\n\n")
    passports = list(
        map(lambda text: Passport(re.findall(r"([a-z]+):([^\s]+)", text)), sections)
    )

required_fields = {"byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"}

field_validator = dict(
    byr=lambda v: 1920 <= int(v) <= 2002,
    iyr=lambda v: 2010 <= int(v) <= 2020,
    eyr=lambda v: 2020 <= int(v) <= 2030,
    hcl=lambda v: re.match("#[0-9a-f]{6}$", v),
    ecl=lambda v: re.match("(amb|blu|brn|gry|grn|hzl|oth)$", v),
    pid=lambda v: re.match("[0-9]{9}$", v),
    hgt=lambda v: (
        (v.endswith("cm") and 150 <= int(v[:-2]) <= 193)
        or (v.endswith("in") and 59 <= int(v[:-2]) <= 76)
    ),
)
print(
    sum(
        1
        for passport in passports
        if all(
            field in passport and field_validator[field](passport[field])
            for field in required_fields
        )
    )
)
