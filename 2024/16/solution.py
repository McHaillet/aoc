from collections import namedtuple
import heapq

Reindeer = namedtuple('Reindeer', ['xy', 'd'])

maze = open(0).read().strip().split('\n')
start, end = None, None
for i, row in enumerate(maze):
    for j, t in enumerate(row):
        if t == 'S':
            start = Reindeer(complex(i, j), 1j)
        if t == 'E':
            end = complex(i, j)

i = 0
# (priority, entry, unique visited spots, Reindeer)
q = [(0, i, set(), start)]
heapq.heapify(q)
visited = dict()
path_len = None
seats = set()
while len(q) > 0:
    s, _, v, r = heapq.heappop(q)
    v.add(r.xy)
    if r.xy == end:
        if path_len is None:
            print(f"part 1 = {s}")
            path_len = s
            seats.update(v)
            continue
        if s == path_len:
            seats.update(v)
    if maze[int(r.xy.real)][int(r.xy.imag)] == '#':
        continue
    if r in visited.keys():
        if s > visited[r]:
            continue
        else:
            visited[r] = s
    else:
        visited[r] = s
    heapq.heappush(q, (s + 1, i + 1, v.copy(), Reindeer(r.xy + r.d, r.d)))
    # to rotate direction: clockwise * 1j; anti-clockwise * -1j
    heapq.heappush(q, (s + 1_000, i + 2, v.copy(), Reindeer(r.xy, r.d * 1j)))
    heapq.heappush(q, (s + 1_000, i + 3, v.copy(), Reindeer(r.xy, r.d * -1j)))
    i += 3

print(f"part 2 = {len(seats)}")
