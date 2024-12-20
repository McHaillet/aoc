import functools

T, D = open(0).read().strip().split('\n\n')
T = T.split(', ')
D = D.split('\n')

@functools.cache
def options(design):
    if len(design) == 0:
        return 1
    n = 0
    for t in T:
        if design.startswith(t):
            n += options(design[len(t):])
    return n

tot_1, tot_2 = 0, 0
for i, d in enumerate(D):
    x = options(d)
    tot_1 += 1 if x > 0 else 0
    tot_2 += x

print(f"part 1 = {tot_1}")
print(f"part 2 = {tot_2}")