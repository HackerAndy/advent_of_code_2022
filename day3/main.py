import os
from itertools import zip_longest

def char_to_number(letter_as_character):
    numeric_value = 0
    if ord(letter_as_character) > 96: #Lowercase
        numeric_value = ord(letter_as_character) - 96
    else: #lowercase
        numeric_value = ord(letter_as_character) - 38
    return numeric_value

def part1():
    rucksack_file = open(rucksack_file_name, 'r')
    rucksacks = rucksack_file.read().splitlines()

    total_score = 0
    for this_rucksack in rucksacks:
        num_of_contents = len(this_rucksack)
        # print(num_of_contents)
        contents_per_pocket = int(num_of_contents / 2)
        pocket_1_contents = this_rucksack[:contents_per_pocket]
        # print("pocket_1", pocket_1_contents)
        pocket_2_contents = this_rucksack[contents_per_pocket:]
        # print("pocket_2", pocket_2_contents)
        matching_characters_as_set = set(pocket_1_contents) & set(pocket_2_contents)
        # print("Matching chars", matching_characters)
        matching_character = list(matching_characters_as_set)[0]
        total_score += char_to_number(matching_character)
    print("total:", total_score)

def part2():
    total_score = 0

    with open(rucksack_file_name, 'r') as rucksack_file:
        for group_of_racksacks in zip_longest(*[rucksack_file] * 3):
            racksack1 = group_of_racksacks[0].replace("\n","")
            racksack2 = group_of_racksacks[1].replace("\n","")
            racksack3 = group_of_racksacks[2].replace("\n","")
            matching_characters_as_set = set(racksack1) & set(racksack2) & set(racksack3)
            matching_character = list(matching_characters_as_set)[0]
            total_score += char_to_number(matching_character)
    print(total_score)

# print("a", ord('a'), "z", ord('z'), "A", ord('A'), "Z", ord('Z'))    

# print("current working directory", os.getcwd())
rucksack_file_name = 'data/data1'
# part1()
part2()
