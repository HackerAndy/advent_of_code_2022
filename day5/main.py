from curses import raw
from collections import deque

crate_stack_height = 8


def parse_crates(raw_data):
    all_crates = []
    crate1 = []
    crate2 = []
    crate3 = []
    crate4 = []
    crate5 = []
    crate6 = []
    crate7 = []
    crate8 = []
    crate9 = []        
    for line in raw_data:
        char_list = list(line)
        if not char_list[1] == " ":
            crate1.append(char_list[1])
        if not char_list[5] == " ":
            crate2.append(char_list[5])
        if not char_list[9] == " ":
            crate3.append(char_list[9])
        if not char_list[13] == " ":
            crate4.append(char_list[13])
        if not char_list[17] == " ":
            crate5.append(char_list[17])
        if not char_list[21] == " ":
            crate6.append(char_list[21])
        if not char_list[25] == " ":
            crate7.append(char_list[25])
        if not char_list[29] == " ":
            crate8.append(char_list[29])
        if not char_list[33] == " ":
            crate9.append(char_list[33])
    all_crates.append(deque(crate1))
    all_crates.append(deque(crate2))
    all_crates.append(deque(crate3))
    all_crates.append(deque(crate4))
    all_crates.append(deque(crate5))
    all_crates.append(deque(crate6))
    all_crates.append(deque(crate7))
    all_crates.append(deque(crate8))
    all_crates.append(deque(crate9))   
    for crate in all_crates: print(crate)     
    return all_crates

def parse_instructions(raw_data):
    all_instructions = []

    for line in raw_data:
        parsed_instructions = []

        instructions = line.split(" ")
        num_crates_to_move = instructions[1]
        parsed_instructions.append(num_crates_to_move)
        move_from_crate = instructions[3]
        parsed_instructions.append(move_from_crate)
        move_to_crate = instructions[5]
        parsed_instructions.append(move_to_crate)
        # print("line instructions:", parsed_instructions)
        all_instructions.append(parsed_instructions)

    return all_instructions

def part1():
    for instruction in instructions_full:
        num_of_crates_to_move = int(instruction[0])
        crate_num_from = int(instruction[1]) - 1
        crate_stack_to = int(instruction[2]) - 1

        for _ in range(num_of_crates_to_move):
            removed_crate = crate_stack_all[crate_num_from].popleft()
            crate_stack_all[crate_stack_to].appendleft(removed_crate)
        # print(crate_stack_all)

def part2():
    for instruction in instructions_full:
        num_of_crates_to_move = int(instruction[0])
        crate_num_from = int(instruction[1]) - 1
        crate_stack_to = int(instruction[2]) - 1

        creates_removed = []
        for _ in range(num_of_crates_to_move):
            removed_crate = crate_stack_all[crate_num_from].popleft()
            creates_removed.append(removed_crate)
        for num_ in range(num_of_crates_to_move):
            add_this_crate = num_of_crates_to_move - num_ -1
            crate_stack_all[crate_stack_to].appendleft(creates_removed[add_this_crate])
        # print(crate_stack_all)

data_file_name = 'data/data'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()

crates_raw = the_data[0:crate_stack_height]
crate_stack_all = parse_crates(crates_raw)

instructions_raw = the_data[crate_stack_height+2:]
instructions_full = parse_instructions(instructions_raw)

# part1()
part2()

for crate in crate_stack_all:
    print(crate.popleft())
# for this_instruction in instructions:


