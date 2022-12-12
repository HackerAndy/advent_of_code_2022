from numpy import place


def head_tail_overlap(x1, y1, x2, y2):
    if (x1 == x2) and (y1 == y2):
        return True

data_file_name = 'data/sample'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()
# data_array = numpy.genfromtxt(data_file, delimiter=1, dtype="int")

places_tail_visited = {"1,1"}
# if up/down then left/right  also reverse is true = diagonal
# if overlap don't move

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

        # if head_tail_overlap(head_x_coord, head_y_coord, tail_x_coord, tail_y_coord):
        #     distance_to_travel -= 1
        
        # Check before head moves 
        if tail_x_coord > head_x_coord: # Head is double backing
            if distance > 1:
                distance_to_travel -= 2
            else:
                distance_to_travel -= 1
        elif tail_x_coord == head_x_coord:
            if distance > 1:
                distance_to_travel -= 1
            else:
                distance_to_travel == 0

        head_x_coord += distance

        # Move diagonally
        if (head_y_coord > tail_y_coord):
            tail_y_coord += 1 
        elif (head_y_coord < tail_y_coord):
            tail_y_coord -= 1

        for _ in range (0, distance_to_travel):
            tail_x_coord += 1            
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

    elif direction == "L":
        distance_to_travel = distance

        # Check before head moves 
        if tail_x_coord < head_x_coord: # Head is double backing
            if distance > 1:
                distance_to_travel -= 2
            else:
                distance_to_travel == 0
        elif tail_x_coord == head_x_coord:
            if distance > 1:
                distance_to_travel -= 1
            else:
                distance_to_travel == 0

        head_x_coord -= distance

        if (head_y_coord > tail_y_coord):
            tail_y_coord += 1
        elif (head_y_coord < tail_y_coord):
            tail_y_coord -= 1

        for _ in range (0, distance_to_travel):
            tail_x_coord -= 1
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

    elif  direction == "U":
        distance_to_travel = distance

        # Check before head moves 
        if tail_y_coord > head_y_coord: # Head is double backing
            if distance > 1:
                distance_to_travel -= 2
            else:
                distance_to_travel == 0
        elif tail_x_coord == head_x_coord: #on same spot
            if distance > 1:
                distance_to_travel -= 1
            else:
                distance_to_travel == 0

        head_y_coord += distance

        if (head_x_coord > tail_x_coord):
            tail_x_coord += 1
        elif (head_x_coord < tail_x_coord):
            tail_x_coord -= 1

        for _ in range (0, distance_to_travel):
            tail_y_coord += 1            
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

    elif direction == "D":
        distance_to_travel = distance

        # Check before head moves 
        if tail_y_coord < head_y_coord: # Head is double backing
            if distance > 1:
                distance_to_travel -= 2
            else:
                distance_to_travel == 0
        elif tail_x_coord == head_x_coord:
            if distance > 1:
                distance_to_travel -= 1
            else:
                distance_to_travel == 0      

        head_y_coord -= distance

        if (head_x_coord > tail_x_coord):
            tail_x_coord += 1
        elif (head_x_coord < tail_x_coord):
            tail_x_coord -= 1

        for _ in range (0, distance_to_travel):
            tail_y_coord -= 1
            places_tail_visited.add(str(tail_x_coord)+","+str(tail_y_coord))

    print("Hx", head_x_coord, "Hy", head_y_coord)
    print("Tx", tail_x_coord, "Ty", tail_y_coord)
print(places_tail_visited)


