
def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    temp = list(l for l in content if '|' in l)
    rules = dict((int(l.split('|')[0]), []) for l in temp)
    [rules[k].append(v) for k, v in (tuple(map(int, l.split('|'))) for l in temp)]
    orders = [list(map(int, l.split(','))) for l in content if '|' not in l]
    return rules, orders

def part_1(data):
    rules, orders = data
    counter = 0
    for order in orders:
        n = len(order)
        for i in range(n - 1, 0, -1):
            x = order[i]
            if x not in rules.keys():
                continue
            if any([y in rules[x] for y in order[:i]]):
                break
        else:
            counter += order[n // 2]
    return counter


def fix_print_order(order, rules):
    for i in range(len(order) - 1, 0, -1):
        x = order[i]
        if x not in rules.keys():
            continue
        for j in range(i - 1, -1, -1):
            y = order[j]
            if y in rules[x]:
                order[i] = y
                order[j] = x
                return fix_print_order(order, rules)
    return order

def part_2(data):
    rules, orders = data
    counter = 0
    # fix the line by swapping?
    for order in orders:
        original = order.copy()
        fixed = fix_print_order(order, rules)
        if original != fixed:
            counter += fixed[len(fixed) // 2]
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