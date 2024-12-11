from collections import namedtuple, defaultdict
import queue

def read(fname):
    with open(fname) as f:
        lines = f.read().strip().split('\n')
    return lines

data = read("input.txt")

Pos = namedtuple("Pos", ['x', 'y'])

trailheads = []
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == '0':
            trailheads += [Pos(i, j)]

dirs = {Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1)}

# part 1
def routes(topo, start):
    q = queue.Queue()
    q.put(start)
    visited = set()
    trails = set()
    nrows, ncols = len(topo), len(topo[0])
    while not q.empty():
        i = q.get()
        if i in visited:
            continue
        visited.add(i)
        if topo[i.x][i.y] == '9':
            trails.add(i)
            continue
        for d in dirs:
            n = Pos(i.x + d.x, i.y + d.y)  # new position
            if (0 <= n.x < nrows and 0 <= n.y < ncols and 
                topo[n.x][n.y] == chr(ord(topo[i.x][i.y]) + 1)):
                q.put(n)
    return trails   

sum(len(routes(data, t)) for t in trailheads)

# part 2
def routes(topo, start):
    q = queue.Queue()
    q.put(start)
    trails = defaultdict(int)
    nrows, ncols = len(topo), len(topo[0])
    while not q.empty():
        i = q.get()
        if topo[i.x][i.y] == '9':
            trails[i] += 1
        for d in dirs:
            n = Pos(i.x + d.x, i.y + d.y)  # new position
            if (0 <= n.x < nrows and 0 <= n.y < ncols and 
                topo[n.x][n.y] == chr(ord(topo[i.x][i.y]) + 1)):
                q.put(n)
    return sum(trails.values())   

sum(routes(data, t) for t in trailheads)
