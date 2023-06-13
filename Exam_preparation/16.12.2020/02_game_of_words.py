initial_string = input()

rows = int(input())

matrix = []
player_position = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(rows):
    line = input()
    matrix.append([])
    for i in range(len(line)):
        matrix[r].append(line[i])

        if line[i] == "P":
            player_position = [r, i]
            matrix[r][i] = "-"

m = int(input())

for _ in range(m):
    move_command = input()

    next_row = player_position[0] + directions[move_command][0]
    next_col = player_position[1] + directions[move_command][1]

    if 0 <= next_row < rows and 0 <= next_col < rows:
        if matrix[next_row][next_col] != "-":
            initial_string += matrix[next_row][next_col]
            player_position = [next_row, next_col]
            matrix[next_row][next_col] = "-"

        else:
            player_position = [next_row, next_col]

    else:
        if initial_string:
            initial_string = initial_string[:-1]

matrix[player_position[0]][player_position[1]] = "P"
print(initial_string)
[print(*inner_list, sep="") for inner_list in matrix]

# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right
#
# Initial
# 5
# -----
# t-r--
# --Pa-
# --S--
# z--t-
# 4
# up
# left
# left
# left
