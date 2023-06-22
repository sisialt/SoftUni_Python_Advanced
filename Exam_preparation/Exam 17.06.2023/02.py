data = input().split(',')
rows = int(data[0])
cols = int(data[1])

cupboard = []
mouse_position = []
cheese_positions = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(rows):
    line = [ch for ch in input()]
    cupboard.append(line)

    if "M" in line or "C" in line:
        for i in range(len(line)):

            if line[i] == "M":
                mouse_position = [r, i]
                cupboard[r][i] = "*"
            elif line[i] == "C":
                cheese_positions.append([r, i])

while True:
    command = input()

    if command == "danger":
        print(f"Mouse will come back later!")
        break

    next_row = mouse_position[0] + directions[command][0]
    next_col = mouse_position[1] + directions[command][1]

    if 0 <= next_row < rows and 0 <= next_col < cols:
        if cupboard[next_row][next_col] == "C":
            cupboard[next_row][next_col] = "*"
            cheese_positions.remove([next_row, next_col])
            mouse_position = [next_row, next_col]

            if not cheese_positions:
                print(f"Happy mouse! All the cheese is eaten, good night!")
                break

        elif cupboard[next_row][next_col] == "T":
            mouse_position = [next_row, next_col]
            print(f"Mouse is trapped!")
            break

        elif cupboard[next_row][next_col] == "@":
            continue

        elif cupboard[next_row][next_col] == "*":
            mouse_position = [next_row, next_col]

    else:
        print(f"No more cheese for tonight!")
        break

cupboard[mouse_position[0]][mouse_position[1]] = "M"

[print(''.join(inner_list)) for inner_list in cupboard]


# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger
#
# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger
#
# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger
