import math
input_file = open("/home/gagandeep/Desktop/Advent_of_code/Day_1/input.txt")
mass_list = input_file.readlines()
input_file.close()

fuel_sum = 0

for item in mass_list:
    fuel = math.floor(int(item.replace("\n","")) / 3) - 2
    fuel_sum = fuel_sum + fuel


print(fuel_sum)