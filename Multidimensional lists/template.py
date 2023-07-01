directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
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
# TRAVERSE WHEN INDEX NOT IN RANGE # directions[command](*positions) / (row, col)
# directions = {
#     "left": lambda r, c: [r, (c - 1) % SIZE],
#     "right": lambda r, c: [r, (c + 1) % SIZE],
#     "up": lambda r, c: [(r - 1) % SIZE, c],
#     "down": lambda r, c: [(r + 1) % SIZE, c],
# }

# READ MATRIX
rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])

# for r in range(rows):
#     line = input()
#     matrix.append([])
#     for i in range(len(line)):
#         matrix[r].append(line[i])


# CREATE MATRIX
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(var)


# CREATE CURRENT SUBMATRIX
submatrix = [
    [matrix[row][col]
     for col in range(2)]
    for row in range(2)
]


# CURRENT ELEMENT
for i in range(rows):
    for j in range(cols):
        current_el = matrix[i][j]


# PRIMARY &DIAGONAL
primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]


# PRINT UNPACKED MATRIX
[print(*inner_list) for inner_list in matrix]


# PRINT MATRIX AS LISTS
[print(inner_list) for inner_list in matrix]


# FIND ROW, COL WHEN GOING OUTSIDE MATRIX from the opposite side in the same direction
last_row = directions[direction][0] * steps
last_col = directions[direction][1] * steps
if last_row < 0:
    last_row = rows - abs(last_row % rows)
elif last_row >= rows:
    last_row = last_row % rows

if last_col < 0:
    last_col = last_col % cols
elif last_col >= cols:
    last_col = cols - abs(last_col % cols)



# my MATRIX TURNED LEFT
new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

rows = len(matrix)
cols = len(matrix[0])
matrix_changed = []
matrix_turned_left = []
matrix_turned_right = []

for j in range(cols):
    inner_list = []
    for i in range(rows):
        current_el = matrix[i][j]
        inner_list.append(current_el)
    matrix_changed.append(inner_list)

for i in range(1, len(matrix_changed) + 1):
    matrix_turned_left.append(matrix_changed[-i])


# my MATRIX TURNED RIGHT
new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):
    inner_list = []
    for i in range(rows):
        current_el = matrix[i][j]
        inner_list.insert(0, current_el)
    matrix_turned_right.append(inner_list)