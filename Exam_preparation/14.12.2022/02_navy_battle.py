rows = int(input())

matrix = []
submarine_position = []
count_hit_mines = 0
count_destroyed_cruisers = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(rows):
    line = [ch for ch in input()]
    matrix.append(line)

    if "S" in line:
        submarine_position = [r, line.index("S")]
        matrix[r][line.index("S")] = "-"

while True:
    command = input()

    submarine_position[0] += directions[command][0]
    submarine_position[1] += directions[command][1]

    if matrix[submarine_position[0]][submarine_position[1]] == "-":
        continue

    elif matrix[submarine_position[0]][submarine_position[1]] == "*":
        matrix[submarine_position[0]][submarine_position[1]] = "-"

        count_hit_mines += 1

        if count_hit_mines == 3:
            matrix[submarine_position[0]][submarine_position[1]] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
            break

    elif matrix[submarine_position[0]][submarine_position[1]] == "C":
        matrix[submarine_position[0]][submarine_position[1]] = "-"

        count_destroyed_cruisers += 1

        if count_destroyed_cruisers == 3:
            matrix[submarine_position[0]][submarine_position[1]] = "S"
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

[print(''.join(inner_list)) for inner_list in matrix]


# 5
# *--*-
# -S-*C
# -*---
# -----
# -C-*C
# right
# down
# left
# up
# right
# right
# right
# down
# down
# down
# up
# left
# left
# left
# down
#
# 5
# *--*-
# -S-*C
# -*---
# -----
# *C-*C
# right
# right
# up
# left
# left
# left
