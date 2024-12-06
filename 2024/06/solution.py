
class Guard:
    def __init__(self, x, y, rot=0):
        self.x = x
        self.y = y
        # direction of guard
        self.rot = rot # ^ is 0, > is 1, v is 2, < is 3

    def next(self):
        match self.rot:
            case 0: return self.x - 1, self.y
            case 1: return self.x, self.y + 1
            case 2: return self.x + 1, self.y
            case 3: return self.x, self.y - 1

    def rotate(self):
        self.rot = (self.rot + 1) % 4

def read(file):
    obstructions = []
    guard = None
    with open(file) as f:
        lines = list(l.strip() for l in f.readlines())
        bounds = len(lines), len(lines[0])
        for i, l in enumerate(lines):
            for j, t in enumerate(l):
                if t == '^':
                    guard = (i, j)
                elif t == '#':
                    obstructions.append((i, j))
    return guard, obstructions, bounds

def part_1(data):
    visited = set()
    guard, obstructions, bounds = data
    guard = Guard(*guard)
    while 0 <= guard.x < bounds[0] and 0 <= guard.y < bounds[1]:
        step = guard.next()
        if step in obstructions:
            guard.rotate()
        else:
            visited.add((guard.x, guard.y))
            guard.x, guard.y = step
    return len(visited)

rot_to_check = {
    0: lambda p1, p2: p1[1] == p2[1] and p1[0] > p2[0],
    1: lambda p1, p2: p1[0] == p2[0] and p1[1] < p2[1],
    2: lambda p1, p2: p1[1] == p2[1] and p1[0] < p2[0],
    3: lambda p1, p2: p1[0] == p2[0] and p1[1] > p2[1]
}

def loop(guard, obstructions):
    visited = set()
    while True:
        # we just moved to an obstacle so rotate first
        guard.rotate()
        rot = guard.rot
        vec = (guard.x, guard.y, rot)
        if vec in visited:
            return True
        else:
            visited.add(vec)
        options = [o for o in obstructions if rot_to_check[rot](vec[:2], o)]
        if len(options) == 0:
            return False  # no obstacle in front of guard -> moves out of bounds
        elif len(options) > 1:
            options.sort(key=lambda t: t[rot % 2], reverse=rot in (0, 3))
        new = list(options[0])
        # update guard, but don't place on top of obstacle
        new[rot % 2] = new[rot % 2] + (1 if rot in (0, 3) else -1)
        guard.x, guard.y = new

def part_2(data):
    new_obstacles = set()
    start, obstructions, bounds = data
    guard = Guard(*start)
    while 0 <= guard.x < bounds[0] and 0 <= guard.y < bounds[1]:
        step = guard.next()
        if step in obstructions:
            guard.rotate()
        else:
            # each location-rotation combo is possible location
            if loop(Guard(guard.x, guard.y, guard.rot), obstructions + [step, ]):
                new_obstacles.add(step)
            guard.x, guard.y = step
    # new_obstacles.discard(start)  # start is never allowed
    return len(new_obstacles)


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