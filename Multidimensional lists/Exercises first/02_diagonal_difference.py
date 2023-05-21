rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = [matrix[i][i] for i in range(rows)]
matrix_turned_left = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
secondary_diagonal = [matrix_turned_left[i][i] for i in range(rows)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))


# 3
# 11 2 4
# 4 5 6
# 10 8 -12
