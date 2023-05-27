rows = int(input())

matrix = []
collected_tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(rows):
    inner = input().split()
    matrix.append(inner)

    if "A" in inner:
        alice_position = r, matrix[r].index("A")
        matrix[r][alice_position[1]] = "*"

command = input()

while command:
    next_row, next_col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        alice_position = [next_row, next_col]

        if matrix[next_row][next_col].isdigit():
            collected_tea_bags += int(matrix[next_row][next_col])
            matrix[next_row][next_col] = "*"

            if collected_tea_bags >= 10:
                print("She did it! She went to the party.")
                break

        elif matrix[next_row][next_col] == "R":
            matrix[next_row][next_col] = "*"
            print(f"Alice didn't make it to the tea party.")
            break

        else:
            matrix[next_row][next_col] = "*"

    else:
        print(f"Alice didn't make it to the tea party.")
        break

    command = input()

[print(*inner) for inner in matrix]


# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
