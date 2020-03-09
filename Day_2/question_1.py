input_file = open("/home/gagandeep/Desktop/Advent_of_code/Day_2/input.txt")
input_data = input_file.read()
input_file.close()

intCode_list = input_data.split(",")
intCode_list = list(map(int, intCode_list))
intCode_list[1] = 12
intCode_list[2] = 2
for item in range(0, len(intCode_list), 4):
    if intCode_list[item] == 1:
        intCode_list[intCode_list[item+3]] = intCode_list[intCode_list[item+1]] + intCode_list[intCode_list[item+2]]
    elif intCode_list[item] == 2:
        intCode_list[intCode_list[item+3]] = intCode_list[intCode_list[item+1]] * intCode_list[intCode_list[item+2]]
    elif intCode_list[item] == 99:
        break

print(intCode_list[0])