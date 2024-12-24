from collections import defaultdict

data = list(map(int, open(0).read().strip().split('\n')))

def get_next(x):
    x ^= (x << 6) & 16_777_215
    x ^= (x >> 5) & 16_777_215
    return (x ^ (x << 11)) & 16_777_215

p1 = 0
N = len(data)
monkey = defaultdict(int)
for i in range(N):
    x = data[i]
    prev = None
    window = (None,) * 4
    visited = list()
    for j in range(2000):
        x = get_next(x)
        d = x % 10
        if j > 0:
            window = window[1:] + (d - prev,)
        if j > 3 and window not in visited:
            monkey[window] += d
            visited += [window]
        prev = d
    p1 += x

print(f"part 1 = {p1}")
print(f"part 2 = {max(monkey.values())}")
