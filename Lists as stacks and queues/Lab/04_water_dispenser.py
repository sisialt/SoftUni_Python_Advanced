from collections import deque

water_quantity = int(input())
people = deque()

while True:
    name = input()
    if name == "Start":
        break

    people.append(name)

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split()

    if len(command_args) == 1:
        litters = int(command_args[0])

        if water_quantity >= litters:
            water_quantity -= litters
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

    else:
        litters_water_to_fill = int(command_args[1])
        water_quantity += litters_water_to_fill

print(f"{water_quantity} liters left")
