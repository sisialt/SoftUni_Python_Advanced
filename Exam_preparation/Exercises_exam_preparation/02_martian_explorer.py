matrix = []
rover_position = []
rows = 6
water_deposit, metal_deposit, concrete_deposit = 0, 0, 0

for r in range(rows):
    line = input().split()
    matrix.append(line)

    if "E" in line:
        rover_position = [r, line.index("E")]

commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for command in commands:
    next_row = rover_position[0] + directions[command][0]
    next_col = rover_position[1] + directions[command][1]

    if next_row == rows:
        next_row = 0
    elif next_row < 0:
        next_row = rows - 1

    if next_col == rows:
        next_col = 0
    elif next_col < 0:
        next_col = rows - 1

    matrix[rover_position[0]][rover_position[1]] = "-"
    rover_position = [next_row, next_col]

    if matrix[rover_position[0]][rover_position[1]] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({rover_position[0]}, {rover_position[1]})")
    elif matrix[rover_position[0]][rover_position[1]] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({rover_position[0]}, {rover_position[1]})")
    elif matrix[rover_position[0]][rover_position[1]] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({rover_position[0]}, {rover_position[1]})")
    elif matrix[rover_position[0]][rover_position[1]] == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

# SIZE = 6
#
# deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}
# directions = {
#     "left": lambda r, c: [r, (c - 1) % SIZE],
#     "right": lambda r, c: [r, (c + 1) % SIZE],
#     "up": lambda r, c: [(r - 1) % SIZE, c],
#     "down": lambda r, c: [(r + 1) % SIZE, c],
# }
#
# mars = []
# rover_pos = []
#
# for row in range(SIZE):
#     current_row = input().split()
#
#     if "E" in current_row:
#         rover_pos = [row, current_row.index("E")]
#
#     mars.append(current_row)
#
# commands = input().split(", ")
#
# for command in commands:
#     rover_pos = directions[command](*rover_pos)
#     position = mars[rover_pos[0]][rover_pos[1]]
#
#     if position in deposits:
#         print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
#
#         deposits[position][1] += 1
#
#     elif position == "R":
#         print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
#         break
#
# if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")
