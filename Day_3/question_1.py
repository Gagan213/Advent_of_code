input_file = open("c:/Users/hp/Desktop/Advent of code/Day_3/input.txt")
input_data = input_file.readlines()
input_file.close()
wire_a = input_data[0].split(",")
wire_b = input_data[1].split(",")


# print(wire_a)
# print(wire_b)

def get_co(wire):
    x = 0
    y = 0
    co_list = list()
    for item in wire:
        if item[0] == "R":
            distance = int(item[1:])
            for i in range(x, distance, 1):
                co_list.append([i, y])
            x = distance
        elif item[0] == "L":
            distance = int(item[1:])
            for i in range(x, distance, -1):
                co_list.append([i, y])
            x = distance

    return co_list

wire = ["R70","L60"]
print(get_co(wire))