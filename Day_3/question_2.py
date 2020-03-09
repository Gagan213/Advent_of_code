with open("/home/gagandeep/Desktop/Advent_of_code/Day_3/input.txt") as input_:
    input_data = input_.readlines()
    wire_a = input_data[0]
    wire_b = input_data[1]

from itertools import groupby

def get_points(wire: str):
    coordinate_list = []
    x = 0
    y = 0
    movements = wire.split(",")
    for command in movements:
        if command[0] == "R":
            for i in range(x, x + int(command[1:]) + 1):
                coordinate_list.append(f"{i},{y}")
                x = i

        if command[0] == "L":
            for i in range(x, x - int(command[1:]) - 1, -1):
                coordinate_list.append(f"{i},{y}")
                x = i

        if command[0] == "U":
            for i in range(y, y + int(command[1:]) + 1):
                coordinate_list.append(f"{x},{i}")
                y = i

        if command[0] == "D":
            for i in range(y, y - int(command[1:]) - 1, -1):
                coordinate_list.append(f"{x},{i}")
                y = i
    return coordinate_list


wire_a_co = get_points(wire_a)
wire_a_co = [i[0] for i in groupby(wire_a_co)] 
wire_b_co = get_points(wire_b)
wire_b_co = [i[0] for i in groupby(wire_b_co)] 

comman_points = list(set(wire_a_co) & set(wire_b_co))

step_taken = 1000000
for item in comman_points:
    a = wire_a_co.index(item)
    b = wire_b_co.index(item)
    current_step = a + b
    if current_step < step_taken and current_step != 0:
        step_taken = current_step

print(f"Fewest combined steps the wires must take to reach an intersection are '{step_taken}'")