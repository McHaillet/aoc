with open('input.txt') as f:
    data = list(map(int, (x.strip() for x in f.readlines())))

print(f"part 1: {sum(x // 3 - 2 for x in data)}")

def fuel(x):
    new = x // 3 - 2
    if new <= 0:
        return 0
    else:
        return new + fuel(new)

print(f"part 2: {sum(fuel(x) for x in data)}")
