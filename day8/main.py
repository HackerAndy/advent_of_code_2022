import numpy


def is_visable(grid, my_tree_height, my_tree_position):
    for position, other_tree_height in enumerate(grid):
        if my_tree_position == position:
            return True
        if my_tree_height > other_tree_height:
            continue
        else:
            return False


def part1():
    max_rows, max_columns = data_array.shape
    max_rows -= 1
    max_columns -= 1
    visable_trees = 0
    for row_num, row in enumerate(data_array):
        reverse_row = row[::-1]    
        for col_num, tree_height in enumerate(data_array[row_num]):
            column = data_array[ : ,col_num]
            reverse_column = column[::-1]
            # try:
            if ( ((col_num - 1) < 0) or ((row_num - 1) < 0) or 
                ((col_num + 1) > max_columns) or ((row_num + 1) > max_rows) ): #boundry tree
                visable_trees += 1
                # print("Boundry", "Row", row_num, "Col", col_num)
            elif is_visable(row, tree_height, col_num): 
                visable_trees += 1 # from the left
                # print("Looking left", "Row", row_num, "Col", col_num)
            elif is_visable(column, tree_height, row_num):
                visable_trees += 1 # from the top
                # print("Looking top", "Row", row_num, "Col", col_num)
            elif is_visable(reverse_row, tree_height, max_columns - col_num):
                visable_trees += 1 # from the right
                # print("Looking right", "Row", row_num, "Col", col_num)
            elif is_visable(reverse_column, tree_height, max_rows - row_num):
                visable_trees += 1 # from the bottom
                # print("Looking down", "Row", row_num, "Col", col_num)
            # elif tree_hieght > data_array[row_num][col_num - 1]: #left
            #     visable_trees += 1
            #     print("Looking left", "Row", row_num, "Col", col_num)
            # elif tree_hieght > data_array[row_num - 1][col_num]: #up
            #     visable_trees += 1
            #     print("Looking up", "Row", row_num, "Col", col_num)
            # elif tree_hieght > data_array[row_num][col_num + 1]: #right
            #     visable_trees += 1
            #     print("Looking right", "Row", row_num, "Col", col_num)
            # elif tree_hieght > data_array[row_num + 1][col_num]: #down
            #     visable_trees += 1
            #     print("Looking down", "Row", row_num, "Col", col_num)
            # except IndexError:
            #     visable_trees += 1                        
    return visable_trees

def viewing_distance(grid, my_tree_height):
    score = 0
    for other_tree_height in grid:
        if my_tree_height > other_tree_height:
            score += 1
        # elif my_tree_height == other_tree_height:
        #     score += 1
        #     break
        else:
            score += 1
            break
    return score

def part2():
    max_rows, max_columns = data_array.shape
    max_rows -= 1
    max_columns -= 1
    max_scenic_score = 0
    scenic_score = 0
    view_from_left = 0
    view_from_top = 0 
    view_from_right = 0
    view_from_bottom = 0

    for row_num, row in enumerate(data_array):
        reverse_row = row[::-1]    
        for col_num, tree_height in enumerate(data_array[row_num]):
            
            column = data_array[ : ,col_num]
            reverse_column = column[::-1]
            if ( ((col_num - 1) < 0) or ((row_num - 1) < 0) or 
                ((col_num + 1) > max_columns) or ((row_num + 1) > max_rows) ): #boundry tree
                continue
                # print("Boundry", "Row", row_num, "Col", col_num)
            else:
                # print("processing:", "row:", row_num, "col:", col_num)

                view_from_left = viewing_distance(reverse_row[max_columns - col_num + 1:], tree_height)
                # print("Score (from left)", view_from_left)
                view_from_top = viewing_distance(reverse_column[max_rows - row_num + 1:], tree_height)
                # print("Score (from top)", view_from_top)
                view_from_right = viewing_distance(row[col_num + 1:], tree_height)
                # print("Score (from right)", view_from_right)
                view_from_bottom = viewing_distance(column[row_num + 1:], tree_height)
                # print("Score (from bottom)", view_from_bottom)
            
            scenic_score = view_from_left * view_from_top * view_from_right * view_from_bottom
        
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score

data_file_name = 'data/data'
data_file = open(data_file_name, 'r')
# the_data = data_file.read().splitlines()
data_array = numpy.genfromtxt(data_file, delimiter=1, dtype="int")


visable_trees = part1()
print("How many visable trees", visable_trees)

max_score = part2()
print("Max viewing score", max_score)

