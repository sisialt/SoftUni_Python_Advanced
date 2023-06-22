def check_mines(r, c):
    mines = 0
    for direction in directions.values():
        next_r = r + direction[0]
        next_c = c + direction[1]

        if 0 <= next_r < size and 0 <= next_c < size:
            if mines_field[next_r][next_c] == "*":
                mines += 1
    return mines


size = int(input())
bombs = int(input())

mines_field = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "left up diagonal": (-1, -1),
    "left down diagonal": (1, -1),
    "right up diagonal": (-1, 1),
    "right down diagonal": (1, 1)
}

for _ in range(size):
    mines_field.append([0] * size)

for _ in range(bombs):
    bomb = input().strip("()").split(", ")
    bomb_position = [int(bomb[0]), int(bomb[1])]
    mines_field[bomb_position[0]][bomb_position[1]] = "*"

for r in range(size):
    for c in range(size):
        if mines_field[r][c] != "*":
            mines_field[r][c] = check_mines(r, c)

[print(*inner_list, sep=" ") for inner_list in mines_field]


# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)
#
# 5
# 3
# (1, 1)
# (2, 4)
# (4, 1)
