rows, cols = 6, 6

matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(rows):
    line = input().split()
    matrix.append(line)

position = input()
my_position = [int(position[1]), int(position[4])]

while True:
    command_args = input().split(", ")
    command = command_args[0]

    if command == "Stop":
        break

    direction = command_args[1]
    my_position = [my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]]

    if command == "Create":
        if matrix[my_position[0]][my_position[1]] == ".":
            matrix[my_position[0]][my_position[1]] = command_args[2]

    elif command == "Update":
        if matrix[my_position[0]][my_position[1]] != ".":
            matrix[my_position[0]][my_position[1]] = command_args[2]

    elif command == "Delete":
        if matrix[my_position[0]][my_position[1]] != ".":
            matrix[my_position[0]][my_position[1]] = "."

    elif command == "Read":
        if matrix[my_position[0]][my_position[1]] != ".":
            print(matrix[my_position[0]][my_position[1]])

[print(*inner_list) for inner_list in matrix]


# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop
#
# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop
#
# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop
