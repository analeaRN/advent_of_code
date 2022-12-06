
from pathlib import Path
import inspect

def read_file(file__name: str = "input.txt"):
    with open(file__name) as f:
        return f.read()


def print_parts(a, b=None, /):
    caller_path = Path(inspect.stack()[1][1])
    title = f"== Advent of Code ({caller_path.name}) =="
    print()
    print(title)
    print()
    print(f"part1: \t{a}")
    if b: 
        print("-"*len(title))
        print(f"part2: \t{b}")
    print()
    print("="*len(title))
        

if __name__ == "__main__":
    pass