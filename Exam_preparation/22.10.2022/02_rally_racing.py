size = int(input())
racing_number = input()

race_route = []
tunnel_positions = []
start_position = [0, 0]
passed_km = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(size):
    line = input().split()
    race_route.append(line)

    if "T" in line:
        for i in range(len(line)):
            if line[i] == "T":
                tunnel_positions.append([r, i])

while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    next_row = start_position[0] + directions[command][0]
    next_col = start_position[1] + directions[command][1]

    if race_route[next_row][next_col] == ".":
        passed_km += 10
        start_position = [next_row, next_col]
        continue

    elif race_route[next_row][next_col] == "T":
        tunnel_positions.remove([next_row, next_col])

        other_tunnel = tunnel_positions[0]
        start_position = [other_tunnel[0], other_tunnel[1]]
        race_route[next_row][next_col] = "."
        race_route[start_position[0]][start_position[1]] = "."

        passed_km += 30

    elif race_route[next_row][next_col] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        start_position = [next_row, next_col]
        passed_km += 10
        break

print(f"Distance covered {passed_km} km.")
race_route[start_position[0]][start_position[1]] = "C"
[print(''.join(inner_list)) for inner_list in race_route]


# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End
#
# 10
# 45
# . . . . . . . . . .
# . . T . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . F . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . T . .
# right
# down
# down
# right
# up
# left
# up
# up
# End
