
with open('input.txt') as f:
    lines = [f.strip() for f in f.readlines()]

counter = 0
for l in lines:
    xx = list(map(int, l.split()))
    signs = set()
    for x, y in zip(xx[:-1], xx[1:]):
        diff = x - y
        if diff == 0 or abs(diff) > 3:
            break
        signs.add(diff > 0)
        if len(signs) > 1:
            break
    else:
        counter += 1

print(f"part 1 : {counter}")

counter = 0
for l in lines:
    xx = list(map(int, l.split()))
    flag = None
    signs = set()
    for i, (x, y) in enumerate(zip(xx[:-1], xx[1:])):
        diff = x - y
        if diff == 0 or abs(diff) > 3:
            flag = i
            break
        signs.add(diff > 0)
        if len(signs) > 1:
            flag = i
            break
    else:
        counter += 1
        continue

    for i in [-1, 0, 1]:
        if flag + i < 0:
            continue
        yy = xx.copy()
        yy.pop(flag + i)  # look for index at -1 0 1
        # -1 is an option as I set to the flag to the first sign change
        signs = set()
        for x, y in zip(yy[:-1], yy[1:]):
            diff = x - y
            if diff == 0 or abs(diff) > 3:
                break
            signs.add(diff > 0)
            if len(signs) > 1:
                break
        else:
            counter += 1
            break

print(f"part 2 : {counter}")
