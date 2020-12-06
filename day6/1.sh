gawk -v RS='' -v FS='[ \t\n]' -v OFS=, '{ $1 = $1 } ; 1' input | python3 <(cat <<-EOPY
import fileinput
from typing import Optional


def main(input_file: fileinput.FileInput) -> Optional[int]:
    cnt = 0
    for line in input_file:
        cnt += len(set("".join(line.strip().split(","))))

    return cnt


if __name__ == "__main__":
    print(main(fileinput.input()))
EOPY
)
