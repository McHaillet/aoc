import heapq

data = open(0).read().strip().split('\n')
B = list(tuple(map(int, x.split(','))) for x in data)

SIZE = 70 + 1
N = 1024
M = len(B)

def find_path(n):
    start = (0, 0)
    q = [(0, start)]
    heapq.heapify(q)
    visited = set()
    blocks = B[:n]
    while True:
        steps, pos = heapq.heappop(q)
        if pos == (SIZE - 1, SIZE - 1):
            return steps
        if pos in blocks or pos in visited:
            continue
        visited.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                heapq.heappush(q, (steps + 1, (nx, ny)))

print(f"part 1 = {find_path(N)}")

# use bisection !!
i, j, k = N, M, (N + M) // 2
while k != i:
    try:
        _ = find_path(k)
        i = k
    except IndexError:
        j = k
    k = (i + j) // 2
print(f"part 2 = {B[k][0]},{B[k][1]}")
