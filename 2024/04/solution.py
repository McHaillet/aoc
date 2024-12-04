import re
from itertools import product

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def part_1(data):
    xs = []
    for i, d in enumerate(data):
        for hit in re.finditer(r"X", d):
            xs.append(i + 1j * hit.start())
    
    nrows = len(data)
    ncols = len(data[0])
    counter = 0
    for start in xs:
        for direction in product((-1, 0, 1), (-1, 0, 1)):
            if direction == (0,0):
                continue
            r, c = direction
            for f, letter in zip((1, 2, 3), ('M', 'A', 'S')):
                i = int(start.real + r * f)
                if i < 0 or i >= nrows:
                    break
                j = int(start.imag + c * f)
                if j < 0 or j >= ncols:
                    break
                if data[i][j] != letter:
                    break
            else:
                counter += 1
    return counter

def roll(l, n):
    return l[n:] + l[:n]

def part_2(data):
    As = []
    for i, d in enumerate(data):
        for hit in re.finditer(r"A", d):
            As.append(i + 1j * hit.start())
    
    nrows = len(data)
    ncols = len(data[0])
    counter = 0
    positions = [-1 - 1j, -1 + 1j, 1 + 1j, 1 - 1j]
    letters = ['M', 'M', 'S', 'S']
    for start in As:
        for direction in (0, 1, 2, 3):  # the M and S can be in 4 orientations around the A
            for p, letter in zip(positions, roll(letters, direction)):
                i = int(start.real + p.real)
                if i < 0 or i >= nrows:
                    break
                j = int(start.imag + p.imag)
                if j < 0 or j >= ncols:
                    break
                if data[i][j] != letter:
                    break
            else:
                counter += 1
                break
    return counter


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
