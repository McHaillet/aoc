from pathlib import Path

def read(file):
    with open(file) as f:
        content = list(l.strip() for l in f.readlines())
    ranges = content[0].split(',')  # remove blank
    return ranges

def part_1(data):
    count = 0
    for x in data:
        start, end = x.split('-')
        if len(start) != len(end):
            # assume start and end only ever bridge single gap
            if len(start) % 2 == 1:
                start = '1' + '0' * len(start)
            else:
                end = '9' * len(start)
        l = len(start)
        if l % 2 == 1:
            continue
        half = l // 2
        hs = start[: half]
        si, ei = int(start), int(end)
        if hs == end[: half]:
            n = int(hs + hs)
            if si <= n <= ei:
                count += n
        else:
            for n in range(si, ei + 1):
                ns = str(n)
                if ns[:half] == ns[half:]:
                    count += n
    return count

def is_valid(code):
    s = str(code)
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i != 0:
            continue
        sub = s[:i]
        if sub * (n // i) == s:
            return True
    else:
        return False


def part_2(data):
    count = 0
    for x in data:
        start, end = x.split('-')
        for i in range(int(start), int(end) + 1):
            if is_valid(i):
                count += i
    return count

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
