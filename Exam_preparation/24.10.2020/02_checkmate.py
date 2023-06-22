rows = 8

matrix = []
king_position = []
queens_positions = []
queens_capture_king = []

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

for r in range(rows):
    line = input().split()
    matrix.append(line)

    if "K" in line:
        king_position = [r, line.index("K")]

    if "Q" in line:
        for i in range(len(line)):
            if line[i] == "Q":
                queens_positions.append([r, i])  # it was line.index(ch) and appended always the first occurrence

for queen in queens_positions:
    is_captured = False
    for pos in directions.values():
        if is_captured:
            break
        for i in range(1, rows):
            next_row = queen[0] + pos[0] * i
            next_col = queen[1] + pos[1] * i

            if [next_row, next_col] in queens_positions:
                break
            if [next_row, next_col] == king_position:
                queens_capture_king.append(queen)
                is_captured = True
                break

if not queens_capture_king:
    print("The king is safe!")
else:
    print(*queens_capture_king, sep="\n")


# . . . . . . . .
# Q Q Q . . . . .
# Q K Q . . Q . .
# Q Q Q Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .
#
#
# . . . . . . . .
# . . . Q . . . .
# . . . . . . . .
# . . . . . . . .
# Q . . . Q . . .
# . . K . . . . .
# . . . . . . Q .
# . . . Q . . . .
