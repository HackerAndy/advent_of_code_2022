
calorie_counts_file_name = 'data/data1'
calorie_counts_file = open(calorie_counts_file_name, 'r')
calories_file_line = calorie_counts_file.readlines()

calories_per_elf = 0
calorie_max = 0
list_of_calories_per_elf = []

for calories in calories_file_line:
    if calories.isspace():
        list_of_calories_per_elf.append(calories_per_elf)
        calories_per_elf = 0
    else:
        calories_as_int = int(calories)
        calories_per_elf += calories_as_int

sorted_list_of_calories_per_elf = sorted(list_of_calories_per_elf, reverse=True)
print(sorted_list_of_calories_per_elf[0])
print(sorted_list_of_calories_per_elf[1])
print(sorted_list_of_calories_per_elf[2])

total_for_top_3 = sum(sorted_list_of_calories_per_elf[:3])
print("sum of top3", total_for_top_3)
calorie_counts_file.close()
