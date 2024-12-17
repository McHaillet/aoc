maze, moves = open(0).read().strip().split("\n\n")
moves = ''.join(moves.split('\n'))
ops = {'>': 1j, '<': -1j, '^': -1, 'v': 1}

# W = walls, B = boulders
bot, W, B = None, [], []
for i, row in enumerate(maze.split('\n')):
    for j, t in enumerate(row):
        if t == '#':
            W += [complex(i, j)]
        elif t == 'O':
            B += [complex(i, j)]
        elif t == '@':
            bot = complex(i, j)

def move_it_1(ind, shift):
    b_s = B[ind] + shift
    if b_s in W:
        return False
    if b_s in B and not move_it_1(B.index(b_s), shift):
        return False
    B[ind] = b_s
    return True

for m in moves:
    shift = ops[m]
    bot_s = bot + shift
    if bot_s in W:
        continue
    if bot_s in B and not move_it_1(B.index(bot_s), shift):
        continue
    bot = bot_s

print(f"part 1 = {int(sum(b.real * 100 + b.imag for b in B))}")

class Boulder(complex):
    def __eq__(self, obj):
        if isinstance(obj, Boulder):
            return obj.real == self.real and (
                obj.imag in [self.imag, self.imag + 1] or
                obj.imag + 1 in [self.imag, self.imag + 1]
            )
        else:
            return obj.real == self.real and obj.imag in [self.imag, self.imag + 1]

# Some tests for the custom Boulder class
# b = complex(1, 1)
# robot = complex(1, 2)
# assert robot != b
#
# b = Boulder(1, 1)
# robot = complex(1, 2)
# assert robot == b
#
# b = [Boulder(1, 1),]
# robot = complex(1, 2)
# assert robot in b
#
# b = [Boulder(1, 2),]
# robot = complex(1, 1)
# assert robot not in b
#
# b = [Boulder(1, 2),]
# robot = Boulder(1, 1)
# assert robot in b

# For part 2 reinterpret the maze
# W = walls, B = boulders
bot, W, B = None, [], []
for i, row in enumerate(maze.split('\n')):
    for j, t in enumerate(row):
        if t == '#':
            W += [Boulder(i, j * 2)]
        elif t == 'O':
            B += [Boulder(i, j * 2)]
        elif t == '@':
            bot = complex(i, j * 2)

def move_it_2(inds, shift):
    # need to reinitialize Boulder class as addition returns default complex
    b_s = [Boulder(B[i] + shift) for i in inds]
    n_inds = []
    for b in b_s:
        if b in W:
            return False
        if b in B[:inds[0]] + B[inds[0] + 1:]:
            n_inds += [i for i, x in enumerate(B) if x == b and not i == inds[0]]
    if len(n_inds) != 0 and not move_it_2(n_inds, shift):
        return False
    for i, b in zip(inds, b_s):
        B[i] = b
    return True

for m in moves:
    shift = ops[m]
    bot_s = bot + shift
    if bot_s in W:
        continue
    if bot_s in B and not move_it_2([B.index(bot_s),], shift):
        continue
    bot = bot_s

print(f"part 1 = {int(sum(b.real * 100 + b.imag for b in B))}")