from dataclasses import dataclass

data = open("input.txt").readline().strip()

# part 1
def part_1(data):
    files = [int(data[x]) for x in range(0, len(data), 2)]
    file_ids = list(range(0, len(files)))
    empty = [int(data[x]) for x in range(1, len(data), 2)]
    checksum = 0
    i = 0
    while files:
        flen, fid = files.pop(0), file_ids.pop(0)
        checksum += sum(range(i, i + flen)) * fid
        i += flen
        space = empty.pop(0)
        if not files:
            break
        while space > 0:  # while space is not filled
            flen, fid = files.pop(-1), file_ids.pop(-1)
            if flen > space:  # fill the space and add back to end
                files.append(flen - space)
                file_ids.append(fid)
                flen = space
                space = 0
            elif flen < space:
                space -= flen
            else:
                space = 0
            checksum += sum(range(i, i + flen)) * fid
            i += flen
    return checksum

part_1(data)

# part 2
@dataclass
class Mem:
    addr: int
    size: int

def part_2(data):
    address = 0
    memory = []
    for size in map(int, data):
        memory += [Mem(address, size)]
        address += size
    
    for used in memory[::-2]:
        for free in memory[1::2]:
            if free.addr <= used.addr and free.size >= used.size:
                used.addr = free.addr
                free.addr += used.size
                free.size -= used.size
    
    return sum(i * sum(range(m.addr, m.addr+m.size)) for i, m in enumerate(memory[::2]))

part_2(data)
