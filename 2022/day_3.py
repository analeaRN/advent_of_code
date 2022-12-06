"""
--- Day 3: Rucksack Reorganization ---
"""
import general as g


bags = g.read_file("input.txt").splitlines()


def get_priority(letter: str):
    if not 0 < len(letter) < 2:
        return -1

    if letter.isupper():
        return (ord(letter) - ord("A")) + 27
    
    # lowercase
    return (ord(letter) - ord("a")) + 1


def find_dup(first_word: str, second_word: str):
    a = set(first_word)
    b = set(second_word)
    # print(first_word)
    # print(second_word)
    # print(a.intersection(b))
    # print()
    return a.intersection(b)


def find_dups(*words):
    return set.intersection(*map(set, words))


def part_1():
    priority = 0
    for ks in bags:
        # print(ks)
        priority += sum(map(get_priority, find_dup(ks[:len(ks) // 2], ks[len(ks) // 2:])))
    return priority


def part_2():
    priority = 0
    total = 0
    work_list = bags

    # print("part 2", len(work_list) // 3)
    for index in range(0, len(work_list) // 3):
        sets = work_list[index * 3: index* 3 + 3]
        # print(sets)
        if len(sets) < 3:
            sets.extend(work_list[:3 - len(sets)])
            
        dups = find_dups(*sets)
        if len(dups) == 1:
            total += 1
            priority += get_priority(dups.pop())
            ignore = 2
    
    return priority
 

def old_part_2():
    priority = 0
    total = 0
    work_list = bags
    ignore = 0
    for count, _ in enumerate(work_list):
        if ignore:
            ignore -= 1
            continue
        sets = work_list[count: count + 3]
        
        if len(sets) < 3:
            sets.extend(work_list[:3 - len(sets)])
        
        dups = find_dups(*sets)
        if len(dups) == 1:
            total += 1
            priority += get_priority(dups.pop())
            ignore = 2

    print(priority)
    print(total)


def main():
    g.print_parts(part_1(), part_2())
   

if __name__ == "__main__":
    main()
