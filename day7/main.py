from anytree import Node, search

data_file_name = 'data/data'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()

dir_structure = {"directories": [], "files": [] , "root": Node("root", size=0)}

current_dir = dir_structure["root"]

def calculate_size(all_nodes, root_node):
    total_size = 0
    for current_node in root_node.children:
        if current_node.size == 0:
            current_node.size = calculate_size(all_nodes, current_node)
        total_size += current_node.size
    return total_size
        
for command_line in the_data:
    command = command_line[0:4]
    if command == "$ ls":
        # print("Command ls")
        continue
    elif command == "$ cd":
        _, _, dir_name  = command_line.split(" ")
        if dir_name == "..":
            current_dir = current_dir.parent
        else:
            # print("Searching for directory", dir_name)
            for child_dir in current_dir.children:
                if child_dir.name == dir_name:
                    current_dir = child_dir
                    break
            # current_dir = search.find(current_dir, lambda node: node.name == dir_name )
        # print("Command cd")
    elif command == "dir ": # Add directories
        _, dir_name  = command_line.split(" ")
        dir_structure["directories"].append(Node(dir_name, current_dir, size=0))
        # print("it's a dir")
    else: # Add files
        file_size, file_name  = command_line.split(" ")
        dir_structure["files"].append(Node(file_name, parent=current_dir, size=int(file_size)))

dir_structure["root"].size = calculate_size(dir_structure, dir_structure["root"])
print(dir_structure["root"].size)

space_needed = 30000000 - (70000000 - dir_structure["root"].size)
smallest_dir_size = dir_structure["root"].size

less_than_1_mil = 0
for this_directory in dir_structure['directories']:
    if this_directory.size <= 100000:
        less_than_1_mil += this_directory.size
    if space_needed <= this_directory.size < smallest_dir_size:
        smallest_dir_size = this_directory.size

print("Part1:", less_than_1_mil)
print("Part2:", smallest_dir_size)