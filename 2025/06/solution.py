from pathlib import Path
from operator import add, mul
from functools import reduce

get_op = {'+': add, '*': mul}

def read(file):
    with open(file) as f:
        content = (l.strip('\n') for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def part_1(data):
    data = [l.split() for l in data]
    rows = len(data)
    cols = len(data[0])
    total = 0
    for i in range(cols):
        op = get_op[data[-1][i]]
        res = int(data[0][i])
        for r in range(1, rows - 1):
            res = op(res, int(data[r][i]))
        total += res
    return total

def part_2(data):
    operators = data[-1]
    n, i = len(operators), 0
    total = 0
    while i < n:
        j = i + 1
        while True:
            if j == n:
                numbers = j - i
                break
            if operators[j] != ' ':
                numbers = j - i - 1
                break
            j += 1
        number_list = []
        for y in range(numbers):
            digits = ''
            for x in range(len(data) - 1):
                digits += data[x][i + y]
            number_list.append(int(digits))
        total += reduce(get_op[operators[i]], number_list)
        i = j
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
