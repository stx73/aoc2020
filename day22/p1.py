import re
from typing import Iterator, List, Tuple


with open("input", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]


def parse_deck() -> Iterator[List[int]]:
    deck: List[int] = []
    for line in input + [""]:
        if not line:
            yield list(reversed(deck))
            deck = []

        m = re.match(r"\d+$", line)
        if not m:
            continue
        deck += [int(line)]


def play_game(deck1: List[int], deck2: List[int]) -> Tuple[List[int], List[int]]:
    while len(deck1) > 0 and len(deck2) > 0:
        card1, card2 = deck1.pop(), deck2.pop()
        if card1 > card2:
            deck1.insert(0, card1)
            deck1.insert(0, card2)
        else:
            deck2.insert(0, card2)
            deck2.insert(0, card1)

    return deck1, deck2


deck1, deck2 = parse_deck()
deck1, deck2 = play_game(deck1, deck2)

print(sum(card * (n + 1) for n, card in enumerate(deck1 if deck1 else deck2)))
