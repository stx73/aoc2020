def find_loop_size(target: int) -> int:
    size, subj = 1, 7
    while subj != target:
        subj *= 7
        subj %= 20201227
        size += 1
    return size


def find_encr_key(subj: int, size: int) -> int:
    n = 1
    for i in range(size):
        n *= subj
        n %= 20201227
    return n


card_pk, door_pk = map(int, open("input").readlines())
print(find_encr_key(door_pk, find_loop_size(card_pk)))
