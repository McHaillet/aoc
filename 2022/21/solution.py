import argparse
from operator import add, sub, truediv, mul
# from tqdm import tqdm  # progress bar

monkeys = dict()
str_to_op = {'+': add, '-': sub, '/': truediv, '*': mul}
op_inv = {'+': '-', '-': '+', '*': '/', '/': '*'}


def read(filename):
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            key, expr = line.split(':')
            if any([s in expr for s in str_to_op.keys()]):
                monkeys[key] = tuple(expr.strip().split())
            else:
                monkeys[key] = int(expr)
            line = f.readline().strip()


def meme(filename):
    lines = []
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            lines.append(line.replace(':', '='))
            line = f.readline().strip()
    # for the memes
    while lines:
        line = lines.pop(0)
        try:
            exec(line)
        except NameError:
            lines.append(line)
    exec('print(root)')


def solve(key):
    expr = monkeys[key]
    if isinstance(expr, tuple):
        return str_to_op[expr[1]](solve(expr[0]), solve(expr[2]))
    else:
        return expr


def solve_to_str(key, inverse=False):
    if key == 'humn':
        return 'x'
    expr = monkeys[key]
    if isinstance(expr, tuple):
        op = expr[1] if not inverse else op_inv[expr[1]]
        return f'({solve_to_str(expr[0])} {op} {solve_to_str(expr[2])})'
    else:
        return expr


def part1():
    print(solve('root'))


def part2():
    var1, _, var2 = monkeys['root']
    eq1, eq2 = solve_to_str(var1), solve_to_str(var2)
    if 'x' in eq1:
        val = eval(eq2)
        eq = solve_to_str(var1, inverse=True)
    else:
        val = eval(eq1)
        eq = solve_to_str(var2, inverse=True)

    # i = 3412044203912
    # while f(i) != val:
    #     i += 1
    #     if i % 1_000_000 == 0: print(i)
    # print('finished', i)
    # y = ax + b
    # x = (y - b) / a
    a = f(1) - f(0)
    b = f(0)
    result = (val - b) / a
    print(result)


def main(filename):
    meme(filename)
    read(filename)
    part1()
    part2()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='AoC example/input txt file.')
    args = parser.parse_args()
    main(args.file)
