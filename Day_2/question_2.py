final_result = 19690720

input_file = open("/home/gagandeep/Desktop/Advent_of_code/Day_2/input.txt")
input_data = input_file.read()
input_file.close()

intCode_list = input_data.split(",")
intCode_list = list(map(int, intCode_list))
reset_list = list(intCode_list)

for noun in range(100):
    for verb in range(100):
        intCode_list = reset_list[:]
        intCode_list[1] = noun
        intCode_list[2] = verb
        for item in range(0, len(intCode_list), 4):
            if intCode_list[item] == 1:
                intCode_list[intCode_list[item+3]] = intCode_list[intCode_list[item+1]] + intCode_list[intCode_list[item+2]]
            elif intCode_list[item] == 2:
                intCode_list[intCode_list[item+3]] = intCode_list[intCode_list[item+1]] * intCode_list[intCode_list[item+2]]
            elif intCode_list[item] == 99:
                if intCode_list[0] == final_result:
                    print(100 * noun + verb)
                break
