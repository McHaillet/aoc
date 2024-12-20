import queue

maze = open(0).read().strip().split('\n')

nrows, ncols = len(maze), len(maze[0])
start, end = None, None
for i, r in enumerate(maze):
    for j, c in enumerate(r):
        if c == 'S':
            start = (i, j)
        if c == 'E':
            end = (i, j)

q = queue.Queue()
q.put(start)
route = list()
while True:
    pos = q.get()
    if pos == end:
        route += [end]
        break
    if pos in route:
        continue
    route += [pos]
    x, y = pos
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 < nx < nrows - 1 and 0 < ny < ncols - 1 and maze[nx][ny] in ['.', 'E']:
            q.put((nx, ny))

# each cheat is just a cut in the current route that is restricted by
# a distance (d)
def find_cheats(d):
    nsteps = len(route)
    cheats = 0
    for i in range(nsteps - 1):
        x, y = route[i]
        options = route[i:]
        for j, (nx, ny) in enumerate(options):
            manh = abs(nx - x) + abs(ny - y)
            if 2 <= manh <= d and j - manh >= 100:
                cheats += 1
    return cheats

print(f"part 1 = {find_cheats(2)}")
print(f"part 1 = {find_cheats(20)}")
