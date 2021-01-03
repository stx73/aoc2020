from typing import List, Dict
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

print(sum(1 for passport in passports if required_fields.issubset(passport)))
