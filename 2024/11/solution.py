import functools

data = open("input.txt").read().strip().split()

def fix(x):
    if len(x) == 1:
        return x
    if x.startswith('0'):
        return fix(x[1:])
    else:
        return x

@functools.cache
def blink(s, i):
    if i == 0:
        return 1
    if s == '0':
        return blink('1', i - 1)
    elif len(s) % 2 == 0:
        split = len(s) // 2
        return blink(s[:split], i - 1) + blink(fix(s[split:]), i - 1)
    else:
        return blink(str(int(s) * 2024), i - 1)

print(f"part 1: {sum(map(functools.partial(blink, i=25), data))}")
print(f"part 2: {sum(map(functools.partial(blink, i=75), data))}")
