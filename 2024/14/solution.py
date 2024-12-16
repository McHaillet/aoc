from collections import defaultdict
from functools import reduce

W, H = 101, 103
data = open(0).read().strip().split('\n')
quadrants = defaultdict(int)
for r in data:
    p, v = r.split(' ')
    p = complex(*map(int, p.split('=')[1].split(',')))
    v = complex(*map(int, v.split('=')[1].split(',')))
    x = p + v * 100
    x = complex(x.real % W - W // 2, x.imag % H - H // 2)
    if x.real == 0 or x.imag == 0:
        continue
    quadrants[(x.real // abs(x.real), x.imag // abs(x.imag))] += 1
    print(quadrants.values())
print(f"part 1 = {reduce(lambda x, y: x * y, quadrants.values())}")

# For part 2 you can only use the info that the pattern repeats after
# some amount of seconds.
# Each robot should have a wave for hitting the same position again
# given by some phase and some frequency.
# Find these parameters for each robot and it should be possible to
# calculate when the image of the tree occurs first.
