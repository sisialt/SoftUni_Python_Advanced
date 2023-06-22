size = int(input())

snake_territory = []
snake_position = []
burrows_positions = []
eaten_food = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(size):
    line = [ch for ch in input()]
    snake_territory.append(line)

    if "S" in line:
        snake_position = [r, line.index("S")]
        snake_territory[snake_position[0]][snake_position[1]] = "."

    if "B" in line:
        for ch in line:
            if ch == "B":
                burrows_positions.append([r, line.index("B")])

while True:
    direction = input()

    next_row = snake_position[0] + directions[direction][0]
    next_col = snake_position[1] + directions[direction][1]

    if 0 <= next_row < size and 0 <= next_col < len(snake_territory):
        if snake_territory[next_row][next_col] == "*":
            snake_territory[next_row][next_col] = "."
            eaten_food += 1
            snake_position = [next_row, next_col]

            if eaten_food == 10:
                snake_territory[next_row][next_col] = "S"
                print("You won! You fed the snake.")
                break

        elif snake_territory[next_row][next_col] == "-":
            snake_territory[next_row][next_col] = "."
            snake_position = [next_row, next_col]

        elif snake_territory[next_row][next_col] == "B":
            burrows_positions.remove([next_row, next_col])
            other_burrow = burrows_positions[0]

            snake_territory[next_row][next_col] = "."
            snake_territory[other_burrow[0]][other_burrow[1]] = "."
            snake_position = [other_burrow[0], other_burrow[1]]

    else:
        print("Game over!")
        break

print(f"Food eaten: {eaten_food}")
[print(''.join(inner_list)) for inner_list in snake_territory]

# 6
# -----S
# ----B-
# ------
# ------
# --B---
# --*---
# left
# down
# down
# down
# left
#
# 7
# --***S-
# --*----
# --***--
# ---**--
# ---*---
# ---*---
# ---*---
# left
# left
# left
# down
# down
# right
# right
# down
# left
# down
