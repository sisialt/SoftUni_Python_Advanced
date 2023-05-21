rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = [matrix[i][i] for i in range(rows)]
matrix_turned_left = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
secondary_diagonal = [matrix_turned_left[i][i] for i in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9