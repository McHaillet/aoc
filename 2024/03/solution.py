import re
from operator import mul  # needed for eval()

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def part_1(data):
    matches = re.findall(r"mul[(]\d*?,\d*?[)]", data)
    return sum(list(eval(x) for x in matches))

def part_2(data):
    total = 0
    op_do = re.search(r"do[(][)]", data)
    do_id = op_do.start() if op_do is not None else len(data)
    op_dont = re.search(r"don't[(][)]", data)
    dont_id = op_dont.start() if op_dont is not None else len(data)
    total += part_1(data[:min(do_id, dont_id)])
    data = data[min(do_id, dont_id):]
    while data:
        op_do = re.search(r"do[(][)]", data)
        do_id = op_do.start() if op_do is not None else len(data)
        op_dont = re.search(r"don't[(][)]", data)
        dont_id = op_dont.start() if op_dont is not None else len(data)
        if do_id == dont_id:
            break
        if dont_id < do_id:
            data = data[do_id:]
        else:
            total += part_1(data[:dont_id])
            data = data[dont_id:]
    return total

def run(file):
    data = ''.join(read(file))
    print(f">>> part 1: {part_1(data)}")
    print(f">>> part 2: {part_2(data)}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
