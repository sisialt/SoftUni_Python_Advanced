def valid_coordinates(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True


rows = int(input())
matrix = [list(input()) for _ in range(rows)]

removed = 0

positions_knight_can_attack = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [2, -1],
    [1, 2],
    [2, 1]
]

while True:
    max_count = 0
    max_knight_position = ""

    for r in range(rows):
        for c in range(rows):
            current_max = 0

            if matrix[r][c] == "K":

                for position in positions_knight_can_attack:
                    next_row, next_col = r + position[0], c + position[1]

                    if valid_coordinates(next_row, next_col):

                        if matrix[next_row][next_col] == "K":
                            current_max += 1

                if current_max > max_count:
                    max_count = current_max
                    max_knight_position = [r, c]

    if max_knight_position:
        matrix[max_knight_position[0]][max_knight_position[1]] = "0"
        removed += 1
    else:
        break

print(removed)

# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
