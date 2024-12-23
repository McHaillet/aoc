import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(strip)
    n = len(data)
    rrock, srock = [], []
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "O":
                rrock.append(n - y + 1j * x)
            if v == "#":
                srock.append(n - y + 1j * x)
    return rrock, srock


def tilt_up(data):
    


def part_1(data):
    pass


def part_2(data):
    pass


def main(fname):
    start = time.time()
    data = read_file(fname)
    print(data)
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
