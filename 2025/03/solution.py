from pathlib import Path

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def get_joltage(bank, digits):
    if digits == 0:
        return ''
    options = bank if digits == 1 else bank[:-(digits - 1)]
    i = max(range(len(options)), key=lambda i: options[i])
    return bank[i] + get_joltage(bank[i + 1:], digits - 1)
    
def f(data, digits):
    count = 0
    for bank in data:
        m = get_joltage(bank, digits)
        count += int(m)
    return count

def run(file):
    data = read(file)
    print(f">>> part 1: {f(data, 2)}")
    print(f">>> part 2: {f(data, 12)}")

def main():
    files = ("example.txt", "input.txt")
    for f in files:
        if not Path(f).exists():
            continue
        print(f"Results for {f}...")
        run(f)

if __name__ == "__main__":
    main()
