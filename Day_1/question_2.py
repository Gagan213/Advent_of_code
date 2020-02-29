import math
input_file = open("input.txt")
mass_list = input_file.readlines()
input_file.close()


def get_fuel(mass, fuel_sum):
    fuel = math.floor(mass / 3) - 2
    if fuel > 0:
        fuel_sum = fuel_sum + fuel
        return get_fuel(fuel, fuel_sum)
    else:
        return fuel_sum

fuel_list = list()
for item in mass_list:
    fuel_list.append(get_fuel(int(item.replace("\n","")), 0))


print(sum(fuel_list))