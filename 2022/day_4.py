"""
Day 4: Camp Cleanup
"""
import general as g
# elf_sections = g.read_file("test_input.txt")
elf_sections = g.read_file()


class Section:
    def __init__(self, range: str) -> None:
        # expects str of num-num
        low, high = range.split("-")
        self.low: int = int(low)
        self.high: int = int(high)
    

    def __is_in_range(self, num: int):
        return self.low <= num <= self.high

    def over_lap(self, other):
        return other.low in self or other.high in self

    def __contains__(self, item):
        if isinstance(item, int):
            return self.__is_in_range(item)
        elif isinstance(item, Section):
            return self.__is_in_range(item.low) and self.__is_in_range(item.high)   
        return False

    def __repr__(self) -> str:
        return f"Section({self.low=}-{self.high=})"


def part_1(all_selections):
    count = 0
    for s in all_selections:
        first, second = s.split(",")
        
        print(first, second)
        a = Section(first)
        b = Section(second)
        
        if a in b or b in a:
            count += 1
    return count


def part_2(all_selections):
    count = 0
    for s in all_selections:
        first, second = s.split(",")
        
        # print(first, second)
        a = Section(first)
        b = Section(second)
        
        
        if a.over_lap(b) or b.over_lap(a):
            count += 1
    return count


def main():
    all_selections = elf_sections.splitlines()
    g.print_parts(part_1(all_selections), part_2(all_selections))


main()