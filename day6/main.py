
data_file_name = 'data/data'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()

char_list = list(the_data[0])

end_index = len(char_list) - 14
for index in range(0, end_index):
    current_array = []
    current_array.append(char_list[index])
    current_array.append(char_list[index+1])
    current_array.append(char_list[index+2])
    current_array.append(char_list[index+3])
    current_array.append(char_list[index+4])
    current_array.append(char_list[index+5])
    current_array.append(char_list[index+6])
    current_array.append(char_list[index+7])
    current_array.append(char_list[index+8])
    current_array.append(char_list[index+9])
    current_array.append(char_list[index+10])
    current_array.append(char_list[index+11])
    current_array.append(char_list[index+12])
    current_array.append(char_list[index+13])


    duplacates = [char for char in current_array if current_array.count(char) > 1]

    if len(duplacates) == 0:
        print("No match at position:", index + 14)
        quit()