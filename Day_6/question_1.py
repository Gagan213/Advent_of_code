with open("/home/gagandeep/Desktop/Advent_of_code/Day_6/input.txt") as connections:
    orbits_con = connections.readlines()

linked_orbits = list()
start_orbit = orbits_con[0].split(")")[0]
end_orbit = orbits_con[0].split(")")[1]


linked_orbits.append(start_orbit+">"+end_orbit.replace('\n',''))
for index, orbits in enumerate(orbits_con):
    orbits = orbits.replace("\n","")
    orbits = orbits.split(")")
    if index == 0:
        continue
    for n_index, item in enumerate(linked_orbits):
        if item.startswith(start_orbit) and item.endswith(orbits[0]):
            linked_orbits.pop(n_index)
            linked_orbits.append(item +">"+orbits[1])
        else:
            linked_orbits.append(f"{orbits[0]}>{orbits[1]}")
            print("In else Loop")
            print(linked_orbits)
            break


print(linked_orbits)