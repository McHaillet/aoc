from operator import add, mul
from itertools import product

def read(file):
    data = []
    with open(file) as f:
        for l in f.readlines():
            a, b = l.strip().split(':')
            data.append((int(a), tuple(map(int, b.split()))))
    return data

key_to_op = {0: add, 1: mul, 2: lambda x, y: int(str(x) + str(y))}

def reduce(X, ops):
    start = X[0]
    for i, o in enumerate(ops):
        start = key_to_op[o](start, X[i + 1])
    return start

def part_1(data):
    total = 0
    for r in data:
        t, X = r
        # use itertools product
        for c in product((0,1), repeat=len(X) - 1):
            if reduce(X, c) == t:
                total += t
                break
    return total

def part_2(data):
    total = 0
    for r in data:
        t, X = r
        # use itertools product
        for c in product((0, 1, 2), repeat=len(X) - 1):
            if reduce(X, c) == t:
                total += t
                break
    return total

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
