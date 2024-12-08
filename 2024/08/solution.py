from collections import defaultdict
from itertools import combinations
import math

def read(file):
    antennae = defaultdict(list)
    with open(file) as f:
        text = f.read().strip()
        lines = text.split('\n')
        bounds = (len(lines), len(lines[0]))
        for i, l in enumerate(lines):
            for j, t in enumerate(l):
                if t != '.':
                    antennae[t].append(complex(i,j))
    return antennae, bounds

def part_1(data):
    antinodes = set()
    antennae, bounds = data
    for t in antennae.keys():
        for x in combinations(antennae[t], 2):
            # >>> c = a - b
            # >>> a + c
            # (5+6j)
            # >>> b - c
            # (-1+0j)
            p1, p2 = x
            dx = p2 - p1
            an1 = p1 - dx
            if 0 <= an1.real < bounds[0] and 0 <= an1.imag < bounds[1]:
                antinodes.add(an1)
            an2 = p2 + dx
            if 0 <= an2.real < bounds[0] and 0 <= an2.imag < bounds[1]:
                antinodes.add(an2)
    return len(antinodes)

def part_2(data):
    antinodes = set()
    antennae, bounds = data
    for t in antennae.keys():
        antinodes.update(antennae[t])
        for points in combinations(antennae[t], 2):
            p1, p2 = points
            # my input never had vertical lines so this works
            dx = p1 - p2  # find line eq.
            a = dx.imag / dx.real
            b = p1.imag - a * p1.real
            f = lambda x: a * x + b
            for x in range(bounds[0]):  # calculate all intersections with grid
                y = f(x)
                # this check is not nice
                # should be possible to use pure ints: using fractions.Fraction?
                if math.isclose(y, round(y), abs_tol=1e-9) and 0 <= y < bounds[1]:
                    antinodes.add(complex(x, round(y)))
    return len(antinodes)

def run(file):
    data = read(file)
    print(f">>> part 1: {part_1(data)}")
    print(f">>> part 2: {part_2(data)}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
