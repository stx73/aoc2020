import re
from typing import Iterator, List, Tuple, Dict


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


def play_game(deck1: List[int], deck2: List[int]) -> Tuple[int, List[int], List[int]]:
    prev_rounds: Dict[str, List[str]] = {}

    while len(deck1) > 0 and len(deck2) > 0:
        h1, h2 = " ".join(str(card) for card in deck1), " ".join(
            str(card) for card in deck2
        )
        if h1 in prev_rounds:
            if h2 in prev_rounds[h1]:
                return (1, deck1, deck2)
            else:
                prev_rounds[h1].append(h2)
        else:
            prev_rounds[h1] = [h2]

        card1, card2 = deck1.pop(), deck2.pop()
        if card1 > len(deck1) or card2 > len(deck2):
            winner = 1 if card1 > card2 else 2
        else:
            winner, _, _ = play_game(deck1[-card1:], deck2[-card2:])

        if winner == 1:
            deck1.insert(0, card1)
            deck1.insert(0, card2)
        else:
            deck2.insert(0, card2)
            deck2.insert(0, card1)

    return 1 if len(deck2) == 0 else 2, deck1, deck2


deck1, deck2 = parse_deck()
winner, deck1, deck2 = play_game(deck1, deck2)
print(sum(card * (n + 1) for n, card in enumerate((deck1, deck2)[winner - 1])))
