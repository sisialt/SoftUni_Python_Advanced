rows, cols = [int(x) for x in input().split(", ")]

matrix = []
my_position = []
count_decorations, count_gifts, count_cookies = 0, 0, 0
collected_decorations, collected_gifts, collected_cookies = 0, 0, 0

for r in range(rows):
    line = input().split()
    matrix.append(line)

    if "Y" in line:
        my_position = [r, line.index("Y")]

    if "D" in line:
        count_decorations += line.count("D")

    if "G" in line:
        count_gifts += line.count("G")

    if "C" in line:
        count_cookies += line.count("C")

count_all = count_gifts + count_cookies + count_decorations

while count_all:
    command = input()

    if command == "End":
        break

    command_args = command.split("-")
    direction = command_args[0]
    steps = int(command_args[1])

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    for _ in range(steps):
        matrix[my_position[0]][my_position[1]] = "x"

        next_row = my_position[0] + directions[direction][0]
        next_col = my_position[1] + directions[direction][1]

        if next_row == rows:
            next_row = 0
        elif next_row < 0:
            next_row = rows - 1

        if next_col == cols:
            next_col = 0
        elif next_col < 0:
            next_col = cols - 1

        if matrix[next_row][next_col] == "D":
            collected_decorations += 1
            count_all -= 1

        elif matrix[next_row][next_col] == "G":
            collected_gifts += 1
            count_all -= 1

        elif matrix[next_row][next_col] == "C":
            collected_cookies += 1
            count_all -= 1

        matrix[next_row][next_col] = "Y"
        my_position = [next_row, next_col]

        if not count_all:
            break

if not count_all:
    print("Merry Christmas!")

print(f"You've collected:\n"
      f"- {collected_decorations} Christmas decorations\n"
      f"- {collected_gifts} Gifts\n"
      f"- {collected_cookies} Cookies")

[print(*inner_list) for inner_list in matrix]


# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End

# 5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3

# 5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End


