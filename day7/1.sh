gawk -v RS='contain|,' 1 input |
    gawk -v OFS=, '/^$/ { next } ; match($0, /^(.+) bags $/, a) { outer = a[1]; next } ; match($0, /^ [0-9]+ (.+) bags?\.?$/, a) { inner = a[1]; inner in arr ? arr[inner] = arr[inner] OFS outer : arr[inner] = outer } ; END { for (val in arr) print val, arr[val] }' |
    sort -t, |
    python3 <(cat <<-EOPY
import fileinput
from typing import Optional, DefaultDict, Set
from collections import defaultdict

contained: DefaultDict[str, Set[str]] = defaultdict(set)


def count(color: str, bags_color: Set[str]) -> int:
    for bag in contained[color]:
        bags_color.add(bag)
        count(bag, bags_color)

    return len(bags_color)


def main(input_file: fileinput.FileInput) -> Optional[int]:
    for line in input_file:
        container, *content = line.strip().split(",")
        contained[container] = set(content)

    return count("shiny gold", set())


if __name__ == "__main__":
    print(main(fileinput.input()))
EOPY
)
