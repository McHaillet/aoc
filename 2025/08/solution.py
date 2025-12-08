from pathlib import Path
from scipy.spatial.distance import pdist
from functools import reduce
from operator import mul
import numpy as np
import math

def read(file):
    boxes = []
    with open(file) as f:
        for l in f.readlines():
            l = l.strip()
            if l:
                xyz = tuple(map(int, l.split(',')))
                boxes.append(xyz)
    return np.array(boxes)

def calc_row_idx(k, n):
    return int(math.ceil((1/2.) * (- (-8*k + 4 *n**2 -4*n - 7)**0.5 + 2*n -1) - 1))

def elem_in_i_rows(i, n):
    return i * (n - 1 - i) + (i*(i + 1))//2

def calc_col_idx(k, i, n):
    return int(n - elem_in_i_rows(i + 1, n) + k)

def condensed_to_square(k, n):
    i = calc_row_idx(k, n)
    j = calc_col_idx(k, i, n)
    return i, j

def solve(data):
    n = len(data)
    m = pdist(data)
    closest = np.argsort(m)[:10000]
    circuits = [set(condensed_to_square(closest[0], n))]
    iteration = 1
    part_1, part_2 = None, None
    while True:
        
        # find how circuits append for the next closest pair
        c = closest[iteration]
        p1, p2 = condensed_to_square(c, n)
        for i in range(len(circuits)):
            x = circuits[i]
            if p1 in x and p2 in x:
                break
            if p1 in x or p2 in x:
                if p2 in x:  # reorder so we can run same code twice
                    p1, p2 = p2, p1
                for j in range(len(circuits)):
                    y = circuits[j]
                    if p2 in y:
                        z = x.union(y)
                        if j > i:  # swap so we pop largest index first
                            i, j = j, i
                        circuits.pop(i)
                        circuits.pop(j)
                        circuits.append(z)
                        break
                else:
                    circuits[i].add(p2)
                break
        else:
            circuits.append(set((p1, p2)))
        
        # part 1: happens at iteration 1000
        if iteration == 1000:
            part_1 = reduce(mul, sorted([len(x) for x in circuits], reverse=True)[: 3])
        
        # part 2: number of circuits is 1 and all boxes are included
        if len(circuits) == 1 and len(circuits[0]) == n:
            part_2 = data[p1][0] * data[p2][0]            
            break
        
        iteration += 1

    return part_1, part_2

def part_2(data):
    pass

def run(file):
    data = read(file)
    part1, part2 = solve(data)
    print(f">>> part 1: {part1}")
    print(f">>> part 2: {part2}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        if not Path(f).exists():
            continue
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
