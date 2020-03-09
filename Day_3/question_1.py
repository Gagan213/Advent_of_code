with open("/home/gagandeep/Desktop/Advent_of_code/Day_3/input.txt") as input_:
    input_data = input_.readlines()
    wire_a = input_data[0]
    wire_b = input_data[1]

# wire_a = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
# wire_b = "U62,R66,U55,R34,D71,R55,D58,R83"

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
wire_b_co = get_points(wire_b)

comman_points = list(set(wire_a_co) & set(wire_b_co))

min = 10000
for item in comman_points:
    item = item.split(",")
    dis = abs(0 - int(item[0])) + abs(0 - int(item[1]))
    if dis < min and dis != 0:
        min = dis


print(f"Manhattan distance from the central port to the closest intersection is '{min}'")