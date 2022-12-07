"""
--- Day 7: No Space Left On Device ---
"""
import general as g


# command = g.read_file("test_input.txt").splitlines()
command = g.read_file().splitlines()


class FileItem:
    def __init__(self, text: str):
        a, b = text.split()
        if a == "dir":
            self.dir = True
            self.name = b
            self.size = -1
        else:
            self.dir = False
            self.name = b
            self.size = int(a)

    def __repr__(self) -> str:
        return f"FileItem({self.dir=} {self.name=} {self.size=})"
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(self, str):
            return self.name == __o
        elif isinstance(self, FileItem):
            return self.dir == self.dir
        return False
    
    def __hash__(self) -> int:
        # return hash(tuple(self.__dict__.values()))
        # we want to find it via it's name
        return hash(self.name)


def find_size(dir, files, all_dict):
    size = 0
    for f in files:
        if f.dir and f.size == -1:
            # f.size = find_size(f"{dir}{f.name}", all_dict[f"{dir}{f.name}"], all_dict)
            f.size = find_size(f"{dir}{f.name}", all_dict[f"{dir}{f.name}"], all_dict)
        size += f.size
    return size


def init_graph():
    file_system = {}
    cur_path = []
    for c in command:
        # print(">", c)
        if c.startswith("$"):
            com = c[2:].split()
            if com[0] == "cd":
                # changed dir
                if com[1] == "..":
                    cur_path.pop()
                else:
                    cur_path.append(com[1])
                
                # set up dir 
                path = "".join(cur_path)
                if path not in file_system:
                    # file_system[path] = []
                    file_system[FileItem(f"dir {path}")] = []
        else:
            # listing out all 
            file_system["".join(cur_path)].append(FileItem(c))
    return file_system


def parts(mock_file_system):
    # part 1
    # find dir with size <= MAX_SIZE
    MAX_SIZE = 100000
    sum_max_size = 0  # total sum of dir with size <= MAX_SIZE
    for dir, files in mock_file_system.items():
        size = find_size(dir.name, files, mock_file_system)
        dir.size = size
        # for part 1
        if  size <= MAX_SIZE:
            sum_max_size += size
    

    # part 2
    FILE_SYS_SIZE = 70000000
    UPDATE_SIZE = 30000000
    need = find_size("/", mock_file_system["/"], mock_file_system) - (FILE_SYS_SIZE - UPDATE_SIZE)
    
    min_size_to_de = sorted(
        filter(lambda x: x.size >= need, mock_file_system.keys()), 
        key=lambda x: x.size
    )[0].size

    return (sum_max_size, min_size_to_de)


def main():
    mock_file_system = init_graph()
    
    g.print_parts(
        *parts(mock_file_system)
    )

main()
