# READ MATRIX
rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


# CREATE MATRIX
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append()


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


# PRIMARY DIAGONAL
primary_diagonal = [matrix[i][i] for i in range(rows)]


# PRINT UNPACKED MATRIX
[print(*inner_list) for inner_list in matrix]


# PRINT MATRIX AS LISTS
[print(inner_list) for inner_list in matrix]


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