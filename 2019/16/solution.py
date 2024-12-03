import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    return [int(x) for x in data[0]]


def part_1(data, phases, pattern):
    n_d = len(data)
    n_p = len(pattern)
    current = data
    for _ in range(phases):
        next = [0, ] * len(current)
        for i in range(n_d):
            total = 0
            for x in range(n_d):
                total += current[x] * pattern[(x + 1) // (i + 1) % n_p]
            next[i] = int(str(total)[-1])
        current = next
    return current


def part_2(data):
    pass


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1 = part_1(data, 100, [0, 1, 0 ,-1])
    t1 = time.time()
    print(len(data))
    print(f"Part 1: {''.join([str(x) for x in total_1[:8]])}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2(data)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)
