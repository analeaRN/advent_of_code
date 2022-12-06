"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""
import general as g
calories = g.read_file("./2022/input.txt")


max = -1
elfs = []
for elf_rations in calories.split("\n\n"):
    rations = (int(i) for i in elf_rations.split())
    r = sum(rations)
    elfs.append(r)
    if r > max:
        max = r
    # print(r)

print(max)

elfs.sort()
print(sum(elfs[-3:]))
