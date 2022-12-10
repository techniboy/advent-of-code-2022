from typing import List

FILE_NAME: str = "day_1/input.txt"

def parse_data(file_name: str) -> List[List[int]]:
  elf_calories: List[List[int]] = [[]]
  with open(file_name) as f:
    for val in f:
      if val != "\n":
        elf_calories[-1].append(int(val))
      else:
        elf_calories.append([])
  return elf_calories

elf_calories: List[List[int]] = parse_data(FILE_NAME)


# part 1
# elf carrying most calories
summed_elf_calories: List[int] = sorted([sum(cals) for cals in elf_calories])
print(summed_elf_calories[-1])

# part 2:
# top 3 elves carrying most calories
print(sum(summed_elf_calories[-3:]))