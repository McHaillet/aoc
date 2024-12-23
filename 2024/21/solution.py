from collections import deque
from itertools import product

codes = open(0).read().strip().split('\n')

keypad = ["789", "456", "123", '.0A']
kdim = (4, 3)
dirpad = [".^A", "<v>"]
ddim = (2, 3)

ddict = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

# start position of each robot
r1 = (3, 2)
r2 = (0, 2)
r3 = (0, 2)

def get_paths(sequence, robot_start, pad, pdim):
    start = robot_start
    R = list()
    for c in sequence:
        routes = list()
        shortest = None
        q = deque([(start, list(), list())])
        while len(q) > 0:
            p, r, b = q.popleft()  # position, route, buttons
            x, y = p
            if pad[x][y] == c:
                b += ['A']
                if shortest is None:
                    shortest = len(b)
                    start = p
                else:
                    if len(b) > shortest: continue
                routes += [b]
                continue
            if p in r:
                continue
            r += [p]
            for key, d in ddict.items():
                dx, dy = d
                nx, ny = x + dx, y + dy
                if (0 <= nx < pdim[0] and 0 <= ny < pdim[1]
                        and pad[nx][ny] !='.'):
                    q.append(((nx, ny), r.copy(), b + [key]))
        R += [(c, routes)]
    return R

total = 0
for code in codes:
    x = get_paths(code, r1, keypad, kdim)
    seqs = []
    for y in product(*(r[1] for r in x)):
        seqs += [''.join(sum(y, []))]

    # print(seqs[0])

    nseqs = []
    for s in seqs:
        x = get_paths(s, r2, dirpad, ddim)
        for y in product(*(r[1] for r in x)):
            nseqs += [''.join(sum(y, []))]

    # print(nseqs[0])

    nnseqs = []
    for s in nseqs:
        x = get_paths(s, r2, dirpad, ddim)
        for y in product(*(r[1] for r in x)):
            nnseqs += [''.join(sum(y, []))]

    def fix(x):
        if x.startswith('0'):
            return fix(x[1:])
        return int(x)

    # print(nnseqs[0])
    N = list(len(x) for x in nnseqs)
    total += (min(N) * fix(code[:-1]))

print(total)
# OBSERVATIONS
# 1. the set of button presses for each shortest path is always the same
# 2. the solutions where multiple keys are chained together might be best
# > however, finding the shortest path and then reordering the key wont work due to the
# dead section on each pad
# Penalize solutions with lots of variation?

# for k, v in x:
#     for l in v:
#         print(f"path {l}")
#         y = get_paths(l, r2, dirpad, ddim)
#         print(y)
#         print(sum(len(j[0]) for i, j in y))
#     print('\n')