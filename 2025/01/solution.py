from pathlib import Path

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
    content = list((l[0], int(l[1:])) for l in content if l)  # remove blank
    content = list(-x if l == 'L' else x for l, x in content)
    return content

def part_1(data):
    p = 50
    counter = 0
    for x in data:
        p = (p + x) % 100
        if p == 0:
            counter += 1
    return counter

def part_2(data):
    p = 50
    counter = 0
    for x in data:
        if x > 0:
            n = p + x
            p = n % 100
            counter += n // 100
        else:  # invert the pointer and invert what we add
            ip = (100 - p) % 100
            ip = ip - x
            counter += ip // 100
            p = (100 - ip) % 100
    return counter

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
