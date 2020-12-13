gawk -v RS='contain|,' 1 input |
    gawk -v OFS=, '/^$/ { next } ; match($0, /^(.+) bags $/, a) { outer = a[1]; next } ; match($0, /^ ([0-9]+) (.+) bags?\.?$/, a) { how_many = a[1]; inner = a[2]; outer in arr ? arr[outer] = arr[outer] OFS inner OFS how_many : arr[outer] = inner OFS how_many } ; END { for (val in arr) print val, arr[val] }' |
    sort -t, |
    python3 <(cat <<-EOPY
import fileinput
from typing import Optional, DefaultDict, List, Tuple, Iterable, Iterator, Any
from collections import defaultdict

contained: DefaultDict[str, List[Tuple[str, int]]] = defaultdict(list)


def pairwise(iterable: Iterable[Any]) -> Iterator[Any]:
    a = iter(iterable)
    return zip(a, a)


def count_bag(bag: str) -> int:
    count = 1
    if bag in contained:
        for b, n in contained[bag]:
            count += n * count_bag(b)

    return count


def main(input_file: fileinput.FileInput) -> Optional[int]:
    for line in input_file:
        container, *content = line.strip().split(",")
        for bag, count in pairwise(content):
            contained[container].append((bag, int(count)))

    return count_bag("shiny gold") - 1


if __name__ == "__main__":
    print(main(fileinput.input()))
EOPY
)
