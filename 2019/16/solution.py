import argparse
import time
from operator import add
from itertools import accumulate
from tqdm import tqdm


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    return [int(x) for x in data[0]]


def fft(data, phases):
    pattern = [0, 1, 0, -1]
    n_d = len(data)
    n_p = len(pattern)
    current = data
    next = [0, ] * len(current)
    for _ in tqdm(range(phases)):
        for i in range(n_d):
            total = 0
            for j in range(n_d - i):
                x = current[i + j]
                index = ((i + j + 1) // (i + 1)) % n_p
                total += x * pattern[index]
            next[i] = abs(total) % 10
        current = next
    return current


def part_1(data):
    result = fft(data, 100)
    return ''.join([str(x) for x in result[:8]])


def part_2(data):
    offset = int(''.join(map(str, data[:7])))
    data = (data * 10_000)[offset:]
    data = data[::-1]  # inverse for fast calculation
    for _ in tqdm(range(100)):
        data = [abs(x) % 10 for x in accumulate(data, add)]
    data = data[::-1]
    return ''.join([str(x) for x in data[:8]])


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1 = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
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
