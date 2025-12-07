from pathlib import Path
from collections import defaultdict

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def solve(d):
    nr = len(d)
    nc = len(d[0])
    beams = {d[0].index('S'): 1}
    splits = 0
    for i in range(2, nr, 2):
        nb = defaultdict(int)
        for beam, worlds in beams.items():
            if d[i][beam] == '^':
                splits += 1
                nb[beam - 1] += worlds
                nb[beam + 1] += worlds
            else:
                nb[beam] += worlds
        beams = nb
    return splits, sum(beams.values())

def run(file):
    p1, p2 = solve(read(file))
    print(f">>> part 1: {p1}")
    print(f">>> part 2: {p2}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        if not Path(f).exists():
            continue
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
