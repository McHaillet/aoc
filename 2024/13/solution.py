import re

data = open(0).read().strip().split("\n\n")

def solve(dx1, dy1, dx2, dy2, xp, yp):
    # this is the solution two the system of two eqs. for the A button
    num, denom = (xp * dy2 - yp * dx2), (dx1 * dy2 - dy1 * dx2)
    if num % denom != 0:
        return 0
    a = num // denom
    num, denom = (xp - a * dx1), dx2  # use A to find B button hits
    if num % denom != 0:
        return 0
    b = num // denom
    return a * 3 + b

t1, t2 = 0, 0
for d in data:
    machine = list(map(int, re.findall(r'\d+', d)))
    t1 += solve(*machine)
    t2 += solve(
        *machine[:4],
        *map(lambda x: x + 10000000000000, machine[4:6])
    )

print(f"part 1 = {t1}")
print(f"part 2 = {t2}")
