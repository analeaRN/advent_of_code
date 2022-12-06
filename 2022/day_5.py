"""
--- Day 5: Supply Stacks ---
"""
import general as g
# crates = g.read_file("test_input.txt")
crates = g.read_file()


def init_crates(placement: str):
    lines = placement.splitlines()[::-1]
    crates_num = int(lines[0][-2])
    crates_ = [[] for _ in range(crates_num)]
    lines = lines[1:]
    # print(lines, crates_)
    
    for _, line in enumerate(lines):
        for i in range(crates_num):
            char = line[i * 4 + 1]
            if char and char != " ":
                crates_[i].append(char)

    print(crates_)
    
    print("completed crate init")
    return crates_


def move_crates(crate, move_from: int, move_to:int, num_boxes: int):
    if not crate[move_from]:
        print(f"Failed to move create... Section {move_from} is empty!")
        return
    
    removed_crates = crate[move_from][-num_boxes:]
    crate[move_from] = crate[move_from][:-num_boxes]
    crate[move_to].extend(removed_crates)
    # I could return the new state of our storage, but that consumes a lot of space


def parse_instructions(instructions: str):
    words = instructions.split()
    count, from_, to = map(int, (words[1], words[3], words[5]))
    from_ -= 1
    to -= 1
    
    return (count, from_, to)


def get_top_crates(crates):
    str = ""
    for c in crates:
        str += c.pop()
    return str


def part_1(instructions, crates):
    # move one crate at a time
    
    
    for instruction in instructions:
        count, from_, to = parse_instructions(instruction)
        for _ in range(count):
            # print(f"moving {from_} to {to}")
            move_crates(crates, from_, to, 1)
            
    return get_top_crates(crates)


def part_2(instructions, crates):
    # move mul crates at a time
    
    for instruction in instructions:
        count, from_, to = parse_instructions(instruction)
        move_crates(crates, from_, to, count)
            
    return get_top_crates(crates)


def main():
    placement, instructions = crates.split("\n\n")
    instructions = instructions.splitlines()
    g.print_parts(
        part_1(instructions, init_crates(placement)), 
        part_2(instructions, init_crates(placement))
    )

main()