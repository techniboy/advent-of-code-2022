from typing import List, Set, Tuple


FILE_NAME: str = "day_4/input.txt"

elf_pair: List[Tuple[Set[int], Set[int]]] = []

def parse_data(file_name: str):
    with open(file_name) as f:
        for line in f:
            pair = line.strip().split(",")
            pair = [(int(p.split("-")[0]), int(p.split("-")[1])) for p in pair]
            elf_pair.append((set([i for i in range(pair[0][0], pair[0][1] + 1)]), set([i for i in range(pair[1][0], pair[1][1] + 1)])))


parse_data(FILE_NAME)

# part A
def get_full_overlap() -> int:
    count = 0
    for pair in elf_pair:
        overlap: Set[int] = pair[0].intersection(pair[1])
        if overlap == pair[0] or overlap == pair[1]:
            count += 1
    return count

part_a = get_full_overlap()
print(part_a)

# part B
def get_partial_overlap() -> int:
    count = 0
    for pair in elf_pair:
        overlap: Set[int] = pair[0].intersection(pair[1])
        if overlap != set():
            count += 1
    return count

part_b = get_partial_overlap()
print(part_b)
