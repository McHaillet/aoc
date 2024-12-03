
def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def part_1(data):
    pass

def part_2(data):
    pass

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