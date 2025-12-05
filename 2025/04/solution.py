from pathlib import Path

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    points, paper = [], []
    nrows, ncols = len(content), len(content[0])
    for i, row in enumerate(content):
        for j, col in enumerate(row):
            if col == '.':
                points += [(i, j)]
            else:
                paper += [(i, j)]
    return set(points), set(paper), nrows, ncols

def part_1(data):
    points, paper, nrows, ncols = data
    total = 0
    for x in paper:
        i, j = x
        count = 0
        for ii in [-1, 0, 1]:
            for jj in [-1, 0, 1]:
                if ii == 0 and jj == 0:
                    continue
                nr, nc = i + ii, j + jj
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if (nr, nc) in paper:
                        count += 1
        if count < 4:
            total += 1
    return total

def part_2(data):
    points, paper, nrows, ncols = data
    total = 0
    while True:
        for x in paper:
            i, j = x
            count = 0
            for ii in [-1, 0, 1]:
                for jj in [-1, 0, 1]:
                    if ii == 0 and jj == 0:
                        continue
                    nr, nc = i + ii, j + jj
                    if 0 <= nr < nrows and 0 <= nc < ncols:
                        if (nr, nc) in paper:
                            count += 1
            if count < 4:
                total += 1
                paper.remove(x)
                break
        else:
            break
    return total

def run(file):
    data = read(file)
    print(f">>> part 1: {part_1(data)}")
    print(f">>> part 2: {part_2(data)}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        if not Path(f).exists():
            continue
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
