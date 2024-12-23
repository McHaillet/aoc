import heapq
import functools
from itertools import product

codes = open(0).read().strip().split('\n')

keypad = ["789", "456", "123", '.0A']
key_dict = dict()
for i, r in enumerate(keypad):
    for j, c in enumerate(r):
        if c != '.':
            key_dict[c] = (i ,j)

dirpad = [".^A", "<v>"]
dir_dict = dict()
for i, r in enumerate(dirpad):
    for j, c in enumerate(r):
        if c != '.':
            dir_dict[c] = (i, j)

hdict = {-1: '<', 1: '>'}
vdict = {-1: '^', 1: 'v'}

# start position of each robot
r0 = (3, 2)
r1 = (0, 2)

def get_num_path(pos, symbol):
    x, y = pos
    nx, ny = key_dict[symbol]
    dx, dy = nx - x, ny - y
    vm = vdict[dx // abs(dx)] * abs(dx) if abs(dx) > 0 else ''
    hm = hdict[dy // abs(dy)] * abs(dy) if abs(dy) > 0 else ''
    if abs(dx) == 0 or abs(dy) == 0:
        return [hm + vm + 'A']
    elif (x + dx, y) == (3, 0):
        return [hm + vm + 'A']
    elif (x, y + dy) == (3, 0):
        return [vm + hm + 'A']
    else:
        return [hm + vm + 'A', vm + hm + 'A']

def get_dir_path(pos, symbol):
    x, y = pos
    nx, ny = dir_dict[symbol]
    dx, dy = nx - x, ny - y
    vm = vdict[dx // abs(dx)] * abs(dx) if abs(dx) > 0 else ''
    hm = hdict[dy // abs(dy)] * abs(dy) if abs(dy) > 0 else ''
    if abs(dx) == 0 or abs(dy) == 0:
        return [hm + vm + 'A']
    elif (x + dx, y) == (0, 0):
        return [hm + vm + 'A']
    elif (x, y + dy) == (0, 0):
        return [vm + hm + 'A']
    else:
        return [hm + vm + 'A', vm + hm + 'A']

# recursively find the shortest path on the direction pad
# each seq only contains one A at the end because we can always recurse over those
@functools.cache
def shortest_seq(seq, robots):
    if robots == 0:
        return len(seq)
    size = 0
    start = r1
    for c in seq:
        ps = get_dir_path(start, c)
        size += min(shortest_seq(p, robots - 1) for p in ps)
        start = dir_dict[c]
    return size

# util for fixing trailing zeros in the code
def fix(x):
    if x.startswith('0'):
        return fix(x[1:])
    return int(x)

total = 0
for code in codes:
    size = 0
    start = r0
    for c in code:
        ps = get_num_path(start, c)
        size += min(shortest_seq(p, 2) for p in ps)
        start = key_dict[c]
    total += size * fix(code[:-1])
print(f"part 1 = {total}")

total = 0
for code in codes:
    size = 0
    start = r0
    for c in code:
        ps = get_num_path(start, c)
        size += min(shortest_seq(p, 25) for p in ps)
        start = key_dict[c]
    total += size * fix(code[:-1])
print(f"part 2 = {total}")
