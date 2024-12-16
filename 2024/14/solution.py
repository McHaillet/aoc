from collections import defaultdict
from functools import reduce
from statistics import variance

W, H = 101, 103
data = open(0).read().strip().split('\n')
quadrants = defaultdict(int)
for r in data:
    p, v = r.split(' ')
    x, y = tuple(map(int, p.split('=')[1].split(',')))
    dx, dy = tuple(map(int, v.split('=')[1].split(',')))
    nx, ny = (x + dx * 100) % W - W // 2, (y + dy * 100) % H - H // 2
    if nx == 0 or ny == 0:
        continue
    quadrants[(nx // abs(nx), ny // abs(ny))] += 1
print(f"part 1 = {reduce(lambda x, y: x * y, quadrants.values())}")

# For part 2 you can only use the info that the pattern repeats after
# some amount of seconds.
# Each robot should have a wave for hitting the same position again
# given by some phase and some frequency.
# Find these parameters for each robot and it should be possible to
# calculate when the image of the tree occurs first.
robots = []
for r in data:
    p, v = r.split(' ')
    p = map(int, p.split('=')[1].split(','))
    v = map(int, v.split('=')[1].split(','))
    robots += [(*p, *v)]

bx = min(range(W), key=lambda t: variance((s+t*v) % W for (s,_,v,_) in robots))
by = min(range(H), key=lambda t: variance((s+t*v) % H for (_,s,_,v) in robots))

# naive approach using chinese remainder theorem
# for i in range(W * H):
#     if i % W == bx and i % H == by:
#         print(f"part 2 = {i}")
#         break

# can also solve the equations mathematically
print(f"part 2 = {bx + ((pow(W, -1, H) * (by - bx)) % H) * W}")

