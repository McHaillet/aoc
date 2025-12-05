from pathlib import Path

def read(file):
    with open(file) as f:
        content = (l.strip() for l in f.readlines())
        content = list(l for l in content if l)  # remove blank
    return content

def compile_ranges(content):
    compiled = []
    for a in content:
        a1, a2 = map(int, a.split('-'))
        i = 0
        while i < len(compiled):
            b1, b2 = compiled[i]
            if a1 > b2 + 1:
                i += 1
                continue
            elif a2 + 1 < b1:
                compiled = compiled[: i] + [(a1, a2)] + compiled[i: ]
                break
            else:
                if a1 > b1:
                    a1 = b1
                if a2 < b2:
                    a2 = b2
                compiled.pop(i)
        if i == len(compiled):
            compiled += [(a1, a2)]
    return compiled

def part_1(ranges, ingredients):
    fresh = 0
    for x in ingredients:
        for l, r in ranges:
            if l <= int(x) <= r:
                fresh += 1
                break
    return fresh

def part_2(ranges):
    total = 0
    for l, r in ranges:
        total += r - l + 1
    return total

def run(range_file, ingredient_file):
    ranges = compile_ranges(read(range_file))
    ingredients = read(ingredient_file)
    print(f">>> part 1: {part_1(ranges, ingredients)}")
    print(f">>> part 2: {part_2(ranges)}")

def main():
    f1 = ["example_ranges.txt", "input_ranges.txt"]
    f2 = ["example_ingredients.txt", "input_ingredients.txt"]
    for r,i in zip(f1, f2):
        if Path(r).exists() and Path(i).exists():
            print(f"Results for ({r}, {i})...")
            run(r, i)

if __name__ == "__main__":
    main()
