data_file_name = 'data/data'
data_file = open(data_file_name, 'r')
the_data = data_file.read().splitlines()

math = []
command = ""

for instruction in the_data:
    if instruction == "noop":
        command = "noop"
    else:
        command, value = instruction.split(" ")

    if command == "noop":
        math.append(0)
    elif command == "addx":
        math.append(0)
        math.append(int(value))

def part1():
    x = 1
    strength_total =[]
    strength = 0
    for cycle, add_this in enumerate(math):
        x += add_this
        print("x=", x)
        if cycle == 20 - 2 :
            strength = x * 20
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)
        elif cycle == 60 - 2 :
            strength = x * 60
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)
        elif cycle == 100 - 2 :
            strength = x * 100
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)
        elif cycle == 140 - 2 :
            strength = x * 140
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)     
        elif cycle == 180 - 2 :
            strength = x * 180
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)  
        elif cycle == 220 - 2:
            strength = x * 220
            print("For cycle", cycle, " x=", x, "strength=", strength)    
            strength_total.append(strength)            
    total = 0
    for strength in strength_total:
        total += strength
    print("strenght total:", total)
    print(math)


def part2():
    message =[]
    sprite_position = 1
    for cycle, maths in enumerate(math):

        if ( cycle == sprite_position - 1 or
             cycle == sprite_position or 
             cycle == sprite_position + 1):
            # print("current cycle", cycle)
            message.append("#")
        else:
            message.append(".")
        
        sprite_position += maths
        if cycle == 40 - 1:
            sprite_position += 40
        elif cycle == 80 - 1:
            sprite_position += 40
        elif cycle == 120 - 1:
            sprite_position += 40
        elif cycle == 160 - 1:
            sprite_position += 40
        elif cycle == 200 - 1:
            sprite_position += 40
        elif cycle == 240 - 1:
            sprite_position += 40            


    for i in message[:40]:
        print(i, end = '')
    print("")
    for i in message[40:80]:
        print(i, end = '')        
    print("")
    for i in message[80:120]:
        print(i, end = '')   
    print("")
    for i in message[120:160]:
        print(i, end = '')   
    print("")
    for i in message[160:200]:
        print(i, end = '')
    print("")        
    for i in message[200:240]:
        print(i, end = '')                               
# part1()
part2()

# print(math)
