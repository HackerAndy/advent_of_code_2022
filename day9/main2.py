data_file_name = 'data/sample'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()

places_tail_visited = {"1,1"}

head_x_coord = 1
head_y_coord = 1
tail_x_coord = 1
tail_y_coord = 1

for move in the_data:
    direction, distance_str = move.split(" ")
    print(direction, distance_str)
    distance = int(distance_str)
    if direction == "R":
        distance_to_travel = distance

        if head_x_coord < tail_x_coord:
            distance_to_travel -= 0
        elif head_x_coord < tail_x_coord:
            distance_to_travel -= 2
        elif head_x_coord == tail_x_coord:
            distance_to_travel -= 1
        
        if head_y_coord > tail_y_coord:
            tail_y_coord += 1
        elif head_y_coord < tail_y_coord:
            tail_y_coord -= 1
        elif head_y_coord == tail_y_coord:
            tail_y_coord += 0

        for _ in range (0, distance_to_travel):
            tail_x_coord += 1            
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

        head_x_coord += distance

    elif direction == "L":
        distance_to_travel = distance

        if head_x_coord < tail_x_coord:
            distance_to_travel -= 2
        elif head_x_coord < tail_x_coord:
            distance_to_travel -= 0
        elif head_x_coord == tail_x_coord:
            distance_to_travel -= 1
        
        if head_y_coord > tail_y_coord:
            tail_y_coord += 1
        elif head_y_coord < tail_y_coord:
            tail_y_coord -= 1
        elif head_y_coord == tail_y_coord:
            tail_y_coord -= 0

        for _ in range (0, distance_to_travel):
            tail_x_coord -= 1
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

        head_x_coord -= distance

    elif  direction == "U":
        distance_to_travel = distance

        if head_x_coord < tail_x_coord:
            tail_x_coord += 1
        elif head_x_coord < tail_x_coord:
            tail_x_coord -= 1
        elif head_x_coord == tail_x_coord:
            tail_x_coord += 0
        
        if head_y_coord > tail_y_coord:
            distance_to_travel -= 0
        elif head_y_coord < tail_y_coord:
            distance_to_travel -= 2
        elif head_y_coord == tail_y_coord:
            distance_to_travel -= 1

        for _ in range (0, distance_to_travel):
            tail_y_coord += 1            
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

        head_y_coord += distance

    elif direction == "D":
        distance_to_travel = distance

        if head_x_coord < tail_x_coord:
            tail_x_coord += 1
        elif head_x_coord < tail_x_coord:
            tail_x_coord -= 1
        elif head_x_coord == tail_x_coord:
            tail_x_coord -= 0
        
        if head_y_coord > tail_y_coord:
            distance_to_travel -= 2
        elif head_y_coord < tail_y_coord:
            distance_to_travel -= 0
        elif head_y_coord == tail_y_coord:
            distance_to_travel -= 1
            
        for _ in range (0, distance_to_travel):
            tail_y_coord -= 1
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

        head_y_coord -= distance

    print("Hx", head_x_coord, "Hy", head_y_coord)
    print("Tx", tail_x_coord, "Ty", tail_y_coord)
print(places_tail_visited)


