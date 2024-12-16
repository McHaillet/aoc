from collections import namedtuple, defaultdict
import queue

raw = open("input.txt").read().strip()
data = raw.split('\n')

Pos = namedtuple("Pos", ['i', 'j'])

farms = dict()
nrows, ncols = len(data), len(data[0])
for i, row in enumerate(data):
    for j, t in enumerate(row):
        farms[Pos(i, j)] = t


def discount(patch):
    # calculate the discounted price of the patch by counting corners
    c = 0
    for k, v in patch.items():
        v = list(v)
        match len(v):
            case 1: c += 2
            case 2:
                if v[0][0] == v[1][0] or v[0][1] == v[1][1]:
                    continue
                else:  # its an outside corner
                    c += 1
                    # check for inside corner
                    for x in ((v[0][0], v[1][1]), (v[1][0], v[0][1])):
                        if x != k and x not in patch.keys():
                            c += 1
                            break
            case 3: 
                for I, J in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    x = (k[0] + I, k[1] + J)
                    n1 = (k[0] + I, k[1])
                    n2 = (k[0], k[1] + J)
                    if n1 in v and n2 in v and x not in patch.keys():
                        c += 1
            case 4:
                # check for inside corners
                for I, J in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    if (k[0] + I, k[1] + J) not in patch.keys():
                        c += 1
    return c * len(patch)

# Treating this as a graph seems easiest:
# > each farm is a node with a position and a type
# > each edge defines an adjacency of two farms of the same type
# the number of fences around a farm depends on its edges

d = ((0, 1), (0, -1), (1, 0), (-1, 0))  # directions
total_1, total_2 = 0, 0
while farms:
    farm = farms.popitem()
    q = queue.Queue()
    q.put(farm)
    patch = defaultdict(set)
    while not q.empty():
        p, t = q.get()
        for I, J in d:
            np = Pos(p.i + I, p.j + J)  # check if option is viable
            if np in farms.keys() and farms[np] == t:
                patch[p].add(np)
                patch[np].add(p)
                q.put((np, t))
                farms.pop(np)
            elif np in patch.keys():
                patch[p].add(np)
                patch[np].add(p)
    if len(patch) == 0:
        total_1 += 4
        total_2 += 4
    else:
        area = len(patch)
        fences = sum(4 - len(v) for k, v in patch.items())
        total_1 += area * fences
        total_2 += discount(patch)
print(f"part 1 = {total_1}")
print(f"part 2 = {total_2}")
