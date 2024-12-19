import re
import queue

reg, ins = open(0).read().strip().split('\n\n')
reg = list(int(re.search(r'\d+', r).group()) for r in reg.split('\n'))
ins = list(map(int, re.findall(r'\d', ins)))
org = tuple(ins.copy())

def run(r, p):
    i = 0  # program pointer
    l = len(p)
    out = []
    while i < l:
        opcode = p[i]
        operand = p[i + 1]
        combo_operand = operand if operand < 4 else r[operand - 4]
        match opcode:
            case 0:
                r[0] = r[0] // pow(2, combo_operand)
            case 1:
                r[1] = r[1] ^ operand
            case 2:
                r[1] = combo_operand % 8
            case 3:
                if r[0] != 0:
                    i = operand
                    continue
            case 4:
                r[1] = r[1] ^ r[2]
            case 5:
                out += [combo_operand % 8]
            case 6:
                r[1] = r[0] // pow(2, combo_operand)
            case 7:
                r[2] = r[0] // pow(2, combo_operand)
        i += 2
    return out

print(f"part 1 = {','.join(map(str, run(reg.copy(), ins.copy())))}")

# solution partly from Reddit user 4HbQ; was very difficult to figure out for me
q = queue.Queue()
q.put((0, 0))
while True:
    a, i = q.get()
    reg[0] = a
    out = run(reg.copy(), ins)
    if out == ins:
        print(f"part 2 = {a}")
        break
    if out == ins[-i:] or not i:
        for n in range(8):
            q.put((a * 8 + n, i + 1))
