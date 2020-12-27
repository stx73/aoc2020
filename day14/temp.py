import re
from itertools import product

with open('input', 'r') as input_file:
    program = [line.strip() for line in input_file.readlines()]

def apply_mask(mask, value):
    bin_value = format(int(value), 'b').rjust(36, '0')
    return ''.join([mask[n] if mask[n] in 'X1' else v for n, v in enumerate(bin_value)])


values = {}

for line in program:
    """
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1
    """
    if line.startswith('mask'):
        mask = re.search(r'[01X]{36}', line).group()
        continue
    ix, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
    ix_value = apply_mask(mask, ix)

    x_ix = [n for n, v in enumerate(ix_value) if v == 'X']
    # x_ix=[32, 34, 35]
    L = [list(v) for v in product(('0', '1'), repeat=len(x_ix))]
    # L=[['0', '0', '0'], ['0', '0', '1'], ['0', '1', '0'], ['0', '1', '1'], ['1', '0', '0'], ['1', '0', '1'], ['1', '1', '0'], ['1', '1', '1']]
    for p in L:
        """
        ix_value=00000000000000000000000000000001X0XX

        ix_value=000000000000000000000000000000010000
        ix_value=000000000000000000000000000000011000
        ix_value=000000000000000000000000000000010010
        ix_value=000000000000000000000000000000011010
        ix_value=000000000000000000000000000000010001
        ix_value=000000000000000000000000000000011001
        ix_value=000000000000000000000000000000010011
        ix_value=000000000000000000000000000000011011
        """
        ix_value = ''.join([p.pop() if n in x_ix else v for n, v in enumerate(ix_value)])
        values[ix_value] = int(val)

print(sum(values.values()))
