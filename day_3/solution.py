import string
from typing import List


FILE_NAME: str = "day_3/input.txt"

rucksacks: List[List[str]] = []

def parse_data(file_name: str):
  with open(file_name) as f:
    for line in f:
        mid = len(line)//2
        rucksacks.append([line[:mid], line[mid:-1]])


parse_data(FILE_NAME)

priority_value = {l: i + 1 for i, l in enumerate(string.ascii_lowercase)}

# part A
def calc_total_priority_value():
    result = 0
    for r in rucksacks:
        common_item = set(r[0]).intersection(set(r[1])).pop()
        if common_item.isupper():
            result += 26
        result += priority_value[common_item.lower()]
    return result

part_a = calc_total_priority_value()
print(part_a)

# part B
def calc_priority_by_group():
    result = 0
    i = 0
    while i < len(rucksacks):
        group = [r[0]+r[1] for r in rucksacks[i:i+3]]
        common_item = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        if common_item.isupper():
            result += 26
        result += priority_value[common_item.lower()]
        i += 3
    return result

part_b = calc_priority_by_group()
print(part_b)
