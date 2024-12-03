from operator import add, mul
from itertools import product


with open('input.txt') as f:
    data = eval('[' + f.readline().strip() + ']')

code_to_op = {1: add, 2: mul}

def run(program):
    data = program[:]  # make sure to not overwrite
    i = 0
    while True:
        opcode = data[i]
        if opcode == 99:
            break
        if opcode in (1, 2):
            data[data[i + 3]] = code_to_op[opcode](
                data[data[i + 1]],
                data[data[i + 2]]
            )
        i += 4
    return data[0]

# alarm state
data[1] = 12
data[2] = 2

print(f"part 1: {run(data)}")

for noun, verb in product(range(100), range(100)):
    data[1] = noun
    data[2] = verb
    if run(data) == 19690720:
        print(f"part 2: {100 * noun + verb}")
        break
